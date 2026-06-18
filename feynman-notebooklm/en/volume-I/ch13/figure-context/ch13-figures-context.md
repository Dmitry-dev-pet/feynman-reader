# Figure context for Chapter 13. Work and Potential Energy (A)

SOURCE: Feynman Lectures on Physics, Volume I, Chapter 13
LANGUAGE: en
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_13.html

NotebookLM use: pair this file with the clean chapter text and the PNG image files below. The visual descriptions here are inferred from the surrounding lecture text; the PNG files are included so NotebookLM can inspect the diagrams directly when image sources are uploaded.

## Ch13-F1: Fig. 13–1.An object moving on a frictionless curve under the influence of gravity.

Section: 13–1 Energy of a falling body
Image file: images/Ch13-F1.png

Context before the figure:

Now in our simple example the force is constant, equal to \(-mg\) , a vertical force (the minus sign means that it acts downward), and the velocity, of course, is the rate of change of the vertical position, or height \(h\) , with time. Thus the rate of change of the kinetic energy is \(-mg(dh/dt)\) , which quantity, miracle of miracles, is minus the rate of change of something else! It is minus the time rate of change of \(mgh\) ! Therefore, as time goes on, the changes in kinetic energy and in the quantity \(mgh\) are equal and opposite, so that the sum of the two quantities remains constant. Q.E.D.

Context after the figure:

We have shown, from Newton’s second law of motion, that energy is conserved for constant forces when we add the potential energy \(mgh\) to the kinetic energy \(\tfrac{1}{2}mv^2\) . Now let us look into this further and see whether it can be generalized, and thus advance our understanding. Does it work only for a freely falling body, or is it more general? We expect from our discussion of the conservation of energy that it would work for an object moving from one point to another in some kind of frictionless curve, under the influence of gravity (Fig.13–1). If the object reaches a certain height \(h\) from the original height \(H\) , then the same formula should again be right, even though the velocity is now in some direction other than the vertical. We would like to understandwhythe law is still correct. Let us follow the same analysis, finding the time rate of change of the kinetic...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch13-F2: Fig. 13–2.A small mass \(m\) falls under the influence of gravity toward a large mass \(M\) .

Section: 13–2 Work done by gravity
Image file: images/Ch13-F2.png

Context before the figure:

We shall first consider the motion of an object which starts at some point \(1\) and falls, say,directlytoward the sun or toward the earth (Fig.13–2). Will there be a law of conservation of energy in these circumstances? The only difference is that in this case, the force ischangingas we go along, it is not just a constant. As we know, the force is \(-GM/r^2\) times the mass \(m\) , where \(m\) is the mass that moves. Now certainly when a body falls toward the earth, the kinetic energy increases as the distance fallen increases, just as it does when we do not worry about the variation of force with height. The question is whether it is possible to find another formula for potential energy different from \(mgh\) , a different function of distance away from the earth, so that conservation of energy will still be true.

Context after the figure:

This one-dimensional case is easy to treat because we know that the change in the kinetic energy is equal to the integral, from one end of the motion to the other, of \(-GMm/r^2\) times the displacement \(dr\) : \[ \begin{equation} \label{Eq:I:13:11} T_2-T_1=-\int_1^2GMm\,\frac{dr}{r^2}. \end{equation} \] There are no cosines needed for this case because the force and the displacement are in the same direction. It is easy to integrate \(dr/r^2\) ; the result is \(-1/r\) , so Eq. (13.11) becomes \[ \begin{equation} \label{Eq:I:13:12} T_2-T_1=+GMm\biggr(\frac{1}{r_2}-\frac{1}{r_1}\biggr). \end{equation} \] Thus we have a different formula for potential energy. Equation (13.12) tells us that the quantity \((\tfrac{1}{2}mv^2 - GMm/r)\) calculated at point \(1\) , at point \(2\) , or at any other place, has a constant value.

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch13-F3: Fig. 13–3.A closed path in a gravitational field.

Section: 13–2 Work done by gravity
Image file: images/Ch13-F3.png

Context before the figure:

We now have the formula for the potential energy in a gravitational field for vertical motion. Now we have an interesting problem. Can we makeperpetual motionin a gravitational field? The gravitational field varies; in different places it is in different directions and has different strengths. Could we do something like this, using a fixed, frictionless track: start at some point and lift an object out to some other point, then move it around an arc to a third point, then lower it a certain distance, then move it in at a certain slope and pull it out some other way, so that when we bring it back to the starting point, a certain amount of work has been done by the gravitational force, and the kinetic energy of the object is increased? Can we design the curve so that it comes back moving a little bit faster than it did before, so that it goes around and around and around, and gives us...

Context after the figure:

Is the work really zero? Let us try to demonstrate that it is. First we shall explain more or less why it is zero, and then we shall examine it a little better mathematically. Suppose that we use a simple path such as that shown in Fig.13–3, in which a small mass is carried from point \(1\) to point \(2\) , and then is made to go around a circle to \(3\) , back to \(4\) , then to \(5\) , \(6\) , \(7\) , and \(8\) , and finally back to \(1\) . All of the lines are either purely radial or circular, with \(M\) as the center. How much work is done in carrying \(m\) around this path? Between points \(1\) and \(2\) , it is \(GMm\) times the difference of \(1/r\) between these two points: \[ \begin{equation*} W_{12}=\int_1^2\FLPF\cdot d\FLPs=\int_1^2-GMm\,\frac{dr}{r^2}= GMm\biggr(\frac{1}{r_2}-\frac{1}{r_1}\biggr). \end{equation*} \] From \(2\) to \(3\) the force is exactly at right angles to...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch13-F4: Fig. 13–4.A “smooth” closed path, showing a magnified segment of it approximated by a series of radial and circumferential steps, and an enlarged view of one step.

Section: 13–2 Work done by gravity
Image file: images/Ch13-F4.png

Context before the figure:

Is the work really zero? Let us try to demonstrate that it is. First we shall explain more or less why it is zero, and then we shall examine it a little better mathematically. Suppose that we use a simple path such as that shown in Fig.13–3, in which a small mass is carried from point \(1\) to point \(2\) , and then is made to go around a circle to \(3\) , back to \(4\) , then to \(5\) , \(6\) , \(7\) , and \(8\) , and finally back to \(1\) . All of the lines are either purely radial or circular, with \(M\) as the center. How much work is done in carrying \(m\) around this path? Between points \(1\) and \(2\) , it is \(GMm\) times the difference of \(1/r\) between these two points: \[ \begin{equation*} W_{12}=\int_1^2\FLPF\cdot d\FLPs=\int_1^2-GMm\,\frac{dr}{r^2}= GMm\biggr(\frac{1}{r_2}-\frac{1}{r_1}\biggr). \end{equation*} \] From \(2\) to \(3\) the force is exactly at right angles to...

Context after the figure:

Of course we may wonder whether this is too trivial a curve. What if we use arealcurve? Let us try it on a real curve. First of all, we might like to assert that a real curve could always be imitated sufficiently well by a series of sawtooth jiggles like those of Fig.13–4, and that therefore, etc., Q.E.D., but without a little analysis, it is not obvious at first that the work done going around even a small triangle is zero. Let us magnify one of the triangles, as shown in Fig.13–4. Is the work done in going from \(a\) to \(b\) and \(b\) to \(c\) on a triangle the same as the work done in going directly from \(a\) to \(c\) ? Suppose that the force is acting in a certain direction; let us take the triangle such that the side \(bc\) is in this direction, just as an example. We also suppose that the triangle is so small that the force is essentially constant over the entire triangle. What...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch13-F5: Fig. 13–5.The gravitational field \(\FigC\) at a mass point produced by an infinite plane sheet of matter.

Section: 13–4 Gravitational field of large objects
Image file: images/Ch13-F5.png

Context before the figure:

In Eq. (13.16), on the other hand, \(\sum\limits_{\text{pairs}}\) means that given values of \(i\) and \(j\) occur only once. Thus the particle pair \(1\) and \(3\) contributes only one term to the sum. To keep track of this, we might agree to let \(i\) range over all values \(1\) , \(2\) , \(3\) , …, and for each \(i\) let \(j\) range only over valuesgreaterthan \(i\) . Thus if \(i = 3\) , \(j\) could only have values \(4\) , \(5\) , \(6\) , … But we notice that for each \(i,j\) value there are two contributions to the sum, one involving \(\FLPv_i\) , and the other \(\FLPv_j\) , and that these terms have the same appearance as those of Eq. (13.15), whereallvalues of \(i\) and \(j\) (except \(i = j\) ) are included in the sum. Therefore, by matching the terms one by one, we see that Eqs. (13.16) and (13.15) are precisely the same, but of opposite sign, so that the time derivative of the...

Context after the figure:

Now we shall calculate the fields which are met in a few physical circumstances involvingdistributions of mass. We have not so far considered distributions of mass, only particles, so it is interesting to calculate the forces when they are produced by more than just one particle. First we shall find the gravitational force on a mass that is produced by a plane sheet of material, infinite in extent. The force on a unit mass at a given point \(P\) , produced by this sheet of material (Fig.13–5), will of course be directed toward the sheet. Let the distance of the point from the sheet be \(a\) , and let the amount of mass per unit area of this huge sheet be \(\mu\) . We shall suppose \(\mu\) to be constant; it is a uniform sheet of material. Now, what small field \(d\FLPC\) is produced by the mass \(dm\) lying between \(\rho\) and \(\rho + d\rho\) from the point \(O\) of the sheet nearest...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch13-F6: Fig. 13–6.A thin spherical shell of mass or charge.

Section: 13–4 Gravitational field of large objects
Image file: images/Ch13-F6.png

Context before the figure:

Now we come to a most interesting and important problem, whose solution we have been assuming all the time, namely, that the force produced by the earth at a point on the surface or outside it is the same as if all the mass of the earth were located at its center. The validity of this assumption is not obvious, because when we are close, some of the mass is very close to us, and some is farther away, and so on. When we add the effects all together, it seems a miracle that the net force is exactly the same as we would get if we put all the mass in the middle!

Context after the figure:

We now demonstrate the correctness of this miracle. In order to do so, however, we shall consider a thin uniform hollow shell instead of the whole earth. Let the total mass of the shell be \(m\) , and let us calculate thepotential energyof a particle of mass \(m'\) a distance \(R\) away from the center of the sphere (Fig.13–6) and show that the potential energy is the same as it would be if the mass \(m\) were a point at the center. (The potential energy is easier to work with than is the field because we do not have to worry about angles, we merely add the potential energies of all the pieces of mass.) If we call \(x\) the distance of a certain plane section from the center, then all the mass that is in a slice \(dx\) is at the same distance \(r\) from \(P\) , and the potential energy due to this ring is \(-Gm'\,dm/r\) . How much mass is in the small slice \(dx\) ? An amount \[...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.
