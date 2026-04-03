import numpy as np
import matplotlib.pyplot as plt

def plot_s1_equilibrium():
    # Radial distance in units of M (Mass)
    r = np.linspace(2.1, 5, 500)
    
    # Equation S1 logic: Tension vs Flux Pressure
    # Representing the cross-over at r=3
    manifold_tension = 1 / (r**2)
    kappa_flux = (3 / r**3) 

    plt.figure(figsize=(8, 5))
    plt.plot(r, manifold_tension, 'b-', label=r'Manifold Tension ($\eta_m$)')
    plt.plot(r, kappa_flux, 'r--', label=r'$\kappa$-flux Pressure ($\rho_\kappa$)')
    
    # Mark the Rd interface
    plt.axvline(x=3, color='black', linestyle=':', label='$R_d \approx 3M$')
    plt.annotate('Equilibrium Point', xy=(3, 0.11), xytext=(3.5, 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05))

    plt.title("Equation S1: OCM Phase Transition Equilibrium")
    plt.xlabel("Radius ($r/M$)")
    plt.ylabel("Normalized Stress/Energy")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    plot_s1_equilibrium()
