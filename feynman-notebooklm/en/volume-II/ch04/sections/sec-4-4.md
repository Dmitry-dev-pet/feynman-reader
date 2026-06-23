## 4–4 [math]\boldsymbol{E=-\nabla\phi}

Who cares about \phi ? Forces on charges are given by \mathbf{E} , the electric field. The point is that \mathbf{E} can be obtained easily from \phi —it is as easy, in fact, as taking a derivative. Consider two points, one at x and one at (x+\Delta x) , but both at the same y and z , and ask how much work is done in carrying a unit charge from one point to the other. The path is along the horizontal line from x to x+\Delta x . The work done is the difference in the potential at the two points:

\Delta W=\phi(x+\Delta x,y,z)-\phi(x,y,z)=\frac{\partial \phi}{\partial x}\,\Delta x.

But the work done against the field for the same path is

\Delta W=-\int\mathbf{E}\cdot d\mathbf{s}=-E_x\,\Delta x.

We see that

E_x=-\frac{\partial \phi}{\partial x}. (4.26)

Similarly, E_y=-\frac{\partial \phi}{\partial y} , E_z=-\frac{\partial \phi}{\partial z} , or, summarizing with the notation of vector analysis,

\mathbf{E}=-\boldsymbol{\nabla}{\phi}. (4.27)

This equation is the differential form of Eq. ( 4.22). Any problem with specified charges can be solved by computing the potential from ( 4.24) or ( 4.25) and using ( 4.27) to get the field. Equation ( 4.27) also agrees with what we found from vector calculus: that for any scalar field \phi

\int_a^b\boldsymbol{\nabla}{\phi}\cdot d\mathbf{s}=\phi(b)-\phi(a). (4.28)

According to Eq. ( 4.25) the scalar potential \phi is given by a three-dimensional integral similar to the one we had for \mathbf{E} . Is there any advantage to computing \phi rather than \mathbf{E} ? Yes. There is only one integral for \phi , while there are three integrals for \mathbf{E} —because it is a vector. Furthermore, 1/r is usually a little easier to integrate than x/r^3 . It turns out in many practical cases that it is easier to calculate \phi and then take the gradient to find the electric field, than it is to evaluate the three integrals for \mathbf{E} . It is merely a practical matter.

There is also a deeper physical significance to the potential \phi . We have shown that \mathbf{E} of Coulomb’s law is obtained from \mathbf{E}=-\grad\phi , when \phi is given by ( 4.22). But if \mathbf{E} is equal to the gradient of a scalar field, then we know from the vector calculus that the curl of \mathbf{E} must vanish:

\mathbf{c}url{\mathbf{E}}=\FLPzero. (4.29)

But that is just our second fundamental equation of electrostatics, Eq. ( 4.6). We have shown that Coulomb’s law gives an \mathbf{E} field that satisfies that condition. So far, everything is all right.

We had really proved that \mathbf{c}url{\mathbf{E}} was zero before we defined the potential. We had shown that the work done around a closed path is zero. That is, that

\oint\mathbf{E}\cdot d\mathbf{s} = 0

for any path. We saw in Chapter 3 that for any such field \mathbf{c}url{\mathbf{E}} must be zero everywhere. The electric field in electrostatics is an example of a curl-free field.

You can practice your vector calculus by proving that \mathbf{c}url{\mathbf{E}} is zero in a different way—by computing the components of \mathbf{c}url{\mathbf{E}} for the field of a point charge, as given by Eq. ( 4.11). If you get zero, the superposition principle says you would get zero for the field of any charge distribution.

We should point out an important fact. For any radial force the work done is independent of the path, and there exists a potential. If you think about it, the entire argument we made above to show that the work integral was independent of the path depended only on the fact that the force from a single charge was radial and spherically symmetric. It did not depend on the fact that the dependence on distance was as 1/r^2 —there could have been any r dependence. The existence of a potential, and the fact that the curl of \mathbf{E} is zero, comes really only from the symmetry and direction of the electrostatic forces. Because of this, Eq. ( 4.28)—or ( 4.29)—can contain only part of the laws of electricity.
