SOURCE: Feynman Lectures on Physics, Volume I, Chapter 9
LANGUAGE: en
SECTION: 9–7 Planetary motions
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_09.html

# 9–7 Planetary motions

The above analysis is very nice for the motion of an oscillating spring, but can we analyze the motion of a planet around the sun? Let us see whether we can arrive at an approximation to an ellipse for the orbit. We shall suppose that the sun is infinitely heavy, in the sense that we shall not include its motion. Suppose a planet starts at a certain place and is moving with a certain velocity; it goes around the sun in some curve, and we shall try to analyze, by Newton’s laws of motion and his law of gravitation, what the curve is. How? At a given moment it is at some position in space. If the radial distance from the sun to this position is called \(r\) , then we know that there is a force directed inward which, according to the law of gravity, is equal to a constant times the product of the sun’s mass and the planet’s mass divided by the square of the distance. To analyze this further we must find out what acceleration will be produced by this force. We shall need thecomponentsof the acceleration along two directions, which we call \(x\) and \(y\) . Thus if we specify the position of the planet at a given moment by giving \(x\) and \(y\) (we shall suppose that \(z\) is always zero because there is no force in the \(z\) -direction and, if there is no initial velocity \(v_z\) , there will be nothing to make \(z\) other than zero), the force is directed along the line joining the planet to the sun, as shown in Fig.9–5.
FIGURE Ch9-F5: Fig. 9–5.The force of gravity on a planet.
From this figure we see that the horizontal component of the force is related to the complete force in the same manner as the horizontal distance \(x\) is to the complete hypotenuse \(r\) , because the two triangles are similar. Also, if \(x\) is positive, \(F_x\) is negative. That is, \(F_x/\abs{F}=-x/r\) , or \(F_x=\) \(-\abs{F}x/r=\) \(-GMmx/r^3\) . Now we use the dynamical law to find that this force component is equal to the mass of the planet times the rate of change of its velocity in the \(x\) -direction. Thus we find the following laws:
\[
\begin{equation}
\begin{aligned}
m(dv_x/dt)&=-GMmx/r^3,\\
m(dv_y/dt)&=-GMmy/r^3,\\
r&=\sqrt{x^2+y^2}.
\end{aligned}
\label{Eq:I:9:17}
\end{equation}
\]
This, then, is the set of equations we must solve. Again, in order to simplify the numerical work, we shall suppose that the unit of time, or the mass of the sun, has been so adjusted (or luck is with us) that \(GM\equiv1\) . For our specific example we shall suppose that the initial position of the planet is at \(x=0.500\) and \(y=0.000\) , and that the velocity is all in the \(y\) -direction at the start, and is of magnitude \(1.630\) . Now how do we make the calculation? We again make a table with columns for the time, the \(x\) -position, the \(x\) -velocity \(v_x\) , and the \(x\) -acceleration \(a_x\) ; then, separated by a double line, three columns for position, velocity, and acceleration in the \(y\) -direction. In order to get the accelerations we are going to need Eq. (9.17); it tells us that the acceleration in the \(x\) -direction is \(-x/r^3\) , and the acceleration in the \(y\) -direction is \(-y/r^3\) , and that \(r\) is the square root of \(x^2+y^2\) . Thus, given \(x\) and \(y\) , we must do a little calculating on the side, taking the square root of the sum of the squares to find \(r\) and then, to get ready to calculate the two accelerations, it is useful also to evaluate \(1/r^3\) . This work can be done rather easily by using a table of squares, cubes, and reciprocals: then we need only multiply \(x\) by \(1/r^3\) , which we do on a slide rule.
Our calculation thus proceeds by the following steps, using time intervals \(\epsilon=0.100\) : Initial values at \(t=0\) :
\[
\begin{alignat*}{2}
x(0)&=0.500&\qquad\qquad y(0)&=\phantom{+}0.000\\[.5ex]
v_x(0)&=0.000&\qquad\qquad v_y(0)&=+1.630
\end{alignat*}
\]
From these we find:
\[
\begin{alignat*}{2}
r(0)&=\phantom{-}0.500&\qquad 1/r^3(0)&=8.000\\[.5ex]
a_x(0)&=-4.000&\qquad a_y(0)&=0.000
\end{alignat*}
\]
Thus we may calculate the velocities \(v_x(0.05)\) and \(v_y(0.05)\) :
\[
\begin{align*}
v_x(0.05) &= 0.000 - 4.000 \times 0.050 = -0.200;\\[1ex]
v_y(0.05) &= 1.630 + 0.000 \times 0.050 = \phantom{-}1.630.
\end{align*}
\]
Now our main calculations begin:
\[
\begin{alignat*}{2}
x(0.1)&=0.500-0.20 \times 0.1&&=\phantom{-}0.480\\[.5ex]
y(0.1)&=0.0+1.63 \times 0.1 &&=\phantom{-}0.163\\[.5ex]
r(0.1)&=\sqrt{0.480^2+0.163^2}&&=\phantom{-}0.507\\[.5ex]
1/r^3(0.1)&=7.677 &&\\[.5ex]
a_x(0.1)&=-0.480 \times 7.677 &&=-3.685\\[.5ex]
a_y(0.1)&=-0.163 \times 7.677 &&=-1.250\\[.5ex]
v_x(0.15)&=-0.200-3.685\times0.1 &&=-0.568\\[.5ex]
v_y(0.15)&=1.630-1.250\times0.1 &&=\phantom{-}1.505\\[.5ex]
x(0.2)&=0.480-0.568\times 0.1&&=\phantom{-}0.423\\[.5ex]
y(0.2)&=0.163+1.505\times0.1&&=\phantom{-}0.313\\[.5ex]
&\qquad\qquad\text{etc.}&&
\end{alignat*}
\]
In this way we obtain the values given in Table9–2, and in \(20\) steps or so we have chased the planet halfway around the sun! In Fig.9–6are plotted the \(x\) - and \(y\) -coordinates given in Table9–2. The dots represent the positions at the succession of times a tenth of a unit apart; we see that at the start the planet moves rapidly and at the end it moves slowly, and so the shape of the curve is determined. Thus we see that wereally doknow how to calculate the motion of planets!
TABLE Ch9-T2: Table 9–2Solution of \(dv_x/dt=-x/r^3\) , \(dv_y/dt=-y/r^3\) , \(r=\sqrt{x^2+y^2}\) .Interval: \(\epsilon=0.100\) Orbit \(v_y=1.63\) \(v_x=0\) \(x=0.5\) \(y=0\) at \(t=0\)
FIGURE Ch9-F6: Fig. 9–6.The calculated motion of a planet around the sun.
Now let us see how we can calculate the motion of Neptune, Jupiter, Uranus, or any other planet. If we have a great many planets, and let the sun move too, can we do the same thing? Of course we can. We calculate the force on a particular planet, let us say planet number \(i\) , which has a position \(x_i,y_i,z_i\) ( \(i=1\) may represent the sun, \(i=2\) Mercury, \(i=3\) Venus, and so on). We must know the positions of all the planets. The force acting on one is due to all the other bodies which are located, let us say, at positions \(x_j,y_j,z_j\) . Therefore the equations are
\[
\begin{align}
m_i\,\ddt{v_{ix}}{t}&=
\sum_{j=1}^N-\frac{Gm_im_j(x_i-x_j)}{r_{ij}^3},\notag\\
\label{Eq:I:9:18}
m_i\,\ddt{v_{iy}}{t}&=
\sum_{j=1}^N-\frac{Gm_im_j(
y_i-
y_j
)}{r_{ij}^3},\\
m_i\,\ddt{v_{iz}}{t}&=
\sum_{j=1}^N-\frac{Gm_im_j(
z_i-
z_j
)}{r_{ij}^3}.\notag
\end{align}
\]
Further, we define \(r_{ij}\) as the distance between the two planets \(i\) and \(j\) ; this is equal to
\[
\begin{equation}
\label{Eq:I:9:19}
r_{ij}=\sqrt{(x_i-x_j)^2+(y_i-y_j)^2+(z_i-z_j)^2}.
\end{equation}
\]
Also, \(\sum\) means a sum over all values of \(j\) —all other bodies—except, of course, for \(j=i\) . Thus all we have to do is to make more columns,lotsmore columns. We need nine columns for the motions of Jupiter, nine for the motions of Saturn, and so on. Then when we have all initial positions and velocities we can calculate all the accelerations from Eq. (9.18) by first calculating all the distances, using Eq. (9.19). How long will it take to do it? If you do it at home, it will take a very long time! But in modern times we have machines which do arithmetic very rapidly; a very good computing machine may take \(1\) microsecond, that is, a millionth of a second, to do an addition. To do a multiplication takes longer, say \(10\) microseconds. It may be that in one cycle of calculation, depending on the problem, we may have \(30\) multiplications, or something like that, so one cycle will take \(300\) microseconds. That means that we can do \(3000\) cycles of computation per second. In order to get an accuracy, of, say, one part in a billion, we would need \(4\times10^5\) cycles to correspond to one revolution of a planet around the sun. That corresponds to a computation time of \(130\) seconds or about two minutes. Thus it takes only two minutes to follow Jupiter around the sun, with all the perturbations of all the planets correct to one part in a billion, by this method! (It turns out that the error varies about as the square of the interval \(\epsilon\) . If we make the interval a thousand times smaller, it is a million times more accurate. So, let us make the interval \(10{,}000\) times smaller.)
So, as we said, we began this chapter not knowing how to calculate even the motion of a mass on a spring. Now, armed with the tremendous power of Newton’s laws, we can not only calculate such simple motions but also, given only a machine to handle the arithmetic, even the tremendously complex motions of the planets, to as high a degree of precision as we wish!
