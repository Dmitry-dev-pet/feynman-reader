# Figure context for Chapter 50. Harmonics

SOURCE: Feynman Lectures on Physics, Volume I, Chapter 50
LANGUAGE: en
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_50.html

NotebookLM use: pair this file with the clean chapter text and the PNG image files below. The visual descriptions here are inferred from the surrounding lecture text; the PNG files are included so NotebookLM can inspect the diagrams directly when image sources are uploaded.

## Ch50-F1: Fig. 50–1.Pressure as a function of time for (a) a noise, and (b) a musical tone.

Section: 50–1 Musical tones
Image file: images/Ch50-F1.png

Context before the figure:

Among the sounds that we hear, there is one kind that we callnoise. Noise corresponds to a sort of irregular vibration of the eardrum that is produced by the irregular vibration of some object in the neighborhood. If we make a diagram to indicate the pressure of the air on the eardrum (and, therefore, the displacement of the drum) as a function of time, the graph which corresponds to a noise might look like that shown in Fig.50–1(a). (Such a noise might correspond roughly to the sound of a stamped foot.) The sound ofmusichas a different character. Music is characterized by the presence of more-or-lesssustained tones—or musical “notes.” (Musical instruments may make noises as well!) The tone may last for a relatively short time, as when a key is pressed on a piano, or it may be sustained almost indefinitely, as when a flute player holds a long note.

Context after the figure:

What is the special character of a musical note from the point of view of the pressure in the air? A musical note differs from a noise in that there is a periodicity in its graph. There is some uneven shape to the variation of the air pressure with time, and the shape repeats itself over and over again. An example of a pressure-time function that would correspond to a musical note is shown in Fig.50–1(b).

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch50-F2: Fig. 50–2.Any periodic function \(f(t)\) is equal to a sum of simple harmonic functions.

Section: 50–2 The Fourier series
Image file: images/Ch50-F2.png

Context before the figure:

We conclude, then, thatanyfunction \(f(t)\) that is periodic with the period \(T\) can be written mathematically as \[ \begin{alignat}{4} f(t) &= a_0\notag\\[.5ex] &\quad\;+\;a_1\cos&&\omega t &&\;+\;b_1\sin&&\omega t\notag\\[.65ex] &\quad\;+\;a_2\cos2&&\omega t &&\;+\;b_2\sin2&&\omega t\notag\\[.65ex] &\quad\;+\;a_3\cos3&&\omega t &&\;+\;b_3\sin3&&\omega t\notag\\[.5ex] \label{Eq:I:50:2} &\quad\;+\;\dotsb && &&\;+\;\dotsb \end{alignat} \] where \(\omega = 2\pi/T\) and the \(a\) ’s and \(b\) ’s are numerical constants which tell us how much of each component oscillation is present in the oscillation \(f(t)\) . We have added the “zero-frequency” term \(a_0\) so that our formula will be completely general, although it is usually zero for a musical tone. It represents a shift of the average value (that is, the “zero” level) of the sound pressure. With it our formula can take care of any...

Context after the figure:

We have said thatanyperiodic function can be made up in this way. We should correct that and say that any sound wave, or any function we ordinarily encounter in physics, can be made up of such a sum. The mathematicians can invent functions which cannot be made up of simple harmonic functions—for instance, a function that has a “reverse twist” so that it has two values for some values of \(t\) ! We need not worry about such functions here.

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch50-F3: Fig. 50–3.Square-wave function.

Section: 50–4 The Fourier coefficients
Image file: images/Ch50-F3.png

Context before the figure:

We now know how to “analyze” a periodic wave into its harmonic components. The procedure is calledFourier analysis, and the separate terms are called Fourier components. We havenotshown, however, that once we find all of the Fourier components and add them together, we do indeed get back our \(f(t)\) . The mathematicians have shown, for a wide class of functions, in fact for all that are of interest to physicists, that if we can do the integrals we will get back \(f(t)\) . There is one minor exception. If the function \(f(t)\) is discontinuous, i.e., if it jumps suddenly from one value to another, the Fourier sum will give a value at the breakpoint halfway between the upper and lower values at the discontinuity. So if we have the strange function \(f(t) = 0\) , \(0 \leq t < t_0\) , and \(f(t) = 1\) for \(t_0 \leq t \leq T\) , the Fourier sum will give the right value everywhereexcept at...

Context after the figure:

As an exercise, we suggest that the reader determine the Fourier series for the function shown in Fig.50–3. Since the function cannot be written in an explicit algebraic form, you will not be able to do the integrals from zero to \(T\) in the usual way. The integrals are easy, however, if we separate them into two parts: the integral from zero to \(T/2\) (over which \(f(t) = 1\) ) and the integral from \(T/2\) to \(T\) (over which \(f(t) = -1\) ). The result should be \[ \begin{equation} \label{Eq:I:50:19} f(t) = \frac{4}{\pi}(\sin\omega t + \tfrac{1}{3}\sin3\omega t + \tfrac{1}{5}\sin5\omega t + \dotsb), \end{equation} \] where \(\omega = 2\pi/T\) . We thus find that our square wave (with the particular phase chosen) has only odd harmonics, and their amplitudes are in inverse proportion to their frequencies.

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch50-F4: Fig. 50–4.Linear and nonlinear responses.

Section: 50–6 Nonlinear responses
Image file: images/Ch50-F4.png

Context before the figure:

The energy in a wave is proportional to the square of its amplitude. For a wave of complex shape, the energy in one period will be proportional to \(\int_0^Tf^2(t)\,dt\) . We can also relate this energy to the Fourier coefficients. We write \[ \begin{gather} \label{Eq:I:50:22} \int_0^Tf^2(t)\,dt =\\ \int_0^T\biggl[a_0 + \sum_{n = 1}^\infty a_n\cos n\omega t + \sum_{n = 1}^\infty b_n\sin n\omega t\biggr]^2\,dt.\notag \end{gather} \] When we expand the square of the bracketed term we will get all possible cross terms, such as \(a_5\cos5\omega t\cdot a_7\cos7\omega t\) and \(a_5\cos5\omega t\cdot b_7\sin7\omega t\) . We have shown above, however, [Eqs. (50.11) and (50.12)] that the integrals of all such terms over one period is zero. We have left only the square terms like \(a_5^2\cos^2 5\omega t\) . The integral of any cosine squared or sine squared over one period is equal to \(T/2\) ...

Context after the figure:

Finally, in the theory of harmonics there is an important phenomenon which should be remarked upon because of its practical importance—that of nonlinear effects. In all the systems that we have been considering so far, we have supposed that everything was linear, that the responses to forces, say the displacements or the accelerations, were always proportional to the forces. Or that the currents in the circuits were proportional to the voltages, and so on. We now wish to consider cases where there is not a strict proportionality. We think, at the moment, of some device in which the response, which we will call \(x_{\text{out}}\) at the time \(t\) , is determined by the input \(x_{\text{in}}\) at the time \(t\) . For example, \(x_{\text{in}}\) might be the force and \(x_{\text{out}}\) might be the displacement. Or \(x_{\text{in}}\) might be the current and \(x_{\text{out}}\) the voltage...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.

## Ch50-F5: Fig. 50–5.The response of a nonlinear device to the input \(\cos\omega
t\) . A linear response is shown for comparison.

Section: 50–6 Nonlinear responses
Image file: images/Ch50-F5.png

Context before the figure:

Finally, in the theory of harmonics there is an important phenomenon which should be remarked upon because of its practical importance—that of nonlinear effects. In all the systems that we have been considering so far, we have supposed that everything was linear, that the responses to forces, say the displacements or the accelerations, were always proportional to the forces. Or that the currents in the circuits were proportional to the voltages, and so on. We now wish to consider cases where there is not a strict proportionality. We think, at the moment, of some device in which the response, which we will call \(x_{\text{out}}\) at the time \(t\) , is determined by the input \(x_{\text{in}}\) at the time \(t\) . For example, \(x_{\text{in}}\) might be the force and \(x_{\text{out}}\) might be the displacement. Or \(x_{\text{in}}\) might be the current and \(x_{\text{out}}\) the voltage...

Context after the figure:

Nonlinear responses have several important practical consequences. We shall discuss some of them now. First we consider what happens if we apply a pure tone at the input. We let \(x_{\text{in}} = \cos\omega t\) . If we plot \(x_{\text{out}}\) as a function of time we get the solid curve shown in Fig.50–5. The dashed curve gives, for comparison, the response of a linear system. We see that the output is no longer a cosine function. It is more peaked at the top and flatter at the bottom. We say that the output isdistorted. We know, however, that such a wave is no longer a pure tone, that it will have harmonics. We can find what the harmonics are. Using \(x_{\text{in}} = \cos\omega t\) with Eq. (50.25), we have \[ \begin{equation} \label{Eq:I:50:26} x_{\text{out}}(t) = K(\cos\omega t + \epsilon\cos^2\omega t). \end{equation} \] From the equality \(\cos^2\theta = \tfrac{1}{2}(1 +...

NotebookLM reading hint:

Use the image together with the nearby text above. Prefer the lecture context over generic image interpretation.
