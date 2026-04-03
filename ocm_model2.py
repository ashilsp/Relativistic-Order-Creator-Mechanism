import numpy as np

def calculate_rd_boundary(M, G=6.674e-11, c=3e8):
    """
    Calculates the Rd boundary radius (Eq. S5).
    Rd = 3GM / c^2
    """
    return (3 * G * M) / (c**2)

def bremsstrahlung_cutoff(kappa_node, Rd, e=1.602e-19, m_e=9.109e-31):
    """
    Calculates the radiative spectral cutoff frequency (Eq. S10).
    nu_c = (1 / 2pi) * sqrt( (kappa_node * e^2) / (m_e * Rd^2) )
    """
    term = (kappa_node * (e**2)) / (m_e * (Rd**2))
    nu_c = (1 / (2 * np.pi)) * np.sqrt(term)
    return nu_c

# Example calculation for a Supermassive Black Hole
# Mass M roughly 10^10 solar masses
M_sun = 1.989e30
M_bh = 10**10 * M_sun

Rd_value = calculate_rd_boundary(M_bh)
print(f"Phase Transition Boundary (Rd): {Rd_value:.2e} meters")

# Assuming a placeholder kappa_node flux density
print(f"Spectral Cutoff Frequency (nu_c): {bremsstrahlung_cutoff(1e35, Rd_value):.2e} Hz")
