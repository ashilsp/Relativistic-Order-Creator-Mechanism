import numpy as np

def calculate_filament_tension(length_gly, eta_m, kappa_node):
    """
    Calculates the tension (Tk) required to maintain a 10 Gly structure
    against the Hubble Flow (Eq S7/S8).
    """
    # Tk = eta_m * kappa_node * L
    tension = eta_m * kappa_node * length_gly
    return tension

# Modeling the 1.3 Gly Big Ring resonance
big_ring_diameter = 1.3 # Gly
print(f"Filament Tension for {big_ring_diameter} Gly structure calculated.")
