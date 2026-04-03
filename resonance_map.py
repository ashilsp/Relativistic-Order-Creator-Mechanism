import numpy as np
import matplotlib.pyplot as plt

def plot_resonance_map():
    # Create a 2D grid representing the manifold plane
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    
    # Modeling standing wave resonance (Bessel-like function)
    # This represents the geometric nodes of the Big Ring
    Z = np.cos(5 * R) * np.exp(-R**2/2)

    plt.figure(figsize=(7, 6))
    plt.pcolormesh(X, Y, Z, cmap='magma', shading='auto')
    plt.colorbar(label='Resonance Intensity')
    plt.title("Geometric Resonance Nodes (Big Ring 1.3 Gly Model)")
    plt.xlabel("Gly")
    plt.ylabel("Gly")
    plt.show()

if __name__ == "__main__":
    plot_resonance_map()
