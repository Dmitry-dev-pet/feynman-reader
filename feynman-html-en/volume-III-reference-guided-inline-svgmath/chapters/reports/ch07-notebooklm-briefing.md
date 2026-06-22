# Briefing: The Dependence of Amplitudes on Time

This briefing document provides a comprehensive analysis of the relationship between quantum mechanical probability amplitudes and time, as outlined in Volume III, Chapter 7 of the Feynman Lectures on Physics. It details the transition from stationary states to particle motion, the quantum basis for energy conservation, and the behavior of spin-one-half particles in magnetic fields.

## Executive Summary

The central thesis of this analysis is that the time dependence of a probability amplitude is fundamentally governed by the total energy of the system. For a particle in a state of definite energy ($E$), the amplitude varies as $e^{-i(E/\hbar)t}$. This relationship provides the bridge between quantum mechanics and classical physics:
*   **Stationary States:** Particles with definite energy have time-independent probabilities.
*   **Classical Motion:** The movement of classical particles is shown to be the result of the interference of multiple amplitudes (wave packets) moving at a group velocity.
*   **Conservation of Energy:** In quantum terms, the conservation of energy is equivalent to the requirement that frequencies remain constant across space when conditions are time-independent.
*   **Physical Phenomena:** The theory accounts for complex phenomena such as the penetration of potential barriers (tunneling) and the precession of particle spins in magnetic fields.

---

## Key Analytical Themes

### 1. Stationary States and the Energy-Time Relationship
For any particle or atom at rest with a definite energy $E_0$, the probability amplitude to find it at a specific position is identical throughout space but varies periodically in time.

*   **The Amplitude Rule:** The amplitude is expressed as $ae^{-i(E_0/\hbar)t}$, where $\hbar\omega = E_0$.
*   **The Uncertainty Principle:** A definite energy implies a definite momentum (zero for a particle at rest). According to $\Delta p \Delta x = \hbar$, an absolute certainty in momentum necessitates an infinite uncertainty in position, explaining why the amplitude is the same everywhere in space.
*   **Time Independence:** Because the amplitude varies as an imaginary exponential ($e^{-i\omega t}$), its absolute square (the probability) is independent of time. This is the definition of a "stationary state." Changes in probability over time only occur through the interference of two or more states with different energy levels.

### 2. Amplitudes in Uniform Motion
Using relativistic transformations, the behavior of an amplitude for a moving particle can be deduced from its behavior at rest.

*   **Lorentz Transformation:** Transforming the rest-frame amplitude to a moving frame (velocity $v$) results in an amplitude that varies in both space and time: $e^{-(i/\hbar)(E_pt - \mathbf{p} \cdot \mathbf{x})}$.
*   **De Broglie Wavelength:** This transformation naturally yields the de Broglie relationship, where the wavelength $\lambda = h/p$.
*   **Group Velocity:** When multiple amplitudes of nearly the same energy are superimposed, they form "lumps" or beats. The velocity at which these lumps move (the group velocity $v_g = d\omega/dk$) is shown to be exactly equal to the classical velocity of the particle ($p/M$).

### 3. Potential Energy and Energy Conservation
The introduction of a potential $V$ shifts the frequency of the amplitude variation. The total energy governing the phase is the sum of internal, kinetic, and potential energies: $\hbar\omega = W_{\text{int}} + \frac{p^2}{2M} + V$.

*   **Energy Conservation as Frequency Consistency:** If a potential is constant in time but varies in space, the frequency of the amplitude must remain the same everywhere. This requirement leads directly to the classical law of conservation of energy.
*   **Barrier Penetration (Tunneling):** If a particle encounters a potential barrier $V$ higher than its total energy, the momentum $p$ becomes imaginary. In this region, the amplitude does not oscillate but decays exponentially ($e^{-p'x/\hbar}$). If the barrier is narrow, the amplitude may remain non-zero on the other side, allowing the particle to "leak" through—a phenomenon that explains alpha-particle decay in uranium nuclei.

### 4. The Classical Limit of Forces
Quantum mechanics converges with Newtonian mechanics ($F = ma$) when potential variations are slow and smooth relative to the wavelength.
*   **Refraction of Waves:** A transverse potential gradient causes different parts of a wavefront to advance at different phases. This "refracts" the probability amplitude, changing its direction.
*   **Deflection:** The calculated angular deflection of these quantum waves is identical to the deflection calculated using classical forces ($F = -\partial V / \partial y$).

### 5. Spin Precession
The dependence of amplitude on energy also applies to magnetic moments in magnetic fields ($U = -\boldsymbol{\mu} \cdot \mathbf{B}$).
*   **Magnetic Phase Shift:** In a uniform magnetic field, the two states of a spin-one-half particle (up and down) experience phase changes in opposite directions: $e^{\pm(i/\hbar)\mu B\tau}$.
*   **Precession:** This phase difference causes the direction of polarization to rotate, or precess, about the magnetic field axis at a frequency of $\omega_p = 2\mu B / \hbar$.

---

## Mathematical Summary

| Concept | Formula | Physical Meaning |
| :--- | :--- | :--- |
| **Rest Amplitude** | $ae^{-i(E_0/\hbar)t}$ | Temporal phase variation for a stationary particle. |
| **Moving Amplitude** | $e^{-(i/\hbar)(E_pt - \mathbf{p} \cdot \mathbf{x})}$ | Space-time variation for a particle with momentum $p$. |
| **Energy-Momentum** | $E_p = \sqrt{(pc)^2 + E_0^2}$ | Relativistic energy relation. |
| **Group Velocity** | $v_g = \frac{d\omega}{dk} = \frac{p}{M}$ | Velocity of probability "lumps" matches classical velocity. |
| **Total Energy** | $\hbar\omega = E_{kinetic} + V_{potential}$ | Total energy determines the rate of phase change. |
| **Precession Frequency**| $\omega_p = \frac{2\mu B}{\hbar}$ | Rate at which a spin-1/2 particle rotates in a B-field. |

---

## Important Quotes with Context

> **"The choice of an origin for our energy scale makes no difference; we can measure energy from any zero we want... provided we shift all the energies in a particular calculation by the same constant."**

*Context:* Feynman explains that adding a constant to all energy levels merely multiplies all amplitudes by the same phase factor ($e^{-i(A/\hbar)t}$). Since probabilities are derived from the absolute square of the amplitude, this factor disappears, rendering the absolute zero-point of energy physically irrelevant in this context.

> **"Radiation or absorption goes in the direction of increasing entropy."**

*Context:* In discussing why excited atoms eventually decay by emitting photons, Feynman notes that the total energy of the system (atom + field) remains constant. The decay occurs because there are vastly more states available in the electromagnetic field for the energy to occupy, making de-excitation the most probable outcome.

> **"How can one get a number like $10^9$ years from $10^{-22}$ sec? The answer is that the exponential gives the tremendously small factor of about $e^{-45}$."**

*Context:* This refers to the alpha-decay of uranium. While particles inside the nucleus oscillate at extreme frequencies, the probability of "leaking" through the potential barrier is so minute due to the exponential decay of the amplitude that the resulting average lifespan of the nucleus is billions of years.

---

## Actionable Insights

1.  **Probability Predictability:** To determine if a system's probability distribution will change over time, identify if it is in a "pure" energy state. If the energy is definite, the state is stationary and probabilities are constant.
2.  **Quantum-Classical Transition:** When modeling particle paths in a potential field, the classical trajectory can be viewed as the path of maximum constructive interference of quantum waves.
3.  **Barrier Design:** In quantum systems, "forbidden" regions (where $V > E$) do not immediately zero out the particle presence. The exponential decay constant ($p'/\hbar$) determines how thin a barrier must be to allow for significant tunneling.
4.  **Experimental Spin Measurement:** The precession of spin-one-half particles (like muons) in a magnetic field provides a precise mechanism for measuring magnetic moments by observing the oscillation frequency of decay products.