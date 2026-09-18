from scipy.optimize import brentq


def r_ab_equation(r, alpha, m, mdot):
    """
    Equation for r_ab:

        r_ab / (1 - r_ab^(-1/2))^(16/21)
        =
        150 * (alpha*m)^(2/21) * mdot^(16/21)

    The roots are obtained by solving:

        equation(r) = 0
    """

    RHS = (
        150
        * (alpha * m) ** (2 / 21)
        * mdot ** (16 / 21)
    )

    LHS = (
        r
        / (1 - r ** (-0.5)) ** (16 / 21)
    )

    return LHS - RHS


def calculate_r_ab(alpha, m, mdot):
    """
    Calculate the two mathematical roots of r_ab.

    Returns
    -------
    tuple
        (root1, root2)
    """

    if alpha <= 0:
        raise ValueError("alpha must be greater than zero.")

    if m <= 0:
        raise ValueError("m must be greater than zero.")

    if mdot <= 0:
        raise ValueError("mdot must be greater than zero.")

    # Minimum of the function
    r_min = (29 / 21) ** 2

    try:

        root1 = brentq(
            lambda r: r_ab_equation(
                r, alpha, m, mdot
            ),
            1.000001,
            r_min
        )

        root2 = brentq(
            lambda r: r_ab_equation(
                r, alpha, m, mdot
            ),
            r_min,
            1e8
        )

        return root1, root2

    except ValueError:

        raise ValueError(
            "No two positive roots were found "
            "for the given parameters."
        )
