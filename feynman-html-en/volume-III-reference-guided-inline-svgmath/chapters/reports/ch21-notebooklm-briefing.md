# The Schrödinger Equation in a Classical Context: A Seminar on Superconductivity

## Executive Summary

This briefing analyzes the transition of the Schrödinger equation from a microscopic probability-based framework to a macroscopic classical context, specifically through the lens of superconductivity. Traditionally, the wave function ($\psi$) is a mathematical tool representing the probability amplitude of a single particle, lacking direct classical significance. However, in systems where a massive number of particles—specifically Bose particles—occupy the same ground state, the wave function manifests as a physical field with observable macroscopic consequences.

The analysis covers the modification of the Schrödinger equation in magnetic fields, the local conservation of probability, and the distinction between kinematic and dynamical momentum. It culminates in an exploration of superconductivity, where electron pairs (acting as bosons) form a macroscopic quantum state. This state explains key phenomena: the Meissner effect (magnetic field expulsion), flux quantization (where magnetic flux is trapped in discrete units), and the Josephson effect (quantum tunneling between superconductors). These effects provide empirical evidence for the physical reality of the vector potential and allow for the development of hyper-precise measurement tools, such as the superconducting quantum interference device (SQUID).

---

## Key Mathematical Foundations

The behavior of superconducting systems is derived from the application of the Schrödinger equation to a macroscopic fluid of charged particles.

### Core Equations and Their Physical Meaning

| Concept | Formula | Physical Significance |
| :--- | :--- | :--- |
| **Magnetic Field Amplitude** | $\braket{b}{a}_{\text{in } \mathbf{A}} = \braket{b}{a}_{A=0} \cdot \exp\left[\frac{iq}{\hbar}\int_a^b\mathbf{A}\cdot d\mathbf{s}\right]$ | The presence of a vector potential $\mathbf{A}$ shifts the phase of the probability amplitude. |
| **Current Density ($\FLPJ$)** | $\FLPJ = \frac{\hbar}{m}\left(\boldsymbol{\nabla}{\theta}-\frac{q}{\hbar}\mathbf{A}\right)\rho$ | Relates the physical current to the gradient of the wave function's phase and the vector potential. |
| **London Equation** | $\FLPJ = -\rho \frac{q}{m} \mathbf{A}$ | Explains the exclusion of magnetic fields from the interior of a superconductor. |
| **Flux Quantization** | $2\pi n\hbar = q\Phi$ | Proves that trapped magnetic flux must exist in discrete units (multiples of $\frac{\pi\hbar}{q_e}$). |
| **Josephson Current** | $J = J_0 \sin \delta$ | The current across an insulator depends on the phase difference $\delta$ between two superconductors. |
| **Josephson Phase Rate** | $\dot{\delta} = \frac{qV}{\hbar}$ | Relates the rate of change of the phase difference to the voltage $V$ across the junction. |

---

## Analysis of Key Themes

### 1. The Macroscopic Interpretation of the Wave Function
Ordinarily, Born’s interpretation defines $\psi^*\psi$ as the probability density of finding a single particle. However, in superconductivity, billion of electron pairs occupy the same quantum state. In this scenario, $\psi^*\psi$ takes on a classical meaning as the actual **charge density** ($\rho$), and the probability current $\FLPJ$ becomes the **electric current density**. This mirrors how Maxwell’s equations for the electromagnetic field represent the wave function for vast numbers of photons in the same state.

### 2. Dual Definitions of Momentum
The seminar distinguishes between two types of momentum that arise in the presence of an electromagnetic field:
*   **Kinematic ($mv$-momentum):** The mass times velocity ($m\mathbf{v}$). This is what changes when a particle is subjected to an electric field force.
*   **Dynamical ($p$-momentum):** Defined as $\mathbf{p} = m\mathbf{v} + q\mathbf{A}$. In quantum mechanics, this $p$-momentum is associated with the gradient operator $\frac{\hbar}{i}\boldsymbol{\nabla}$.
The $p$-momentum remains unchanged during a sudden change in vector potential, while the $mv$-momentum changes immediately to compensate, ensuring the continuity of the wave function.

### 3. The Meissner Effect and London Equations
The Meissner effect describes the expulsion of magnetic fields from a superconductor as it is cooled below its critical temperature.
*   **Mechanism:** Inside a superconducting lump, the charge density $\rho$ is uniform. For the divergence of the current to be zero in a steady state, the phase $\theta$ must be constant.
*   **Result:** The current becomes directly proportional to the vector potential ($\FLPJ \propto -\mathbf{A}$).
*   **Penetration Depth:** Combining this with Maxwell’s equations shows that the vector potential $\mathbf{A}$ decreases exponentially from the surface. In metals like lead, the field only penetrates to a depth of approximately $2 \times 10^{-6}$ cm, leaving the interior field-free (Fig. 21–3).

### 4. Flux Quantization in Superconducting Rings
A unique quantum effect occurs when a superconductor is shaped like a ring. For the wave function to be single-valued, the phase $\theta$ must change by exactly $2\pi n$ when traversing the loop.
*   **Discovery of Pairings:** Initially, it was predicted that the charge $q$ in the flux equation would be the electronic charge $q_e$. However, experiments by Deaver-Fairbank and Doll-Näbauer found the flux unit was exactly half as large as predicted.
*   **Validation of BCS Theory:** This confirmed that the carriers in a superconductor are **electron pairs** ($q = 2q_e$). The basic flux unit is thus $\Phi_0 = \frac{\pi\hbar}{q_e} \approx 2 \times 10^{-7} \text{ gauss}\cdot\text{cm}^2$.

### 5. The Josephson Junction
When two superconductors are separated by a thin insulator (Fig. 21–6), electrons can "tunnel" through the barrier.
*   **DC Effect:** A current can flow with zero voltage across the junction, determined by the phase difference $\delta$.
*   **AC Effect:** Applying a DC voltage $V_0$ causes the phase to oscillate, resulting in an alternating current with no net DC component unless an external AC frequency $\omega = \frac{qV_0}{\hbar}$ is applied.
*   **Interference:** Using two Josephson junctions in parallel (Fig. 21–7) creates a quantum interferometer. The total current through the system varies oscillates with the magnetic flux $\Phi$ passing between the branches, allowing for the measurement of incredibly small magnetic fields.

---

## Important Quotes with Context

> **"The wave function for a single particle is a 'field'... but it does not generally have a classical significance. Nevertheless, there are some situations in which a quantum mechanical wave function does have classical significance."**
*   *Context:* This introduces the central premise of the seminar: that superconductivity allows us to observe quantum mechanics on a macroscopic scale.

> **"A pair is a Bose particle."**
*   *Context:* This explains why electrons, which are fermions, can all occupy the same ground state. By forming Cooper pairs, they follow Bose-Einstein statistics, leading to the "locking" of all particles into a single wave function.

> **"The absolute phase is not observable, but if the gradient of the phase is known everywhere, the phase is known except for a constant."**
*   *Context:* Discussing the physical reality of the phase $\theta$ in the wave function. In a superconductor, the phase is a "real thing" because its gradient determines the current density.

> **"The quantum mechanics which was discovered in 1926 has had nearly 40 years of development, and rather suddenly it has begun to be exploited in many practical and real ways."**
*   *Context:* The concluding reflection on the transition of quantum theory from abstract physics to the foundation of modern technology (transistors, lasers, and magnetometers).

---

## Actionable Insights and Physical Meanings

*   **Reality of the Vector Potential:** The interference effects in Josephson junctions occur even when the magnetic field $\mathbf{B}$ is shielded from the superconducting wires (using a tiny solenoid). This demonstrates that the vector potential $\mathbf{A}$ has a physical reality independent of the magnetic field $\mathbf{B}$ it produces.
*   **Precision Magnetometry:** The sensitivity of double-junction interference allows for the measurement of magnetic fields as small as $2 \times 10^{-7}$ gauss. This suggests that magnetic field measurement could eventually reach the precision of light wavelength measurements.
*   **The "Quantum Potential" Force:** The equations of motion for a superconducting fluid include a term $\boldsymbol{\nabla}\frac{\hbar^2}{2m} (\frac{1}{\sqrt{\rho}}\nabla^2\sqrt{\rho})$. This represents a "mystical" quantum mechanical force that only becomes significant at junctions or boundaries where the charge density $\rho$ changes rapidly.
*   **Superconductivity as Ideal Hydrodynamics:** The behavior of a superconductor can be modeled as an electrically charged ideal fluid where the curl of the velocity is proportional to the magnetic field ($\mathbf{c}url{\mathbf{v}} = -\frac{q}{m}\mathbf{B}$), rather than zero as in standard ideal fluids.