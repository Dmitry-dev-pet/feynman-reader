# The Maxwell Equations: Comprehensive Briefing

This document provides a detailed analysis of the Maxwell equations as presented in Chapter 18 of the *Feynman Lectures on Physics, Volume II*. It covers the mathematical synthesis, physical implications, and the unification of classical physics.

## Executive Summary

Chapter 18 marks the culmination of the study of electromagnetic fields by presenting the complete set of Maxwell's equations. The central development is Maxwell’s addition of a new term—the time derivative of the electric field—to the law governing the curl of the magnetic field. This modification ensures the consistency of electromagnetic theory with the fundamental law of charge conservation. This synthesis reveals that electromagnetic influences propagate as waves at the speed of light ($c$), effectively unifying electricity, magnetism, and optics into a single, beautiful theory.

---

## 1. The Complete Maxwell Equations

The following table summarizes the fundamental laws of electromagnetism in both their differential and integral forms, as they were understood by 1905.

### Table 18-1: The Fundamental Equations

| Law | Mathematical Form | Physical Meaning |
| :--- | :--- | :--- |
| **I. Gauss’ Law for E** | $\text{div } \mathbf{E} = \frac{\rho}{\epsilon_0}$ | Flux of $\mathbf{E}$ through a closed surface = (Charge inside)$ / \epsilon_0$ |
| **II. Faraday’s Law** | $\text{curl } \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ | Line integral of $\mathbf{E}$ around a loop = $-\frac{d}{dt}$(Flux of $\mathbf{B}$ through the loop) |
| **III. Gauss’ Law for B** | $\text{div } \mathbf{B} = 0$ | Flux of $\mathbf{B}$ through a closed surface = 0 (No magnetic charges) |
| **IV. Ampère-Maxwell Law**| $c^2 \text{curl } \mathbf{B} = \frac{\mathbf{j}}{\epsilon_0} + \frac{\partial \mathbf{E}}{\partial t}$ | $c^2$(Integral of $\mathbf{B}$ around a loop) = (Current through loop)$ / \epsilon_0 + \frac{d}{dt}$(Flux of $\mathbf{E}$ through the loop) |
| **Charge Conservation** | $\text{div } \mathbf{j} = -\frac{\partial \rho}{\partial t}$ | Flux of current through a closed surface = $-\frac{d}{dt}$(Charge inside) |
| **Force Law** | $\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$ | Force on a charge $q$ moving with velocity $\mathbf{v}$ |
| **Law of Motion** | $\frac{d}{dt}(\mathbf{p}) = \mathbf{F}$ | Newton’s law with relativistic momentum $\mathbf{p} = \frac{m\mathbf{v}}{\sqrt{1-v^2/c^2}}$ |

---

## 2. Maxwell’s Discovery: The "New Term"

Prior to Maxwell’s work, the equation for the magnetic field of steady currents was known only as:
$$\text{curl } \mathbf{B} = \frac{\mathbf{j}}{\epsilon_0 c^2} \quad (18.1)$$

### The Mathematical Inconsistency
Maxwell noticed a logical flaw in Equation 18.1. Mathematically, the divergence of a curl is always zero ($\text{div}(\text{curl } \mathbf{B}) = 0$). Therefore, Equation 18.1 implies that $\text{div } \mathbf{j}$ must always be zero. However, the law of conservation of charge states:
$$\text{div } \mathbf{j} = -\frac{\partial \rho}{\partial t} \quad (18.2)$$
If charge is being moved (changing $\rho$), $\text{div } \mathbf{j}$ cannot be zero.

### The Maxwell Correction
To resolve this, Maxwell added the term $\frac{\partial \mathbf{E}}{\partial t}$ to the equation. Taking the divergence of the corrected Equation IV:
$$\text{div}(\frac{\mathbf{j}}{\epsilon_0}) + \text{div}(\frac{\partial \mathbf{E}}{\partial t}) = 0$$
By reversing the order of derivatives and substituting $\text{div } \mathbf{E} = \rho/\epsilon_0$, the equation returns to the correct expression for charge conservation (Eq. 18.2).

---

## 3. Physical Examples of the New Term in Action

### Spherically Symmetric Current (Fig. 18-1)
Imagine a sphere leaking charge symmetrically in all directions.
*   **The Paradox:** Current flows radially, suggesting a magnetic field might circulate.
*   **The Resolution:** The changing electric field ($\frac{\partial E}{\partial t} = -j/\epsilon_0$) exactly cancels the current term in Maxwell's Fourth Equation.
*   **Result:** The curl of $\mathbf{B}$ is zero; there is no magnetic field.

### Charging a Capacitor (Fig. 18-2)
When a capacitor is charged by a wire:
*   **Loop 1 (around the wire):** The magnetic field is produced by the current $I$ in the wire.
*   **Loop 2 (between the plates):** There is no physical current $I$ between the plates. However, the electric field between the plates is changing.
*   **Result:** The $\frac{\partial \mathbf{E}}{\partial t}$ term between the plates produces the exact same magnetic field as the current in the wire, ensuring continuity of the field.

---

## 4. The Traveling Field and the Speed of Light

Maxwell’s equations imply that electromagnetic fields can travel through space independently of their source.

### The Infinite Sheet Experiment (Figs. 18-3 to 18-6)
If an infinite sheet of charge is suddenly set in motion (creating a surface current $J$):
1.  **Generation:** A magnetic field $\mathbf{B}$ and an electric field $\mathbf{E}$ are generated near the sheet.
2.  **Propagation:** These fields do not appear everywhere instantly. They travel outward as a "wavefront" at a constant velocity $v$.
3.  **The "Butterfly" Effect:** If the current is stopped, a "block" of field continues to propagate through space.

### Velocity and Properties of the Wave
By applying Faraday’s Law and Maxwell’s Fourth Equation to the moving wavefront, two conditions emerge:
*   $E = vB$
*   $c^2B = Ev$

For both to be true, the velocity must be $v = c$.
**Key properties of electromagnetic waves:**
*   The fields are **transverse**: $\mathbf{E}$ and $\mathbf{B}$ are perpendicular to the direction of propagation.
*   $\mathbf{E}$ and $\mathbf{B}$ are **perpendicular** to each other.
*   The magnitudes are related by $E = cB$.

### Historical Unification
The constant $c$ was originally just a ratio of experimental constants from electrostatics ($\epsilon_0$) and magnetostatics ($\epsilon_0 c^2$). Maxwell’s discovery that $c$ matched the measured speed of light led to the inference that light is an electromagnetic phenomenon.

---

## 5. Mathematical Reformulation: Potentials

To simplify calculations, Maxwell’s equations can be written in terms of a scalar potential $\phi$ and a vector potential $\mathbf{A}$.

### Definitions
*   **Magnetic Field:** $\mathbf{B} = \text{curl } \mathbf{A}$
*   **Electric Field:** $\mathbf{E} = -\nabla\phi - \frac{\partial \mathbf{A}}{\partial t}$

### The Wave Equation
By choosing the gauge $\text{div } \mathbf{A} = -\frac{1}{c^2}\frac{\partial \phi}{\partial t}$, the equations for the potentials separate into a symmetrical form:
$$\nabla^2\phi - \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2} = -\frac{\rho}{\epsilon_0}$$
$$\nabla^2\mathbf{A} - \frac{1}{c^2}\frac{\partial^2\mathbf{A}}{\partial t^2} = -\frac{\mathbf{j}}{\epsilon_0 c^2}$$

These are **three-dimensional wave equations**, showing that any change in charge ($\rho$) or current ($\mathbf{j}$) propagates through the potentials at speed $c$.

---

## 6. Important Quotes with Context

> **"Anything said in this chapter that contradicts something said earlier is true and what was said earlier is false—because what was said earlier applied to such special situations..."**
*   **Context:** Feynman introduces the "whole truth" of Maxwell's equations, moving beyond the restrictions of steady currents and fixed charges used in previous chapters.

> **"If we take away the scaffolding he used to build it, we find that Maxwell’s beautiful edifice stands on its own."**
*   **Context:** Referring to Maxwell's mechanical model of the vacuum as an "elastic solid." Feynman emphasizes that the equations themselves are the fundamental reality, regardless of the models used to derive them.

> **"The caterpillar has turned into a butterfly!"**
*   **Context:** A metaphor for a pulse of electromagnetic field that has left its source (the current sheet) and is propagating through space "all by itself," no longer connected to the charges that created it.

> **"We have climbed a great peak. We are on the top of K2—we are nearly ready for Mount Everest, which is quantum mechanics."**
*   **Context:** Feynman reflects on the completion of classical physics (the 1905 synthesis) and the transition toward the study of its consequences and the eventual move to quantum theory.

---

## 7. Actionable Insights

*   **Universal Consistency:** Maxwell’s equations are the definitive authority for classical electromagnetism. If a previous formula (e.g., for steady currents) contradicts these, the Maxwell version is the correct general form.
*   **Field Self-Maintenance:** The interplay between $\text{curl } \mathbf{E}$ (Faraday's Law) and $\text{curl } \mathbf{B}$ (Maxwell's term) allows fields to sustain each other in space without charges; a changing $\mathbf{B}$ creates $\mathbf{E}$, and a changing $\mathbf{E}$ creates $\mathbf{B}$.
*   **Computational Efficiency:** When dealing with time-varying fields, it is often simpler to solve the wave equations for the potentials $\phi$ and $\mathbf{A}$ rather than solving for $\mathbf{E}$ and $\mathbf{B}$ directly.
*   **Charge Conservation as a Constraint:** The laws of physics do not permit the sudden creation of charge at a point; any model must account for the transport of charge, or it will violate Maxwell's equations.