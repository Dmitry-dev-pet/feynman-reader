# Chapter 35: Paramagnetism and Magnetic Resonance

This briefing document provides a comprehensive analytical synthesis of the principles of paramagnetism and magnetic resonance as outlined in the source text. It covers the transition from classical to quantum descriptions of magnetic moments, experimental verifications, and the practical application of resonance phenomena in bulk materials.

## Executive Summary

The study of paramagnetism and magnetic resonance reveals the fundamental departure of atomic behavior from classical physics. While classical theory predicts continuous orientations for magnetic moments, quantum mechanics dictates that angular momentum and its associated magnetic moments are quantized. This quantization is experimentally verified by the Stern-Gerlach and Rabi molecular-beam experiments. These principles are further applied to understand the magnetization of bulk materials and are utilized in sophisticated technological applications such as adiabatic demagnetization for reaching temperatures near absolute zero and Nuclear Magnetic Resonance (NMR) for chemical and physical analysis.

---

## 1. The Physics of Quantized Magnetic States

In quantum mechanics, the angular momentum component along any given axis is restricted to discrete, equally spaced values. For any atomic system, there is a spin $j$ (an integer or half-integer), and the component of angular momentum ($J_z$) along an axis is defined by:

$$J_z = \{j, j-1, j-2, \dots, -j\} \cdot \hbar \tag{35.1}$$

### 1.1 Magnetic Moments and Energy Splitting
Every atomic system with angular momentum possesses a magnetic moment $\mu$ in the same direction. In a weak magnetic field ($B$), the energy of the system changes by:

$$\Delta U = -\mu_z B \tag{35.2}$$

The $z$-component of the magnetic moment is related to $J_z$ by the $g$-factor and the charge-to-mass ratio:

$$\mu_z = g\left(\frac{q}{2m}\right)J_z \tag{35.3}$$

When a magnetic field is applied, the previously degenerate energy states split into $(2j+1)$ distinct levels. The spacing between these levels is constant and defined as $\hbar\omega_p$.

### 1.2 The Larmor Precession Frequency
The angular velocity of precession, $\omega_p$, is consistent between classical and quantum descriptions:

$$\omega_p = g\left(\frac{q}{2m}\right)B \tag{35.4}$$

| Entity | Symbol | Physical Meaning |
| :--- | :--- | :--- |
| **Spin** | $j$ | An integer or half-integer characteristic of the system. |
| **Bohr Magneton** | $\mu_B$ | $q_e\hbar/2m$; the scale of electronic magnetic moments. |
| **g-factor** | $g$ | A dimensionless proportionality constant for the magnetic moment. |
| **Precession Frequency** | $\omega_p$ | The frequency at which the moment precesses in field $B$. |

---

## 2. Experimental Verification: Stern-Gerlach and Rabi

### 2.1 The Stern-Gerlach Experiment (1922)
This experiment provided direct evidence of quantized angular momentum. Silver atoms were passed through a strong magnetic field gradient ($\partial B/\partial z$).
*   **Classical Expectation:** A continuous smear of atoms on the detector plate, as magnetic moments should be randomly oriented.
*   **Quantum Result:** The beam split into two distinct spots (for $j=1/2$). This confirmed that the atoms could only exist in specific magnetic states relative to the field axis.
*   **Force Equation:** $F_z = \mu \cos\theta \frac{\partial B}{\partial z}$ (where $\cos\theta$ takes only discrete values).

### 2.2 The Rabi Molecular-Beam Method
I. I. Rabi improved upon the precision of Stern-Gerlach by using resonance to measure $g$-factors. The apparatus uses three magnets:
1.  **Magnet 1:** Creates a field gradient to deflect atoms based on their spin state.
2.  **Magnet 2:** Provides a uniform field ($B_0$) and a weak oscillating horizontal field ($B'$). If the frequency $\omega$ of $B'$ matches $\omega_p$, transitions (spin flips) are induced.
3.  **Magnet 3:** An inverted gradient that refocuses the atoms toward the detector unless their spin was flipped in Magnet 2.

**Key Insight:** A decrease in detected current signifies resonance ($\omega = \omega_p$), allowing for the precise determination of the magnetic moment.

---

## 3. Paramagnetism in Bulk Materials

Paramagnetism occurs in materials containing atoms with permanent magnetic moments, typically those with unfilled inner electron shells (e.g., transition elements, rare earths).

### 3.1 Classical vs. Quantum Theory
Classical theory (Langevin) assumes all orientations are possible, while quantum theory accounts for discrete states.

| Model | Magnetization Formula ($M$) | Conditions |
| :--- | :--- | :--- |
| **Classical** | $M = \frac{N\mu^2B}{3kT}$ | Small fields ($\mu B \ll kT$) |
| **Quantum ($j=1/2$)** | $M = N\mu_0 \tanh\left(\frac{\mu_0B}{kT}\right)$ | General Case |
| **Quantum (General $j$)** | $M = Ng^2 \frac{j(j+1)}{3} \frac{\mu_B^2 B}{kT}$ | Low fields |

### 3.2 Saturation
At very high magnetic fields or very low temperatures, magnetization $M$ approaches a limiting value $N\mu_0$. This "saturation" occurs because all available moments become aligned with the external field.

---

## 4. Advanced Applications of Magnetic Resonance

### 4.1 Adiabatic Demagnetization
This technique is used to reach temperatures within a millionth of a degree of absolute zero.
1.  **Alignment:** A paramagnetic salt is cooled (via liquid helium) in a strong magnetic field, aligning the spins and lowering the system's entropy.
2.  **Isolation:** The salt is thermally isolated.
3.  **Demagnetization:** The external field is slowly reduced. As spins randomize due to thermal fluctuations, they must do work against the remaining field, absorbing energy from the lattice vibrations and cooling the material.
4.  **Nuclear Cooling:** Because nuclear moments are $\approx 1000$ times smaller than atomic moments, they can be used in a second stage to reach even lower temperatures.

### 4.2 Nuclear Magnetic Resonance (NMR)
NMR detects the extremely weak magnetism of atomic nuclei. Even in substances where electron spins balance out (like water), nuclear moments persist.
*   **Mechanism:** An oscillating field induces transitions between nuclear spin states. Absorption of energy is detected by a sensitive amplifier.
*   **Thermal Contact:** To observe the signal, "thermal contact" between the nuclei and the lattice is often required (e.g., adding iron oxide to water) to allow excited nuclei to return to the lower energy state.
*   **Applications:**
    *   **Magnetometry:** Precise measurement of magnetic field strengths.
    *   **Chemistry:** Determining molecular structures based on the "shift" in resonance caused by local chemical environments.
    *   **Free Radicals:** Detection of short-lived chemical intermediates.

---

## 5. Important Quotes and Contextual Analysis

> "The behavior of matter on a small scale... is different from anything that you are used to and is very strange indeed."

**Context:** Feynman introduces the "shocking" nature of quantized angular momentum, emphasizing that it cannot be made intelligible through classical analogies.

> "Understanding of these matters comes very slowly, if at all... one never gets a comfortable feeling that these quantum-mechanical rules are 'natural.'"

**Context:** A reflection on the pedagogical challenge of quantum mechanics, where "understanding" is defined more by the ability to predict results than by intuitive comfort.

> "The abject failure of classical ideas was completely revealed when Stern and Gerlach saw what actually happened."

**Context:** Highlighting the pivotal moment in 1922 when experimental results directly contradicted the classical prediction of a continuous distribution of magnetic moments.

---

## 6. Actionable Physical Insights

*   **Precession Frequency Consistency:** It is a notable coincidence of physics that the classical precession frequency of a gyroscope in a magnetic field is identical to the quantum mechanical frequency required to induce transitions between energy levels ($\omega_p = g(q/2m)B$).
*   **Temperature Dependence:** Paramagnetism is inversely proportional to temperature ($1/T$). At high temperatures, thermal agitation overcomes the aligning force of the magnetic field.
*   **Scale of Magnetism:** Nuclear magnetism is significantly weaker than atomic magnetism (by a factor of roughly $10^{-6}$ in susceptibility). This necessitates the use of resonance techniques or extremely low temperatures to observe nuclear effects.
*   **Transition Probability:** In a system with an oscillating horizontal field, transitions occur only at $\omega_p$. Transitions of "two steps" (e.g., jumping from $-3/2$ to $+1/2$ at $2\omega_p$) have zero probability in the described resonance methods.