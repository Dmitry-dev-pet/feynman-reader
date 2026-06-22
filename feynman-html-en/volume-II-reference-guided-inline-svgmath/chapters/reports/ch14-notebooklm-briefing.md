# Chapter 14: The Magnetic Field in Various Situations

This briefing document analyzes the mathematical and physical properties of the magnetic field in steady-current situations (magnetostatics). It focuses on the introduction of the vector potential $\mathbf{A}$ as a primary tool for solving magnetic problems and explores its application across various configurations, from simple wires to complex solenoids and dipoles.

## Executive Summary

The study of magnetostatics is governed by two basic equations: $\text{div } \mathbf{B} = 0$ and $c^2 \text{curl } \mathbf{B} = \mathbf{j}/\epsilon_0$. Because the divergence of the magnetic field is always zero, it can be represented as the curl of another vector field, the **vector potential $\mathbf{A}$**. This potential is not unique, allowing for the selection of a "gauge" (specifically $\text{div } \mathbf{A} = 0$ in magnetostatics) that simplifies calculations.

The core takeaway is that calculating the magnetic field can be broken down into three independent electrostatic-like problems. Each component of the vector potential ($A_x, A_y, A_z$) corresponds to the electrostatic potential produced by a charge density proportional to the respective current density component ($j_x, j_y, j_z$). This methodology allows for the determination of magnetic fields for wires, solenoids, and small loops (magnetic dipoles) by leveraging existing knowledge of electrostatic potentials.

---

## I. Mathematical Foundations of the Vector Potential

### 1. Definition and Gauge Latitude
The vector potential $\mathbf{A}$ is defined such that:
$$\mathbf{B} = \text{curl } \mathbf{A}$$
This relationship automatically satisfies $\text{div } \mathbf{B} = 0$. However, $\mathbf{A}$ is not unique. One can add the gradient of any scalar field $\psi$ to $\mathbf{A}$ without changing the resulting $\mathbf{B}$ field:
$$\mathbf{A}' = \mathbf{A} + \nabla\psi$$

To standardize $\mathbf{A}$ for magnetostatics, the convention is to set:
$$\text{div } \mathbf{A} = 0$$

### 2. The Governing Equations
Using the vector identity $\text{curl}(\text{curl } \mathbf{A}) = \nabla(\text{div } \mathbf{A}) - \nabla^2 \mathbf{A}$ and the gauge choice $\text{div } \mathbf{A} = 0$, the basic magnetostatic equation transforms into:
$$\nabla^2 \mathbf{A} = -\frac{\mathbf{j}}{\epsilon_0 c^2}$$

This results in three independent Poisson equations, one for each Cartesian component:
| Component | Equation |
| :--- | :--- |
| **x-component** | $\nabla^2 A_x = -j_x / \epsilon_0 c^2$ |
| **y-component** | $\nabla^2 A_y = -j_y / \epsilon_0 c^2$ |
| **z-component** | $\nabla^2 A_z = -j_z / \epsilon_0 c^2$ |

### 3. General Integral Solution
The general solution for the vector potential at point (1) due to currents at point (2) is:
$$\mathbf{A}(1) = \frac{1}{4\pi\epsilon_0 c^2} \int \frac{\mathbf{j}(2) \, dV_2}{r_{12}}$$

---

## II. Analysis of Key Physical Situations

The source context provides detailed analysis of four primary configurations.

### 1. Uniform Magnetic Field
In a uniform field $\mathbf{B}_0$ directed along the $z$-axis, the vector potential can be represented as:
$$\mathbf{A} = \frac{1}{2} \mathbf{B}_0 \times \mathbf{r}'$$
Where $\mathbf{r}'$ is the displacement from the $z$-axis.
*   **Physical Meaning:** $\mathbf{A}$ rotates about the $z$-axis. Its circulation around any closed loop is equal to the magnetic flux $\mathbf{B}$ through that loop.
*   **Formula:** $A = Br'/2$

### 2. The Straight Wire
For an infinite wire of radius $a$ carrying current $I$ along the $z$-axis:
*   **Vector Potential:** Outside the wire, $A_x = 0$ and $A_y = 0$. The $z$-component is:
    $$A_z = -\frac{I}{2\pi\epsilon_0 c^2} \ln r'$$
*   **Magnetic Field:** Calculated by taking the curl of $\mathbf{A}$, resulting in the standard circular field:
    $$B = \frac{1}{4\pi\epsilon_0 c^2} \frac{2I}{r'}$$

### 3. The Long Solenoid
A long solenoid with surface current density $J$ (where $J = nI$) exhibits unique properties outside its volume:
*   **Field Discrepancy:** Inside the solenoid, there is a uniform magnetic field. Outside, the magnetic field $\mathbf{B}$ is zero. However, the vector potential $\mathbf{A}$ is **not** zero outside.
*   **A-Field Magnitude:** Outside, $A$ circulates around the solenoid with magnitude:
    $$A = \frac{nIa^2}{2\epsilon_0 c^2} \frac{1}{r'}$$
*   **Rotating Cylinders:** A rotating charged cylinder produces the same magnetic field as a solenoid. However, the text notes that while rotation induces effects (like charges on a radial wire), these cannot be analyzed from the frame of the rotating cylinder, as it is not an inertial frame.

### 4. The Magnetic Dipole (Small Loops)
At large distances, any small current loop of any shape produces a "dipole field."
*   **Magnetic Moment ($\mu$):** Defined as the current times the area of the loop ($\mu = I \times \text{Area}$).
*   **Vector Potential of a Dipole:**
    $$\mathbf{A} = \frac{1}{4\pi\epsilon_0 c^2} \frac{\boldsymbol{\mu} \times \mathbf{e}_R}{R^2}$$
*   **B-Field Behavior:** The components of the $\mathbf{B}$-field for a magnetic dipole are mathematically identical to the $\mathbf{E}$-field components of an electric dipole.

---

## III. Direct Integration: The Law of Biot and Savart

While the vector potential is often easier for complex problems, the magnetic field can be calculated directly using the Biot-Savart Law.

### Formulas for B-Field Calculation
| Source Type | Formula |
| :--- | :--- |
| **Volume Current** | $\mathbf{B}(1) = \frac{1}{4\pi\epsilon_0 c^2} \int \frac{\mathbf{j}(2) \times \mathbf{e}_{12}}{r_{12}^2} dV_2$ |
| **Thin Wire (Circuit)** | $\mathbf{B}(1) = -\frac{1}{4\pi\epsilon_0 c^2} \int \frac{I \mathbf{e}_{12} \times d\mathbf{s}_2}{r_{12}^2}$ |

**Observation on Complexity:** The integrals for $\mathbf{B}$ are typically more complicated than those for $\mathbf{A}$ due to the cross product in the integrand.

---

## IV. Important Quotes with Context

*   **On the utility of the Vector Potential:**
    > "The x-component of vector potential arising from a current density $\mathbf{j}$ is the same as the electric potential $\phi$ that would be produced by a charge density $\rho$ equal to $j_x/c^2$—and similarly for the y- and z-components."
    *Context:* Explaining the "imaginary electrostatic problems" used to solve for $\mathbf{A}$.

*   **On the nature of Magnetic Dipoles:**
    > "The word 'dipole' is slightly misleading when applied to a magnetic field because there are no magnetic 'poles' that correspond to electric charges. The magnetic 'dipole field' is not produced by two 'charges,' but by an elementary current loop."
    *Context:* Clarifying the physical difference between electric dipoles (separated charges) and magnetic dipoles (circulating currents) despite their identical field patterns at a distance.

*   **On the frame of reference in rotation:**
    > "A rotating system is not an inertial frame, and the laws of physics are different. We must be sure to use equations of electromagnetism only with respect to inertial coordinate systems."
    *Context:* Explaining why the magnetic effects of a rotating charged cylinder do not disappear just because an observer rotates with the cylinder.

---

## V. Actionable Physical Insights

1.  **Analogy as a Computational Shortcut:** To find the magnetic field of a current distribution, one can treat each component of the current density as a static charge distribution and solve for the "electrostatic" potential. The result is the vector potential $\mathbf{A}$, from which $\mathbf{B}$ is easily derived.
2.  **The "A" Field vs. The "B" Field:** The solenoid example demonstrates that the vector potential $\mathbf{A}$ can exist in regions where the magnetic field $\mathbf{B}$ is zero. This highlights that $\mathbf{A}$ is a distinct physical entity, not just a mathematical convenience.
3.  **Dipole Equivalence:** At large distances, the specific shape of a current loop (circle, square, triangle) is irrelevant. Only the product of the current and the enclosed area (the magnetic moment) determines the field.
4.  **Inertial Frames Requirement:** Maxwell’s equations and the derived magnetostatic formulas are strictly valid in inertial frames. When dealing with rotating systems (like the "angular-velocity meter" example), one must account for the non-inertial nature of the frame or stick to the laboratory (inertial) frame for calculations.
5.  **Theoretical Importance:** Beyond calculation, the vector potential $\mathbf{A}$ is foundational for advanced physics, including relativity, quantum mechanics, and the principle of least action.