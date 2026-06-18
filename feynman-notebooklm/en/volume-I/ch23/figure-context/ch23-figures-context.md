# Figure context for Chapter 23. Resonance

SOURCE: Feynman Lectures on Physics, Volume I, Chapter 23
LANGUAGE: en
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_23.html

NotebookLM use: pair this file with the clean chapter text and the PNG image files below. The visual descriptions here are inferred from the surrounding lecture text; the PNG files are included so NotebookLM can inspect the diagrams directly when image sources are uploaded.

## Ch23-F1: Fig. 23–1.A complex number may be represented by a point in the “complex plane.”

Section: 23–1 Complex numbers and harmonic motion
Image file: images/Ch23-F1.png

Context before the figure:

In the present chapter we shall continue our discussion of the harmonic oscillator and, in particular, the forced harmonic oscillator, using a new technique in the analysis. In the preceding chapter we introduced the idea of complex numbers, which have real and imaginary parts and which can be represented on a diagram in which the ordinate represents the imaginary part and the abscissa represents the real part. If \(a\) is a complex number, we may write it as \(a = a_r + ia_i\) , where the subscript \(r\) means the real part of \(a\) , and the subscript \(i\) means the imaginary part of \(a\) . Referring to Fig.23–1, we see that we may also write a complex number \(a = x + iy\) in the form \(x + iy = re^{i\theta}\) , where \(r^2 = x^2 + y^2 = (x + iy)(x - iy) = aa\cconj\) . (The complex conjugate of \(a\) , written \(a\cconj\) , is obtained by reversing the sign of \(i\) in \(a\) .) So...

Context after the figure:

We are going to apply complex numbers to our analysis of physical phenomena by the following trick. We have examples of things that oscillate; the oscillation may have a driving force which is a certain constant times \(\cos\omega t\) . Now such a force, \(F = F_0\cos\omega t\) , can be written as the real part of a complex number \(F = F_0e^{i\omega t}\) because \(e^{i\omega t} = \cos\omega t + i\sin\omega t\) . The reason we do this is that it is easier to work with an exponential function than with a cosine. So the whole trick is to represent our oscillatory functions as the real parts of certain complex functions. The complex number \(F\) that we have so defined is not a real physical force, because no force in physics is really complex; actual forces have no imaginary part, only a real part. We shall, however, speak of the “force” \(F_0e^{i\omega t}\) , but of course the actual...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F2: Fig. 23–2.Plot of \(\rho^2\) versus \(\omega\) .

Section: 23–2 The forced oscillator with damping
Image file: images/Ch23-F2.png

Context before the figure:

In addition, the phase angle \(\theta\) is easy to find, for if we write \[ \begin{equation} 1/R=1/\rho e^{i\theta}=(1/\rho)e^{-i\theta}= m(\omega_0^2-\omega^2+i\gamma\omega),\notag \end{equation} \] we see that \[ \begin{equation} \label{Eq:I:23:12} \tan\theta=-\gamma\omega/(\omega_0^2-\omega^2). \end{equation} \] It is minus because \(\tan (-\theta) =-\tan\theta\) . A negative value for \(\theta\) results for all \(\omega\) , and this corresponds to the displacement \(x\) lagging the force \(F\) .

Context after the figure:

Figure23–2shows how \(\rho^2\) varies as a function of frequency ( \(\rho^2\) is physically more interesting than \(\rho\) , because \(\rho^2\) is proportional to the square of the amplitude, or more or less to theenergythat is developed in the oscillator by the force). We see that if \(\gamma\) is very small, then \(1/(\omega_0^2 - \omega^2)^2\) is the most important term, and the response tries to go up toward infinity when \(\omega\) equals \(\omega_0\) . Now the “infinity” is not actually infinite because if \(\omega=\omega_0\) , then \(1/\gamma^2\omega^2\) is still there. The phase shift varies as shown in Fig.23–3.

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F3: Fig. 23–3.Plot of \(\theta\) versus \(\omega\) .

Section: 23–2 The forced oscillator with damping
Image file: images/Ch23-F3.png

Context before the figure:

In addition, the phase angle \(\theta\) is easy to find, for if we write \[ \begin{equation} 1/R=1/\rho e^{i\theta}=(1/\rho)e^{-i\theta}= m(\omega_0^2-\omega^2+i\gamma\omega),\notag \end{equation} \] we see that \[ \begin{equation} \label{Eq:I:23:12} \tan\theta=-\gamma\omega/(\omega_0^2-\omega^2). \end{equation} \] It is minus because \(\tan (-\theta) =-\tan\theta\) . A negative value for \(\theta\) results for all \(\omega\) , and this corresponds to the displacement \(x\) lagging the force \(F\) .

Context after the figure:

Figure23–2shows how \(\rho^2\) varies as a function of frequency ( \(\rho^2\) is physically more interesting than \(\rho\) , because \(\rho^2\) is proportional to the square of the amplitude, or more or less to theenergythat is developed in the oscillator by the force). We see that if \(\gamma\) is very small, then \(1/(\omega_0^2 - \omega^2)^2\) is the most important term, and the response tries to go up toward infinity when \(\omega\) equals \(\omega_0\) . Now the “infinity” is not actually infinite because if \(\omega=\omega_0\) , then \(1/\gamma^2\omega^2\) is still there. The phase shift varies as shown in Fig.23–3.

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F4: Fig. 23–4.The three passive circuit elements.

Section: 23–3 Electrical resonance
Image file: images/Ch23-F4.png

Context before the figure:

The simplest and broadest technical applications of resonance are in electricity. In the electrical world there are a number of objects which can be connected to make electric circuits. Thesepassive circuit elements, as they are often called, are of three main types, although each one has a little bit of the other two mixed in. Before describing them in greater detail, let us note that the whole idea of our mechanical oscillator being a mass on the end of a spring is only an approximation. All the mass is not actually at the “mass”; some of the mass is in the inertia of the spring. Similarly, all of the spring is not at the “spring”; the mass itself has a little elasticity, and although it may appear so, it is notabsolutelyrigid, and as it goes up and down, it flexes ever so slightly under the action of the spring pulling it. The same thing is true in electricity. There is an...

Context after the figure:

The three main kinds of circuit elements are the following. The first is called acapacitor(Fig.23–4); an example is two plane metallic plates spaced a very small distance apart by an insulating material. When the plates are charged there is a certain voltage difference, that is, a certain difference in potential, between them. The same difference of potential appears between the terminals \(A\) and \(B\) , because if there were any difference along the connecting wire, electricity would flow right away. So there is a certain voltage difference \(V\) between the plates if there is a certain electric charge \(+q\) and \(-q\) on them, respectively. Between the plates there will be a certain electric field; we have even found a formula for it (Chapters13and14): \[ \begin{equation} \label{Eq:I:23:14} V=\sigma d/\epsO=qd/\epsO A, \end{equation} \] where \(d\) is the spacing and \(A\) is the...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F5: Fig. 23–5.An oscillatory electrical circuit with resistance, inductance, and capacitance.

Section: 23–3 Electrical resonance
Image file: images/Ch23-F5.png

Context before the figure:

If we think of the charge \(q\) on a capacitor as being analogous to the displacement \(x\) of a mechanical system, we see that the current, \(I = dq/dt\) , is analogous to velocity, \(1/C\) is analogous to a spring constant \(k\) , and \(R\) is analogous to the resistive coefficient \(c=m\gamma\) in Eq. (23.6). Now it is very interesting that there exists another circuit element which is the analog ofmass! This is a coil which builds up a magnetic field within itself when there is a current in it. Achangingmagnetic field develops in the coil a voltage that is proportional to \(dI/dt\) (this is how a transformer works, in fact). The magnetic field is proportional to a current, and the induced voltage (so-called) in such a coil is proportional to the rate of change of the current: \[ \begin{equation} \label{Eq:I:23:16} V=L\,dI/dt=L\,d^2q/dt^2. \end{equation} \] The coefficient \(L\) is...

Context after the figure:

Suppose we make a circuit in which we have connected the three circuit elements in series (Fig.23–5); then the voltage across the whole thing from \(1\) to \(2\) is the work done in carrying a charge through, and it consists of the sum of several pieces: across the inductor, \(V_L = L\,d^2q/dt^2\) ; across the resistance, \(V_R = R\,dq/dt\) ; across the capacitor, \(V_C = q/C\) . The sum of these is equal to the applied voltage, \(V\) : \[ \begin{equation} \label{Eq:I:23:17} L\,d^2q/dt^2+R\,dq/dt+q/C=V(t). \end{equation} \] Now we see that this equation is exactly the same as the mechanical equation (23.6), and of course it can be solved in exactly the same manner. We suppose that \(V(t)\) is oscillatory: we are driving the circuit with a generator with a pure sine wave oscillation. Then we can write our \(V(t)\) as a complex \(\hat{V}\) with the understanding that it must be ultimately...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F6: Fig. 23–6.Response of the atmosphere to external excitation. \(a\) is the required response if the atmospheric \(S_2\) -tide is of gravitational origin; peak amplification is \(100:1\) . \(b\) is derived from observed magnification and phase of \(M_2\) -tide. [Munk and MacDonald, “Rotation of the Earth,” Cambridge University Press (1960)]

Section: 23–4 Resonance in nature
Image file: images/Ch23-F6.png

Context before the figure:

Although we have discussed the electrical case in detail, we could also bring up case after case in many fields, and show exactly how the resonance equation is the same. There are many circumstances in nature in which something is “oscillating” and in which the resonance phenomenon occurs. We said that in an earlier chapter; let us now demonstrate it. If we walk around our study, pulling books off the shelves and simply looking through them to find an example of a curve that corresponds to Fig.23–2and comes from the same equation, what do we find? Just to demonstrate the wide range obtained by taking the smallest possible sample, it takes only five or six books to produce quite a series of phenomena which show resonances.

Context after the figure:

The first two are from mechanics, the first on a large scale: the atmosphere of the whole earth. If the atmosphere, which we suppose surrounds the earth evenly on all sides, is pulled to one side by the moon or, rather, squashed prolate into a double tide, and if we could then let it go, it would go sloshing up and down; it is an oscillator. This oscillator isdrivenby the moon, which is effectively revolving about the earth; any one component of the force, say in the \(x\) -direction, has a cosine component, and so the response of the earth’s atmosphere to the tidal pull of the moon is that of an oscillator. The expected response of the atmosphere is shown in Fig.23–6, curve \(b\) (curve \(a\) is another theoretical curve under discussion in the book from which this is taken out of context). Now one might think that we only have one point on this resonance curve, since we only have the...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F7: Fig. 23–7.Transmission of infrared radiation through a thin (0.17 \(\mu\) m) sodium chloride film. [After R. B. Barnes,Z. Physik75, 723 (1932). Kittel,Introduction to Solid State Physics, Wiley, 1956.]

Section: 23–4 Resonance in nature
Image file: images/Ch23-F7.png

Context before the figure:

Next we go to the small scale of mechanical oscillation. This time we take a sodium chloride crystal, which has sodium ions and chlorine ions next to each other, as we described in an early chapter. These ions are electrically charged, alternately plus and minus. Now there is an interesting oscillation possible. Suppose that we could drive all the plus charges to the right and all the negative charges to the left, and let go; they would then oscillate back and forth, the sodium lattice against the chlorine lattice. How can we ever drive such a thing? That is easy, for if we apply an electric field on the crystal, it will push the plus charge one way and the minus charge the other way! So, by having an external electric field we can perhaps get the crystal to oscillate. The frequency of the electric field needed is so high, however, that it corresponds toinfrared radiation!So we try to...

Context after the figure:

But what about the width? What determines the width? There are many cases in which the width that is seen on the curve is not really the natural width \(\gamma\) that one would have theoretically. There are two reasons why there can be a wider curve than the theoretical curve. If the objects do not all have the same frequency, as might happen if the crystal were strained in certain regions, so that in those regions the oscillation frequency were slightly different than in other regions, then what we have is many resonance curves on top of each other; so we apparently get a wider curve. The other kind of width is simply this: perhaps we cannot measure the frequency precisely enough—if we open the slit of the spectrometer fairly wide, so although we thought we had only one frequency, we actually had a certain range \(\Delta\omega\) , then we may not have the resolving power needed to see...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F8: Fig. 23–8.Magnetic energy loss in paramagnetic organic compound as function of applied magnetic field intensity. [Holdenet al.,Phys. Rev.75, 1614 (1949)]

Section: 23–4 Resonance in nature
Image file: images/Ch23-F8.png

Context before the figure:

But what about the width? What determines the width? There are many cases in which the width that is seen on the curve is not really the natural width \(\gamma\) that one would have theoretically. There are two reasons why there can be a wider curve than the theoretical curve. If the objects do not all have the same frequency, as might happen if the crystal were strained in certain regions, so that in those regions the oscillation frequency were slightly different than in other regions, then what we have is many resonance curves on top of each other; so we apparently get a wider curve. The other kind of width is simply this: perhaps we cannot measure the frequency precisely enough—if we open the slit of the spectrometer fairly wide, so although we thought we had only one frequency, we actually had a certain range \(\Delta\omega\) , then we may not have the resolving power needed to see...

Context after the figure:

Now we turn to a more esoteric example, and that is the swinging of a magnet. If we have a magnet, with north and south poles, in a constant magnetic field, the N end of the magnet will be pulled one way and the S end the other way, and there will in general be a torque on it, so it will vibrate about its equilibrium position, like a compass needle. However, the magnets we are talking about areatoms. These atoms have an angular momentum, the torque does not produce a simple motion in the direction of the field, but instead, of course, aprecession. Now, looked at from the side, any one component is “swinging,” and we can disturb or drive that swinging and measure an absorption. The curve in Fig.23–8represents a typical such resonance curve. What has been done here is slightly different technically. The frequency of the lateral field that is used to drive this swinging is always kept the...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F9: Fig. 23–9.The intensity of gamma-radiation from lithium as a function of the energy of the bombarding protons. The dashed curve is a theoretical one calculated for protons with an angular momentum \(\ell = 0\) . [Bonner and Evans,Phys. Rev.73, 666 (1948)]

Section: 23–4 Resonance in nature
Image file: images/Ch23-F9.png

Context before the figure:

Now we turn to a more esoteric example, and that is the swinging of a magnet. If we have a magnet, with north and south poles, in a constant magnetic field, the N end of the magnet will be pulled one way and the S end the other way, and there will in general be a torque on it, so it will vibrate about its equilibrium position, like a compass needle. However, the magnets we are talking about areatoms. These atoms have an angular momentum, the torque does not produce a simple motion in the direction of the field, but instead, of course, aprecession. Now, looked at from the side, any one component is “swinging,” and we can disturb or drive that swinging and measure an absorption. The curve in Fig.23–8represents a typical such resonance curve. What has been done here is slightly different technically. The frequency of the lateral field that is used to drive this swinging is always kept the...

Context after the figure:

Now we go still further. Our next example has to do with atomic nuclei. The motions of protons and neutrons in nuclei are oscillatory in certain ways, and we can demonstrate this by the following experiment. We bombard a lithium atom with protons, and we discover that a certain reaction, producing \(\gamma\) -rays, actually has a very sharp maximum typical of resonance. We note in Fig.23–9, however, one difference from other cases: the horizontal scale is not a frequency, it is anenergy!The reason is that in quantum mechanics what we think of classically as the energy will turn out to be really related to a frequency of a wave amplitude. When we analyze something which in simple large-scale physics has to do with a frequency, we find that when we do quantum-mechanical experiments with atomic matter, we get the corresponding curve as a function of energy. In fact, this curve is a...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F10: Fig. 23–10.[Courtesy of Dr. R. Mössbauer]

Section: 23–4 Resonance in nature
Image file: images/Ch23-F10.png

Context before the figure:

Now we go still further. Our next example has to do with atomic nuclei. The motions of protons and neutrons in nuclei are oscillatory in certain ways, and we can demonstrate this by the following experiment. We bombard a lithium atom with protons, and we discover that a certain reaction, producing \(\gamma\) -rays, actually has a very sharp maximum typical of resonance. We note in Fig.23–9, however, one difference from other cases: the horizontal scale is not a frequency, it is anenergy!The reason is that in quantum mechanics what we think of classically as the energy will turn out to be really related to a frequency of a wave amplitude. When we analyze something which in simple large-scale physics has to do with a frequency, we find that when we do quantum-mechanical experiments with atomic matter, we get the corresponding curve as a function of energy. In fact, this curve is a...

Context after the figure:

Now we turn to another example which also involves a nuclear energy level, but now a much, much narrower one. The \(\omega_0\) in Fig.23–10corresponds to an energy of \(100{,}000\) electron volts, while the width \(\gamma\) is approximately \(10^{-5}\) electron volt; in other words, this has a \(Q\) of \(10^{10}\) ! When this curve was measured it was the largest \(Q\) of any oscillator that had ever been measured. It was measured by Dr. Mössbauer, and it was the basis of his Nobel prize. The horizontal scale here is velocity, because the technique for obtaining the slightly different frequencies was to use the Doppler effect, by moving the source relative to the absorber. One can see how delicate the experiment is when we realize that the speed involved is a few centimeters per second! On the actual scale of the figure, zero frequency would correspond to a point about \(10^{10}\) cm to...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch23-F11: Fig. 23–11.Momentum dependence of the cross section for the reactions (a) \(\text{K}^- + \text{p} \to \Lambda + \pi^+ + \pi^-\) and (b) \(\text{K}^- +
\text{p} \to \overline{\text{K}}{}^0 + \text{n}\) . The lower curves in (a) and (b) represent the presumed nonresonant backgrounds, while the upper curves contain in addition the superposed resonance. [Ferro-Luzziet al.,Phys. Rev. Lett.8, 28 (1962)]

Section: 23–4 Resonance in nature
Image file: images/Ch23-F11.png

Context before the figure:

Now we turn to another example which also involves a nuclear energy level, but now a much, much narrower one. The \(\omega_0\) in Fig.23–10corresponds to an energy of \(100{,}000\) electron volts, while the width \(\gamma\) is approximately \(10^{-5}\) electron volt; in other words, this has a \(Q\) of \(10^{10}\) ! When this curve was measured it was the largest \(Q\) of any oscillator that had ever been measured. It was measured by Dr. Mössbauer, and it was the basis of his Nobel prize. The horizontal scale here is velocity, because the technique for obtaining the slightly different frequencies was to use the Doppler effect, by moving the source relative to the absorber. One can see how delicate the experiment is when we realize that the speed involved is a few centimeters per second! On the actual scale of the figure, zero frequency would correspond to a point about \(10^{10}\) cm to...

Context after the figure:

Finally, if we look in an issue of thePhysical Review, say that of January 1, 1962, will we find a resonance curve? Every issue has a resonance curve, and Fig.23–11is the resonance curve for this one. This resonance curve turns out to be very interesting. It is the resonance found in a certain reaction among strange particles, a reaction in which a K \(^-\) and a proton interact. The resonance is detected by seeing how many of some kinds of particles come out, and depending on what and how many come out, one gets different curves, but of the same shape and with the peak at the same energy. We thus determine that there is a resonance at a certain energy for the K \(^-\) meson. That presumably means that there is some kind of a state, or condition, corresponding to this resonance, which can be attained by putting together a K \(^-\) and a proton. This is a new particle, or resonance...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.
