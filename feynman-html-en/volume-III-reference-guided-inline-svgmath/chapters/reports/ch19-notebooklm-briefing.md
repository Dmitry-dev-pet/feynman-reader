# Chapter 19: The Hydrogen Atom and The Periodic Table

This briefing document provides an analytical synthesis of the quantum mechanical description of the hydrogen atom and its extension to the periodic table of elements. It details the mathematical derivation of wave functions, the physical significance of quantum numbers, and the qualitative explanation of chemical properties based on electronic configurations.

## Executive Summary

The application of Schrödinger’s equation to the hydrogen atom represents a definitive success for quantum mechanics, providing a rigorous theoretical basis for atomic spectra and the periodicities of chemical elements. By treating the proton as a fixed center of force and utilizing spherical polar coordinates, the analysis identifies specific energy states characterized by three quantum numbers ($n, l, m$). These states describe the spatial distribution (wave functions) of electrons. The document further explains how the exclusion principle and the filling of electronic "shells" give rise to the chemical properties observed in the periodic table, including the geometry of molecular bonds.

---

## 1. Mathematical Framework and Schrödinger’s Equation

To describe the hydrogen atom, the analysis employs the non-relativistic Schrödinger equation, assuming the proton is fixed at the origin and neglecting electron spin and relativistic effects.

### 1.1 The Hamiltonian and Potential
The rate of change of the amplitude $\psi(\mathbf{r}, t)$ is governed by:
$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$$
Where the Hamiltonian $\hat{H}$ is:
$$\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})$$
For hydrogen, the potential energy $V$ is the electrostatic field of the proton: $V = -e^2/r$.

### 1.2 Coordinate Transformation
Because the potential depends only on the radius $r$, the Laplacian $\nabla^2$ is converted from rectangular $(x, y, z)$ to spherical polar coordinates $(r, \theta, \phi)$.
*   **Figure 19-1** illustrates these coordinates: $r$ is the distance from the origin, $\theta$ is the polar angle from the $z$-axis, and $\phi$ is the azimuthal angle.

The resulting equation for the stationary state wave function $\psi(r, \theta, \phi)$ is:
$$\frac{1}{r}\frac{\partial^2}{\partial r^2}(r\psi) + \frac{1}{r^2}\left\{ \frac{1}{\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial \psi}{\partial \theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2\psi}{\partial \phi^2} \right\} = -\frac{2m}{\hbar^2}\left(E + \frac{e^2}{r}\right)\psi$$

---

## 2. Analysis of Energy States and Quantum Numbers

The solutions to the Schrödinger equation are restricted by physical requirements—specifically, that the wave function must approach zero as the radius $r$ approaches infinity for bound states.

### 2.1 Natural Atomic Units
To simplify the algebra, the following scale changes are used:
*   **Bohr Radius ($r_B$):** $\frac{\hbar^2}{me^2} \approx 0.529 \text{ \AA}$.
*   **Rydberg Energy ($E_R$):** $\frac{me^4}{2\hbar^2} \approx 13.6 \text{ eV}$.

### 2.2 Principal Quantum Number ($n$) and Energy
For the radial wave function to remain finite at large distances, the energy $E$ must be quantized according to the integer $n$:
$$E_n = -E_R \frac{1}{n^2}$$
*   **$n=1$:** The ground state (lowest energy).
*   **$n \to \infty$:** The energy approaches zero, representing a free electron.
*   **Figure 19-7** displays this energy level diagram, showing the convergence of levels as $n$ increases.

### 2.3 Angular Momentum ($l, m$)
The angular dependence of the wave function is characterized by the orbital angular momentum $l$ and its $z$-component $m$.
*   **$l$ (Orbital Quantum Number):** Must be an integer such that $0 \le l < n$.
*   **$m$ (Magnetic Quantum Number):** Can range from $-l$ to $+l$ (a total of $2l+1$ states).

#### Table 19-1: Dictionary of Orbital Angular Momentum
| $l$ | $m$ | Name | Number of States | Parity |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | $s$ | 1 | $+$ |
| 1 | $+1, 0, -1$ | $p$ | 3 | $-$ |
| 2 | $+2, \dots, -2$ | $d$ | 5 | $+$ |
| 3 | $\dots$ | $f$ | 7 | $-$ |

---

## 3. Physical Characteristics of Wave Functions

### 3.1 Spherically Symmetric States ($s$-states)
When $l=0$, the wave function depends only on $r$.
*   **$1s$ state:** $\psi_1 = e^{-\rho}$. The amplitude is maximum at the proton and drops exponentially.
*   **Higher $s$-states:** These involve oscillations (nodes). The $2s$ state has one node, and the $3s$ has two.
*   **Figure 19-2** shows the wave functions for the first three $l=0$ states, demonstrating that the number of "bumps" equals $n$.

### 3.2 Angular Dependence and "Pseudo-potential"
For states with $l > 0$, the electron possesses angular momentum. This introduces a "centrifugal force" term (a pseudo-potential) in the radial equation:
$$\text{Extra Term} = \frac{l(l+1)\hbar^2}{2mr^2}$$
This term pushes the electron amplitude away from the nucleus. For $l > 0$, the amplitude is zero at the center ($r=0$).
*   **Figure 19-5** shows a polar graph of the probability for a $p$-state ($l=1, m=0$), which follows a $\cos^2\theta$ distribution.
*   **Figure 19-6** provides sketches of various states, showing the shaded regions of high amplitude and the phase (plus/minus signs).

---

## 4. The Periodic Table of Elements

While exact solutions for many-electron atoms are not analytically possible, the hydrogen-like model, combined with the **Pauli Exclusion Principle**, explains the structure of the periodic table.

### 4.1 The Exclusion Principle and Shell Filling
The exclusion principle dictates that each individual electronic state can be occupied by only one electron (or two, if considering spin up/down).
*   **Shells:** States with the same $n$ form a shell.
*   **Sub-shells:** States with the same $n$ and $l$.

### 4.2 Representative Data for the First 36 Elements (Table 19-2 Excerpts)
The chemical properties are determined by the most loosely bound electron (ionization energy $W_I$) and the configuration of the outer shell.

| Z | Element | $W_I$ (eV) | Electron Configuration (Outer) | Chemical Character |
| :--- | :--- | :--- | :--- | :--- |
| 2 | He | 24.6 | $1s^2$ | Inert (Filled shell) |
| 3 | Li | 5.4 | $2s^1$ | Active (One outer electron) |
| 10 | Ne | 21.6 | $2s^2 2p^6$ | Inert (Filled $n=2$ shell) |
| 11 | Na | 5.1 | $3s^1$ | Active (New shell starts) |
| 18 | Ar | 15.8 | $3s^2 3p^6$ | Inert |
| 19 | K | 4.3 | $4s^1$ | Active (4s fills before 3d) |

### 4.3 Key Anomalies and Observations
*   **3d vs. 4s:** In potassium ($Z=19$), the $4s$ state is filled before the $3d$ because the $s$-state (with some amplitude near the nucleus) has lower energy than the $d$-state (which is pushed out by the centrifugal term).
*   **Chemical Groups:** Elements like Lithium, Sodium, and Potassium have similar configurations ($s^1$) and thus similar chemical activity.
*   **Noble Gases:** Helium, Neon, Argon, and Krypton have high ionization energies due to filled shells/sub-shells, making them chemically inert.

---

## 5. Actionable Insights: Molecular Geometry

Quantum mechanics explains not only the existence of bonds but their directional properties (directed valences).

*   **Water ($H_2O$):** Oxygen has two vacancies in its $2p$ shell (e.g., in the $x$ and $y$ orbitals). Hydrogen atoms share electrons to fill these vacancies. While the orbitals are at $90^\circ$, electrical repulsion between the now-positive hydrogens pushes the bond angle to $105^\circ$.
*   **Ammonia ($NH_3$):** Nitrogen has three vacancies in the $2p$ orbitals ($x, y, z$). This results in a non-flat, pyramidal structure, which is the physical basis for the ammonia maser.
*   **Trends in Hydrides:** As the central atom gets larger (e.g., from Oxygen to Sulfur to Selenium), the hydrogens are further apart, reducing repulsion and allowing the bond angle to return closer to $90^\circ$ (e.g., $93^\circ$ for $H_2S$, and nearly $90^\circ$ for $H_2Se$).

---

## 6. Important Quotes

> "The most dramatic success in the history of the quantum mechanics was the understanding of the details of the spectra of some simple atoms and the understanding of the periodicities which are found in the table of chemical elements."

> "A state with zero orbital angular momentum is called by a special name. It is called an 's-state'—you can remember 's for spherically symmetric.'"

> "The Schrödinger equation... by providing the key to the underlying machinery of atomic structure it has given an explanation for atomic spectra, for chemistry, and for the nature of matter."

> "The energies are negative because when we chose to write $V = -e^2/r$, we picked our zero point as the energy of an electron located far from the proton. When it is close to the proton, its energy is less, so somewhat below zero."