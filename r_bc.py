from scipy.optimize import brentq


def r_bc_equation(r, mdot):
    """
    Equation for r_bc:

        r_bc =
        6.3e3 * mdot^(2/3)
        * (1 - r_bc^(-1/2))^(2/3)

    The root is obtained by solving:

        equation(r) = 0
    """

    RHS = (
        6.3e3
        * mdot ** (2 / 3)
        * (1 - r ** (-0.5)) ** (2 / 3)
    )

    return r - RHS


def calculate_r_bc(mdot):
    """
    Calculate the two mathematical roots of r_bc.

    Parameters
    ----------
    mdot : float
        Dimensionless accretion rate.

    Returns
    -------
    tuple
        (root1, root2)
    """

    if mdot <= 0:
        raise ValueError(
            "mdot must be greater than zero."
        )

    # The characteristic minimum location
    A = 6.3e3 * mdot ** (2 / 3)

    # r must be greater than 1
    r_lower = 1.000001

    # The outer root is below A
    r_upper = A

    try:

        # Search for the first root
        root1 = brentq(
            lambda r: r_bc_equation(r, mdot),
            r_lower,
            2.0
        )

    except ValueError:

        root1 = None

    try:

        # Search for the outer root
        root2 = brentq(
            lambda r: r_bc_equation(r, mdot),
            2.0,
            r_upper
        )

    except ValueError:

        root2 = None

    if root1 is None and root2 is None:
        raise ValueError(
            "No positive roots were found "
            "for the given mdot."
        )

    return root1, root2
