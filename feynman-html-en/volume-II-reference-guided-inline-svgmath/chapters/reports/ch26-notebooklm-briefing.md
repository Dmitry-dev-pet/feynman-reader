# Lorentz Transformations of the Fields: Analytical Briefing

This briefing document provides a comprehensive analysis of the relativistic transformation of electromagnetic fields, as detailed in the technical records of Volume II, Chapter 26. It explores the synthesis of electric and magnetic fields into a single four-dimensional entity, the behavior of fields for charges in motion, and the relativistic notation of the equations of motion.

## Executive Summary

The transition from classical electrodynamics to relativistic electrodynamics reveals that electric and magnetic fields are not independent vectors but components of a single second-rank antisymmetric tensor ($F_{\mu\nu}$). For a charge moving at a constant velocity, the electric field remains radial from the "present" position but undergoes a geometric distortion—contracting in the direction of motion and intensifying in the transverse direction. This document outlines the mathematical framework for transforming these fields between inertial frames and establishes the four-dimensional notation for the forces acting on charged particles.

---

## 1. Potentials and the Principle of Retarded Time

The electromagnetic potential $A_\mu = (\phi, \mathbf{A})$ is a four-vector where $\phi$ is the scalar potential and $\mathbf{A}$ is the vector potential. The potentials at a specific point $(x, y, z)$ and time $t$ are determined not by the "present" position of a charge, but by its "retarded" position $P'$ at the time $t' = t - r'/c$.

### The Projected Position Method
For a charge moving with uniform velocity, the potentials can be expressed in terms of the coordinates from its current position $P$. For arbitrary motion, a "projected position" ($P_{\text{proj}}$) can be used to calculate potentials. This is an imaginary position the charge would occupy if it continued at its retarded velocity $v'$ during the delay time $(t' - t)$.

**Fundamental Postulates of Electrodynamics:**
1.  $A_\mu$ is a four-vector.
2.  The Coulomb potential for a stationary charge is $q / 4\pi\epsilon_0 r$.
3.  Potentials produced by a charge in any motion depend only on the velocity and position at the retarded time.

---

## 2. Fields of a Point Charge with Constant Velocity

When a charge moves at a constant speed $v$, the electric field $\mathbf{E}$ points radially from the charge’s "present" position. However, the field is no longer spherically symmetric.

### Geometric Distortion of the Electric Field
The field lines of a moving charge are "squashed" due to relativistic effects. This results in:
*   **Transverse Strength:** The field at right angles to the motion is increased by the factor $1 / \sqrt{1 - v^2/c^2}$.
*   **Longitudinal Strength:** The field ahead and behind the charge is reduced by the factor $(1 - v^2/c^2)$.

| Direction | Field Strength Formula | Comparison to Coulomb |
| :--- | :--- | :--- |
| **Sidewise (Transverse)** | $E = \frac{q}{4\pi\epsilon_0\sqrt{1-v^2/c^2}} \cdot \frac{1}{y^2+z^2}$ | Stronger than Coulomb |
| **Ahead/Behind (Longitudinal)** | $E = \frac{q(1-v^2/c^2)}{4\pi\epsilon_0(x-vt)^2}$ | Weaker than Coulomb |

### The Magnetic Field Component
For a moving charge, a magnetic field $\mathbf{B}$ is generated. It is related to the electric field by the velocity of the charge:
$$\mathbf{B} = \frac{\mathbf{v} \times \mathbf{E}}{c^2}$$
The $\mathbf{B}$-field circles around the line of motion, consistent with the magnetic field of a current.

---

## 3. The Electromagnetic Field Tensor ($F_{\mu\nu}$)

In four-dimensional space-time, $\mathbf{E}$ and $\mathbf{B}$ are not four-vectors. Because the curl operation in four dimensions involves six independent components (combinations of $x, y, z,$ and $t$), the fields are synthesized into an **antisymmetric tensor of the second rank**.

### Component Mapping
The tensor $F_{\mu\nu}$ is defined by the four-gradient and the four-potential: $F_{\mu\nu} = \nabla_\mu A_\nu - \nabla_\nu A_\mu$.

| Tensor Component | Physical Field Component |
| :--- | :--- |
| $F_{xt}, F_{yt}, F_{zt}$ | $E_x, E_y, E_z$ |
| $F_{xy}, F_{yz}, F_{zx}$ | $-B_z, -B_x, -B_y$ |
| $F_{\mu\mu}$ | 0 (Diagonal elements) |

### Transformation Laws
To find the fields in a moving frame ($S'$), the following transformations apply (assuming motion $v$ along the $x$-axis):

| Electric Field Transformation | Magnetic Field Transformation |
| :--- | :--- |
| $E_x' = E_x$ | $B_x' = B_x$ |
| $E_y' = \frac{E_y - vB_z}{\sqrt{1-v^2/c^2}}$ | $B_y' = \frac{B_y + vE_z/c^2}{\sqrt{1-v^2/c^2}}$ |
| $E_z' = \frac{E_z + vB_y}{\sqrt{1-v^2/c^2}}$ | $B_z' = \frac{B_z - vE_y/c^2}{\sqrt{1-v^2/c^2}}$ |

---

## 4. Relativistic Equations of Motion

Newton's Second Law ($F=ma$) is insufficient for high-velocity particles. The relativistically correct equation of motion is:
$$\frac{d}{dt} \left( \frac{m_0\mathbf{v}}{\sqrt{1-v^2/c^2}} \right) = \mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$$

### The Four-Force ($f_\mu$)
To maintain relativistic invariance, differentiation must be performed with respect to the **proper time** ($s$), where $ds = dt\sqrt{1-v^2/c^2}$. The "four-force" is then defined as:
$$f_\mu = \left( \frac{\mathbf{F} \cdot \mathbf{v}/c}{\sqrt{1-v^2/c^2}}, \frac{\mathbf{F}}{\sqrt{1-v^2/c^2}} \right)$$

The complete motion of a particle in an electromagnetic field is summarized by the elegant four-vector formula:
$$m_0 \frac{d^2x_\mu}{ds^2} = f_\mu = qu_\nu F_{\mu\nu}$$

---

## Important Quotes with Context

### On the Limits of Logical Deduction
> "It is sometimes said... that all of electrodynamics can be deduced solely from the Lorentz transformation and Coulomb’s law. Of course, that is completely false."

**Context:** This addresses the common misconception that relativity alone explains magnetism. It emphasizes that additional assumptions—such as the fact that potentials form a four-vector and depend only on velocity/position at the retarded time—are necessary to complete the theory.

### On the Reality of Field Lines
> "The miracle of it is that the picture you would see as the page flies by would still represent the field lines of the point charge... In this particular case, if you make the mistake of thinking that the field lines are somehow really there in space, and transform them, you get the correct field."

**Context:** Feynman explains that while field lines are a conceptual tool, the way they "contract" due to the Lorentz transformation actually yields the correct physical field densities for a moving charge.

### On Action and Reaction
> "There is a sidewise (magnetic) force on $q_1$ and no sidewise force on $q_2$. Does action not equal reaction? We leave it for you to worry about."

**Context:** Referring to two charges moving at right angles, Feynman highlights a paradox where the forces between them are not equal and opposite, challenging classical interpretations of Newton's Third Law in relativistic electrodynamics.

---

## Actionable Insights

*   **Field Intensification:** When designing systems involving high-speed particles (e.g., accelerators or cosmic ray detectors), assume the transverse electric field is significantly stronger than the static Coulomb field by the factor $\gamma = 1/\sqrt{1-v^2/c^2}$.
*   **Frame Dependency:** A "pure" static magnetic field in one frame will always appear as a combination of an electric and magnetic field in a moving frame. For slow-moving systems ($v \ll c$), the induced electric field is approximately $\mathbf{v} \times \mathbf{B}$.
*   **Computational Shortcut:** To find the fields of any system of fixed charges moving past an observer, calculate the static fields in the rest frame and apply the Lorentz transformation of Table 26-2.
*   **Measurement Limitations:** While motion through a magnetic field (like the Earth's) produces an electric field ($E = \mathbf{v} \times \mathbf{B}$), this effect is often masked by larger atmospheric fluctuations, making it impractical for applications like determining an airplane's ground speed.