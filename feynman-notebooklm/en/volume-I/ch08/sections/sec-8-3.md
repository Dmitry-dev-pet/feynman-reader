SOURCE: Feynman Lectures on Physics, Volume I, Chapter 8
LANGUAGE: en
SECTION: 8–3 Speed as a derivative
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_08.html

# 8–3 Speed as a derivative

The procedure we have just carried out is performed so often in mathematics that for convenience special notations have been assigned to our quantities \(\epsilon\) and \(x\) . In this notation, the \(\epsilon\) used above becomes \(\Delta t\) and \(x\) becomes \(\Delta s\) . This \(\Delta t\) means “an extra bit of \(t\) ,” and carries an implication that it can be made smaller. The prefix \(\Delta\) is not a multiplier, any more than \(\sin\theta\) means \(\text{s}\cdot\text{i}\cdot\text{n}\cdot\theta\) —it simply defines a time increment, and reminds us of its special character. \(\Delta s\) has an analogous meaning for the distance \(s\) . Since \(\Delta\) is not a factor, it cannot be cancelled in the ratio \(\Delta s/\Delta t\) to give \(s/t\) , any more than the ratio \(\sin\theta/\sin2\theta\) can be reduced to \(1/2\) by cancellation. In this notation, velocity is equal to the limit of \(\Delta s/\Delta t\) when \(\Delta t\) gets smaller, or
\[
\begin{equation}
\label{Eq:I:8:5}
v=\lim_{\Delta t\to0}\frac{\Delta s}{\Delta t}.
\end{equation}
\]
This is really the same as our previous expression (8.3) with \(\epsilon\) and \(x\) , but it has the advantage of showing that something is changing, and it keeps track of what is changing.
Incidentally, to a good approximation we have another law, which says that the change in distance of a moving point is the velocity times the time interval, or \(\Delta s=v\,\Delta t\) . This statement is true only if the velocity is not changing during that time interval, and this condition is true only in the limit as \(\Delta t\) goes to \(0\) . Physicists like to write it \(ds=v\,dt\) , because by \(dt\) they mean \(\Delta t\) in circumstances in which it is very small; with this understanding, the expression is valid to a close approximation. If \(\Delta t\) is too long, the velocity might change during the interval, and the approximation would become less accurate. For a time \(dt\) , approaching zero, \(ds=v\,dt\) precisely. In this notation we can write (8.5) as
\[
\begin{equation*}
v=\lim_{\Delta t\to0}\frac{\Delta s}{\Delta t}=\ddt{s}{t}.
\end{equation*}
\]
The quantity \(ds/dt\) which we found above is called the “derivative of \(s\) with respect to \(t\) ” (this language helps to keep track of what was changed), and the complicated process of finding it is called finding a derivative, or differentiating. The \(ds\) ’s and \(dt\) ’s which appear separately are calleddifferentials. To familiarize you with the words, we say we found the derivative of the function \(16t^2\) , or the derivative (with respect to \(t\) ) of \(16t^2\) is \(32t\) . When we get used to the words, the ideas are more easily understood. For practice, let us find the derivative of a more complicated function. We shall consider the formula \(s=At^3+Bt+C\) , which might describe the motion of a point. The letters \(A\) , \(B\) , and \(C\) represent constant numbers, as in the familiar general form of a quadratic equation. Starting from the formula for the motion, we wish to find the velocity at any time. To find the velocity in the more elegant manner, we change \(t\) to \(t+\Delta
t\) and note that \(s\) is then changed to \(s+\text{some } \Delta s\) ; then we find the \(\Delta s\) in terms of \(\Delta t\) . That is to say,
\[
\begin{align*}
s+\Delta s&=A(t+\Delta t)^3+B(t+\Delta t)+C\\[1ex]
&=At^3+Bt+C+3At^2\,\Delta t+B\,\Delta t\\[1ex]
&\phantom{= At^3~}+3At(\Delta t)^2+
A(\Delta t)^3,
\end{align*}
\]
but since
\[
\begin{equation*}
s=At^3+Bt+C,
\end{equation*}
\]
we find that
\[
\begin{equation*}
\Delta s=3At^2\,\Delta t+B\,\Delta t+3At(\Delta t)^2+A(\Delta t)^3.
\end{equation*}
\]
But we do not want \(\Delta s\) —we want \(\Delta s\) divided by \(\Delta
t\) . We divide the preceding equation by \(\Delta t\) , getting
\[
\begin{equation*}
\frac{\Delta s}{\Delta t}=3At^2+B+3At(\Delta t)+A(\Delta t)^2.
\end{equation*}
\]
As \(\Delta t\) goes toward \(0\) the limit of \(\Delta s/\Delta t\) is \(ds/dt\) and is equal to
\[
\begin{equation*}
\ddt{s}{t}=3At^2+B.
\end{equation*}
\]
This is the fundamental process of calculus, differentiating functions. The process is even more simple than it appears. Observe that when these expansions contain any term with a square or a cube or any higher power of \(\Delta t\) , such terms may be dropped at once, since they will go to \(0\) when the limit is taken. After a little practice the process gets easier because one knows what to leave out. There are many rules or formulas for differentiating various types of functions. These can be memorized, or can be found in tables. A short list is found in Table8–3.
TABLE Ch8-T3: Table 8–3A Short Table of Derivatives \(s\) , \(u\) , \(v\) , \(w\) are arbitrary functions of \(t\) ; \(a\) , \(b\) , \(c\) , and \(n\) are arbitrary constants
