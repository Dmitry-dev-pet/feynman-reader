# Figure context for Chapter 40. The Principles of Statistical Mechanics

SOURCE: Feynman Lectures on Physics, Volume I, Chapter 40
LANGUAGE: en
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_40.html

NotebookLM use: pair this file with the clean chapter text and the PNG image files below. The visual descriptions here are inferred from the surrounding lecture text; the PNG files are included so NotebookLM can inspect the diagrams directly when image sources are uploaded.

## Ch40-F1: Fig. 40–1.The pressure at height \(h\) must exceed that at \(h + dh\) by the weight of the intervening gas.

Section: 40–1 The exponential atmosphere
Image file: images/Ch40-F1.png

Context before the figure:

Let us begin with an example: the distribution of the molecules in an atmosphere like our own, but without the winds and other kinds of disturbance. Suppose that we have a column of gas extending to a great height, and at thermal equilibrium—unlike our atmosphere, which as we know gets colder as we go up. We could remark that if the temperature differed at different heights, we could demonstrate lack of equilibrium by connecting a rod to some balls at the bottom (Fig.40–1), where they would pick up \(\tfrac{1}{2}kT\) from the molecules there and would shake, via the rod, the balls at the top and those would shake the molecules at the top. So, ultimately, of course, the temperature becomes the same at all heights in a gravitational field.

Context after the figure:

If the temperature is the same at all heights, the problem is to discover by what law the atmosphere becomes tenuous as we go up. If \(N\) is the total number of molecules in a volume \(V\) of gas at pressure \(P\) , then we know \(PV = NkT\) , or \(P = nkT\) , where \(n = N/V\) is the number of molecules per unit volume. In other words, if we know the number of molecules per unit volume, we know the pressure, and vice versa: they are proportional to each other, since the temperature is constant in this problem. But the pressure is not constant, it must increase as the altitude is reduced, because it has to hold, so to speak, the weight of all the gas above it. That is the clue by which we may determine how the pressure changes with height. If we take a unit area at height \(h\) , then the vertical force from below, on this unit area, is the pressure \(P\) . The vertical force per unit...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch40-F2: Fig. 40–2.The normalized density as a function of height in the earth’s gravitational field for oxygen and for hydrogen, at constant temperature.

Section: 40–1 The exponential atmosphere
Image file: images/Ch40-F2.png

Context before the figure:

We thus have an equation for the particle density \(n\) , which varies with height, but which has a derivative which is proportional to itself. Now a function which has a derivative proportional to itself is an exponential, and the solution of this differential equation is \[ \begin{equation} \label{Eq:I:40:1} n = n_0e^{-mgh/kT}. \end{equation} \] Here the constant of integration, \(n_0\) , is obviously the density at \(h = 0\) (which can be chosen anywhere), and the density goes down exponentially with height.

Context after the figure:

Note that if we have different kinds of molecules with different masses, they go down with different exponentials. The ones which were heavier would decrease with altitude faster than the light ones. Therefore we would expect that because oxygen is heavier than nitrogen, as we go higher and higher in an atmosphere with nitrogen and oxygen the proportion of nitrogen would increase. This does not really happen in our own atmosphere, at least at reasonable heights, because there is so much agitation which mixes the gases back together again. It is not an isothermal atmosphere. Nevertheless, thereisa tendency for lighter materials, like hydrogen, to dominate at very great heights in the atmosphere, because the lowest masses continue to exist, while the other exponentials have all died out (Fig.40–2).

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch40-F3: Fig. 40–3.A potential-energy function for two molecules, which depends only on their separation.

Section: 40–3 Evaporation of a liquid
Image file: images/Ch40-F3.png

Context before the figure:

In more advanced statistical mechanics one tries to solve the following important problem. Consider an assembly of molecules which attract each other, and suppose that the force between any two, say \(i\) and \(j\) , depends only on their separation \(r_{ij}\) , and can be represented as the derivative of a potential function \(V(r_{ij})\) . Figure40–3shows a form such a function might have. For \(r > r_0\) , the energy decreases as the molecules come together, because they attract, and then the energy increases very sharply as they come still closer together, because they repel strongly, which is characteristic of the way molecules behave, roughly speaking.

Context after the figure:

Now suppose we have a whole box full of such molecules, and we would like to know how they arrange themselves on the average. The answer is \(e^{-\text{P.E.}/kT}\) . The total potential energy in this case would be the sum over all the pairs, supposing that the forces are all in pairs (there may be three-body forces in more complicated things, but in electricity, for example, the potential energy is all in pairs). Then the probability for finding molecules in any particular combination of \(r_{ij}\) ’s will be proportional to \[ \begin{equation*} \exp\Bigl[-\sum_{i,j}V(r_{ij})/kT\Bigr]. \end{equation*} \]

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch40-F4: Fig. 40–4.Only those molecules moving up at \(h= 0\) with sufficient velocity can arrive at height \(h\) .

Section: 40–4 The distribution of molecular speeds
Image file: images/Ch40-F4.png

Context before the figure:

Now we go on to discuss the distribution of velocities, because sometimes it is interesting or useful to know how many of them are moving at different speeds. In order to do that, we may make use of the facts which we discovered with regard to the gas in the atmosphere. We take it to be a perfect gas, as we have already assumed in writing the potential energy, disregarding the energy of mutual attraction of the atoms. The only potential energy that we included in our first example was gravity. We would, of course, have something more complicated if there were forces between the atoms. Thus we assume that there are no forces between the atoms and, for a moment, disregard collisions also, returning later to the justification of this. Now we saw that there are fewer molecules at the height \(h\) than there are at the height \(0\) ; according to formula (40.1), they decrease exponentially...

Context after the figure:

Now let us put that idea a little more precisely: let us count how many molecules are passing from below to above the plane \(h = 0\) (by calling it height \({} = 0\) , we do not mean that there is a floor there; it is just a convenient label, and there is gas at negative \(h\) ). These gas molecules are moving around in every direction, but some of them are moving through the plane, and at any moment a certain number per second of them are passing through the plane from below to above with different velocities. Now we note the following: if we call \(u\) the velocity which is just needed to get up to the height \(h\) (kinetic energy \(mu^2/2 = mgh\) ), then the number of molecules per second which are passing upward through the lower plane in a vertical direction with velocity component greater than \(u\) is exactly the same as the number which pass through the upper plane...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch40-F5: Fig. 40–5.A velocity distribution function. The shaded area is \(f(u)\,du\) , the fraction of particles having velocities within a range \(du\) about \(u\) .

Section: 40–4 The distribution of molecular speeds
Image file: images/Ch40-F5.png

Context before the figure:

This way of describing the distribution of velocities, by giving the number of molecules that pass a given area with a certain minimum \(z\) -component, is not the most convenient way of giving the velocity distribution. For instance, inside the gas, one more often wants to know how many molecules are moving with a \(z\) -component of velocity between two given values, and that, of course, is not directly given by Eq. (40.4). We would like to state our result in the more conventional form, even though what we already have written is quite general.Note that it is not possible to say that any molecule has exactly some stated velocity;none of them has a velocityexactly equalto \(1.7962899173\) meters per second. So in order to make a meaningful statement, we have to ask how many are to be found in somerangeof velocities. We have to say how many have velocities between \(1.796\) and...

Context after the figure:

Now we have only to get this distribution by comparing it with the theorem we derived before. First we ask, what is the number of molecules passing through an area per second with a velocity greater than \(u\) , expressed in terms of \(f(u)\) ? At first we might think it is merely the integral of \(\int_u^\infty f(u)\,du\) , but it is not, because we want the number that are passing the areaper second. The faster ones pass more often, so to speak, than the slower ones, and in order to express how many pass, you have to multiply by the velocity. (We discussed that in the previous chapter when we talked about the number of collisions.) In a given time \(t\) the total number which pass through the surface is all of those which have been able to arrive at the surface, and the number which arrive come from a distance \(ut\) . So the number of molecules which arrive is not simply the number...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch40-F6: Fig. 40–6.Experimental values of \(\gamma\) as a function of temperature for hydrogen and oxygen. Classical theory predicts \(\gamma = 1.286\) , independent of temperature.

Section: 40–5 The specific heats of gases
Image file: images/Ch40-F6.png

Context before the figure:

Furthermore, the whole mystery is deep, because the diatomic molecule cannot be made rigid by a limit. Even if we made the couplings stiffer indefinitely, although it might not vibrate much, it would nevertheless keep vibrating. The vibrational energy inside is still \(kT\) , since it does not depend on the strength of the coupling. But if we could imagineabsoluterigidity, stopping all vibration to eliminate a variable, then we would get \(U = \tfrac{5}{2}kT\) and \(\gamma = 1.40\) for the diatomic case. This looks good for H \(_2\) or O \(_2\) . On the other hand, we would still have problems, because \(\gamma\) for either hydrogen or oxygen varies with temperature! From the measured values shown in Fig.40–6, we see that for H \(_2\) , \(\gamma\) varies from about \(1.6\) at \(-185^\circ\) C to \(1.3\) at \(2000^\circ\) C. The variation is more substantial in the case of hydrogen than...

Context after the figure:

So, all in all, we might say that we have some difficulty. We might try some force law other than a spring, but it turns out that anything else will only make \(U\) higher. If we include more forms of energy, \(\gamma\) approaches unity more closely, contradicting the facts. All the classical theoretical things that one can think of will only make it worse. The fact is that there are electrons in each atom, and we know from their spectra that there are internal motions; each of the electrons should have at least \(\tfrac{1}{2}kT\) of kinetic energy, and something for the potential energy, so when these are added in, \(\gamma\) gets still smaller. It is ridiculous. It is wrong.

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.
