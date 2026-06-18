# Chapter 18: Rotation in Two Dimensions

This briefing document provides an analytical overview of the mechanics of rotation in two dimensions, as outlined in the Feynman Lectures on Physics. It covers the transition from point-particle mechanics to the study of complex, rigid bodies, focusing on the center of mass, rotational kinematics, torque, and the conservation of angular momentum.

## Executive Summary

Chapter 18 marks a transition from the mechanics of point particles to the study of complex systems, specifically "rigid bodies." The analysis establishes that even complex motions can be understood through two primary lenses: the motion of the **center of mass** and the **rotation** of the body around an axis. 

A central theme is the direct analogy between linear and rotational dynamics. Just as force causes linear acceleration, **torque** causes angular acceleration. Similarly, just as linear momentum is conserved in the absence of external force, **angular momentum** is conserved in the absence of external torque. A unique distinction is highlighted: while an object's mass remains constant, its **moment of inertia** (its resistance to turning) can change if the distribution of its mass relative to the axis changes, leading to dramatic effects in angular velocity.

---

## I. The Theorem of the Center of Mass

When analyzing a "complicated" object—such as a collection of blocks and spokes—its motion may appear chaotic. However, the theorem of the center of mass proves that a specific "mean position" exists that follows a simple trajectory, such as a parabola under gravity.

### Mathematical Definition
The center of mass $(\FLPR)$ is an average position where each constituent particle's position $(\FLPr_i)$ is weighted by its mass $(m_i)$:
$$\FLPR = \frac{\sum_i m_i \FLPr_i}{M}$$
*(Where $M$ is the total mass of the object.)*

### Physical Significance
*   **External vs. Internal Forces:** Newton’s Third Law ensures that internal forces (actions and reactions between particles within the object) cancel out. Therefore, the acceleration of the center of mass is determined solely by external forces: $\FLPF_{\text{ext}} = M \frac{d^2\FLPR}{dt^2}$.
*   **Constant Velocity:** In the absence of external forces, the center of mass moves at a constant velocity, regardless of how much the object wiggles or rotates internally.
*   **Propulsion:** Rocket propulsion does not move the center of mass of the system (rocket plus exhaust gas). Instead, it moves the "interesting part" (the rocket) by ejecting an "uninteresting part" (the gas) in the opposite direction.

---

## II. Kinematics of Plane Rotation

Rotation in two dimensions (plane rotation) involves a rigid body turning about a fixed axis. The motion of any point on the body is defined by its angular change.

### The Linear-Rotational Analogy
There is a direct relationship between one-dimensional displacement and two-dimensional rotation:

| Linear Quantity | Rotational Analog | Relation/Formula |
| :--- | :--- | :--- |
| Distance ($s$) | Angle ($\theta$) | Measured in radians |
| Velocity ($v$) | Angular Velocity ($\omega$) | $\omega = d\theta/dt$ |
| Acceleration ($a$) | Angular Acceleration ($\alpha$) | $\alpha = d\omega/dt$ |

### Particle Motion in Rotation
For a particle at distance $r$ from the axis (as seen in **Figure 18-1**):
*   The distance moved is $r \Delta\theta$.
*   The magnitude of velocity is $v = \omega r$.
*   The velocity components are $v_x = -\omega y$ and $v_y = +\omega x$.

---

## III. Torque: The "Twisting Force"

Torque ($\tau$) is the rotational analog of force. It is the "twist" applied to an object.

### Quantitative Definition
Torque is defined through the concept of work. If $\Delta W = \tau \Delta\theta$, then for a force applied at point $(x, y)$:
$$\tau = xF_y - yF_x$$

### Geometric Interpretations
As illustrated in **Figure 18-2**, torque can be calculated in three equivalent ways:
1.  **Component Form:** $\tau = xF_y - yF_x$.
2.  **Tangential Force:** $\tau = r F_{\text{tang}}$ (only the component of force perpendicular to the radius causes rotation).
3.  **Lever Arm:** $\tau = F \cdot (\text{lever arm})$, where the lever arm is the perpendicular distance from the axis to the line of action of the force.

### Equilibrium
For an object to be in equilibrium, two conditions must be met:
1.  The sum of all forces must be zero ($\sum \FLPF = 0$).
2.  The sum of all torques about any axis must be zero ($\sum \tau = 0$).

---

## IV. Angular Momentum and Conservation

Angular momentum ($L$) is the rotational analog of linear momentum ($p$). The external torque acting on a system is equal to the rate of change of its total angular momentum: $\tau = dL/dt$.

### Formulas for Angular Momentum
For a single particle (as seen in **Figure 18-3**):
*   $L = xp_y - yp_x$
*   $L = r p_{\text{tang}}$
*   $L = p \cdot (\text{momentum lever arm})$

### Moment of Inertia ($I$)
For a rigid body, angular momentum is the product of its "inertia for turning" and its angular velocity:
$$L = I\omega$$
Where the **Moment of Inertia** ($I$) is defined as:
$$I = \sum_i m_i r_i^2$$
This indicates that the resistance to rotation depends not just on the total mass, but on how far that mass is distributed from the axis. As shown in **Figure 18-4**, moving masses farther from the axis increases $I$ and decreases acceleration for a given torque.

### The Law of Conservation
If the net external torque is zero, the total angular momentum is conserved ($L = \text{constant}$).
*   **Variable Moment of Inertia:** Unlike mass, the moment of inertia can change (e.g., a rotating person pulling their arms in). 
*   **Resulting Motion:** If $I$ decreases, $\omega$ must increase to keep $L$ constant ($I_1\omega_1 = I_2\omega_2$).

---

## V. Key Physical Applications

### Planetary Motion (Kepler's Law)
In the case of a planet orbiting the sun, the force is purely radial. Since the force is directed toward the sun, the torque about the sun is zero. Consequently:
*   The angular momentum of the planet is constant.
*   This conservation of angular momentum is the physical basis for **Kepler’s Law of Equal Areas**, as the rate at which area is swept is proportional to the angular momentum.

### Action and Reaction in Rotation
The briefing notes that internal torques within a system cancel out because the "action" and "reaction" forces are directed oppositely along the same line, resulting in equal and opposite lever arms for any given axis.

---

## Important Quotes with Context

> **"The external force is the total mass times the acceleration of an imaginary point whose location is $\FLPR$. This point is called the center of mass of the body."**
*   *Context:* Defining the mathematical simplification that allows complex objects to be treated as point particles for certain translational calculations.

> **"Torque is going to be so arranged that the theorem of work has an absolute analog: force times distance is work, and torque times angle is going to be work."**
*   *Context:* Explaining the derivation of torque as a quantitative measurement of "twist" based on the energy required to rotate a body.

> **"There is one important difference between mass and moment of inertia which is very dramatic. The mass of an object never changes, but its moment of inertia can be changed."**
*   *Context:* Describing why conservation of angular momentum leads to changes in speed (like a skater spinning faster), whereas conservation of linear momentum with a constant mass does not.

---

## Actionable Insights for Analysis

*   **Identify the Axis:** Torque and angular momentum values are dependent on the chosen axis. When calculating equilibrium or motion, always define the axis clearly.
*   **Use the Analogy:** When faced with a complex rotational problem, substitute the rotational variables ($\theta, \omega, \alpha, \tau, I, L$) into known linear formulas ($s, v, a, F, m, p$).
*   **Check for External Torque:** To determine if angular momentum is conserved, verify if there are any forces acting at a distance from the axis that have a tangential component.
*   **Assess Mass Distribution:** When predicting the behavior of a system (like the falling weight in **Figure 18-4**), consider how changes in mass distribution will affect the moment of inertia and, consequently, the angular acceleration.