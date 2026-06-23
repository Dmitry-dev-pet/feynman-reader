# Solutions of Maxwell’s Equations with Currents and Charges

## Executive Summary

This briefing explores the synthesis of Maxwell’s equations with the phenomena of light and electromagnetic radiation. The primary objective is to demonstrate that Maxwell’s equations serve as the foundational bedrock for the behavior of light by solving them in the presence of arbitrary currents and charges.

The analysis moves from the general solutions of wave equations to specific applications, including oscillating dipoles and moving point charges. Key findings include the derivation of **Retarded Potentials**, which account for the finite speed of light ($c$), and the **Liénard-Wiechert potentials**, which describe the fields of relativistic moving charges. Ultimately, this framework reveals that the laws of electromagnetism naturally lead to the Lorentz transformation, providing the historical and theoretical origins of Einstein’s relativity.

---

## Key Themes and Physical Analysis

### 1. The Synthesis of Light and Electromagnetism
The study of light is fundamentally the study of solutions to Maxwell’s equations involving waves of electricity and magnetism. While earlier treatments of light focused on the fields produced by moving charges (radio, light, x-rays), this analysis provides the mathematical bridge to show that these fields are direct consequences of Maxwell’s equations.

The complete electric field $\mathbf{E}$ of a charge moving in an arbitrary way is expressed as:
$$\mathbf{E}=\frac{q}{4\pi\epsilon_0}\biggl[ \frac{\mathbf{e} _{r'}}{r'^2}+\frac{r'}{c}\frac{d }{d t}\biggl( \frac{\mathbf{e}_{r'}}{r'^2}\biggr)+\frac{1}{c^2}\frac{d^2}{dt^2}\mathbf{e}_{r'} \biggr]$$

**Physical Components of the Electric Field:**
*   **Retarded Coulomb Field (Term 1):** The standard inverse-square field, but directed from the "retarded" position—where the charge was at time $t - r'/c$.
*   **Correction Term (Term 2):** Compensates for retardation by extrapolating the field linearly toward the future. For slowly changing fields, Terms 1 and 2 together approximate the instantaneous Coulomb field.
*   **Radiation Term (Term 3):** Dominates at large distances as it decreases only as $1/r$. It is proportional to the acceleration of the charge projected at right angles to the line of sight.

### 2. General Solutions for Potentials ($\phi$ and $\mathbf{A}$)
To solve Maxwell’s equations with sources (charge density $\rho$ and current density $\mathbf{j}$), the problem is reduced to solving the inhomogeneous wave equation:
$$\nabla^2\psi-\frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2}= -s$$

The solution for a point source involves "retardation": the effect at a distance $r$ at time $t$ depends on the source at time $(t - r/c)$. For spread-out sources, the general solutions (integrals) for the scalar potential $\phi$ and vector potential $\mathbf{A}$ are:

| Potential | Integral Formula |
| :--- | :--- |
| **Scalar Potential ($\phi$)** | $\phi(1,t)=\int\frac{\rho(2,t-r_{12}/c)}{4\pi\epsilon_0 r_{12}}dV_2$ |
| **Vector Potential ($\mathbf{A}$)** | $\mathbf{A}(1,t)=\int\frac{\mathbf{j}(2,t-r_{12}/c)}{4\pi\epsilon_0 c^2r_{12}}dV_2$ |

These integrals represent the "center of the universe of electromagnetism," providing a complete description of fields produced by any moving charges.

### 3. Radiation from an Oscillating Dipole
In a system where a charge $q$ oscillates (creating a dipole moment $\mathbf{p} = q\mathbf{d}$), the vector potential $\mathbf{A}$ produces spherical waves.

**Radiation Field Characteristics:**
*   **Magnetic Field ($\mathbf{B}$):** Far from the source, $\mathbf{B}$ depends on the acceleration of the charge ($\ddot{\mathbf{p}}$). Near the source, the formula reduces to the Law of Biot and Savart, as the retardation effects are partially canceled by second-order terms.
*   **Spatial Oscillation:** The radiation term arises because time variations at the source are translated into steep spatial variations (slopes) as waves propagate.
*   **The Radiation Formula:**
    $$\mathbf{B}=\frac{1}{4\pi\epsilon_0 c^2} \frac{[\dot{\mathbf{p}}+(r/c)\ddot{\mathbf{p}}]_{t-r/c}\times\mathbf{r}}{r^3}$$

### 4. The Liénard-Wiechert Potentials
For a point charge moving at high or relativistic velocities, a subtle "sweeping" effect occurs during the integration of the charge density. As the integral "sweeps over the charge," the movement of the charge toward or away from the observer changes the effective amount of charge contributing to the potential at any given instant.

**The Correction Factor:**
The potential is not simply $q/r'$, but must be corrected by the factor $\frac{1}{1-v_{r'}/c}$, where $v_{r'}$ is the component of the velocity toward the observation point.
$$\phi(1,t)=\frac{q}{4\pi\epsilon_0 r'[1-(v_r/c)]_{\text{ret}}}$$
This demonstrates that the perceived charge density is increased when the source moves toward the observer.

### 5. Electrodynamics and the Origin of Relativity
Calculations for a charge moving with uniform velocity $v$ reveal that Maxwell’s equations are inherently relativistic. By solving for the potential of a charge in steady motion, the Lorentz transformation emerges naturally:
$$\phi(x,y,z,t)= \frac{q}{4\pi\epsilon_0} \frac{1}{\sqrt{1-v^2/c^2}} \frac{1} {\biggl[ \biggl( \frac{x-vt}{\sqrt{1-v^2/c^2}} \biggr)^2+y^2+z^2 \biggr]^{1/2}}$$

This result shows that $\mathbf{A}$ and $\phi/c$ constitute a **four-vector**. Unlike Newtonian mechanics, the laws of Maxwell do not require "fixing up" for relativity; they were already correct.

---

## Important Quotes with Context

> **"If we can deduce Eq. (21.1) from Maxwell’s equations, we will really understand the connection between light and electromagnetism. To make this connection is the main purpose of this chapter."**
*Context:* Feynman establishes the instructional goal of uniting the disparate treatments of light (from Volume I) and Maxwell's equations (Volume II).

> **"So here is the center of the universe of electromagnetism—the complete theory of electricity and magnetism, and of light... It is all here. Here is the structure built by Maxwell, complete in all its power and beauty."**
*Context:* Following the presentation of the general integral solutions for $\phi$ and $\mathbf{A}$, emphasizing that these equations describe all classical electromagnetic phenomena.

> **"The static formulas are very accurate, much more accurate than you might think. Of course, the compensation only works for points close in."**
*Context:* Explaining how the retarded potential formulas for dipoles remarkably resemble the instantaneous Biot-Savart law at short distances because different retardation terms cancel each other out.

> **"The formulas of the Lorentz transformation... were discoveries made by Lorentz when he was studying the equations of electricity and magnetism."**
*Context:* Highlighting that special relativity was historically derived from the needs of electrodynamics, rather than vice-versa.

---

## Actionable Insights for Physical Analysis

1.  **Prioritize Retardation in Dynamic Systems:** When calculating fields for non-static charges, one must always use the "retarded" position $t' = t - r'/c$. The physical effect observed now is due to the charge's position and velocity in the past.
2.  **Use $1/r$ for Long-Range Effects:** In communication and optics (far-field), ignore the $1/r^2$ Coulomb terms. Focus exclusively on the acceleration of the charge, as this defines the radiation field.
3.  **Account for the Relativistic "Sweeping" Effect:** When dealing with high-speed particles, the scalar potential must include the $1/(1 - v_r/c)$ factor. Failure to do so ignores the fact that the charge moves while its own signal is being "emitted" from different parts of its volume.
4.  **Vector Potential as a Four-Vector:** Treat $\mathbf{A}$ and $\phi/c$ as a single entity under coordinate transformations. This simplifies calculations for systems moving at constant velocities, as they can be solved in the rest frame and then transformed using the Lorentz factor $1/\sqrt{1-v^2/c^2}$.