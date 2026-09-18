import streamlit as st
from scipy.optimize import brentq


# --------------------------------------------------
# Equation
# --------------------------------------------------

def equation(r, alpha, m, mdot):
    """
    Returns the difference between the two sides of

        r / (1 - r^(-1/2))^(16/21)
        = 150 * (alpha*m)^(2/21) * mdot^(16/21)

    The solution is obtained when equation(r) = 0.
    """

    RHS = 150 * ((alpha * m)**(2/21)) * (mdot**(16/21))

    LHS = r / (1 - r**(-0.5))**(16/21)

    return LHS - RHS


# --------------------------------------------------
# Streamlit Web App
# --------------------------------------------------

st.title("Calculation of $r_{ab}$")

st.write(
    r"""
    We solve the equation
    """
)

st.latex(
    r"""
    \frac{r_{ab}}
    {\left(1-r_{ab}^{-1/2}\right)^{16/21}}
    =
    150(\alpha m)^{2/21}\dot{m}^{16/21}
    """
)

st.subheader("Input parameters")

alpha = st.number_input(
    r"$\alpha$",
    min_value=0.000001,
    value=0.1,
    format="%.6f"
)

m = st.number_input(
    r"$m$",
    min_value=0.000001,
    value=10.0,
    format="%.6f"
)

mdot = st.number_input(
    r"$\dot{m}$",
    min_value=0.000001,
    value=0.1,
    format="%.6f"
)


# --------------------------------------------------
# Calculate
# --------------------------------------------------

if st.button("Calculate $r_{ab}$"):

    RHS = 150 * ((alpha * m)**(2/21)) * (mdot**(16/21))

    st.write("Right-hand side:")

    st.latex(
        rf"""
        150(\alpha m)^{{2/21}}\dot{{m}}^{{16/21}}
        = {RHS:.6f}
        """
    )

    # The function has a minimum at
    # r = (29/21)^2 ≈ 1.90703

    r_min = (29 / 21)**2

    f_min = equation(r_min, alpha, m, mdot)

    # Search for roots on two sides of the minimum

    try:

        root1 = brentq(
            lambda r: equation(r, alpha, m, mdot),
            1.000001,
            r_min
        )

        root2 = brentq(
            lambda r: equation(r, alpha, m, mdot),
            r_min,
            1e8
        )

        st.success("Two mathematical solutions found.")

        st.write("Solution 1:")

        st.latex(
            rf"r_{{ab}} = {root1:.8f}"
        )

        st.write("Solution 2:")

        st.latex(
            rf"r_{{ab}} = {root2:.8f}"
        )

    except ValueError:

        st.warning(
            "No two positive physical roots were found for these parameters.")
        
