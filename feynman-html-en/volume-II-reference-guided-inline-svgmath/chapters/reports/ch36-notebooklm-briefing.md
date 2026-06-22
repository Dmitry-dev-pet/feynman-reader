# Chapter 36: Ferromagnetism – Analytical Briefing

This briefing document provides a comprehensive analysis of the physical principles, mathematical formulations, and macroscopic behaviors of ferromagnetic materials, based on the physics of large induced magnetic moments and their internal dynamics.

## Executive Summary

Ferromagnetism represents a state in matter where induced magnetic moments are so strong they become the dominant factor in producing observed magnetic fields. Unlike paramagnetic or diamagnetic materials, ferromagnetic substances like iron and nickel exhibit massive induced moments that require a specialized mathematical framework. This chapter establishes the relationship between magnetization ($\FLPM$) and current density ($\mathbf{j}_{\text{mag}}$), defines the auxiliary field $\FLPH$, and explores the nonlinear phenomena of hysteresis and saturation. While a classical "magnetic" approach to spontaneous magnetization fails to account for experimental observations by a factor of 2600, it provides the groundwork for understanding the Curie temperature and the necessity of quantum mechanical explanations for the strong alignment of atomic spins.

---

## I. Mathematical Foundations: Magnetization Currents

The internal properties of magnetic matter are described by the magnetization vector $\FLPM$, the average dipole moment per unit volume. The magnetic effects of matter arise from circulating "Ampèrian" atomic currents—spinning electrons or orbital motions—rather than mythical "magnetic poles."

### 1. Equivalent Current Density
The total current density $\mathbf{j}$ in a material is categorized into three components:
$$\mathbf{j}=\mathbf{j}_{\text{pol}}+\mathbf{j}_{\text{mag}}+\mathbf{j}_{\text{cond}}$$
Where $\mathbf{j}_{\text{pol}}$ is the polarization current and $\mathbf{j}_{\text{cond}}$ is the conduction current. The specific contribution from magnetized material is given by the curl of the magnetization:
$$\mathbf{j}_{\text{mag}}=\mathbf{c}url{\FLPM}$$

### 2. Physical Meaning of the Curl of M
*   **Uniform Magnetization:** Inside a uniformly magnetized rod, neighboring atomic current loops cancel each other out, resulting in zero net internal current. However, at the surface, these currents do not cancel, creating a net surface current equivalent to a solenoid.
*   **Non-uniform Magnetization:** If $\FLPM$ varies between neighboring regions, the cancellation of circulating currents is imperfect. This gradient produces a net volume current density. For example, a variation of $M_z$ in the $x$-direction contributes to a current density in the $y$-direction: $j_y = -\partial M_z / \partial x$.

---

## II. The Auxiliary Field H

To manage the complexity of internal currents, a new vector field $\FLPH$ is defined to relate the magnetic field $\mathbf{B}$ to the magnetization $\FLPM$.

### 1. Definition and Maxwell’s Equation
The field $\FLPH$ is defined as:
$$\FLPH = \mathbf{B} - \frac{\FLPM}{\epsilon_0 c^2}$$
In this framework, the Maxwell equation for the curl of $\FLPH$ (for static or slowly varying fields) simplifies to:
$$\epsilon_0 c^2 \mathbf{c}url{\FLPH} = \mathbf{j}_{\text{cond}}$$
This implies that $\FLPH$ is directly driven by conduction currents, earning it the name "magnetizing field."

### 2. Units and Conventions
There is significant naming and unit confusion across different systems (mks vs. others). The following table summarizes the relationships:

| Property | Unit / Relationship |
| :--- | :--- |
| **B (Magnetic Field)** | Weber/meter$^2$ (10$^4$ gauss) |
| **H (Our Definition)** | Weber/meter$^2$ (10$^4$ oersted) |
| **H' (Engineer's H)** | Ampere/meter |
| **Conversion** | $H \text{ (gauss)} = 0.0126 H' \text{ (amp/meter)}$ |

---

## III. Macroscopic Behavior: Hysteresis and Inductance

The relationship between $\mathbf{B}$ and $\FLPH$ in ferromagnetic materials is famously complex, being both nonlinear and history-dependent.

### 1. The Magnetization Curve and Hysteresis
*   **Saturation:** As $\FLPH$ increases, $\FLPM$ eventually levels off. The iron "saturates," and further increases in $\FLPH$ only yield a proportional increase in $\mathbf{B}$ with unit slope.
*   **Hysteresis Loop:** The value of $\mathbf{B}$ depends on the "past history" of the material. If $\FLPH$ is reduced to zero after saturation, a residual field (remanence) remains. Repeatedly oscillating the current creates a loop.
*   **Hysteresis Loss:** The energy density required to drive a material through one cycle is the area enclosed by the hysteresis loop: $u = \epsilon_0 c^2 \int H \, dB$. This energy is lost as heat.

### 2. Iron-Core Inductances
Iron cores allow for much larger fields and higher inductances for a given current. The iron atoms act as "slave magnets" that line up to produce a tremendously greater magnetic current than the winding current alone.
*   **Permeability ($\mu$):** For small loops, $B \approx \mu H$, where $\mu$ is the permeability (often several thousand).
*   **Inductance Formula:** $\selfInd = \frac{\mu N^2 A}{\epsilon_0 c^2 l}$

---

## IV. Microscopic Theory: Spontaneous Magnetization

The central mystery of ferromagnetism is why moments align so strongly even without an external field.

### 1. The Local Field Paradox
Using the "spherical hole" approximation (analytically derived from dielectrics), the local field $\mathbf{B}_a$ acting on an atom should be:
$$\mathbf{B}_a = \FLPH + \lambda \frac{\FLPM}{\epsilon_0 c^2}$$
In the spherical model, $\lambda = 1/3$.

### 2. The Curie Temperature (T$_c$)
The theory predicts a critical temperature above which thermal motions destroy alignment. This Curie temperature is defined by:
$$T_c = \lambda \frac{N \mu^2}{k \epsilon_0 c^2}$$
*   **Theoretical Failure:** For Nickel, using $\lambda = 1/3$ predicts $T_c = 0.24^\circ\text{K}$. The actual observed $T_c$ is $631^\circ\text{K}$.
*   **Conclusion:** The purely "magnetic" interaction is too weak by a factor of **2600**. Ferromagnetism must be driven by a non-magnetic interaction—quantum mechanical exchange forces related to the Pauli exclusion principle—that forces spins to align.

---

## V. Important Quotes with Context

> **"The induced moments are so strong that they are often the dominant effect in producing the observed fields."**
*   *Context:* Introducing the scale of ferromagnetism compared to the weak effects seen in paramagnetism and diamagnetism.

> **"Physically, the field in the hole is reduced because of the surface currents—which are given by $\mathbf{c}url{\FLPM}$."**
*   *Context:* Explaining the microscopic field inside a material and why the geometry of a cavity (needle, disc, or sphere) changes the observed field.

> **"It is as if we had a lot more current going through the coil than we really have. When we reverse the current, all the little magnets flip over... and we get a much higher induced emf."**
*   *Context:* Describing the efficiency of iron-core inductors and the "slave magnet" behavior of internal atomic moments.

> **"Clearly, our 'magnetic' theory of ferromagnetism is a dismal failure."**
*   *Context:* Acknowledging that classical electrostatics analogies cannot explain the massive internal fields required for spontaneous magnetization at room temperature.

---

## VI. Actionable Insights

1.  **Field Design for Electromagnets:** To calculate the field in a gap, one must solve the intersection of the magnetizing line $H_1 l_1 + H_2 l_2 = NI / \epsilon_0 c^2$ with the specific material's hysteresis curve. The field is not just a function of current, but of the sequence in which the current was applied.
2.  **Material Selection for Transformers:** To minimize "hysteresis loss," engineers must select "transformer irons" (e.g., iron-silicon alloys) designed with narrow hysteresis loops.
3.  **Permanent Magnet Criteria:** A good permanent magnet requires a material with a "wide hysteresis loop" (high coercive force) to maintain a high residual $\mathbf{B}$ field when the external magnetizing current is zero.
4.  **The Domain Constraint:** Although microscopic theory predicts spontaneous magnetization below $T_c$, bulk materials may show zero net magnetization due to the formation of "domains"—small regions magnetized in different directions that cancel each other out on a macroscopic scale.