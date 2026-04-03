import numpy as np
import matplotlib.pyplot as plt

def generate_ocm_plot():
    # Physical Constants (Standard SI)
    e = 1.602e-19
    m_e = 9.109e-31
    
    # Parameters based on OCM Theory (Eq. S10)
    kappa_node = 1e35  # Flux density at interface
    Rd = 1.5e13        # Example Rd for a supermassive node
    
    # Calculate Cutoff Frequency nu_c
    nu_c = (1 / (2 * np.pi)) * np.sqrt((kappa_node * e**2) / (m_e * Rd**2))
    
    # Frequency range for plotting
    nu = np.linspace(0.01 * nu_c, 2.5 * nu_c, 1000)
    
    # Standard Bremsstrahlung Model (Exponential Decay)
    emissivity_std = np.exp(-nu / nu_c)
    
    # OCM Truncated Model
    emissivity_ocm = np.where(nu <= nu_c, emissivity_std, 0)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(nu, emissivity_std, 'k--', alpha=0.6, label='Classical Bremsstrahlung (Theoretical)')
    plt.plot(nu, emissivity_ocm, color='#1f77b4', linewidth=2.5, label='OCM Regulated Emission')
    
    # Visual cues for the "Dark Zone"
    plt.axvline(x=nu_c, color='red', linestyle='-', linewidth=1, label=r'Cutoff Frequency $\nu_c$')
    plt.fill_between(nu, 0, 1.1, where=(nu > nu_c), color='gray', alpha=0.15, label='OCM Dark Zone')
    
    # Formatting to match "A Relativistic Order Creator Mechanism"
    plt.title("Radiative Suppression at the $R_d$ Interface", fontsize=14)
    plt.xlabel(r"Frequency $\nu$ (Hz)", fontsize=12)
    plt.ylabel(r"Emissivity $\epsilon_\nu$ (Normalized)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.ylim(0, 1.1)
    
    print(f"Calculated Cutoff Frequency (nu_c): {nu_c:.2e} Hz")
    plt.show()

if __name__ == "__main__":
    generate_ocm_plot()
