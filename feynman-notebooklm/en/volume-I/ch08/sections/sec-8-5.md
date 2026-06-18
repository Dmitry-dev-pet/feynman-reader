SOURCE: Feynman Lectures on Physics, Volume I, Chapter 8
LANGUAGE: en
SECTION: 8–5 Acceleration
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_08.html

# 8–5 Acceleration

The next step in developing the equations of motion is to introduce another idea which goes beyond the concept of velocity to that ofchangeof velocity, and we now ask, “How does the velocitychange?” In previous chapters we have discussed cases in which forces produce changes in velocity. You may have heard with great excitement about some car that can get from rest to \(60\) miles an hour in ten seconds flat. From such a performance we can see how fast the speed changes, but only on the average. What we shall now discuss is the next level of complexity, which is how fast the velocity is changing. In other words, by how many feet per second does the velocity change in a second, that is, how many feet per second, per second? We previously derived the formula for the velocity of a falling body as \(v=32t\) , which is charted in Table8–4, and now we want to find out how much the velocity changes per second; this quantity is called the acceleration.
Acceleration is defined as the time rate of change of velocity. From the preceding discussion we know enough already to write the acceleration as the derivative \(dv/dt\) , in the same way that the velocity is the derivative of the distance. If we now differentiate the formula \(v=32t\) we obtain, for a falling body,
\[
\begin{equation}
\label{Eq:I:8:9}
a=\ddt{v}{t}=32.
\end{equation}
\]
[To differentiate the term \(32t\) we can utilize the result obtained in a previous problem, where we found that the derivative of \(Bt\) is simply \(B\) (a constant). So by letting \(B=32\) , we have at once that the derivative of \(32t\) is \(32\) .] This means that the velocity of a falling body is changing by \(32\) feet per second, per second always. We also see from Table8–4that the velocity increases by \(32\) ft/sec in each second. This is a very simple case, for accelerations are usually not constant. The reason the acceleration is constant here is that the force on the falling body is constant, and Newton’s law says that the acceleration is proportional to the force.
As a further example, let us find the acceleration in the problem we have already solved for the velocity. Starting with
\[
\begin{equation*}
s=At^3+Bt+C
\end{equation*}
\]
we obtained, for \(v=ds/dt\) ,
\[
\begin{equation*}
v=3At^2+B.
\end{equation*}
\]
Since acceleration is the derivative of the velocity with respect to the time, we need to differentiate the last expression above. Recall the rule that the derivative of the two terms on the right equals the sum of the derivatives of the individual terms. To differentiate the first of these terms, instead of going through the fundamental process again we note that we have already differentiated a quadratic term when we differentiated \(16t^2\) , and the effect was to double the numerical coefficient and change the \(t^2\) to \(t\) ; let us assume that the same thing will happen this time, and you can check the result yourself. The derivative of \(3At^2\) will then be \(6At\) . Next we differentiate \(B\) , a constant term; but by a rule stated previously, the derivative of \(B\) is zero; hence this term contributes nothing to the acceleration. The final result, therefore, is \(a=\) \(dv/dt=\) \(6At\) .
For reference, we state two very useful formulas, which can be obtained by integration. If a body starts from rest and moves with a constant acceleration, \(g\) , its velocity \(v\) at any time \(t\) is given by
\[
\begin{equation*}
v=gt.
\end{equation*}
\]
The distance it covers in the same time is
\[
\begin{equation*}
s=\tfrac{1}{2}gt^2.
\end{equation*}
\]
Various mathematical notations are used in writing derivatives. Since velocity is \(ds/dt\) and acceleration is the time derivative of the velocity, we can also write
\[
\begin{equation}
\label{Eq:I:8:10}
a=\ddt{}{t}\biggl(\ddt{s}{t}\biggr)=\frac{d^2s}{dt^2},
\end{equation}
\]
which are common ways of writing a second derivative.
We have another law that the velocity is equal to the integral of the acceleration. This is just the opposite of \(a=dv/dt\) ; we have already seen that distance is the integral of the velocity, so distance can be found by twice integrating the acceleration.
In the foregoing discussion the motion was in only one dimension, and space permits only a brief discussion of motion in three dimensions. Consider a particle \(P\) which moves in three dimensions in any manner whatsoever. At the beginning of this chapter, we opened our discussion of the one-dimensional case of a moving car by observing the distance of the car from its starting point at various times. We then discussed velocity in terms of changes of these distances with time, and acceleration in terms of changes in velocity. We can treat three-dimensional motion analogously. It will be simpler to illustrate the motion on a two-dimensional diagram, and then extend the ideas to three dimensions. We establish a pair of axes at right angles to each other, and determine the position of the particle at any moment by measuring how far it is from each of the two axes. Thus each position is given in terms of an \(x\) -distance and a \(y\) -distance, and the motion can be described by constructing a table in which both these distances are given as functions of time. (Extension of this process to three dimensions requires only another axis, at right angles to the first two, and measuring a third distance, the \(z\) -distance. The distances are now measured from coordinateplanesinstead of lines.) Having constructed a table with \(x\) - and \(y\) -distances, how can we determine the velocity? We first find the components of velocity in each direction. The horizontal part of the velocity, or \(x\) -component, is the derivative of the \(x\) -distance with respect to the time, or
\[
\begin{equation}
\label{Eq:I:8:11}
v_x =dx/dt.
\end{equation}
\]
Similarly, the vertical part of the velocity, or \(y\) -component, is
\[
\begin{equation}
\label{Eq:I:8:12}
v_y = dy/dt.
\end{equation}
\]
In the third dimension,
\[
\begin{equation}
\label{Eq:I:8:13}
v_z = dz/dt.
\end{equation}
\]
Now, given the components of velocity, how can we find the velocity along the actual path of motion? In the two-dimensional case, consider two successive positions of the particle, separated by a short distance \(\Delta s\) and a short time interval \(t_2-t_1=\Delta t\) . In the time \(\Delta t\) the particle moves horizontally a distance \(\Delta
x\approx v_x\,\Delta t\) , and vertically a distance \(\Delta y\approx
v_y\,\Delta t\) . (The symbol “ \(\approx\) ” is read “is approximately.”) The actual distance moved is approximately
\[
\begin{equation}
\label{Eq:I:8:14}
\Delta s\approx\sqrt{(\Delta x)^2+(\Delta y)^2},
\end{equation}
\]
as shown in Fig.8–3. The approximate velocity during this interval can be obtained by dividing by \(\Delta t\) and by letting \(\Delta t\) go to \(0\) , as at the beginning of the chapter. We then get the velocity as
\[
\begin{align}
v=\ddt{s}{t}&=\sqrt{(dx/dt)^2+(dy/dt)^2}\notag\\[.5ex]
\label{Eq:I:8:15}
&=\sqrt{v_x^2+v_y^2}.
\end{align}
\]
For three dimensions the result is
\[
\begin{equation}
\label{Eq:I:8:16}
v=\sqrt{v_x^2+v_y^2+v_z^2}.
\end{equation}
\]
In the same way as we defined velocities, we can define accelerations: we have an \(x\) -component of acceleration \(a_x\) , which is the derivative of \(v_x\) , the \(x\) -component of the velocity (that is, \(a_x=d^2x/dt^2\) , the second derivative of \(x\) with respect to \(t\) ), and so on.
FIGURE Ch8-F3: Fig. 8–3.Description of the motion of a body in two dimensions and the computation of its velocity.
Let us consider one nice example of compound motion in a plane. We shall take a motion in which a ball moves horizontally with a constant velocity \(u\) , and at the same time goes vertically downward with a constant acceleration \(-g\) ; what is the motion? We can say \(dx/dt=\) \(v_x=\) \(u\) . Since the velocity \(v_x\) is constant,
\[
\begin{equation}
\label{Eq:I:8:17}
x=ut,
\end{equation}
\]
and since the downward acceleration \(-g\) is constant, the distance \(y\) the object falls can be written as
\[
\begin{equation}
\label{Eq:I:8:18}
y=-\tfrac{1}{2}gt^2.
\end{equation}
\]
What is the curve of its path, i.e., what is the relation between \(y\) and \(x\) ? We can eliminate \(t\) from Eq. (8.18), since \(t=x/u\) . When we make this substitution we find that
\[
\begin{equation}
\label{Eq:I:8:19}
y=-\frac{g}{2u^2}\,x^2.
\end{equation}
\]
This relation between \(y\) and \(x\) may be considered as the equation of the path of the moving ball. When this equation is plotted we obtain a curve that is called a parabola; any freely falling body that is shot out in any direction will travel in a parabola, as shown in Fig.8–4.
FIGURE Ch8-F4: Fig. 8–4.The parabola described by a falling body with an initial horizontal velocity.
