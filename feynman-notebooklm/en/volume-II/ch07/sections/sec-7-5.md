## 7–5 The electrostatic field of a grid

As our last example, we would like to describe another interesting property of electric fields. It is one which is made use of in the design of electrical instruments, in the construction of vacuum tubes, and for other purposes. This is the character of the electric field near a grid of charged wires. To make the problem as simple as possible, let us consider an array of parallel wires lying in a plane, the wires being infinitely long and with a uniform spacing between them.

If we look at the field a large distance above the plane of the wires, we see a constant electric field, just as though the charge were uniformly spread over a plane. As we approach the grid of wires, the field begins to deviate from the uniform field we found at large distances from the grid. We would like to estimate how close to the grid we have to be in order to see appreciable variations in the potential. Figure 7–8 shows a rough sketch of the equipotentials at various distances from the grid. The closer we get to the grid, the larger the variations. As we travel parallel to the grid, we observe that the field fluctuates in a periodic manner.

### Figure Ch7-F8
Caption: Fig. 7–8.Equipotential surfaces above a uniform grid of charged wires.
Image: figures/Ch7-F8.svg
![Fig. 7–8.Equipotential surfaces above a uniform grid of charged wires.](figures/Ch7-F8.svg)

Now we have seen (Chapter 50, Vol. I) that any periodic quantity can be expressed as a sum of sine waves (Fourier’s theorem). Let’s see if we can find a suitable harmonic function that satisfies our field equations.

If the wires lie in the xy -plane and run parallel to the y -axis, then we might try terms like

\phi(x,z)=F_n(z)\cos\frac{2\pi nx}{a}, (7.41)

where a is the spacing of the wires and n is the harmonic number. (We have assumed long wires, so there should be no variation with y .) A complete solution would be made up of a sum of such terms for n=1 , 2 , 3 , \dotsc .

If this is to be a valid potential, it must satisfy Laplace’s equation in the region above the wires (where there are no charges). That is,

\frac{\partial^2\phi}{\partial x^2}+ \frac{\partial^2\phi}{\partial z^2}=0.

Trying this equation on the \phi in ( 7.41), we find that

-\frac{4\pi^2n^2}{a^2}F_n(z)\cos\frac{2\pi nx}{a}+ \frac{d^2F_n}{dz^2}\cos\frac{2\pi nx}{a}=0, (7.42)

or that F_n(z) must satisfy

\frac{d^2F_n}{dz^2}=\frac{4\pi^2 n^2}{a^2}\,F_n. (7.43)

So we must have

F_n=A_ne^{-z/z_0}, (7.44)

where

z_0=\frac{a}{2\pi n}. (7.45)

We have found that if there is a Fourier component of the field of harmonic n , that component will decrease exponentially with a characteristic distance z_0=a/2\pi n . For the first harmonic ( n=1 ), the amplitude falls by the factor e^{-2\pi} (a large decrease) each time we increase z by one grid spacing a . The other harmonics fall off even more rapidly as we move away from the grid. We see that if we are only a few times the distance a away from the grid, the field is very nearly uniform, i.e., the oscillating terms are small. There would, of course, always remain the “zero harmonic” field

\phi_0=-E_0z

to give the uniform field at large z . For a complete solution, we would combine this term with a sum of terms like ( 7.41) with F_n from ( 7.44). The coefficients A_n would be adjusted so that the total sum would, when differentiated, give an electric field that would fit the charge density \lambda of the grid wires.

The method we have just developed can be used to explain why electrostatic shielding by means of a screen is often just as good as with a solid metal sheet. Except within a distance from the screen a few times the spacing of the screen wires, the fields inside a closed screen are zero. We see why copper screen—lighter and cheaper than copper sheet—is often used to shield sensitive electrical equipment from external disturbing fields.
