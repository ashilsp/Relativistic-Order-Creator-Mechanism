import numpy as np

def calculate_ocm_boundary(M, G=1.0, c=1.0):
    """
    Calculates the Rd boundary where Manifold Tension equals kappa-flux.
    Based on Section S1.4: Rd = 3GM/c^2
    """
    Rd = (3 * G * M) / (c**2)
    return Rd

def manifold_tension(r, M):
    """
    Derivative of the effective potential (Eq S3) representing 
    structural 'stiffness' of the manifold.
    """
    # V_eff = (1 - 2M/r) / r^2 (simplified for L=1)
    # The gradient is taken at the limit r -> 3M
    tension = (6 * M - 2 * r) / (r**4)
    return abs(tension)

# Example: Mass of a Supermassive Black Hole (e.g., TON 618)
M_example = 6.6e10 # Solar masses
print(f"Calculated Rd Boundary: {calculate_ocm_boundary(M_example)} units")
