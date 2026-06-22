# Analysis of Probability Amplitudes: Quantum Mechanical Principles and Applications

This briefing document provides a comprehensive analysis of the fundamental principles of quantum mechanics as they relate to probability amplitudes, based on the pedagogical approach outlined in Chapter 3 of the *Feynman Lectures on Physics, Volume III*.

## Executive Summary

The transition from classical to quantum mechanics necessitates a departure from describing the detailed behavior of particles in space to a framework based on probability amplitudes. This chapter establishes the core mathematical rules for combining these amplitudes: summing amplitudes for indistinguishable alternative paths and multiplying them for successive events. The presence of any mechanism—even in principle—that allows for the determination of a particle's specific path destroys interference, shifting the calculation from the sum of amplitudes to the sum of individual probabilities. These principles are demonstrated through electron interference, neutron scattering in crystals, and the behavior of identical particles such as $\alpha$-particles and electrons.

## I. Fundamental Laws for Combining Amplitudes

Quantum mechanics relies on three general principles for calculating the probability of physical events. These are expressed using Dirac’s "bra-ket" shorthand notation: $\braket{\text{Final State}}{\text{Initial State}}$.

### 1. The Probability Principle
The probability ($P$) of an event is the absolute square of a complex number called the probability amplitude ($\phi$):
$$P = |\phi|^2$$

### 2. The Superposition Principle (Indistinguishable Alternatives)
When a particle can reach a final state through two or more indistinguishable routes, the total amplitude for the process is the sum of the amplitudes for each route considered separately.
$$\braket{x}{s}_{\text{total}} = \braket{x}{s}_{\text{route 1}} + \braket{x}{s}_{\text{route 2}}$$
The resulting probability is $P_{12} = |\phi_1 + \phi_2|^2$.

### 3. The Succession Principle (Sequential Events)
If a particle goes through a particular route by a succession of events, the amplitude for that route is the product of the amplitudes for each individual step.
$$\braket{x}{s}_{\text{via 1}} = \braket{x}{1}\braket{1}{s}$$
This is read from right to left: the amplitude to go from source $s$ to hole 1, then from hole 1 to detector $x$.

### Mathematical Representation of a Free Particle
For a free particle with momentum $p$ moving from $\mathbf{r}_1$ to $\mathbf{r}_2$, the amplitude is approximately:
$$\braket{\mathbf{r}_2}{\mathbf{r}_1} \approx \frac{e^{i(p \cdot r_{12}/\hbar)}}{r_{12}}$$
where $r_{12} = |\mathbf{r}_2 - \mathbf{r}_1|$. This illustrates the wavelike properties of particles, where the amplitude propagates with a wave number equal to $p/\hbar$.

---

## II. Distinguishability and the Role of Observation

A critical distinction in quantum mechanics is whether different paths can be distinguished. The act of "observing" or the mere existence of a "record" of the path taken changes the outcome.

### The Two-Slit Experiment with Light
In an experiment where light is used to detect which hole an electron passes through (Fig. 3-3):
*   **Without Path Information:** If the wavelength of light is long (ineffective detection), the amplitudes interfere: $|\phi_1 + \phi_2|^2$.
*   **With Path Information:** If the light identifies the hole (short wavelength), the interference is destroyed. The observer must square the amplitudes first and then sum them: $|\phi_1|^2 + |\phi_2|^2$.

**Rule of Final States:** Amplitudes must never be added for different and distinct final states. If a photon is scattered into a specific detector, that constitutes a distinct final state. Nature behaves according to the potential to distinguish the path, regardless of whether a human actually records the data.

---

## III. Case Study: Neutron Scattering from Crystals

The scattering of neutrons from a periodic array of nuclei (Fig. 3-5) serves as a proof of the distinguishability rule involving internal particle states (spin).

| Nuclei Type | Physical Process | Result |
| :--- | :--- | :--- |
| **Spin Zero** | All routes are indistinguishable; no record of which nucleus scattered the neutron. | Sharp interference peaks (Fig. 3-6a). |
| **Spin One-Half (No Spin Flip)** | If the neutron scatters without changing spin, the atoms remain in their original state. | Interference pattern persists. |
| **Spin One-Half (With Spin Flip)** | If a neutron flips its spin, it must flip the spin of a specific nucleus. This "leaves a record" of which atom did the scattering. | No interference; smooth distribution (Fig. 3-6b). |

In a crystal with spin, both processes occur. The total counting rate is the sum of the interference probability and the non-interference (spin-flip) probability (Fig. 3-6c).

---

## IV. The Physics of Identical Particles

The behavior of particles during collisions depends on whether they are "identical" (indistinguishable) or "distinguishable."

### 1. Distinguishable Particles (e.g., $\alpha$-particles on Oxygen)
When an $\alpha$-particle hits an oxygen nucleus, there are two ways to get a particle in a detector at angle $\theta$:
1.  The $\alpha$-particle scatters at angle $\theta$.
2.  The Oxygen nucleus scatters at angle $\theta$ (meaning the $\alpha$-particle went to $\pi-\theta$).
Since we can tell an $\alpha$-particle from an oxygen nucleus, we sum the probabilities:
$$P = |f(\theta)|^2 + |f(\pi-\theta)|^2$$

### 2. Identical Particles with Positive Interference (e.g., $\alpha$-on-$\alpha$)
If both particles are $\alpha$-particles, they are identical. We cannot know if the detected particle was the projectile or the target. We sum the amplitudes:
$$P = |f(\theta) + f(\pi-\theta)|^2$$
At $90^\circ$, this results in **four times** the individual scattering amplitude, or twice what classical physics predicts.

### 3. Identical Particles with Negative Interference (e.g., Electrons)
Electrons (and protons) follow a "most peculiar rule": when their roles are exchanged, the new amplitude interferes with the old one with an **opposite phase** (a minus sign).

*   **Parallel Spins:** If both electrons have the same spin, they are indistinguishable, but the amplitudes subtract:
    $$P = |f(\theta) - f(\pi-\theta)|^2$$
*   **Antiparallel Spins:** If one is "up" and one is "down," they are distinguishable by their spin. No interference occurs; we add probabilities.

#### Unpolarized Electron Scattering
In a random (unpolarized) beam, the total probability is calculated by summing the cases of different spin alignments:

| Case | Alignment | Probability Formula |
| :--- | :--- | :--- |
| 1/4 | Both Up | $|f(\theta) - f(\pi-\theta)|^2$ |
| 1/4 | Both Down | $|f(\theta) - f(\pi-\theta)|^2$ |
| 1/4 | Up/Down | $|f(\theta)|^2 + |f(\pi-\theta)|^2$ (No interference) |
| 1/4 | Down/Up | $|f(\pi-\theta)|^2 + |f(\theta)|^2$ (No interference) |

---

## V. Key Quotes and Contextual Analysis

> **"What are usually called the advanced parts of quantum mechanics are, in fact, quite simple. The mathematics that is involved is particularly simple, involving simple algebraic operations..."**
*   **Context:** Feynman explains his pedagogical choice to teach amplitudes and spin early, rather than focusing on the complex differential equations of the Schrödinger equation.

> **"Nature does not know what you are looking at, and she behaves the way she is going to behave whether you bother to take down the data or not."**
*   **Context:** Discussing the two-slit experiment with light. This emphasizes that interference is destroyed by the *possibility* of path determination (the scattering of a photon), not the conscious act of human observation.

> **"If you could, in principle, distinguish the alternative final states... the total, final probability is obtained by calculating the probability for each state... and then adding them together."**
*   **Context:** This is the fundamental rule for when to stop adding amplitudes and start adding probabilities. It applies to both the "which-path" electron experiments and the neutron spin-flip scenarios.

---

## VI. Actionable Insights for Analysis

1.  **Identify Distinguishability First:** Before calculating probabilities, determine if the paths taken are indistinguishable. If any change in the environment or internal state (like a spin-flip or a scattered photon) identifies the path, do not add amplitudes.
2.  **Sequential vs. Alternative Logic:**
    *   Use **multiplication** for events happening in a "chain" (succession).
    *   Use **addition** for events happening as "options" (alternatives).
3.  **Account for Particle Identity:** When dealing with collisions of identical particles, verify if the exchange of particles introduces a positive ($\alpha$-particles) or negative (electrons) interference term.
4.  **State Completeness:** To predict the future of a quantum system, one only needs the amplitudes for the possible intermediate states (e.g., $\braket{1}{s}$ and $\braket{2}{s}$). These numbers contain all necessary information about the previous history of the particle.