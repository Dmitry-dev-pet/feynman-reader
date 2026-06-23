## 4–5 The flux of [math]\FLPE

We will now derive a field equation that depends specifically and directly on the fact that the force law is inverse square. That the field varies inversely as the square of the distance seems, for some people, to be “only natural,” because “that’s the way things spread out.” Take a light source with light streaming out: the amount of light that passes through a surface cut out by a cone with its apex at the source is the same no matter at what radius the surface is placed. It must be so if there is to be conservation of light energy. The amount of light per unit area—the intensity—must vary inversely as the area cut by the cone, i.e., inversely as the square of the distance from the source. Certainly the electric field should vary inversely as the square of the distance for the same reason! But there is no such thing as the “same reason” here. Nobody can say that the electric field measures the flow of something like light which must be conserved. If we had a “model” of the electric field in which the electric field vector represented the direction and speed—say the current—of some kind of little “bullets” which were flying out, and if our model required that these bullets were conserved, that none could ever disappear once it was shot out of a charge, then we might say that we can “see” that the inverse square law is necessary. On the other hand, there would necessarily be some mathematical way to express this physical idea. If the electric field were like conserved bullets going out, then it would vary inversely as the square of the distance and we would be able to describe that behavior by an equation—which is purely mathematical. Now there is no harm in thinking this way, so long as we do not say that the electric field is made out of bullets, but realize that we are using a model to help us find the right mathematics.

Suppose, indeed, that we imagine for a moment that the electric field did represent the flow of something that was conserved—everywhere, that is, except at charges. (It has to start somewhere!) We imagine that whatever it is flows out of a charge into the space around. If \mathbf{E} were the vector of such a flow (as \FLPh is for heat flow), it would have a 1/r^2 dependence near a point source. Now we wish to use this model to find out how to state the inverse square law in a deeper or more abstract way, rather than simply saying “inverse square.” (You may wonder why we should want to avoid the direct statement of such a simple law, and want instead to imply the same thing sneakily in a different way. Patience! It will turn out to be useful.)

### Figure Ch4-F5
Caption: Fig. 4–5. The flux of [math]\FigE out of the surface [math]S is zero.
Image: figures/Ch4-F5.svg
![Fig. 4–5. The flux of [math]\FigE out of the surface [math]S is zero.](figures/Ch4-F5.svg)

We ask: What is the “flow” of \mathbf{E} out of an arbitrary closed surface in the neighborhood of a point charge? First let’s take an easy surface—the one shown in Fig. 4-5 . If the \mathbf{E} field is like a flow, the net flow out of this box should be zero. That is what we get if by the “flow” from this surface we mean the surface integral of the normal component of \mathbf{E} —that is, the flux of \mathbf{E} . On the radial faces, the normal component is zero. On the spherical faces, the normal component E_n is just the magnitude of \mathbf{E} —minus for the smaller face and plus for the larger face. The magnitude of \mathbf{E} decreases as 1/r^2 , but the surface area is proportional to r^2 , so the product is independent of r . The flux of \mathbf{E} into face a is just cancelled by the flux out of face b . The total flow out of S is zero, which is to say that for this surface

\int_S E_n\,da=0. (4.30)

### Figure Ch4-F6
Caption: Fig. 4–6. The flux of [math]\FigE out of the surface [math]S is zero.
Image: figures/Ch4-F6.svg
![Fig. 4–6. The flux of [math]\FigE out of the surface [math]S is zero.](figures/Ch4-F6.svg)

Next we show that the two end surfaces may be tilted with respect to the radial line without changing the integral ( 4.30). Although it is true in general, for our purposes it is only necessary to show that this is true when the end surfaces are small, so that they subtend a small angle from the source—in fact, an infinitesimal angle. In Fig. 4-6 we show a surface S whose “sides” are radial, but whose “ends” are tilted. The end surfaces are not small in the figure, but you are to imagine the situation for very small end surfaces. Then the field \mathbf{E} will be sufficiently uniform over the surface that we can use just its value at the center. When we tilt the surface by an angle \theta , the area is increased by the factor 1/\cos\theta . But E_n , the component of \mathbf{E} normal to the surface, is decreased by the factor \cos\theta . The product E_n\,\Delta a is unchanged. The flux out of the whole surface S is still zero.

### Figure Ch4-F7
Caption: Fig. 4–7. Any volume can be thought of as completely made up of infinitesimal truncated cones. The flux of [math]\FigE from one end of each conical segment is equal and opposite to the flux from the other end. The total flux from the surface [math]S is therefore zero.
Image: figures/Ch4-F7.svg
![Fig. 4–7. Any volume can be thought of as completely made up of infinitesimal truncated cones. The flux of [math]\FigE from one end of each conical segment is equal and opposite to the flux from the other end. The total flux from the surface [math]S is therefore zero.](figures/Ch4-F7.svg)

Now it is easy to see that the flux out of a volume enclosed by any surface S must be zero. Any volume can be thought of as made up of pieces, like that in Fig. 4-6 . The surface will be subdivided completely into pairs of end surfaces, and since the fluxes in and out of these end surfaces cancel by pairs, the total flux out of the surface will be zero. The idea is illustrated in Fig. 4-7 . We have the completely general result that the total flux of \mathbf{E} out of any surface S in the field of a point charge is zero.

### Figure Ch4-F8
Caption: Fig. 4–8. If a charge is inside a surface, the flux out is not zero.
Image: figures/Ch4-F8.svg
![Fig. 4–8. If a charge is inside a surface, the flux out is not zero.](figures/Ch4-F8.svg)

### Figure Ch4-F9
Caption: Fig. 4–9. The flux through [math]S is the same as the flux through [math]S'.
Image: figures/Ch4-F9.svg
![Fig. 4–9. The flux through [math]S is the same as the flux through [math]S'.](figures/Ch4-F9.svg)

But notice! Our proof works only if the surface S does not surround the charge. What would happen if the point charge were inside the surface? We could still divide our surface into pairs of areas that are matched by radial lines through the charge, as shown in Fig. 4-8 . The fluxes through the two surfaces are still equal—by the same arguments as before—only now they have the same sign. The flux out of a surface that surrounds a charge is not zero. Then what is it? We can find out by a little trick. Suppose we “remove” the charge from the “inside” by surrounding the charge by a little surface S' totally inside the original surface S , as shown in Fig. 4-9. Now the volume enclosed between the two surfaces S and S' has no charge in it. The total flux out of this volume (including that through S' ) is zero, by the arguments we have given above. The arguments tell us, in fact, that the flux into the volume through S' is the same as the flux outward through S .

### Figure Ch4-F10
Caption: Fig. 4–10. The flux through a spherical surface containing a point charge [math]q is [math]q/\epsO.
Image: figures/Ch4-F10.svg
![Fig. 4–10. The flux through a spherical surface containing a point charge [math]q is [math]q/\epsO.](figures/Ch4-F10.svg)

We can choose any shape we wish for S' , so let’s make it a sphere centered on the charge, as in Fig. 4-10. Then we can easily calculate the flux through it. If the radius of the little sphere is r , the value of \mathbf{E} everywhere on its surface is

\frac{1}{4\pi\epsilon_0}\,\frac{q}{r^2},

and is directed always normal to the surface. We find the total flux through S' if we multiply this normal component of \mathbf{E} by the surface area:

\begin{aligned} \begin{pmatrix} \text{Flux through}\\[-.5ex] \text{the surface $S'$} \end{pmatrix} &=\biggl(\frac{1}{4\pi\epsilon_0}\,\frac{q}{r^2}\biggr) (4\pi r^2)\\[1ex] &=\frac{q}{\epsilon_0}, \end{aligned} (4.31)

a number independent of the radius of the sphere! We know then that the flux outward through S is also q/\epsilon_0 —a value independent of the shape of S so long as the charge q is inside.

We can write our conclusions as follows:

\underset{\substack{\text{any closed}\\\text{surface $S$}}}{\int}\kern{-1em} E_n\,da = \begin{cases} 0;&\text{$q$ outside $S$}\\[1ex] {\dfrac{q}{\epsilon_0}};&\text{$q$ inside $S$} \end{cases} (4.32)

Let’s return to our “bullet” analogy and see if it makes sense. Our theorem says that the net flow of bullets through a surface is zero if the surface does not enclose the gun that shoots the bullets. If the gun is enclosed in a surface, whatever size and shape it is, the number of bullets passing through is the same—it is given by the rate at which bullets are generated at the gun. It all seems quite reasonable for conserved bullets. But does the model tell us anything more than we get simply by writing Eq. ( 4.32)? No one has succeeded in making these “bullets” do anything else but produce this one law. After that, they produce nothing but errors. That is why today we prefer to represent the electromagnetic field purely abstractly.
