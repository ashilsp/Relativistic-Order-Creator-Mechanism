import numpy as np
import matplotlib.pyplot as plt

def generate_cutoff_plot(kappa_node=1e35, Rd=1.5e13):
    # Constants from Eq S10
    e = 1.602e-19
    m_e = 9.109e-31
    
    # Calculate nu_c (Eq S10)
    nu_c = (1 / (2 * np.pi)) * np.sqrt((kappa_node * e**2) / (m_e * Rd**2))
    
    # Generate Frequency range
    frequencies = np.linspace(0, nu_c * 2, 1000)
    
    # Model Emissivity (Standard vs OCM)
    emissivity = np.exp(-frequencies / nu_c) 
    ocm_emissivity = np.where(frequencies <= nu_c, emissivity, 0)
    
    plt.figure(figsize=(8, 5))
    plt.plot(frequencies, emissivity, 'k--', label='Classical Bremsstrahlung')
    plt.plot(frequencies, ocm_emissivity, 'b-', linewidth=2, label='OCM Restricted')
    
    plt.axvline(x=nu_c, color='red', linestyle=':', label=f'Cutoff νc')
    plt.fill_between(frequencies, 0, 1, where=(frequencies > nu_c), 
                     color='gray', alpha=0.2, label='Dark Zone')
    
    plt.title("Bremsstrahlung Spectral Cutoff at Rd Interface (Eq. S10)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Normalized Emissivity")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    generate_cutoff_plot()
