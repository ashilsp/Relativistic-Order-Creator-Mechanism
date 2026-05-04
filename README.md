# Relativistic-Order-Creator-Mechanism

Numerical implementation of the **Order Creator Mechanism (OCM)** for non-singular black hole interiors and the mass-energy equivalence of the Dark Sector.

## Overview
This repository provides the computational framework for the OCM, which identifies the $R_d$ interface (at $r \approx 3M$) as a physical, stress-energy stabilized boundary.

## Key Features
* **Equilibrium Modeling**: Calculates the balance between Manifold Tension ($\eta_m$) and $\kappa$-flux energy density ($\rho_{\kappa}$).
* **Spectral Cutoff**: Computes the radiative Bremsstrahlung cutoff frequency ($\nu_c$) at the phase-transition boundary.
* **Geometric Resonance**: Models manifold standing waves responsible for large-scale structures like the 1.3 Gly Big Ring.

## Files
* `ocm_model.py`: Calculations for the $R_d$ boundary.
*  `ocm_model2.py`: Core calculations for the $R_d$ boundary and spectral cutoff.
* `resonance_mapper.py`: Simulation of manifold harmonic resonances and filaments.
* `plot_equilibrium.py`: Graphs showing  two lines intersecting exactly at the 3M mark.
* `resonance_map.py`: This script models the harmonic standing waves mentioned in our supplementary material (the math that explains why we see 1.3 Gly structures like the Big Ring). It creates a "Heat Map" of resonance nodes.
## Reference
Based on the paper: *A Relativistic Order Creator Mechanism for Non-Singular Black Hole Interiors and the Mass-Energy Equivalence of the Dark Sector.*

## Supplemental Materials (Videos)

The OCM framework is supported by a suite of 16 high-resolution simulations. These videos visualize the transition from chaotic GR singularities to ordered OCM nodes.

### Video Index (v2.0)
| ID | Simulation Title | Research Significance |
|:---|:---|:---|
| **S1-S4** | **The $R_d$ Transition** | Visualizing non-singular geometric arrest and laminar flow. |
| **S5-S8** | **Mass-Flow & Metrics** | Demonstration of Super-Eddington flux and metric stabilization. |
| **S9-S12** | **Cosmic Resonances** | GW Echoes, Dark Matter ratios, and the HCB Great Wall ($L_{res}$). |
| **S13-S16**| **The Planck Floor** | Spacetime bulk modulus and vacuum impedance ($Z_{man}$). |

> [!TIP]
> **[Click Here to Download the Full v2.0 Simulation Suite](https://github.com/ashilsp/Relativistic-Order-Creator-Mechanism/releases/tag/v2-simulations)**
> *Note: High-resolution files are hosted as Release Assets to ensure repository performance.*
