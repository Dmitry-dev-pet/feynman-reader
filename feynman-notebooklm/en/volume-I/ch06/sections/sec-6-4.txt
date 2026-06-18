SOURCE: Feynman Lectures on Physics, Volume I, Chapter 6
LANGUAGE: en
SECTION: 6–4 A probability distribution
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_06.html

# 6–4 A probability distribution

Let us return now to the random walk and consider a modification of it. Suppose that in addition to a random choice of thedirection( \(+\) or \(-\) ) of each step, thelengthof each step also varied in some unpredictable way, the only condition being thaton the averagethe step length was one unit. This case is more representative of something like the thermal motion of a molecule in a gas. If we call the length of a step \(S\) , then \(S\) may have any value at all, but most often will be “near” \(1\) . To be specific, we shall let \(\expval{S^2}=1\) or, equivalently, \(S_{\text{rms}}=1\) . Our derivation for \(\expval{D^2}\) would proceed as before except that Eq. (6.8) would be changed now to read
\[
\begin{equation}
\label{Eq:I:6:15}
\expval{D_N^2}=\expval{D_{N-1}^2}+\expval{S^2}=\expval{D_{N-1}^2}+1.
\end{equation}
\]
We have, as before, that
\[
\begin{equation}
\label{Eq:I:6:16}
\expval{D_N^2}=N.
\end{equation}
\]
What would we expect now for the distribution of distances \(D\) ? What is, for example, the probability that \(D=0\) after \(30\) steps? The answer is zero! The probability is zero that \(D\) will beany particularvalue, since there is no chance at all that the sum of the backward steps (of varying lengths) would exactly equal the sum of forward steps. We cannot plot a graph like that of Fig.6–2.
We can, however, obtain a representation similar to that of Fig.6–2, if we ask, not what is the probability of obtaining \(D\) exactly equal to \(0\) , \(1\) , or \(2\) , but instead what is the probability of obtaining \(D\) near \(0\) , \(1\) , or \(2\) . Let us define \(P(x,\Delta x)\) as the probability that \(D\) will lie in the interval \(\Delta x\) located at \(x\) (say from \(x\) to \(x+\Delta x\) ). We expect that for small \(\Delta x\) the chance of \(D\) landing in the interval is proportional to \(\Delta x\) , the width of the interval. So we can write
\[
\begin{equation}
\label{Eq:I:6:17}
P(x,\Delta x)=p(x)\,\Delta x.
\end{equation}
\]
The function \(p(x)\) is called theprobability density.
The form of \(p(x)\) will depend on \(N\) , the number of steps taken, and also on the distribution of individual step lengths. We cannot demonstrate the proofs here, but for large \(N\) , \(p(x)\) is thesamefor all reasonable distributions in individual step lengths, and depends only on \(N\) . We plot \(p(x)\) for three values of \(N\) in Fig.6–7. You will notice that the “half-widths” (typical spread from \(x=0\) ) of these curves is \(\sqrt{N}\) , as we have shown it should be.
FIGURE Ch6-F7: Fig. 6–7.The probability density for ending up at the distance \(D\) from the starting place in a random walk of \(N\) steps. ( \(D\) is measured in units of the rms step length.)
You may notice also that the value of \(p(x)\) near zero is inversely proportional to \(\sqrt{N}\) . This comes about because the curves are all of a similar shape and their areas under the curves must all be equal. Since \(p(x)\,\Delta x\) is the probability of finding \(D\) in \(\Delta x\) when \(\Delta x\) is small, we can determine the chance of finding \(D\) somewhereinside an arbitrary interval from \(x_1\) to \(x_2\) , by cutting the interval in a number of small increments \(\Delta x\) and evaluating the sum of the terms \(p(x)\,\Delta x\) for each increment. The probability that \(D\) lands somewhere between \(x_1\) and \(x_2\) , which we may write \(P(x_1 < D < x_2)\) , is equal to the shaded area in Fig.6–8. The smaller we take the increments \(\Delta x\) , the more correct is our result. We can write, therefore,
\[
\begin{equation}
\begin{gathered}
P(x_1 < D < x_2)=\sum p(x)\Delta x\\[1ex]
=\int_{x_1}^{x_2}p(x)\,dx.
\end{gathered}
\label{Eq:I:6:18}
\end{equation}
\]
FIGURE Ch6-F8: Fig. 6–8.The probability that the distance \(D\) traveled in a random walk is between \(x_1\) and \(x_2\) is the area under the curve of \(p(x)\) from \(x_1\) to \(x_2\) .
The area under the whole curve is the probability that \(D\) lands somewhere (that is, hassomevalue between \(x=-\infty\) and \(x=+\infty\) ). That probability is surely \(1\) . We must have that
\[
\begin{equation}
\label{Eq:I:6:19}
\int_{-\infty}^{+\infty}p(x)\,dx=1.
\end{equation}
\]
Since the curves in Fig.6–7get wider in proportion to \(\sqrt{N}\) , their heights must be proportional to \(1/\sqrt{N}\) to maintain the total area equal to \(1\) .
The probability density function we have been describing is one that is encountered most commonly. It is known as thenormalorGaussianprobability density. It has the mathematical form
\[
\begin{equation}
\label{Eq:I:6:20}
p(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-x^2/2\sigma^2},
\end{equation}
\]
where \(\sigma\) is called thestandard deviationand is given, in our case, by \(\sigma=\sqrt{N}\) or, if the rms step size is different from \(1\) , by \(\sigma=\sqrt{N}S_{\text{rms}}\) .
We remarked earlier that the motion of a molecule, or of any particle, in a gas is like a random walk. Suppose we open a bottle of an organic compound and let some of its vapor escape into the air. If there are air currents, so that the air is circulating, the currents will also carry the vapor with them. But even inperfectly still air, the vapor will gradually spread out—will diffuse—until it has penetrated throughout the room. We might detect it by its color or odor. The individual molecules of the organic vapor spread out in still air because of the molecular motions caused by collisions with other molecules. If we know the average “step” size, and the number of steps taken per second, we can find the probability that one, or several, molecules will be found at some distance from their starting point after any particular passage of time. As time passes, more steps are taken and the gas spreads out as in the successive curves of Fig.6–7. In a later chapter, we shall find out how the step sizes and step frequencies are related to the temperature and pressure of a gas.
Earlier, we said that the pressure of a gas is due to the molecules bouncing against the walls of the container. When we come later to make a more quantitative description, we will wish to know how fast the molecules are going when they bounce, since the impact they make will depend on that speed. We cannot, however, speak ofthespeed of the molecules. It is necessary to use a probability description. A molecule may have any speed, but some speeds are more likely than others. We describe what is going on by saying that the probability that any particular molecule will have a speed between \(v\) and \(v+\Delta v\) is \(p(v)\,\Delta v\) , where \(p(v)\) , a probability density, is a given function of the speed \(v\) . We shall see later how Maxwell, using common sense and the ideas of probability, was able to find a mathematical expression for \(p(v)\) . The form2of the function \(p(v)\) is shown in Fig.6–9. Velocities may have any value, but are most likely to be near the most probable value \(v_p\) .
FIGURE Ch6-F9: Fig. 6–9.The distribution of velocities of the molecules in a gas.
We often think of the curve of Fig.6–9in a somewhat different way. If we consider the molecules in a typical container (with a volume of, say, one liter), then there are a very large number \(N\) of molecules present ( \(N\approx10^{22}\) ). Since \(p(v)\,\Delta v\) is the probability thatonemolecule will have its velocity in \(\Delta v\) , by our definition of probability we mean that theexpectednumber \(\expval{\Delta N}\) to be found with a velocity in the interval \(\Delta v\) is given by
\[
\begin{equation}
\label{Eq:I:6:21}
\expval{\Delta N}=N\,p(v)\,\Delta v.
\end{equation}
\]
We call \(N\,p(v)\) the “distribution in velocity.” The area under the curve between two velocities \(v_1\) and \(v_2\) , for example the shaded area in Fig.6–9, represents [for the curve \(N\,p(v)\) ] the expected number of molecules with velocities between \(v_1\) and \(v_2\) . Since with a gas we are usually dealing with large numbers of molecules, we expect the deviations from the expected numbers to be small (like \(1/\sqrt{N}\) ), so we often neglect to say the “expected” number, and say instead: “The number of molecules with velocities between \(v_1\) and \(v_2\) isthe area under the curve.” We should remember, however, that such statements are always aboutprobablenumbers.
