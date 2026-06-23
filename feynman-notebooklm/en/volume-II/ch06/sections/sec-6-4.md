## 6–4 The dipole potential as a gradient

We would like to point out a rather amusing thing about the dipole formula, Eq. ( 6.13). The potential can also be written as

\phi=-\frac{1}{4\pi\epsilon_0}\mathbf{p}\cdot\boldsymbol{\nabla}{\biggl(\frac{1}{r}\biggr)}. (6.16)

If you calculate the gradient of 1/r , you get

\boldsymbol{\nabla}{\biggl(\frac{1}{r}\biggr)}=-\frac{\mathbf{r}}{r^3}= -\frac{\mathbf{e}_r}{r^2},

and Eq. ( 6.16) is the same as Eq. ( 6.13).

How did we think of that? We just remembered that \mathbf{e}_r/r^2 appeared in the formula for the field of a point charge, and that the field was the gradient of a potential which has a 1/r dependence.

### Figure Ch6-F5
Caption: Fig. 6–5.The potential at PP from a point charge at Δz\Delta z above the origin is the same as the potential at P′P' (Δz\Delta z below PP) from the same charge at the origin.
Image: figures/Ch6-F5.svg
![Fig. 6–5.The potential at PP from a point charge at Δz\Delta z above the origin is the same as the potential at P′P' (Δz\Delta z below PP) from the same charge at the origin.](figures/Ch6-F5.svg)

There is a physical reason for being able to write the dipole potential in the form of Eq. ( 6.16). Suppose we have a point charge q at the origin. The potential at the point P at (x,y,z) is

\phi_0=\frac{q}{r}.

(Let’s leave off the 1/4\pi\epsilon_0 while we make these arguments; we can stick it in at the end.) Now if we move the charge +q up a distance \Delta z , the potential at P will change a little, by, say, \Delta\phi_+ . How much is \Delta\phi_+ ? Well, it is just the amount that the potential would change if we were to leave the charge at the origin and move P downward by the same distance \Delta z (Fig. 6–5 ). That is,

\Delta\phi_+=-\frac{\partial \phi_0}{\partial z}\Delta z,

where by \Delta z we mean the same as d/2 . So, using \phi_0=q/r , we have that the potential from the positive charge is

\phi_+=\frac{q}{r}-\frac{\partial }{\partial z}\biggl(\frac{q}{r}\biggr)\frac{d}{2}. (6.17)

Applying the same reasoning for the potential from the negative charge, we can write

\phi_-=\frac{-q}{r}+\frac{\partial }{\partial z}\biggl(\frac{-q}{r}\biggr)\frac{d}{2}. (6.18)

The total potential is the sum of ( 6.17) and ( 6.18):

\begin{aligned} \phi=\phi_++\phi_-&=-\frac{\partial }{\partial z}\biggl(\frac{q}{r}\biggr)d\\[1ex] &=-\frac{\partial }{\partial z}\biggl(\frac{1}{r}\biggr)qd \end{aligned} (6.19)

For other orientations of the dipole, we could represent the displacement of the positive charge by the vector \Delta\mathbf{r}_+ . We should then write the equation above Eq. ( 6.17) as

\Delta\phi_+=-\boldsymbol{\nabla}{\phi_0}\cdot\Delta\mathbf{r}_+,

where \Delta\mathbf{r}_+ is then to be replaced by \mathbf{d}/2 . Completing the derivation as before, Eq. ( 6.19) would then become

\phi=-\boldsymbol{\nabla}{\biggl(\frac{1}{r}\biggr)}\cdot q\mathbf{d}.

This is the same as Eq. ( 6.16), if we replace q\mathbf{d}=\mathbf{p} , and put back the 1/4\pi\epsilon_0 . Looking at it another way, we see that the dipole potential, Eq. ( 6.13), can be interpreted as

\phi=-\mathbf{p}\cdot\boldsymbol{\nabla}{\Phi_0}, (6.20)

where \Phi_0=1/4\pi\epsilon_0 r is the potential of a unit point charge.

Although we can always find the potential of a known charge distribution by an integration, it is sometimes possible to save time by getting the answer with a clever trick. For example, one can often make use of the superposition principle. If we are given a charge distribution that can be made up of the sum of two distributions for which the potentials are already known, it is easy to find the desired potential by just adding the two known ones. One example of this is our derivation of ( 6.20), another is the following.

Suppose we have a spherical surface with a distribution of surface charge that varies as the cosine of the polar angle. The integration for this distribution is fairly messy. But, surprisingly, such a distribution can be analyzed by superposition. For imagine a sphere with a uniform volume density of positive charge, and another sphere with an equal uniform volume density of negative charge, originally superposed to make a neutral—that is, uncharged—sphere. If the positive sphere is then displaced slightly with respect to the negative sphere, the body of the uncharged sphere would remain neutral, but a little positive charge will appear on one side, and some negative charge will appear on the opposite side, as illustrated in Fig. 6–6 . If the relative displacement of the two spheres is small, the net charge is equivalent to a surface charge (on a spherical surface), and the surface charge density will be proportional to the cosine of the polar angle.

### Figure Ch6-F6
Caption: Fig. 6–6.Two uniformly charged spheres, superposed with a slight displacement, are equivalent to a nonuniform distribution of surface charge.
Image: figures/Ch6-F6.svg
![Fig. 6–6.Two uniformly charged spheres, superposed with a slight displacement, are equivalent to a nonuniform distribution of surface charge.](figures/Ch6-F6.svg)

Now if we want the potential from this distribution, we do not need to do an integral. We know that the potential from each of the spheres of charge is—for points outside the sphere—the same as from a point charge. The two displaced spheres are like two point charges; the potential is just that of a dipole.

In this way you can show that a charge distribution on a sphere of radius a with a surface charge density

\sigma=\sigma_0\cos\theta

produces a field outside the sphere which is just that of a dipole whose moment is

p=\frac{4\pi\sigma_0 a^3}{3}.

It can also be shown that inside the sphere the field is constant, with the value

E=\frac{\sigma_0}{3\epsilon_0}.

If \theta is the angle from the positive z -axis, the electric field inside the sphere is in the negative z -direction. The example we have just considered is not as artificial as it may appear; we will encounter it again in the theory of dielectrics.
