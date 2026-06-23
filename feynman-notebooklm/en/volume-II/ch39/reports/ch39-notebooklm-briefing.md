# Chapter 39: Elastic Materials

This briefing document provides a comprehensive analytical synthesis of the physical principles, mathematical formulations, and atomic foundations of elastic materials. It explores the transition from specific elastic objects to the general internal conditions of stress and strain within a continuous medium.

## Executive Summary

The study of elastic materials centers on describing the local state of deformation (strain) and the internal forces (stress) at every point within a body. This is achieved through the use of symmetric tensors. The relationship between stress and strain is governed by Hooke's law, which, in its most general form, involves a fourth-rank tensor of elasticity. For isotropic materials, this complexity reduces to two constants: the Lamé elastic constants ($\lambda$ and $\mu$). The dynamics of these materials are described by vector wave equations that reveal two distinct types of internal motion: longitudinal (compressional) waves and transverse (shear) waves. While linear elasticity is a robust first-order approximation, real materials exhibit non-linear behaviors, including hysteresis and specific fracture patterns determined by their internal atomic structures and force laws.

## 1. The Tensor of Strain

To describe the distortion of an elastic body, we track the displacement $\FLPu$ of a speck of material from its unstrained position $\mathbf{r}$ to a strained position $\mathbf{r}'$.

### 1.1 Mathematical Definition
The displacement $\FLPu$ is a vector function of position:
$$\FLPu = \mathbf{r}' - \mathbf{r}$$

In a general distortion involving stretching, compression, and shear, the state of strain is defined by a symmetric tensor $e_{ij}$ with six independent components. The general term is defined as:
$$e_{ij} = \frac{1}{2}\left(\frac{\partial u_j}{\partial x_i} + \frac{\partial u_i}{\partial x_j}\right)$$

### 1.2 Distinguishing Strain from Rotation
It is critical to separate actual material distortion from pure rotation. If the partial derivatives of displacement are equal and opposite (e.g., $\partial u_y/\partial x = -\partial u_x/\partial y$), the result is a rigid-body rotation with no change in the relative positions of atoms (Fig. 39–4). The symmetric definition of $e_{ij}$ ensures that pure rotations—described by the antisymmetric tensor $\omega_{ij}$—are excluded from the strain description.

## 2. The Tensor of Elasticity

The relationship between internal stresses ($S_{ij}$) and strains ($e_{ij}$) is defined by the tensor of elasticity ($C_{ijkl}$), representing a generalized Hooke’s Law.

### 2.1 The Generalized Hooke's Law
The stress-strain relation is expressed as:
$$S_{ij} = \sum_{k,l}C_{ijkl}e_{kl}$$
While there are $3 \times 3 \times 3 \times 3 = 81$ possible coefficients, the symmetry of the stress and strain tensors reduces this to a maximum of 36 independent terms.

### 2.2 Material Symmetries
The number of independent elastic constants is further reduced by the symmetry of the material:

| Material Type | Independent Constants | Key Relations |
| :--- | :--- | :--- |
| **Cubic Crystal** | 3 | $C_{xxxx}, C_{xxyy}, C_{xyxy}$ |
| **Isotropic** | 2 | $C_{xxxx} = C_{xxyy} + 2C_{xyxy}$ |

For isotropic materials, the stress-strain relation is simplified using the Lamé constants $\lambda$ and $\mu$:
$$S_{ij} = 2\mu e_{ij} + \lambda\left(\sum_k e_{kk}\right)\delta_{ij}$$
Here, $\mu$ corresponds to the shear modulus.

### 2.3 Potential Energy Density
The work $w$ done per unit volume to distort a material is stored as potential energy:
$$w = \frac{1}{2}\sum_{ijkl}C_{ijkl}e_{ij}e_{kl}$$
In equilibrium, the internal displacements adjust themselves to minimize the total integral of this energy over the volume of the body.

## 3. Dynamics and Wave Propagation

When internal forces are not in equilibrium, the material undergoes motion described by its density $\rho$ and acceleration $\ddot{\mathbf{r}}$.

### 3.1 The Equation of Motion
For an isotropic material, the relationship between force density $\FLPf$ and displacement $\FLPu$ results in the vector equation:
$$\rho \frac{\partial^2 \FLPu}{\partial t^2} = (\lambda + \mu)\nabla(\text{div } \FLPu) + \mu \nabla^2 \FLPu$$

### 3.2 Types of Elastic Waves
The general solution for motion in an elastic solid decomposes into two independent wave types:

1.  **Longitudinal (Compressional) Waves:**
    *   **Condition:** $\text{curl } \FLPu = 0$
    *   **Speed:** $C_{long} = \sqrt{(\lambda + 2\mu)/\rho}$
    *   **Meaning:** Waves of density change with no shearing.
2.  **Transverse (Shear) Waves:**
    *   **Condition:** $\text{div } \FLPu = 0$
    *   **Speed:** $C_{shear} = \sqrt{\mu/\rho}$
    *   **Meaning:** Waves of shear distortion with no change in density.

## 4. Nonelastic Behavior and Fracture

Hooke's Law is a first-order approximation. For large strains, materials deviate from linearity and eventually fail.

*   **Ductile vs. Brittle:** Ductile materials show a curve-over in the stress-strain relation before breaking, while brittle materials fail shortly after leaving the linear regime.
*   **Hysteresis:** In some materials, the stress returns along a different path when strain is removed, indicating energy loss.
*   **Fracture Mechanics:** Failure depends on the type of stress. Blackboard chalk, for example, is weak in tension but strong in shear. Consequently, when twisted (torsion), it breaks at a 45° angle—the plane of maximum tension (Fig. 39–9).
*   **Viscoelasticity:** Some materials (like Saran-Wrap) exhibit time-dependent return to their original shape. This can be modeled as a system of fibers and viscous liquid-filled cells, where the internal friction of moving molecules (viscosity) slows the restoration process.

## 5. Atomic Basis of Elasticity

Elastic constants can be derived by modeling a crystal as a lattice of atoms connected by springs.

### 5.1 Simple Cubic Model (e.g., NaCl)
In a model using central forces (forces acting along the line between atoms) and considering nearest-neighbor (constant $k_1$) and next-nearest-neighbor (constant $k_2$) interactions, the elastic constants are:
*   $C_{xxxx} = \frac{k_1 + 2k_2}{a}$
*   $C_{xyxy} = C_{xxyy} = \frac{k_2}{a}$ (where $a$ is the lattice constant)

### 5.2 The Cauchy Relation
The model predicts that $C_{xyxy} = C_{xxyy}$. This "Cauchy relation" holds for ionic crystals like LiF and NaCl where central forces dominate. It fails for:
*   **Metals (Na, K, Fe):** Interatomic forces do not act strictly along the lines joining atoms.
*   **Covalent Crystals (Diamond):** Bonds have directional properties (e.g., tetrahedral angles) that resist sideways pushing, acting more like cantilevered beams than simple springs.

## Important Quotes and Context

> **On the definition of strain:** "The key point is that if $\frac{\partial u_y}{\partial x}$ and $\frac{\partial u_x}{\partial y}$ are equal and opposite, there is no strain; so we can fix things up by defining $e_{xy} = e_{yx} = \frac{1}{2}(\frac{\partial u_y}{\partial x} + \frac{\partial u_x}{\partial y})$."
*   **Context:** This explains the necessity of a symmetric tensor to ensure that pure rotations do not contribute to the mathematical description of material deformation.

> **On Hooke's Law:** "The remarkable thing is perhaps not that Hooke’s law breaks down for large strains but that it should be so generally true."
*   **Context:** Feynman explains that any energy function $U(\theta)$ can be expanded as a Taylor series; the linear term in the force (derivative of energy) will always dominate for sufficiently small displacements, making Hooke’s law a universal first-order approximation.

> **On Wave Types:** "Since $\text{div } \FLPu_1$ is zero, $\FLPu_1$ produces no changes in density; the vector $\FLPu_1$ corresponds to the transverse, or shear-type, wave... $\FLPu_2$ is just the compressional—sound-type—wave."
*   **Context:** This distinguishes the two fundamental modes of mechanical energy propagation through a solid medium.

## Physical Meaning and Insights

1.  **Symmetry Simplification:** The transition from 81 possible elastic constants to just 2 for isotropic materials demonstrates how physical symmetry (rotation and reflection invariance) drastically reduces the complexity of physical laws.
2.  **Minimum Energy Principle:** The static configuration of an elastic body is not arbitrary; it is the specific state that minimizes the total stored potential energy. This provides a powerful tool for numerical analysis of complex shapes like crane hooks or turbine rotors.
3.  **Experimental Visualization:** Stresses in complex shapes can be visualized using photoelasticity. Transparent plastics become birefringent under stress, rotating the plane of polarized light in proportion to the internal stress, allowing for direct experimental measurement (Fig. 39–6, 39–7).
4.  **Atomic Predetermination:** The macroscopic stiffness of a crystal is a direct manifestation of the interatomic "spring" constants. However, the failure of simple models in metals and diamonds reveals the importance of non-central and directional bonding forces in solid-state physics.