## 2–2 Scalar and vector fields—T\boldsymbol{T} and h\FLPh

We begin now with the abstract, mathematical view of the theory of electricity and magnetism. The ultimate idea is to explain the meaning of the laws given in Chapter 1. But to do this we must first explain a new and peculiar notation that we want to use. So let us forget electromagnetism for the moment and discuss the mathematics of vector fields. It is of very great importance, not only for electromagnetism, but for all kinds of physical circumstances. Just as ordinary differential and integral calculus is so important to all branches of physics, so also is the differential calculus of vectors. We turn to that subject.

Listed below are a few facts from the algebra of vectors. It is assumed that you already know them.

\begin{aligned} &\mathbf{A}\,\cdot\,\mathbf{B}=\text{scalar}=A_xB_x+A_yB_y+A_zB_z\\[1ex] &\mathbf{A}\times\mathbf{B}=\text{vector}\\[1pt] &\begin{alignedat}{5} % ebook insert: &\qquad(\mathbf{A}\times\mathbf{B})_z&&=A_x&&B_y&&-A_y&&B_x\\[.25ex] % ebook insert: &\qquad(\mathbf{A}\times\mathbf{B})_x&&=A_y&&B_z&&-A_z&&B_y\\[.25ex] % ebook insert: &\qquad(\mathbf{A}\times\mathbf{B})_y&&=A_z&&B_x&&-A_x&&B_z \end{alignedat}\\[1ex] &\mathbf{A}\times\mathbf{A}=\FLPzero\\[1ex] &\mathbf{A}\cdot(\mathbf{A}\times\mathbf{B})=0\\[1ex] &\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C})=(\mathbf{A}\times\mathbf{B})\cdot\mathbf{C}\\[1ex] &\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{C}(\mathbf{A}\cdot\mathbf{B}) \end{aligned} (2.1)

Also we will want to use the two following equalities from the calculus:

\begin{aligned} \Delta f(x,y,z)=\frac{\partial f}{\partial x}\,\Delta x+\frac{\partial f}{\partial y}\,\Delta y+\frac{\partial f}{\partial z}\,\Delta z,\\[1ex] \frac{\partial^2f}{\partial x\,\partial y}= \frac{\partial^2f}{\partial y\,\partial x}. \end{aligned} (2.7)

The first equation ( 2.7) is, of course, true only in the limit that \Delta x , \Delta y , and \Delta z go toward zero.

The simplest possible physical field is a scalar field. By a field, you remember, we mean a quantity which depends upon position in space. By a scalar field we merely mean a field which is characterized at each point by a single number—a scalar. Of course the number may change in time, but we need not worry about that for the moment. We will talk about what the field looks like at a given instant. As an example of a scalar field, consider a solid block of material which has been heated at some places and cooled at others, so that the temperature of the body varies from point to point in a complicated way. Then the temperature will be a function of x , y , and z , the position in space measured in a rectangular coordinate system. Temperature is a scalar field.

### Figure Ch2-F1
Caption: Fig. 2–1. Temperature TT is an example of a scalar field. With each point (x,y,z)(x,y,z) in space there is associated a number T(x,y,z)T(x,y,z). All points on the surface marked T=20∘T=20^\circ (shown as a curve at z=0z=0) are at the same temperature. The arrows are samples of the heat flow vector h\Figh.
Image: figures/Ch2-F1.svg
![Fig. 2–1. Temperature TT is an example of a scalar field. With each point (x,y,z)(x,y,z) in space there is associated a number T(x,y,z)T(x,y,z). All points on the surface marked T=20∘T=20^\circ (shown as a curve at z=0z=0) are at the same temperature. The arrows are samples of the heat flow vector h\Figh.](figures/Ch2-F1.svg)

One way of thinking about scalar fields is to imagine “contours” which are imaginary surfaces drawn through all points for which the field has the same value, just as contour lines on a map connect points with the same height. For a temperature field the contours are called “isothermal surfaces” or isotherms. Figure 2–1 illustrates a temperature field and shows the dependence of T on x and y when z=0 . Several isotherms are drawn.

### Figure Ch2-F2
Caption: Fig. 2–2. The velocity of the atoms in a rotating object is an example of a vector field.
Image: figures/Ch2-F2.svg
![Fig. 2–2. The velocity of the atoms in a rotating object is an example of a vector field.](figures/Ch2-F2.svg)

There are also vector fields. The idea is very simple. A vector is given for each point in space. The vector varies from point to point. As an example, consider a rotating body. The velocity of the material of the body at any point is a vector which is a function of position (Fig. 2–2 ). As a second example, consider the flow of heat in a block of material. If the temperature in the block is high at one place and low at another, there will be a flow of heat from the hotter places to the colder. The heat will be flowing in different directions in different parts of the block. The heat flow is a directional quantity which we call \FLPh . Its magnitude is a measure of how much heat is flowing. Examples of the heat flow vector are also shown in Fig. 2–1 .

### Figure Ch2-F3
Caption: Fig. 2–3. Heat flow is a vector field. The vector h\Figh points along the direction of the flow. Its magnitude is the energy transported per unit time across a surface element oriented perpendicular to the flow, divided by the area of the surface element.
Image: figures/Ch2-F3.svg
![Fig. 2–3. Heat flow is a vector field. The vector h\Figh points along the direction of the flow. Its magnitude is the energy transported per unit time across a surface element oriented perpendicular to the flow, divided by the area of the surface element.](figures/Ch2-F3.svg)

Let’s make a more precise definition of \FLPh : The magnitude of the vector heat flow at a point is the amount of thermal energy that passes, per unit time and per unit area, through an infinitesimal surface element at right angles to the direction of flow. The vector points in the direction of flow (see Fig. 2–3 ). In symbols: If \Delta J is the thermal energy that passes per unit time through the surface element \Delta a , then

\FLPh=\frac{\Delta J}{\Delta a}\,\mathbf{e}_f, (2.9)

where \mathbf{e}_f is a unit vector in the direction of flow.

### Figure Ch2-F4
Caption: Fig. 2–4. The heat flow through Δa2\Delta a_2 is the same as through Δa1\Delta a_1.
Image: figures/Ch2-F4.svg
![Fig. 2–4. The heat flow through Δa2\Delta a_2 is the same as through Δa1\Delta a_1.](figures/Ch2-F4.svg)

The vector \FLPh can be defined in another way—in terms of its components. We ask how much heat flows through a small surface at any angle with respect to the flow. In Fig. 2–4 we show a small surface \Delta a_2 inclined with respect to \Delta a_1 , which is perpendicular to the flow. The unit vector \FLPn is normal to the surface \Delta a_2 . The angle \theta between \FLPn and \FLPh is the same as the angle between the surfaces (since \FLPh is normal to \Delta a_1 ). Now what is the heat flow per unit area through \Delta a_2 ? The flow through \Delta a_2 is the same as through \Delta a_1 ; only the areas are different. In fact, \Delta a_1=\Delta a_2\cos\theta . The heat flow through \Delta a_2 is

\frac{\Delta J}{\Delta a_2}=\frac{\Delta J}{\Delta a_1}\cos\theta= \FLPh\cdot\FLPn. (2.10)

We interpret this equation: the heat flow (per unit time and per unit area) through any surface element whose unit normal is \FLPn , is given by \FLPh\cdot\FLPn . Equally, we could say: the component of the heat flow perpendicular to the surface element \Delta a_2 is \FLPh\cdot\FLPn . We can, if we wish, consider that these statements define \FLPh . We will be applying the same ideas to other vector fields.
