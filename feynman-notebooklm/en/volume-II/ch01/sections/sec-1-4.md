## 1–4 The laws of electromagnetism

The first law of electromagnetism describes the flux of the electric field:

\begin{pmatrix} \text{Flux of $\mathbf{E}$}\\[-.5ex] \text{through any}\\[-.5ex] \text{closed surface} \end{pmatrix} = \frac{\begin{pmatrix} \text{net charge}\\[-.5ex] \text{inside} \end{pmatrix} }{\epsilon_0}, (1.6)

where \epsilon_0 is a convenient constant. (The constant \epsilon_0 is usually read as “epsilon-zero” or “epsilon-naught”.) If there are no charges inside the surface, even though there are charges nearby outside the surface, the average normal component of \mathbf{E} is zero, so there is no net flux through the surface. To show the power of this type of statement, we can show that Eq. ( 1.6) is the same as Coulomb’s law, provided only that we also add the idea that the field from a single charge is spherically symmetric. For a point charge, we draw a sphere around the charge. Then the average normal component is just the value of the magnitude of \mathbf{E} at any point, since the field must be directed radially and have the same strength for all points on the sphere. Our rule now says that the field at the surface of the sphere, times the area of the sphere—that is, the outgoing flux—is proportional to the charge inside. If we were to make the radius of the sphere bigger, the area would increase as the square of the radius. The average normal component of the electric field times that area must still be equal to the same charge inside, and so the field must decrease as the square of the distance—we get an “inverse square” field.

If we have an arbitrary stationary curve in space and measure the circulation of the electric field around the curve, we will find that it is not, in general, zero (although it is for the Coulomb field). Rather, for electricity there is a second law that states: for any surface S (not closed) whose edge is the curve C ,

\begin{pmatrix} \text{Circulation of $\mathbf{E}$}\\[-.5ex] \text{around $C$} \end{pmatrix} =-\frac{d }{d t}\begin{pmatrix} \text{flux of $\mathbf{B}$}\\[-.5ex] \text{through $S$} \end{pmatrix}. (1.7)

We can complete the laws of the electromagnetic field by writing two corresponding equations for the magnetic field \mathbf{B} :

\begin{pmatrix} \text{Flux of $\mathbf{B}$}\\[-.5ex] \text{through any}\\[-.5ex] \text{closed surface} \end{pmatrix} =0. (1.8)

For a surface S bounded by the curve C ,

\begin{aligned} c^2 \begin{pmatrix} \text{circulation of $\mathbf{B}$}\\[-.5ex] \text{around $C$} \end{pmatrix} =\\[1.5ex] \frac{d }{d t} \begin{pmatrix} \text{flux of $\mathbf{E}$}\\[-.5ex] \text{through $S$} \end{pmatrix} +\frac{ \begin{pmatrix} \text{flux of}\\[-.75ex] \text{electric current}\\[-.5ex] \text{through $S$} \end{pmatrix} }{\epsilon_0}. \end{aligned} (1.9)

The constant c^2 that appears in Eq. ( 1.9) is the square of the velocity of light. It appears because magnetism is in reality a relativistic effect of electricity. The constant \epsilon_0 has been stuck in to make the units of electric current come out in a convenient way.

Equations ( 1.6) through ( 1.9), together with Eq. ( 1.1), are all the laws of electrodynamics 1. As you remember, the laws of Newton were very simple to write down, but they had a lot of complicated consequences and it took us a long time to learn about them all. These laws are not nearly as simple to write down, which means that the consequences are going to be more elaborate and it will take us quite a lot of time to figure them all out.

### Figure Ch1-F6
Caption: Fig. 1–6.A bar magnet gives a field B\FigB at a wire. When there is a current along the wire, the wire moves because of the force F=qv×B\FigF = q\Figv\times\FigB.
Image: figures/Ch1-F6.svg
![Fig. 1–6.A bar magnet gives a field B\FigB at a wire. When there is a current along the wire, the wire moves because of the force F=qv×B\FigF = q\Figv\times\FigB.](figures/Ch1-F6.svg)

We can illustrate some of the laws of electrodynamics by a series of small experiments which show qualitatively the interrelationships of electric and magnetic fields. You have experienced the first term of Eq. ( 1.1) when combing your hair, so we won’t show that one. The second part of Eq. ( 1.1) can be demonstrated by passing a current through a wire which hangs above a bar magnet, as shown in Fig. 1–6 . The wire will move when a current is turned on because of the force \mathbf{F}=q\mathbf{v}\times\mathbf{B} . When a current exists, the charges inside the wire are moving, so they have a velocity \mathbf{v} , and the magnetic field from the magnet exerts a force on them, which results in pushing the wire sideways.

When the wire is pushed to the left, we would expect that the magnet must feel a push to the right. (Otherwise we could put the whole thing on a wagon and have a propulsion system that didn’t conserve momentum!) Although the force is too small to make movement of the bar magnet visible, a more sensitively supported magnet, like a compass needle, will show the movement.

How does the wire push on the magnet? The current in the wire produces a magnetic field of its own that exerts forces on the magnet. According to the last term in Eq. ( 1.9), a current must have a circulation of \mathbf{B} —in this case, the lines of \mathbf{B} are loops around the wire, as shown in Fig. 1–7. This \mathbf{B} -field is responsible for the force on the magnet.

### Figure Ch1-F7
Caption: Fig. 1–7.The magnetic field of the wire exerts a force on the magnet.
Image: figures/Ch1-F7.svg
![Fig. 1–7.The magnetic field of the wire exerts a force on the magnet.](figures/Ch1-F7.svg)

Equation ( 1.9) tells us that for a fixed current through the wire the circulation of \mathbf{B} is the same for any curve that surrounds the wire. For curves—say circles—that are farther away from the wire, the circumference is larger, so the tangential component of \mathbf{B} must decrease. You can see that we would, in fact, expect \mathbf{B} to decrease linearly with the distance from a long straight wire.

Now, we have said that a current through a wire produces a magnetic field, and that when there is a magnetic field present there is a force on a wire carrying a current. Then we should also expect that if we make a magnetic field with a current in one wire, it should exert a force on another wire which also carries a current. This can be shown by using two hanging wires as shown in Fig. 1–8. When the currents are in the same direction, the two wires attract, but when the currents are opposite, they repel.

### Figure Ch1-F8
Caption: Fig. 1–8.Two wires, carrying current, exert forces on each other.
Image: figures/Ch1-F8.svg
![Fig. 1–8.Two wires, carrying current, exert forces on each other.](figures/Ch1-F8.svg)

In short, electrical currents, as well as magnets, make magnetic fields. But wait, what is a magnet, anyway? If magnetic fields are produced by moving charges, is it not possible that the magnetic field from a piece of iron is really the result of currents? It appears to be so. We can replace the bar magnet of our experiment with a coil of wire, as shown in Fig. 1–9. When a current is passed through the coil—as well as through the straight wire above it—we observe a motion of the wire exactly as before, when we had a magnet instead of a coil. In other words, the current in the coil imitates a magnet. It appears, then, that a piece of iron acts as though it contains a perpetual circulating current. We can, in fact, understand magnets in terms of permanent currents in the atoms of the iron. The force on the magnet in Fig. 1–7 is due to the second term in Eq. ( 1.1).

### Figure Ch1-F9
Caption: Fig. 1–9.The bar magnet of Fig. 1–6 can be replaced by a coil carrying an electrical current. A similar force acts on the wire.
Image: figures/Ch1-F9.svg
![Fig. 1–9.The bar magnet of Fig. 1–6 can be replaced by a coil carrying an electrical current. A similar force acts on the wire.](figures/Ch1-F9.svg)

Where do the currents come from? One possibility would be from the motion of the electrons in atomic orbits. Actually, that is not the case for iron, although it is for some materials. In addition to moving around in an atom, an electron also spins about on its own axis—something like the spin of the earth—and it is the current from this spin that gives the magnetic field in iron. (We say “something like the spin of the earth” because the question is so deep in quantum mechanics that the classical ideas do not really describe things too well.) In most substances, some electrons spin one way and some spin the other, so the magnetism cancels out, but in iron—for a mysterious reason which we will discuss later—many of the electrons are spinning with their axes lined up, and that is the source of the magnetism.

Since the fields of magnets are from currents, we do not have to add any extra term to Eqs. ( 1.8) or ( 1.9) to take care of magnets. We just take all currents, including the circulating currents of the spinning electrons, and then the law is right. You should also notice that Eq. ( 1.8) says that there are no magnetic “charges” analogous to the electrical charges appearing on the right side of Eq. ( 1.6). None has been found.

### Figure Ch1-F10
Caption: Fig. 1–10.The circulation of B\FigB around the curve CC is given either by the current passing through the surface S1S_1, or by the rate of change of the flux of E\FigE through the surface S2S_2.
Image: figures/Ch1-F10.svg
![Fig. 1–10.The circulation of B\FigB around the curve CC is given either by the current passing through the surface S1S_1, or by the rate of change of the flux of E\FigE through the surface S2S_2.](figures/Ch1-F10.svg)

The first term on the right-hand side of Eq. ( 1.9) was discovered theoretically by Maxwell and is of great importance. It says that changing electric fields produce magnetic effects. In fact, without this term the equation would not make sense, because without it there could be no currents in circuits that are not complete loops. But such currents do exist, as we can see in the following example. Imagine a capacitor made of two flat plates. It is being charged by a current that flows toward one plate and away from the other, as shown in Fig. 1–10. We draw a curve C around one of the wires and fill it in with a surface which crosses the wire, as shown by the surface S_1 in the figure. According to Eq. ( 1.9), the circulation of \mathbf{B} around C (times c^2 ) is given by the current in the wire (divided by \epsilon_0 ). But what if we fill in the curve with a different surface S_2 , which is shaped like a bowl and passes between the plates of the capacitor, staying always away from the wire? There is certainly no current through this surface. But, surely, just changing the location of an imaginary surface is not going to change a real magnetic field! The circulation of \mathbf{B} must be what it was before. The first term on the right-hand side of Eq. ( 1.9) does, indeed, combine with the second term to give the same result for the two surfaces S_1 and S_2 . For S_2 the circulation of \mathbf{B} is given in terms of the rate of change of the flux of \mathbf{E} between the plates of the capacitor. And it works out that the changing \mathbf{E} is related to the current in just the way required for Eq. ( 1.9) to be correct. Maxwell saw that it was needed, and he was the first to write the complete equation.

With the setup shown in Fig. 1–6 we can demonstrate another of the laws of electromagnetism. We disconnect the ends of the hanging wire from the battery and connect them to a galvanometer which tells us when there is a current through the wire. When we push the wire sideways through the magnetic field of the magnet, we observe a current. Such an effect is again just another consequence of Eq. ( 1.1)—the electrons in the wire feel the force \mathbf{F}=q\mathbf{v}\times\mathbf{B} . The electrons have a sidewise velocity because they move with the wire. This \mathbf{v} with a vertical \mathbf{B} from the magnet results in a force on the electrons directed along the wire, which starts the electrons moving toward the galvanometer.

Suppose, however, that we leave the wire alone and move the magnet. We guess from relativity that it should make no difference, and indeed, we observe a similar current in the galvanometer. How does the magnetic field produce forces on charges at rest? According to Eq. ( 1.1) there must be an electric field. A moving magnet must make an electric field. How that happens is said quantitatively by Eq. ( 1.7). This equation describes many phenomena of great practical interest, such as those that occur in electric generators and transformers.

The most remarkable consequence of our equations is that the combination of Eq. ( 1.7) and Eq. ( 1.9) contains the explanation of the radiation of electromagnetic effects over large distances. The reason is roughly something like this: suppose that somewhere we have a magnetic field which is increasing because, say, a current is turned on suddenly in a wire. Then by Eq. ( 1.7) there must be a circulation of an electric field. As the electric field builds up to produce its circulation, then according to Eq. ( 1.9) a magnetic circulation will be generated. But the building up of this magnetic field will produce a new circulation of the electric field, and so on. In this way fields work their way through space without the need of charges or currents except at their source. That is the way we see each other! It is all in the equations of the electromagnetic fields.
