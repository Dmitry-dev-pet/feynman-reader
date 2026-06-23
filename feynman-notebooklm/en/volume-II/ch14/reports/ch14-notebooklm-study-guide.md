# Chapter 14: The Magnetic Field in Various Situations

This study guide provides a comprehensive overview of magnetostatics, focusing on the vector potential, the mathematical analogies between electrostatics and magnetostatics, and the specific magnetic fields produced by various current configurations.

---

## Key Concepts

### 1. The Vector Potential ($\mathbf{A}$)
In magnetostatics, the divergence of the magnetic field ($\mathbf{B}$) is always zero ($\text{div} \mathbf{B} = 0$). This allows $\mathbf{B}$ to be represented as the curl of another vector field, known as the **vector potential**:
$$\mathbf{B} = \text{curl} \mathbf{A}$$
While the scalar potential $\phi$ in electrostatics is determined by a gradient, the vector potential is determined by its curl. This definition allows for "gauge latitude"—adding the gradient of any scalar field to $\mathbf{A}$ does not change the resulting $\mathbf{B}$ field. For mathematical convenience in magnetostatics, the divergence of $\mathbf{A}$ is typically set to zero ($\text{div} \mathbf{A} = 0$).

### 2. The Electrostatic Analogy
One of the most powerful tools in solving for the vector potential is the mathematical identity between the equations for $\mathbf{A}$ and the equations for the electrostatic potential $\phi$.

| Feature | Electrostatics | Magnetostatics (per component) |
| :--- | :--- | :--- |
| **Governing Equation** | $\nabla^2 \phi = -\frac{\rho}{\epsilon_0}$ | $\nabla^2 A_x = -\frac{j_x}{\epsilon_0 c^2}$ |
| **Source Term** | Charge density ($\rho$) | Current density component ($j_x / c^2$) |
| **Integral Solution** | $\phi(1) = \frac{1}{4\pi\epsilon_0} \int \frac{\rho(2) dV_2}{r_{12}}$ | $A_x(1) = \frac{1}{4\pi\epsilon_0 c^2} \int \frac{j_x(2) dV_2}{r_{12}}$ |

By solving three "imaginary" electrostatic problems (one for each component $j_x, j_y, j_z$), the complete vector potential $\mathbf{A}$ can be determined.

### 3. Magnetic Dipoles
A small loop of current $I$ with area $a \times b$ behaves at large distances as a **magnetic dipole**.
*   **Magnetic Dipole Moment ($\mu$):** Defined as the current times the area of the loop ($\mu = I \cdot \text{Area}$).
*   **Vector Potential of a Dipole:** $\mathbf{A} = \frac{1}{4\pi\epsilon_0 c^2} \frac{\boldsymbol{\mu} \times \mathbf{e}_R}{R^2}$.
*   **Field Characteristics:** Far from the source, the $\mathbf{B}$ field components of a magnetic dipole are mathematically identical to the $\mathbf{E}$ field components of an electric dipole.

### 4. The Law of Biot and Savart
While $\mathbf{B}$ can be found by taking the curl of $\mathbf{A}$, it can also be calculated directly from the current distribution using the Biot-Savart Law:
$$\mathbf{B}(1) = \frac{1}{4\pi\epsilon_0 c^2} \int \frac{\mathbf{j}(2) \times \mathbf{e}_{12}}{r_{12}^2} dV_2$$
For thin wires, the term $\mathbf{j} dV$ is replaced by $I d\mathbf{s}$. Although this direct integral exists, it is often more complex to evaluate than the vector potential due to the cross-product within the integral.

---

## Common Misconceptions

*   **Physical Reality of $\mathbf{A}$ vs. $\mathbf{B}$:** It is a common misconception that if the magnetic field $\mathbf{B}$ is zero in a region, the vector potential $\mathbf{A}$ must also be zero. The example of a long solenoid proves this false: outside the solenoid, $\mathbf{B}$ is zero, but $\mathbf{A}$ is non-zero and circulates around the solenoid.
*   **Relativity of Rotation:** One might assume that a rotating charged cylinder can be analyzed from the frame of the cylinder to simplify the physics. However, a rotating system is **not** an inertial frame. The laws of electromagnetism as presented must be applied with respect to inertial coordinate systems.
*   **Magnetic Poles:** Unlike electric fields, which originate from point charges (monopoles), magnetic "dipole" fields are produced by circulating current loops. There are no actual magnetic "poles" equivalent to electric charges.

---

## Self-Check Questions

1.  **What is the circulation of the vector potential $\mathbf{A}$ around a closed loop equal to?**
    *   *Answer:* It is equal to the magnetic flux of $\mathbf{B}$ through that loop ($\oint \mathbf{A} \cdot d\mathbf{s} = \int \mathbf{B} \cdot \mathbf{n} \, da$).
2.  **Why is $\text{div} \mathbf{A} = 0$ chosen as a condition in magnetostatics?**
    *   *Answer:* It is a choice of mathematical convenience that simplifies the relation between the vector potential and current density to a Poisson equation ($\nabla^2 \mathbf{A} = -\mathbf{j}/\epsilon_0 c^2$).
3.  **For a uniform magnetic field $\mathbf{B}_0$ in the $z$-direction, what is the simplest vector form of $\mathbf{A}$?**
    *   *Answer:* $\mathbf{A} = \frac{1}{2} \mathbf{B}_0 \times \mathbf{r}'$, where $\mathbf{r}'$ is the displacement from the $z$-axis.
4.  **How does the vector potential of a long straight wire behave outside the wire?**
    *   *Answer:* The $z$-component $A_z$ is proportional to the natural log of the distance from the wire ($A_z \propto \ln r'$).
5.  **What happens to the magnetic field inside a long solenoid if it is replaced by a rotating charged cylinder?**
    *   *Answer:* It produces a similar magnetic field $B = \sigma a \omega / \epsilon_0 c^2$, where $\sigma$ is surface charge, $a$ is radius, and $\omega$ is angular velocity.

---

## Essay Prompts for Deeper Exploration

1.  **The Utility of the Vector Potential:** Compare the process of finding the magnetic field using the Biot-Savart law versus using the vector potential. In what specific mathematical or physical scenarios does the vector potential offer a distinct advantage?
2.  **Analogies in Field Theory:** Discuss how the mathematical parallels between $\nabla^2 \phi = -\rho/\epsilon_0$ and $\nabla^2 \mathbf{A} = -\mathbf{j}/\epsilon_0 c^2$ allow physicists to apply solutions from electrostatics to magnetostatic problems. Provide examples such as the straight wire or the solenoid.
3.  **Non-Inertial Frames in Electromagnetism:** Using the example of the "angular-velocity meter" (a rotating charged cylinder with a radial wire), explain why the laws of electromagnetism must be used with caution in non-inertial frames and how the induced charges are interpreted.

---

## Glossary of Important Terms

| Term | Definition |
| :--- | :--- |
| **Magnetostatics** | The study of magnetic fields associated with steady (constant) currents. |
| **Vector Potential ($\mathbf{A}$)** | A vector field whose curl is the magnetic field ($\mathbf{B} = \text{curl} \mathbf{A}$) and whose divergence is typically set to zero in magnetostatics. |
| **Magnetic Dipole Moment ($\mu$)** | A vector representing the strength and orientation of a current loop; for a plane loop, it equals the current times the area. |
| **Biot-Savart Law** | An equation that describes the magnetic field generated by a constant electric current in terms of an integral over the current distribution. |
| **Surface Current Density ($\mathbf{J}$)** | The current per unit length flowing along a surface, such as the windings of a solenoid. |
| **Gauge Latitude** | The freedom to add the gradient of a scalar field to the vector potential without changing the resulting physical magnetic field. |
| **Solenoid** | A coil of wire, usually acting as an electromagnet, which produces a uniform magnetic field inside when carrying a current. |