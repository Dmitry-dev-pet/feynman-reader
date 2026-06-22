# Analytical Briefing: The Dependence of Amplitudes on Position

## Executive Summary

This document provides a comprehensive analysis of the transition in quantum mechanical description from discrete base states to a continuous spatial representation. Traditionally, quantum systems like the ammonia molecule or an electron in a crystal lattice are described using a finite number of base states. However, a complete theory requires accounting for the "anywhere and everywhere" probability of a particle's position. By taking the limit of a crystal lattice spacing to zero, the discrete Hamiltonian equations evolve into the **Schrödinger Equation**, the fundamental law of motion for quantum particles in free space and potential fields.

Key takeaways include the definition of the **wave function** ($\psi$) as an amplitude density, the mathematical necessity of the **Dirac delta function** for normalization in continuous space, the quantitative derivation of the **Heisenberg Uncertainty Principle**, and the explanation of how discrete energy levels arise from continuous differential equations in bound systems.

---

## 1. From Discrete Lattices to the Continuum

In previous models, such as an electron moving along a line of atoms with spacing $b$, the state was defined by the amplitude $C_n$ to be at atom $n$. The energy for small wave numbers $k$ was given by:
$$E = Ak^2b^2$$
Where $A$ is the amplitude per unit time for the electron to jump between atoms. By imagining the lattice spacing $b$ shrinking to zero while keeping $Ab^2$ constant (defined by the effective mass $m_{\text{eff}}$), the discrete system transitions into a continuous one.

### The Limit Process
As $b \to 0$, the discrete difference equation:
$$i\hbar \frac{\partial C(x_n)}{\partial t} = E_0 C(x_n) - AC(x_n+b) - AC(x_n-b)$$
transforms into the second derivative of a continuous function $C(x)$. This results in the fundamental Schrödinger equation for a free particle:
$$i\hbar \frac{\partial C(x)}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 C(x)}{\partial x^2}$$

---

## 2. The Wave Function and Probability Density

In a continuous system, the state vector $|\psi\rangle$ is described by an infinite set of amplitudes $\langle x | \psi \rangle$, labeled as the wave function $\psi(x)$.

### Probability Interpretation
Because the probability of finding a particle at an exact point is zero, $\psi(x)$ is interpreted as an **amplitude density**. The probability of finding the particle in a small interval $\Delta x$ is:
$$\text{Prob}(x, \Delta x) = |\psi(x)|^2 \Delta x$$

### Normalization and Summation
When moving to the continuum, discrete summations are replaced by integrals. The amplitude to find a state $|\psi\rangle$ in state $|\phi\rangle$ is:
$$\langle \phi | \psi \rangle = \int \phi^*(x) \psi(x) \, dx$$

---

## 3. Momentum States and the Uncertainty Principle

A particle with a definite momentum $p$ has a spatial amplitude variation defined by:
$$\langle x | \text{mom } p \rangle = e^{ipx/\hbar}$$

### The Momentum Distribution
To find the amplitude $\phi(p)$ for a specific momentum in a state $\psi(x)$, one performs a Fourier-like transformation:
$$\phi(p) = \langle \text{mom } p | \psi \rangle = \int_{-\infty}^{+\infty} e^{-ipx/\hbar} \psi(x) \, dx$$

### The Quantitative Uncertainty Principle
Using a Gaussian wave function $\psi(x) = Ke^{-x^2/4\sigma^2}$, the analysis demonstrates that the momentum distribution is also a Gaussian. The relationship between the spatial width ($\sigma$) and the momentum width ($\eta$) is:
$$\eta = \frac{\hbar}{2\sigma}$$
Defining these as uncertainties $\Delta p$ and $\Delta x$ leads to the minimum product:
$$\Delta p \Delta x \geq \frac{\hbar}{2}$$
This confirms that narrowing the distribution in position $(\sigma \to 0)$ inevitably spreads the distribution in momentum $(\eta \to \infty)$.

---

## 4. Mathematical Infrastructure: The Dirac Delta Function

In discrete space, base states are orthogonal: $\langle i | j \rangle = \delta_{ij}$. In continuous space, a new function is required to satisfy the condition $\psi(x') = \int \langle x' | x \rangle \psi(x) \, dx$.

### The $\delta(x)$ Function
The "function" $\delta(x)$ is defined by its behavior under an integral:
1. $\delta(x) = 0$ for all $x \neq 0$.
2. $\int \delta(x) \, dx = 1$.
3. $\int \delta(x-x') \psi(x) \, dx = \psi(x')$.

This represents a physical state where the particle is located precisely at a single point, visualized as the limit of a sequence of narrower and taller rectangles of unit area (**Fig. 16–2**).

---

## 5. The Schrödinger Equation

The full Schrödinger equation accounts for forces acting on a particle via a potential energy $V(x)$. For low energies and non-relativistic motion:

### One-Dimensional Form
$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} + V(x)\psi(x)$$

### Three-Dimensional Form
$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi + V\psi$$

### Many-Particle Systems
For systems with multiple particles, the wave function $\psi(\mathbf{r}_1, \mathbf{r}_2, \dots)$ is not a wave in 3D space but a function in a high-dimensional space (3 variables per particle). Interactions, such as electrostatic energy, are included in the potential term $V(\mathbf{r}_1, \mathbf{r}_2, \dots)$. This explains why measurements on one particle can instantly affect the description of another; they share a single, multi-variable wave function.

---

## 6. Quantized Energy Levels in Potential Wells

A major triumph of the Schrödinger equation is explaining how discrete energy levels arise from a continuous equation. For a particle in a potential well (**Fig. 16–3**), we look for steady states: $\psi = a(x) e^{-iEt/\hbar}$.

### Curvature and Energy
The spatial part $a(x)$ must satisfy:
$$\frac{d^2 a(x)}{dx^2} = \frac{2m}{\hbar^2} [V(x) - E] a(x)$$

| Condition | Curvature of $a(x)$ | Shape |
| :--- | :--- | :--- |
| **$V > E$** | Concave *away* from x-axis | Exponential growth/decay (**Fig. 16–4a**) |
| **$V < E$** | Concave *toward* x-axis | Sinusoidal/Oscillatory (**Fig. 16–4b**) |

### The Origin of Discrete States
For a particle to be "bound," the wave function must approach zero at $x = \pm \infty$.
*   If the energy $E$ is chosen arbitrarily, the function $a(x)$ typically "blows up" to infinity outside the well (**Fig. 16–6**, **Fig. 16–7**).
*   Only for specific, discrete values of energy ($E_c$) will the wave function curve back to zero at both ends (**Fig. 16–8**).
*   Higher energy levels correspond to wave functions with more nodes (crossings of the x-axis) (**Fig. 16–9**).

---

## 7. Important Quotes with Context

> **"The correct quantum mechanical equation for the motion of an electron in free space was first discovered by Schrödinger... he gave a kind of derivation based on some heuristic arguments and some brilliant intuitive guesses."**
*   *Context:* Discussing the transition from the lattice model to Eq. (16.13) and emphasizing that while it can be motivated by lattice models, it is a fundamental postulate of physics.

> **"The probability of finding a particle exactly at any particular point is zero... We can only describe the probability of finding an electron in terms of a probability distribution."**
*   *Context:* Explaining why the absolute square of the wave function must be treated as a density rather than a direct probability for discrete points in a continuum.

> **"Any physical state $|\psi\rangle$ can be defined by giving all of the amplitudes $\langle x_1, x_2 | \psi \rangle$... It is, in general, some kind of a wave in the six dimensions defined by $x_1$ and $x_2$."**
*   *Context:* Addressing the complexity of multi-particle systems and explaining why independent 3D wave functions are insufficient to describe interacting particles.

---

## 8. Summary of Physical Principles

| Principle | Description |
| :--- | :--- |
| **Continuum Limit** | Quantum laws for space are the limit of laws for a dense lattice of points. |
| **Wave Function ($\psi$)** | An "amplitude density" whose square is the probability density per unit volume. |
| **Uncertainty Relation** | Localizing a particle in space ($x$) necessarily increases the spread of its possible momenta ($p$). |
| **Schrödinger Equation** | Describes the diffusion of probability amplitude from one point to neighboring points. |
| **Energy Quantization** | Result of the requirement that a bound particle's wave function must vanish at infinity. |