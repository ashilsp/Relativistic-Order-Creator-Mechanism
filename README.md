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
