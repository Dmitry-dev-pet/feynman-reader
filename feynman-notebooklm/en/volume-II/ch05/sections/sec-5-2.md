## 5–2 Equilibrium in an electrostatic field

Consider first the following question: When can a point charge be in stable mechanical equilibrium in the electric field of other charges? As an example, imagine three negative charges at the corners of an equilateral triangle in a horizontal plane. Would a positive charge placed at the center of the triangle remain there? (It will be simpler if we ignore gravity for the moment, although including it would not change the results.) The force on the positive charge is zero, but is the equilibrium stable? Would the charge return to the equilibrium position if displaced slightly? The answer is no.

There are no points of stable equilibrium in any electrostatic field—except right on top of another charge. Using Gauss’ law, it is easy to see why. First, for a charge to be in equilibrium at any particular point P_0 , the field must be zero. Second, if the equilibrium is to be a stable one, we require that if we move the charge away from P_0 in any direction, there should be a restoring force directed opposite to the displacement. The electric field at all nearby points must be pointing inward—toward the point P_0 . But that is in violation of Gauss’ law if there is no charge at P_0 , as we can easily see.

### Figure Ch5-F1
Caption: Fig. 5–1.If P0P_0 were a position of stable equilibrium for a positive charge, the electric field everywhere in the neighborhood would point toward P0P_0.
Image: figures/Ch5-F1.svg
![Fig. 5–1.If P0P_0 were a position of stable equilibrium for a positive charge, the electric field everywhere in the neighborhood would point toward P0P_0.](figures/Ch5-F1.svg)

Consider a tiny imaginary surface that encloses P_0 , as in Fig. 5–1 . If the electric field everywhere in the vicinity is pointed toward P_0 , the surface integral of the normal component is certainly not zero. For the case shown in the figure, the flux through the surface must be a negative number. But Gauss’ law says that the flux of electric field through any surface is proportional to the total charge inside. If there is no charge at P_0 , the field we have imagined violates Gauss’ law. It is impossible to balance a positive charge in empty space—at a point where there is not some negative charge. A positive charge can be in equilibrium if it is in the middle of a distributed negative charge. Of course, the negative charge distribution would have to be held in place by other than electrical forces!

Our result has been obtained for a point charge. Does the same conclusion hold for a complicated arrangement of charges held together in fixed relative positions—with rods, for example? We consider the question for two equal charges fixed on a rod. Is it possible that this combination can be in equilibrium in some electrostatic field? The answer is again no. The total force on the rod cannot be restoring for displacements in every direction.

Call \mathbf{F} the total force on the rod in any position— \mathbf{F} is then a vector field. Following the argument used above, we conclude that at a position of stable equilibrium, the divergence of \mathbf{F} must be a negative number. But the total force on the rod is the first charge times the field at its position, plus the second charge times the field at its position:

\mathbf{F}=q_1\mathbf{E}_1+q_2\mathbf{E}_2. (5.1)

The divergence of \mathbf{F} is given by

\mathbf{d}iv{\mathbf{F}}=q_1(\mathbf{d}iv{\mathbf{E}_1})+q_2(\mathbf{d}iv{\mathbf{E}_2}).

If each of the two charges q_1 and q_2 is in free space, both \mathbf{d}iv{\mathbf{E}_1} and \mathbf{d}iv{\mathbf{E}_2} are zero, and \mathbf{d}iv{\mathbf{F}} is zero—not negative, as would be required for equilibrium. You can see that an extension of the argument shows that no rigid combination of any number of charges can have a position of stable equilibrium in an electrostatic field in free space.

### Figure Ch5-F2
Caption: Fig. 5–2.A charge can be in equilibrium if there are mechanical constraints.
Image: figures/Ch5-F2.svg
![Fig. 5–2.A charge can be in equilibrium if there are mechanical constraints.](figures/Ch5-F2.svg)

Now we have not shown that equilibrium is forbidden if there are pivots or other mechanical constraints. As an example, consider a hollow tube in which a charge can move back and forth freely, but not sideways. Now it is very easy to devise an electric field that points inward at both ends of the tube if it is allowed that the field may point laterally outward near the center of the tube. We simply place positive charges at each end of the tube, as in Fig. 5–2 . There can now be an equilibrium point even though the divergence of \mathbf{E} is zero. The charge, of course, would not be in stable equilibrium for sideways motion were it not for “nonelectrical” forces from the tube walls.
