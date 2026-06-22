# Chapter 21: Solutions of Maxwell’s Equations with Currents and Charges

This study guide explores the connection between Maxwell’s equations and the phenomena of light and electromagnetic radiation. It details how the motion of charges and currents produces potentials and fields, accounting for the finite speed of light through the concept of retardation.

## Key Concepts

### 1. Light and Electromagnetic Waves
Maxwell’s equations provide the foundation for understanding radio waves, light, and x-rays. The electric and magnetic fields at a specific point depend on the position and motion of a charge at an earlier "retarded" time.
*   **The Retarded Time ($t'$):** Defined as $t' = t - r'/c$, where $r'$ is the distance from the charge’s retarded position to the field point.
*   **The Three-Term Electric Field Equation:** The complete field of a point charge consists of:
    1.  **The Retarded Coulomb Field:** Points away from the retarded position; follows the $1/r'^2$ law.
    2.  **The Correction Term:** Compensates for retardation by extrapolating the field change linearly.
    3.  **The Radiation Term:** Dominates at large distances; follows a $1/r$ law and depends on the acceleration of the charge projected at right angles to the line of sight.

### 2. General Solutions for Potentials
To solve Maxwell’s equations with sources (charges $\rho$ and currents $\mathbf{j}$), we utilize the scalar potential $\phi$ and the vector potential $\mathbf{A}$. These satisfy the wave equations:
$$\nabla^2\phi - \frac{1}{c^2} \frac{\partial^2\phi}{\partial t^2} = -\frac{\rho}{\epsilon_0}$$
$$\nabla^2\mathbf{A} - \frac{1}{c^2} \frac{\partial^2\mathbf{A}}{\partial t^2} = -\frac{\mathbf{j}}{\epsilon_0 c^2}$$

The general solutions are integrals over all source elements at their respective retarded times:
*   **Scalar Potential:** $\phi(1,t) = \int \frac{\rho(2, t-r_{12}/c)}{4\pi\epsilon_0 r_{12}} dV_2$
*   **Vector Potential:** $\mathbf{A}(1,t) = \int \frac{\mathbf{j}(2, t-r_{12}/c)}{4\pi\epsilon_0 c^2 r_{12}} dV_2$

### 3. The Oscillating Dipole
An oscillating dipole ($\mathbf{p} = q\mathbf{d}$) creates radiation. In the nonrelativistic case:
*   **Vector Potential:** $\mathbf{A}$ is proportional to the first derivative of the dipole moment ($\dot{\mathbf{p}}$) at the retarded time.
*   **Radiation Field:** The magnetic field $\mathbf{B}$ and electric field $\mathbf{E}$ far from the source decrease only as $1/r$ and are proportional to the acceleration of the charge ($\ddot{\mathbf{p}}$).
*   **Physical Mechanism:** The radiation term arises because time variations at the source are translated into spatial variations as waves propagate, creating steep slopes (derivatives) in the potentials.

### 4. Liénard-Wiechert Potentials
For a point charge moving at any velocity (including relativistic), the potentials are modified by a factor that accounts for the "sweeping" of the charge during the time light travels across it.
*   **The Correction Factor:** $1 / (1 - v_r/c)$, where $v_r$ is the component of velocity toward the observation point.
*   **Potentials:**
    $$\phi(1,t) = \frac{q}{4\pi\epsilon_0 [r - (\mathbf{v}\cdot\mathbf{r}/c)]_{\text{ret}}}$$
    $$\mathbf{A}(1,t) = \frac{q\mathbf{v}_{\text{ret}}}{4\pi\epsilon_0 c^2 [r - (\mathbf{v}\cdot\mathbf{r}/c)]_{\text{ret}}}$$

### 5. Relativity and Maxwell’s Equations
Maxwell’s equations naturally lead to the Lorentz transformation. Calculating the potentials of a charge moving with uniform velocity reveals coordinates transformed by $\sqrt{1 - v^2/c^2}$. Potentials $\mathbf{A}$ and $\phi/c$ function as a four-vector, and the laws of electrodynamics remain correct under Einstein’s relativity without modification.

---

## Self-Check Questions

### Short-Answer Quiz
1.  **What is "retarded distance"?**
    *   It is the distance between the field point and the position the charge occupied at the earlier time $t - r'/c$.
2.  **Why do the first two terms of the electric field equation for a moving charge approximate the "instantaneous Coulomb field" for low velocities?**
    *   The second term acts as a linear extrapolation that compensates for the delay in the first (retarded) term, effectively shifting the field to where the charge is at the current time $t$.
3.  **What determines the direction of the magnetic field $\mathbf{B}$ in the radiation zone of an oscillating dipole?**
    *   The direction is given by $\ddot{\mathbf{p}} \times \mathbf{r}$, meaning it is at right angles to both the radius vector and the acceleration of the charge.
4.  **In the Liénard-Wiechert potential, what happens to the scalar potential as the charge's velocity toward the observer ($v_r$) approaches the speed of light?**
    *   The term $(1 - v_r/c)$ approaches zero, causing the potential to become very large.
5.  **What is the relationship between the vector potential $\mathbf{A}$ and the scalar potential $\phi$ for a charge moving with a constant velocity $\mathbf{v}$?**
    *   $\mathbf{A} = \frac{\mathbf{v}}{c^2}\phi$.

### Essay Questions
1.  **Synthesize the connection between Maxwell’s equations and the wave nature of light.**
    *   *Guidance:* Discuss how the wave equations for $\phi$ and $\mathbf{A}$ are derived from Maxwell's equations and how the solutions represent spherical waves traveling at speed $c$. Explain that these mathematical solutions describe the same physical phenomena—light, radio, and x-rays—previously studied in optics.
2.  **Analyze the derivation of the radiation term in an oscillating dipole.**
    *   *Guidance:* Explain why the spatial derivatives of the vector potential do not simply result in a $1/r^2$ field. Focus on how the oscillation $p = p_0 \sin \omega t$ creates spatial variations in the potential wave that, when differentiated, produce a $1/r$ term proportional to $\omega^2$ (or acceleration).
3.  **Evaluate the "Sweeping" effect in the Liénard-Wiechert potentials.**
    *   *Guidance:* Describe the thought experiment of a cubical charge distribution moving toward an observer. Explain how the observer's "integration" of the charge density picks up different parts of the cube at different retarded times, effectively stretching the volume of charge seen by the observer.

---

## Common Misconceptions

| Misconception | Reality |
| :--- | :--- |
| **Instantaneous Influence:** Changes in charge position affect the field at distant points immediately. | **Retardation:** Information about charge motion travels at the speed $c$. Fields depend on the position/motion of the charge at the retarded time $t - r'/c$. |
| **Simple Retarded Potential:** The scalar potential of a moving point charge is simply $q/4\pi\epsilon_0 r'$. | **Correction Factor:** The motion of the charge during the retardation delay requires a correction factor $1/(1 - v_r/c)$, resulting in the Liénard-Wiechert potentials. |
| **Static Formulas are Inaccurate:** Static laws like Biot and Savart are useless for moving charges. | **Compensating Terms:** For small distances and low velocities, the retardation effects in the first-order terms often cancel out, making static formulas surprisingly accurate. |
| **Relativity "Fixes" Maxwell:** Maxwell's equations had to be adjusted to fit Einstein's relativity. | **Intrinsic Consistency:** Maxwell's equations are already relativistically correct. The Lorentz transformation was actually discovered through the study of Maxwell's equations. |

---

## Concise Glossary

*   **$\mathbf{A}$ (Vector Potential):** A vector field used to calculate the magnetic field ($\mathbf{B} = \text{curl } \mathbf{A}$).
*   **Dipole Moment ($\mathbf{p}$):** The product of charge $q$ and displacement $\mathbf{d}$; its derivatives ($\dot{\mathbf{p}}, \ddot{\mathbf{p}}$) drive electromagnetic radiation.
*   **Liénard-Wiechert Potentials:** The complete scalar and vector potentials for a single point charge in arbitrary motion.
*   **$\phi$ (Scalar Potential):** A scalar field used to calculate the electric field ($\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$).
*   **Radiation Term:** The component of the electromagnetic field that decreases as $1/r$, allowing energy to be transported over large distances.
*   **Retardation:** The delay between a cause (charge motion at point 2) and its effect (field measured at point 1) due to the finite speed of light.
*   **Source Function ($s$):** A general term for charge density ($\rho$) or current density ($\mathbf{j}$) that generates potentials.
*   **Wave Equation:** A second-order partial differential equation describing how waves (like $\phi$ or $\mathbf{A}$) propagate through space over time.