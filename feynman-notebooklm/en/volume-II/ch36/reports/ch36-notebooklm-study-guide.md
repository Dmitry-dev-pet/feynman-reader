# Study Guide: Ferromagnetism

This study guide explores the principles of ferromagnetism as outlined in the Feynman Lectures on Physics, Volume II, Chapter 36. It covers the mathematical description of magnetization currents, the definition of the magnetizing field $\FLPH$, the behavior of magnetic materials in circuits, and the microscopic origins of spontaneous magnetization.

---

## Key Concepts

### 1. Magnetization Currents ($\mathbf{j}_{\text{mag}}$)
Ferromagnetism involves induced magnetic moments far stronger than those in paramagnetism or diamagnetism. The magnetic state of matter is described macroscopically by $\FLPM$, the average magnetic dipole moment per unit volume.
*   **Physical Basis:** Magnetism arises from "Ampèrian" currents—circulating atomic currents from electron spin or orbital motion.
*   **Mathematical Relation:** The circulating atomic currents are equivalent to a macroscopic current density:
    $$\mathbf{j}_{\text{mag}} = \mathbf{curl} \FLPM$$
*   **Surface vs. Volume:** In a uniformly magnetized material, internal currents cancel out, leaving only a net surface current (similar to a solenoid). If magnetization varies ($\mathbf{curl} \FLPM \neq 0$), a net volume current density exists.

### 2. The Field $\FLPH$
The vector field $\FLPH$ is a derived quantity used to simplify Maxwell’s equations in the presence of magnetic materials.
*   **Definition:** $\FLPH = \mathbf{B} - \frac{\FLPM}{\epsilon_0 c^2}$
*   **Maxwell Equation:** $\epsilon_0 c^2 \mathbf{curl} \FLPH = \mathbf{j}_{\text{cond}} + \frac{\partial \FLPD}{\partial t}$
*   **Units and Confusion:** In the MKS system, $\mathbf{B}$ is measured in webers/meter² (tesla). Feynman defines $\FLPH$ to have the same units as $\mathbf{B}$. However, engineers often use a different definition ($\FLPH' = \epsilon_0 c^2 \mathbf{B} - \FLPM$) where $\FLPH$ has units of amperes/meter.

| Field | Feynman Unit | MKS/Engineering Unit |
| :--- | :--- | :--- |
| $\mathbf{B}$ | Weber/m² (Gauss) | Weber/m² |
| $\FLPH$ | Weber/m² (Oersted) | Ampere/meter ($\FLPH'$) |
| $\FLPM$ | Ampere/meter | Ampere/meter |

### 3. Hysteresis and Magnetization Curves
The relationship between $\mathbf{B}$ and $\FLPH$ in ferromagnetic materials is non-linear and depends on the material's history.
*   **Magnetization Curve:** The initial path $\mathbf{B}$ takes as $\FLPH$ increases from zero.
*   **Saturation:** The point where all atomic magnets are aligned; further increases in $\FLPH$ result in only marginal increases in $\mathbf{B}$.
*   **Hysteresis Loop:** When $\FLPH$ is cycled, the $\mathbf{B}$ field follows a loop. The area inside this loop represents energy lost as heat (**hysteresis loss**).
*   **Remanence:** The residual $\mathbf{B}$ field remaining when the magnetizing field $\FLPH$ returns to zero, allowing for permanent magnets.

### 4. Spontaneous Magnetization and the Curie Temperature
Ferromagnetic materials can exhibit magnetization even in the absence of an external field ($\FLPH = 0$).
*   **Curie Temperature ($T_c$):** The critical temperature above which ferromagnetic behavior disappears and the material becomes paramagnetic.
*   **Weiss Theory vs. Reality:** The classical "magnetic" explanation for ferromagnetism fails by a factor of 2600. The actual alignment is caused by non-magnetic quantum mechanical interactions (Pauli exclusion principle).
*   **Domains:** Large pieces of iron may have zero net magnetization because they are composed of many small "domains," each spontaneously magnetized in a different direction.

---

## Short-Answer Self-Check Questions

1.  **Why is a uniformly magnetized rod equivalent to a long solenoid?**
    The internal circulating atomic currents cancel each other out, leaving only the uncancelled currents at the surface to flow around the rod, mimicking a solenoid's windings.
2.  **What is the physical meaning of the area enclosed by a hysteresis loop?**
    The area represents the energy per unit volume lost as heat in the material during one full cycle of magnetization.
3.  **How is the "magnetizing field" $\FLPH$ related to the conduction current in a torus?**
    $H$ is directly proportional to the magnetizing current: $H = \frac{1}{\epsilon_0 c^2} \frac{NI}{l}$.
4.  **Why does the purely "magnetic" theory of the local field fail to explain ferromagnetism in nickel?**
    The predicted Curie temperature is $0.24^\circ \text{K}$, whereas the experimental value is $631^\circ \text{K}$. The magnetic interaction is too weak to cause alignment against thermal motion.
5.  **In an electromagnet with a small air gap, how does the magnetic field $\mathbf{B}$ in the gap compare to $\mathbf{B}$ in the iron?**
    Because $\mathbf{div} \mathbf{B} = 0$, the magnetic field $\mathbf{B}$ is approximately the same in both the iron and the gap, assuming the flux is contained.

---

## Essay Prompts for Deeper Exploration

1.  **The Role of Mathematical Analogy in Field Theory:** Explain how the equations of static ferromagnetism can be mapped onto the equations of electrostatics. Discuss the utility of the $\FLPH$ field and why Feynman warns that despite the mathematical similarity, the physics of $\FLPH$ and $\mathbf{E}$ is fundamentally different.
2.  **Energy Dynamics in Iron-Core Inductors:** Analyze the process of energy storage and loss in a ferromagnetic inductor. Compare an "ideal" air-core inductor to an iron-core inductor, focusing on why the latter provides higher inductance and how hysteresis affects efficiency.
3.  **From Microscopic Spins to Macroscopic Domains:** Discuss the discrepancy between the spontaneous magnetization of individual atoms and the observed zero magnetization of bulk iron. How does the concept of magnetic domains bridge this gap?

---

## Common Misconceptions

*   **"$\FLPH$ is the 'Real' Magnetic Field":** Historically, $\FLPH$ was treated as the primary field (the "magnetic poles" model). In reality, $\mathbf{B}$ and $\mathbf{E}$ are the fundamental physical fields; $\FLPH$ is a convenient mathematical construct for macroscopic averages.
*   **"Magnetic Forces Cause Alignment":** It is a common mistake to assume that the magnetic dipoles of atoms line up because of their magnetic attraction to one another. As shown by the failure of the $T_c$ calculation, these magnetic forces are far too weak to overcome thermal agitation.
*   **"Gauss and Oersteds are Different Units":** While given different names to distinguish $\mathbf{B}$ and $\FLPH$, in the system used by Feynman, they have the same dimensions and are physically the same size.

---

## Glossary of Important Terms

*   **Ampèrian Currents:** The microscopic, circulating currents within atoms that give rise to materials' magnetic properties.
*   **Curie Temperature ($T_c$):** The temperature at which a material transitions from ferromagnetic to paramagnetic behavior.
*   **Hysteresis:** The phenomenon where the state of a system (magnetization) depends on its previous history.
*   **Magnetization ($\FLPM$):** The magnetic dipole moment per unit volume of a material.
*   **Permeability ($\mu$):** The ratio of $\mathbf{B}$ to $\FLPH$ in the linear approximation ($B = \mu H$); it indicates how easily a material can be magnetized.
*   **Remanence (Residual Field):** The magnetization remaining in a ferromagnetic material after the external magnetizing field is removed.
*   **Saturation:** The state reached when an increase in the external magnetizing field produces no further significant increase in the material's magnetization.