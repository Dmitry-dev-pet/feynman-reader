SOURCE: Feynman Lectures on Physics, Volume I, Chapter 8
LANGUAGE: en
SECTION: 8–4 Distance as an integral
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_08.html

# 8–4 Distance as an integral

TABLE Ch8-T4: Table 8–4Velocity of a Falling Ball
Now we have to discuss the inverse problem. Suppose that instead of a table of distances, we have a table of speeds at different times, starting from zero. For the falling ball, such speeds and times are shown in Table8–4. A similar table could be constructed for the velocity of the car, by recording the speedometer reading every minute or half-minute. If we know how fast the car is going at any time, can we determine how far it goes? This problem is just the inverse of the one solved above; we are given the velocity and asked to find the distance. How can we find the distance if we know the speed? If the speed of the car is not constant, and the lady goes sixty miles an hour for a moment, then slows down, speeds up, and so on, how can we determine how far she has gone? That is easy. We use the same idea, and express the distance in terms of infinitesimals. Let us say, “In the first second her speed was such and such, and from the formula \(\Delta
s=v\,\Delta t\) we can calculate how far the car went the first second at that speed.” Now in the next second her speed is nearly the same, but slightly different; we can calculate how far she went in the next second by taking the new speed times the time. We proceed similarly for each second, to the end of the run. We now have a number of little distances, and the total distance will be the sum of all these little pieces. That is, the distance will be the sum of the velocities times the times, or \(s=\sum v\,\Delta t\) , where the Greek letter \(\sum\) (sigma) is used to denote addition. To be more precise, it is the sum of the velocity at a certain time, let us say the \(i\) -th time, multiplied by \(\Delta t\) .
\[
\begin{equation}
\label{Eq:I:8:6}
s=\sum_iv(t_i)\,\Delta t.
\end{equation}
\]
The rule for the times is that \(t_{i+1}=t_i+\Delta t\) . However, the distance we obtain by this method will not be correct, because the velocity changes during the time interval \(\Delta t\) . If we take the times short enough, the sum is precise, so we take them smaller and smaller until we obtain the desired accuracy. The true \(s\) is
\[
\begin{equation}
\label{Eq:I:8:7}
s=\lim_{\Delta t\to0}\sum_iv(t_i)\,\Delta t.
\end{equation}
\]
The mathematicians have invented a symbol for this limit, analogous to the symbol for the differential. The \(\Delta\) turns into a \(d\) to remind us that the time is as small as it can be; the velocity is then called \(v\) at the time \(t\) , and the addition is written as a sum with a great “ \(s\) ,” \(\int\) (from the Latinsumma), which has become distorted and is now unfortunately just called an integral sign. Thus we write
\[
\begin{equation}
\label{Eq:I:8:8}
s=\int v(t)\,dt.
\end{equation}
\]
This process of adding all these terms together is called integration, and it is the opposite process to differentiation. The derivative of this integral is \(v\) , so one operator ( \(d\) ) undoes the other ( \(\int\) ). One can get formulas for integrals by taking the formulas for derivatives and running them backwards, because they are related to each other inversely. Thus one can work out his own table of integrals by differentiating all sorts of functions. For every formula with a differential, we get an integral formula if we turn it around.
Every function can be differentiated analytically, i.e., the process can be carried out algebraically, and leads to a definite function. But it is not possible in a simple manner to write an analytical value for any integral at will. You can calculate it, for instance, by doing the above sum, and then doing it again with a finer interval \(\Delta t\) and again with a finer interval until you have it nearly right. In general, given some particular function, it is not possible to find, analytically, what the integral is. One may always try to find a function which, when differentiated, gives some desired function; but one may not find it, and it may not exist, in the sense of being expressible in terms of functions that have already been given names.
