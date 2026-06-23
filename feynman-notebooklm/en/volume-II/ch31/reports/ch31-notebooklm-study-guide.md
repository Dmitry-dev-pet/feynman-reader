# Study Guide: Tensors in Physics

This study guide explores the fundamental principles of tensors as presented in the context of Chapter 31 of the *Feynman Lectures on Physics*. It covers the mathematical framework of tensors, their physical applications in electricity and mechanics, and their extension into relativistic four-dimensional space.

---

## I. Key Concepts

### 1. The Nature of Tensors
Tensors are mathematical objects used to describe physical properties that vary depending on direction (anisotropy). While a scalar is a single number and a vector is a set of three numbers (in three dimensions), a second-rank tensor consists of nine numbers that transform in a specific way when the coordinate system changes.

*   **Rank 0:** Scalar (e.g., energy density).
*   **Rank 1:** Vector (e.g., Electric field $\mathbf{E}$, Polarization $\mathbf{P}$).
*   **Rank 2:** A set of nine coefficients relating two vectors (e.g., Polarizability $\alpha_{ij}$).

### 2. The Tensor of Polarizability
In isotropic materials, $\mathbf{P} = \alpha \mathbf{E}$, meaning polarization is always parallel to the electric field. In anisotropic crystals, however, the induced dipole moment per unit volume $\mathbf{P}$ depends on the direction of $\mathbf{E}$. This is represented by:
$$P_i = \sum_j \alpha_{ij} E_j$$
Where $\alpha_{ij}$ is the tensor of polarizability. If $\mathbf{E}$ is in the $x$-direction, $\mathbf{P}$ can have components in $x$, $y$, and $z$.

### 3. Symmetry and the Energy Ellipsoid
Many physical tensors are **symmetric**, meaning $\alpha_{ij} = \alpha_{ji}$. This property allows the tensor to be visualized as an **energy ellipsoid**.
*   **Principal Axes:** For any symmetric second-rank tensor, there exists a set of orthogonal axes ($a, b, c$) where all off-diagonal terms are zero. This is called a "diagonal" tensor.
*   **Isotropic Case:** If the three diagonal elements are equal, the ellipsoid becomes a sphere, and the material is isotropic.

### 4. Examples of Second-Rank Tensors
| Tensor | Symbol | Relationship |
| :--- | :--- | :--- |
| **Polarizability** | $\alpha_{ij}$ | Relates Electric Field ($\mathbf{E}$) to Polarization ($\mathbf{P}$) |
| **Conductivity** | $\sigma_{ij}$ | Relates Electric Field ($\mathbf{E}$) to Current Density ($\mathbf{j}$) |
| **Inertia** | $I_{ij}$ | Relates Angular Velocity ($\boldsymbol{\omega}$) to Angular Momentum ($\mathbf{L}$) |
| **Stress** | $S_{ij}$ | Relates a unit normal vector ($\mathbf{n}$) to the internal force ($\mathbf{F}_n$) |
| **Strain** | $T_{ij}$ | Describes internal distortion in an elastic body |

### 5. The Stress Tensor ($S_{ij}$)
The stress tensor describes internal forces within a solid or viscous liquid.
*   The first index ($i$) refers to the direction of the force component.
*   The second index ($j$) refers to the direction normal to the area across which the force acts.
*   **Symmetry:** Because there is no net torque on an infinitesimal cube in equilibrium, $S_{ij} = S_{ji}$.
*   **Hydrostatic Pressure:** In a static liquid, the stress tensor is diagonal with all elements equal to the pressure $p$ ($S_{ij} = p\delta_{ij}$).

### 6. Tensors of Higher Rank
*   **Third-Rank:** The piezoelectric effect, where stress generates an electric field ($E_i = \sum P_{ijk} S_{jk}$).
*   **Fourth-Rank:** Elasticity coefficients ($\gamma_{ijkl}$) relating stress to strain. A crystal with the lowest symmetry requires 21 independent constants to describe its elastic properties.

### 7. Relativistic Four-Tensors
Tensors can be extended to the four dimensions of space-time ($t, x, y, z$). The **stress-energy tensor** ($S_{\mu\nu}$) combines energy density, momentum density, energy flow (Poynting vector), and momentum flow (stress) into a single symmetric 4x4 matrix.

---

## II. Common Misconceptions

*   **"A tensor is just a matrix."** While a tensor can be represented by a matrix (a table of numbers), a true tensor must transform in a specific mathematical way when the coordinate axes are rotated.
*   **"The induced polarization is always in the direction of the electric field."** This is only true for isotropic substances. In crystals, internal asymmetric forces often cause charges to displace in directions not aligned with the external force.
*   **"Angular momentum ($\mathbf{L}$) is always parallel to angular velocity ($\boldsymbol{\omega}$)."** This is a special case for rotation about a principal axis. For an asymmetrical object, $\mathbf{L}$ and $\boldsymbol{\omega}$ are generally not parallel.
*   **"Stress is the same as pressure."** Pressure is a specific type of stress that is normal to a surface and equal in all directions. Stress also includes "shear" forces, which are tangential to the surface.

---

## III. Self-Check Questions (Short Answer)

1.  What is the definition of a tensor of the "zero rank"?
2.  How many components does a second-rank tensor have in three-dimensional space?
3.  Why must the polarization tensor $\alpha_{ij}$ be symmetric ($\alpha_{xy} = \alpha_{yx}$)?
4.  What is the "Kronecker delta" ($\delta_{ij}$), and what does it represent in tensor form?
5.  If an electric field is applied along one of the "principal axes" of a crystal, what is the direction of the resulting polarization?
6.  How does the shape of the energy ellipsoid change for a cubic crystal?
7.  In the stress tensor $S_{yx}$, what do the $y$ and $x$ subscripts represent?
8.  Why are the piezoelectric coefficients ($P_{ijk}$) zero in crystals with a center of inversion?
9.  In the four-dimensional stress-energy tensor, what physical quantity is represented by the component $S_{tt}$?
10. What is the relationship between the Poynting vector and the components of the four-dimensional stress-energy tensor?

---

## IV. Essay Prompts for Deeper Exploration

1.  **The Geometry of Physics:** Explain how the energy ellipsoid serves as a visualization tool for tensors. Discuss how the concept of "principal axes" simplifies the mathematical description of an anisotropic substance.
2.  **Symmetry and Physical Properties:** Discuss the relationship between a crystal's internal geometric symmetry (e.g., monoclinic vs. cubic) and the properties of its polarization tensor. How does group-theoretical analysis apply here?
3.  **From Vectors to Tensors in Mechanics:** Compare the relationship between force and acceleration in basic mechanics to the relationship between angular velocity and angular momentum in a rigid body. Why is a tensor necessary for the latter?
4.  **Tensors in Relativity:** Describe the transition from the three-dimensional stress tensor to the four-dimensional stress-energy tensor. Explain how the conservation of energy and momentum are unified in this framework.

---

## V. Glossary of Important Terms

*   **Anisotropic:** Having physical properties that differ in value when measured in different directions.
*   **Axial Vector (Pseudo-vector):** A quantity like torque or angular momentum that transforms like a vector in three dimensions but is actually an antisymmetric second-rank tensor.
*   **Cross Product:** A mathematical operation between two vectors that, in three dimensions, results in a pseudo-vector (e.g., $\mathbf{r} \times \mathbf{F}$).
*   **Isotropic:** Having physical properties that are the same in all directions.
*   **Kronecker Delta ($\delta_{ij}$):** The unit tensor, where $\delta_{ij} = 1$ if $i=j$ and $0$ if $i \neq j$.
*   **Principal Axes:** The specific coordinate axes for which a symmetric tensor becomes diagonal (all off-diagonal components are zero).
*   **Shear Force:** The component of force acting tangential to a surface.
*   **Stress-Energy Tensor:** A 4x4 symmetric tensor in relativity that describes the density and flow of energy and momentum in space-time.
*   **Tensor Field:** A situation where a tensor's components (such as stress) vary as a function of position $(x, y, z)$ within a material.
*   **Tensor of Inertia ($I_{ij}$):** The set of coefficients that relate the components of angular velocity to the components of angular momentum.