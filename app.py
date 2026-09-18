import streamlit as st

from r_ab import calculate_r_ab
from r_bc import calculate_r_bc


# --------------------------------------------------
# Streamlit page
# --------------------------------------------------

st.title("Calculation of $r_{ab}$ and $r_{bc}$")

st.write(
    "Calculate the boundaries between the different "
    "regions using their respective equations."
)


# --------------------------------------------------
# Equations
# --------------------------------------------------

st.subheader("Equations")

st.latex(
    r"""
    \frac{r_{ab}}
    {\left(1-r_{ab}^{-1/2}\right)^{16/21}}
    =
    150(\alpha m)^{2/21}\dot{m}^{16/21}
    """
)

st.latex(
    r"""
    r_{bc}
    =
    6.3\times10^3
    \dot{m}^{2/3}
    \left(1-r_{bc}^{-1/2}\right)^{2/3}
    """
)


# --------------------------------------------------
# Input parameters
# --------------------------------------------------

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

if st.button("Calculate $r_{ab}$ and $r_{bc}$"):

    try:

        # Calculate r_ab
        r_ab_1, r_ab_2 = calculate_r_ab(
            alpha,
            m,
            mdot
        )

        # Calculate r_bc
        r_bc_1, r_bc_2 = calculate_r_bc(
            mdot
        )

        # --------------------------------------------------
        # Display r_ab
        # --------------------------------------------------

        st.subheader(r"$r_{ab}$")

        st.write("First mathematical solution:")

        st.latex(
            rf"""
            r_{{ab,1}} = {r_ab_1:.8f}
            """
        )

        st.write("Second mathematical solution:")

        st.latex(
            rf"""
            r_{{ab,2}} = {r_ab_2:.8f}
            """
        )

        # --------------------------------------------------
        # Display r_bc
        # --------------------------------------------------

        st.subheader(r"$r_{bc}$")

        if r_bc_1 is not None:

            st.write("First mathematical solution:")

            st.latex(
                rf"""
                r_{{bc,1}} = {r_bc_1:.8f}
                """
            )

        if r_bc_2 is not None:

            st.write("Second mathematical solution:")

            st.latex(
                rf"""
                r_{{bc,2}} = {r_bc_2:.8f}
                """
            )

    except ValueError as error:

        st.error(str(error))
