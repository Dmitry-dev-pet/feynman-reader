# Field Energy and Field Momentum: Study Guide

This study guide provides a comprehensive overview of the principles of local conservation, energy density, energy flow, and momentum within electromagnetic fields, based on the analysis of electromagnetic field theory.

---

## Key Concepts

### 1. Local vs. World-Wide Conservation
In classical mechanics, conservation often implies that the total quantity of something (like charge or energy) remains constant globally. However, the theory of relativity requires a stricter form known as **local conservation**.

*   **World-Wide Conservation:** A quantity is conserved if the total amount in the universe remains constant. Relativity makes this concept problematic because "simultaneity" is relative; a charge disappearing in one location and appearing in another simultaneously in one frame would not be simultaneous in another.
*   **Local Conservation:** A quantity is conserved locally if its decrease in a specific volume is accounted for exactly by its flow through the boundaries of that volume.
*   **Mathematical Form (Charge):** $\text{div } \mathbf{j} = -\frac{\partial \rho}{\partial t}$. This states that the divergence of current density equals the rate of decrease of charge density.

### 2. The Law of Energy Conservation in Fields
Energy conservation in electromagnetism must account for both the energy stored in the field and the work done on matter.

*   **Work on Matter:** The field does work on matter at a rate of $\mathbf{E} \cdot \mathbf{j}$ per unit volume.
*   **Energy Balance Equation:** The rate of change of field energy density ($u$) is equal to the negative divergence of the energy flow ($\mathbf{S}$) minus the work done on matter:
    $$-\frac{\partial u}{\partial t} = \text{div } \mathbf{S} + \mathbf{E} \cdot \mathbf{j}$$

### 3. Energy Density ($u$) and the Poynting Vector ($\mathbf{S}$)
By manipulating Maxwell’s equations, specific formulas for energy density and energy flow are derived:

| Quantity | Formula | Description |
| :--- | :--- | :--- |
| **Field Energy Density ($u$)** | $u = \frac{\epsilon_0}{2}\mathbf{E} \cdot \mathbf{E} + \frac{\epsilon_0 c^2}{2}\mathbf{B} \cdot \mathbf{B}$ | The energy per unit volume stored in the electric and magnetic fields. |
| **Poynting Vector ($\mathbf{S}$)** | $\mathbf{S} = \epsilon_0 c^2 (\mathbf{E} \times \mathbf{B})$ | The vector representing the rate of energy flow per unit area per unit time. |

### 4. Field Momentum and Angular Momentum
Electromagnetic fields possess momentum, not just energy. This is essential for maintaining the laws of physics in electrodynamic systems.

*   **Momentum Density ($\mathbf{g}$):** Whenever there is energy flow, there is momentum. The momentum density is related to the Poynting vector by:
    $$\mathbf{g} = \frac{1}{c^2}\mathbf{S}$$
*   **Conservation of Total Momentum:** In systems where the forces between particles do not satisfy Newton's third law (action and reaction), the total momentum is still conserved when the momentum stored in the field is included.
*   **Angular Momentum:** Static configurations of charges and magnets can have circulating energy flow, implying the existence of angular momentum in the field. This explains why objects can begin to rotate when a static magnetic field is turned off.

---

## Examples of Energy Flow

The Poynting vector often points to energy flow paths that contradict intuition:

*   **Light Waves:** For a light wave, the intensity (average energy flow) is $\langle S \rangle = \epsilon_0 c \langle E^2 \rangle$.
*   **Charging a Capacitor:** Energy does not flow down the charging wires into the space between the plates. Instead, the $\mathbf{E} \times \mathbf{B}$ vector shows energy flowing inward from the surrounding space through the edges of the capacitor gap.
*   **Resistive Wires:** In a wire carrying current, energy flows radially inward from the surrounding field to compensate for the energy lost as heat (Joule heating).
*   **Static Charge and Magnet:** If a point charge is placed near a bar magnet, the Poynting vector is non-zero and circulates in closed loops, indicating a constant circulation of energy even in a "static" system.

---

## Self-Check Questions

### Short Answer
1.  **Why does the theory of relativity require "local" rather than "world-wide" conservation?**
2.  **What physical process does the term $\mathbf{E} \cdot \mathbf{j}$ represent in the energy conservation equation?**
3.  **In the context of a light wave, how is the energy density $u$ related to the average energy flow $S$?**
4.  **What is the relationship between the Poynting vector and the momentum density of the field?**
5.  **If the action and reaction forces between two moving charges are not equal, how is the law of conservation of momentum preserved?**

### Common Misconceptions
*   **Misconception:** Energy in an electrical circuit travels inside the wires.
    *   **Reality:** The Poynting theory shows that energy actually travels through the electromagnetic field in the space *outside* the wires and enters the wires or components (like capacitors) from the sides.
*   **Misconception:** "Static" fields have no motion or flow.
    *   **Reality:** A static configuration of an electric charge and a magnetic field can produce a non-zero Poynting vector, resulting in a constant circulation of field energy and hidden angular momentum.
*   **Misconception:** The formulas for $u$ and $\mathbf{S}$ are uniquely proven.
    *   **Reality:** There are an infinite number of possible formulas for $u$ and $\mathbf{S}$ that satisfy the conservation law. The standard formulas are chosen because they are the simplest and agree with experimental observations.

---

## Essay Prompts for Deeper Exploration

1.  **The Boxcar Thought Experiment:** Describe Einstein’s argument regarding a railroad car and a flash of light. Explain how this thought experiment proves that energy $U$ must carry a momentum $p = U/c$ to preserve the law of the center of gravity.
2.  **The Ambiguity of Field Energy Location:** Discuss the philosophical and physical implications of the fact that we cannot uniquely determine the exact location of electromagnetic energy. Why do physicists rely on the simplest form of the Poynting vector despite this ambiguity?
3.  **Relativistic Invariance and Conservation:** Analyze how the requirement for Lorentz relativistic invariance restricts the possible laws of nature, specifically regarding the transition from non-local to local interactions.

---

## Glossary of Important Terms

*   **Divergence (div):** A mathematical operator that measures the magnitude of a field's source or sink at a given point; used to describe the flow of charge or energy.
*   **Energy Density ($u$):** The amount of energy stored in the electromagnetic field per unit volume, measured in joules per cubic meter.
*   **Energy Flux:** The rate of energy transfer through a surface, represented by the Poynting vector.
*   **Intensity:** The average rate of energy flow per unit area, typically associated with the brightness of light.
*   **Local Conservation:** The principle that a quantity can only move from one place to another by passing through the intervening space.
*   **Momentum Density ($\mathbf{g}$):** The momentum stored in the electromagnetic field per unit volume.
*   **Poynting Vector ($\mathbf{S}$):** A vector representing the direction and magnitude of the directional energy flux of an electromagnetic field.
*   **Work ($\mathbf{E} \cdot \mathbf{j}$):** The rate at which the electromagnetic field transfers energy to matter per unit volume.