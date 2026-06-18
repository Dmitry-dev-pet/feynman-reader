SOURCE: Feynman Lectures on Physics, Volume I, Chapter 9
LANGUAGE: en
SECTION: 9–5 Meaning of the dynamical equations
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_09.html

# 9–5 Meaning of the dynamical equations

Now let us try to analyze just what Eq. (9.12) means. Suppose that at a given time \(t\) the object has a certain velocity \(v_x\) and position \(x\) . What is the velocity and what is the position at a slightly later time \(t+\epsilon\) ? If we can answer this question our problem is solved, for then we can start with the given condition and compute how it changes for the first instant, the next instant, the next instant, and so on, and in this way we gradually evolve the motion. To be specific, let us suppose that at the time \(t=0\) we are given that \(x=1\) and \(v_x=0\) . Why does the object move at all? Because there is aforceon it when it is at any position except \(x=0\) . If \(x>0\) , that force is upward. Therefore the velocity which is zero starts to change, because of the law of motion. Once it starts to build up some velocity the object starts to move up, and so on. Now at any time \(t\) , if \(\epsilon\) is very small, we may express the position at time \(t+\epsilon\) in terms of the position at time \(t\) and the velocity at time \(t\) to a very good approximation as
\[
\begin{equation}
\label{Eq:I:9:13}
x(t+\epsilon)=x(t)+\epsilon v_x(t).
\end{equation}
\]
The smaller the \(\epsilon\) , the more accurate this expression is, but it is still usefully accurate even if \(\epsilon\) is not vanishingly small. Now what about the velocity? In order to get the velocity later, the velocity at the time \(t+\epsilon\) , we need to know how the velocity changes, theacceleration. And how are we going to find the acceleration? That is where the law of dynamics comes in. The law of dynamics tells us what the acceleration is. It says the acceleration is \(-x\) .
\[
\begin{align}
\label{Eq:I:9:14}
v_x(t+\epsilon)&=v_x(t)+\epsilon a_x(t)\\[1ex]
\label{Eq:I:9:15}
&=v_x(t)-\epsilon x(t).
\end{align}
\]
Equation (9.14) is merely kinematics; it says that a velocity changes because of the presence of acceleration. But Eq. (9.15) isdynamics, because it relates the acceleration to the force; it says that at this particular time for this particular problem, you can replace the acceleration by \(-x(t)\) . Therefore, if we know both the \(x\) and \(v\) at a given time, we know the acceleration, which tells us the new velocity, and we know the new position—this is how the machinery works. The velocity changes a little bit because of the force, and the position changes a little bit because of the velocity.
