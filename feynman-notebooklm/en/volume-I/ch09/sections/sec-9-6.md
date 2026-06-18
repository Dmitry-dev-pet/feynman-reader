SOURCE: Feynman Lectures on Physics, Volume I, Chapter 9
LANGUAGE: en
SECTION: 9–6 Numerical solution of the equations
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_09.html

# 9–6 Numerical solution of the equations

Now let us really solve the problem. Suppose that we take \(\epsilon=0.100\) sec. After we do all the work if we find that this is not small enough we may have to go back and do it again with \(\epsilon=0.010\) sec. Starting with our initial value \(x(0)=1.00\) , what is \(x(0.1)\) ? It is the old position \(x(0)\) plus the velocity (which is zero) times \(0.10\) sec. Thus \(x(0.1)\) is still \(1.00\) because it has not yet started to move. But the new velocity at \(0.10\) sec will be the old velocity \(v(0)=0\) plus \(\epsilon\) times the acceleration. The acceleration is \(-x(0)=-1.00\) . Thus
\[
\begin{equation*}
v(0.1) =0.00-0.10\times1.00=-0.10.
\end{equation*}
\]
Now at \(0.20\) sec
\[
\begin{align*}
x(0.2) &=x(0.1)+\epsilon v(0.1)\\[1ex]
&=1.00-0.10\times0.10=0.99
\end{align*}
\]
and
\[
\begin{align*}
v(0.2) &=v(0.1)+\epsilon a(0.1)\\[1ex]
&=-0.10-0.10\times1.00=-0.20.
\end{align*}
\]
And so, on and on and on, we can calculate the rest of the motion, and that is just what we shall do. However, for practical purposes there are some little tricks by which we can increase the accuracy. If we continued this calculation as we have started it, we would find the motion only rather crudely because \(\epsilon=0.100\) sec is rather crude, and we would have to go to a very small interval, say \(\epsilon=0.01\) . Then to go through a reasonable total time interval would take a lot of cycles of computation. So we shall organize the work in a way that will increase the precision of our calculations, using the same coarse interval \(\epsilon=0.10\) sec. This can be done if we make a subtle improvement in the technique of the analysis.
Notice that the new position is the old position plus the time interval \(\epsilon\) times the velocity. But the velocitywhen?The velocity at the beginning of the time interval is one velocity and the velocity at the end of the time interval is another velocity. Our improvement is to use the velocityhalfway between. If we know the speed now, but the speed is changing, then we are not going to get the right answer by going at the same speed as now. We should use some speed between the “now” speed and the “then” speed at the end of the interval. The same considerations also apply to the velocity: to compute the velocity changes, we should use the acceleration midway between the two times at which the velocity is to be found. Thus the equations that we shall actually use will be something like this: the position later is equal to the position before plus \(\epsilon\) times the velocityat the time in the middle of the interval. Similarly, the velocity at this halfway point is the velocity at a time \(\epsilon\) before (which is in the middle of the previous interval) plus \(\epsilon\) times the acceleration at the time \(t\) . That is, we use the equations
\[
\begin{equation}
\begin{aligned}
x(t+\epsilon)&=x(t)+\epsilon v(t+\epsilon/2),\\
v(t+\epsilon/2)&=v(t-\epsilon/2)+\epsilon a(t),\\
a(t)&=-x(t).
\end{aligned}
\label{Eq:I:9:16}
\end{equation}
\]
There remains only one slight problem: what is \(v(\epsilon/2)\) ? At the start, we are given \(v(0)\) , not \(v(-\epsilon/2)\) . To get our calculation started, we shall use a special equation, namely, \(v(\epsilon/2)=v(0)+(\epsilon/2)a(0)\) .
TABLE Ch9-T1: Table 9–1Solution of \(dv_x/dt=-x\) Interval: \(\epsilon=0.10\) sec
Now we are ready to carry through our calculation. For convenience, we may arrange the work in the form of a table, with columns for the time, the position, the velocity, and the acceleration, and the in-between lines for the velocity, as shown in Table9–1. Such a table is, of course, just a convenient way of representing the numerical values obtained from the set of equations (9.16), and in fact the equations themselves need never be written. We just fill in the various spaces in the table one by one. This table now gives us a very good idea of the motion: it starts from rest, first picks up a little upward (negative) velocity and it loses some of its distance. The acceleration is then a little bit less but it is still gaining speed. But as it goes on it gains speed more and more slowly, until as it passes \(x=0\) at about \(t=1.50\) sec we can confidently predict that it will keep going, but now it will be on the other side; the position \(x\) will become negative, the acceleration therefore positive. Thus the speed decreases. It is interesting to compare these numbers with the function \(x=\cos t\) , which is done in Fig.9–4. The agreement is within the three significant figure accuracy of our calculation! We shall see later that \(x=\cos t\) is the exact mathematical solution of our equation of motion, but it is an impressive illustration of the power of numerical analysis that such an easy calculation should give such precise results.
FIGURE Ch9-F4: Fig. 9–4.Graph of the motion of a mass on a spring.
