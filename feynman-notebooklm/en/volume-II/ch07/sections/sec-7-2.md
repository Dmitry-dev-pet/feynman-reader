## 7–2 Two-dimensional fields; functions of the complex variable

The complex variable \frakz is defined as

\frakz=x+iy.

(Do not confuse \frakz with the z -coordinate, which we ignore in the following discussion because we assume there is no z -dependence of the fields.) Every point in x and y then corresponds to a complex number \frakz . We can use \frakz as a single (complex) variable, and with it write the usual kinds of mathematical functions F(\frakz) . For example,

F(\frakz) =\frakz^2,

or

F(\frakz) =1/\frakz^3,

or

F(\frakz) =\frakz\ln\frakz,

and so forth.

Given any particular F(\frakz) we can substitute \frakz=x+iy , and we have a function of x and y —with real and imaginary parts. For example,

\frakz^2=(x+iy)^2=x^2-y^2+2ixy. (7.3)

Any function F(\frakz) can be written as a sum of a pure real part and a pure imaginary part, each part a function of x and y :

F(\frakz)=U(x,y)+iV(x,y), (7.4)

where U(x,y) and V(x,y) are real functions. Thus from any complex function F(\frakz) two new functions U(x,y) and V(x,y) can be derived. For example, F(\frakz)=\frakz^2 gives us the two functions

U(x,y) =x^2-y^2, (7.5)

and

V(x,y) =2xy. (7.6)

Now we come to a miraculous mathematical theorem which is so delightful that we shall leave a proof of it for one of your courses in mathematics. (We should not reveal all the mysteries of mathematics, or that subject matter would become too dull.) It is this. For any “ordinary function” (mathematicians will define it better) the functions U and V automatically satisfy the relations

\begin{aligned} \frac{\partial U}{\partial x}&=\frac{\partial V}{\partial y},\\[1ex] \frac{\partial V}{\partial x}&=-\frac{\partial U}{\partial y}. \end{aligned} (7.7)

It follows immediately that each of the functions U and V satisfy Laplace’s equation:

\begin{aligned} \frac{\partial^2 U}{\partial x^2}+ \frac{\partial^2 U}{\partial y^2}&=0,\\[1ex] \frac{\partial^2 V}{\partial x^2}+ \frac{\partial^2 V}{\partial y^2}&=0, \end{aligned} (7.9)

These equations are clearly true for the functions of ( 7.5) and ( 7.6).

Thus, starting with any ordinary function, we can arrive at two functions U(x,y) and V(x,y) , which are both solutions of Laplace’s equation in two dimensions. Each function represents a possible electrostatic potential. We can pick any function F(\frakz) and it should represent some electric field problem—in fact, two problems, because U and V each represent solutions. We can write down as many solutions as we wish—by just making up functions—then we just have to find the problem that goes with each solution. It may sound backwards, but it’s a possible approach.

As an example, let’s see what physics the function F(\frakz)=\frakz^2 gives us. From it we get the two potential functions of ( 7.5) and ( 7.6). To see what problem the function U belongs to, we solve for the equipotential surfaces by setting U=A , a constant:

x^2-y^2=A.

This is the equation of a rectangular hyperbola. For various values of A , we get the hyperbolas shown in Fig. 7–1 . When A=0 , we get the special case of diagonal straight lines through the origin.

### Figure Ch7-F1
Caption: Fig. 7–1.Two sets of orthogonal curves which can represent equipotentials in a two-dimensional electrostatic field.
Image: figures/Ch7-F1.svg
![Fig. 7–1.Two sets of orthogonal curves which can represent equipotentials in a two-dimensional electrostatic field.](figures/Ch7-F1.svg)

Such a set of equipotentials corresponds to the field at an inside right-angle corner of a conductor. If we have two electrodes shaped like those in Fig. 7–2 , which are held at different potentials, the field near the corner marked C will look just like the field above the origin in Fig. 7–1 . The solid lines are the equipotentials, and the broken lines at right angles correspond to lines of \mathbf{E} . Whereas at points or protuberances the electric field tends to be high, it tends to be low in dents or hollows.

### Figure Ch7-F2
Caption: Fig. 7–2.The field near the point CC is the same as that in Fig. 7–1.
Image: figures/Ch7-F2.svg
![Fig. 7–2.The field near the point CC is the same as that in Fig. 7–1.](figures/Ch7-F2.svg)

The solution we have found also corresponds to that for a hyperbola-shaped electrode near a right-angle corner, or for two hyperbolas at suitable potentials. You will notice that the field of Fig. 7–1 has an interesting property. The x -component of the electric field, E_x , is given by

E_x=-\frac{\partial \phi}{\partial x}=-2x.

The electric field is proportional to the distance from the axis. This fact is used to make devices (called quadrupole lenses) that are useful for focusing particle beams (see Section 29–7 ). The desired field is usually obtained by using four hyperbola shaped electrodes, as shown in Fig. 7–3 . For the electric field lines in Fig. 7–3 , we have simply copied from Fig. 7–1 the set of broken-line curves that represent V=\text{constant} . We have a bonus! The curves for V=\text{constant} are orthogonal to the ones for U=\text{constant} because of the equations ( 7.7) and ( 7.8). Whenever we choose a function F(\frakz) , we get from U and V both the equipotentials and field lines. And you will remember that we have solved either of two problems, depending on which set of curves we call the equipotentials.

### Figure Ch7-F3
Caption: Fig. 7–3.The field in a quadrupole lens.
Image: figures/Ch7-F3.svg
![Fig. 7–3.The field in a quadrupole lens.](figures/Ch7-F3.svg)

As a second example, consider the function

F(\frakz)=\sqrt{\frakz}. (7.11)

If we write

\frakz=x+iy=\rho e^{i\theta},

where

\rho=\sqrt{x^2+y^2}

and

\tan\theta=y/x,

then

\begin{aligned} F(\frakz)&=\rho^{1/2}e^{i\theta/2}\\ &=\rho^{1/2}\biggl(\cos\frac{\theta}{2}+i\sin\frac{\theta}{2}\biggr), \end{aligned}

from which

\begin{aligned} F(\frakz)=&\biggl[\frac{(x^2\!+y^2)^{1/2}\!+x}{2}\biggr]^{1/2}\\[1ex] &+\,i\biggl[\frac{(x^2\!+y^2)^{1/2}\!-x}{2}\biggr]^{1/2}\!. \end{aligned} (7.12)

### Figure Ch7-F4
Caption: Fig. 7–4.Curves of constant U(x,y)U(x,y) and V(x,y)V(x,y) from Eq. (7.12).
Image: figures/Ch7-F4.svg
![Fig. 7–4.Curves of constant U(x,y)U(x,y) and V(x,y)V(x,y) from Eq. (7.12).](figures/Ch7-F4.svg)

The curves for U(x,y)=A and V(x,y)=B , using U and V from Eq. ( 7.12), are plotted in Fig. 7–4 . Again, there are many possible situations that could be described by these fields. One of the most interesting is the field near the edge of a thin plate. If the line B=0 —to the right of the y -axis—represents a thin charged plate, the field lines near it are given by the curves for various values of A . The physical situation is shown in Fig. 7–5 .

### Figure Ch7-F5
Caption: Fig. 7–5.The electric field near the edge of a thin grounded plate.
Image: figures/Ch7-F5.svg
![Fig. 7–5.The electric field near the edge of a thin grounded plate.](figures/Ch7-F5.svg)

Further examples are

F(\frakz)=\frakz^{2/3}, (7.13)

which yields the field outside a rectangular corner

F(\frakz)=\ln\frakz, (7.14)

which yields the field for a line charge, and

F(\frakz)=1/\frakz, (7.15)

which gives the field for the two-dimensional analog of an electric dipole, i.e., two parallel line charges with opposite polarities, very close together.

We will not pursue this subject further in this course, but should emphasize that although the complex variable technique is often powerful, it is limited to two-dimensional problems; and also, it is an indirect method.
