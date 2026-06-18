SOURCE: Feynman Lectures on Physics, Volume I, Chapter 8
LANGUAGE: en
TITLE: Chapter 8. Motion
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_08.html
NOTEBOOKLM_USE: clean lecture text with TeX math and figure captions; reader navigation removed.

# Chapter 8. Motion

## 8–1 Description of motion

In order to find the laws governing the various changes that take place in bodies as time goes on, we must be able todescribethe changes and have some way to record them. The simplest change to observe in a body is the apparent change in its position with time, which we call motion. Let us consider some solid object with a permanent mark, which we shall call a point, that we can observe. We shall discuss the motion of the little marker, which might be the radiator cap of an automobile or the center of a falling ball, and shall try to describe the fact that it moves and how it moves.

These examples may sound trivial, but many subtleties enter into the description of change. Some changes are more difficult to describe than the motion of a point on a solid object, for example the speed of drift of a cloud that is drifting very slowly, but rapidly forming or evaporating, or the change of a woman’s mind. We do not know a simple way to analyze a change of mind, but since the cloud can be represented or described by many molecules, perhaps we can describe the motion of the cloud in principle by describing the motion of all its individual molecules. Likewise, perhaps even the changes in the mind may have a parallel in changes of the atoms inside the brain, but we have no such knowledge yet.

At any rate, that is why we begin with the motion of points; perhaps we should think of them as atoms, but it is probably better to be more rough in the beginning and simply to think of some kind of small objects—small, that is, compared with the distance moved. For instance, in describing the motion of a car that is going a hundred miles, we do not have to distinguish between the front and the back of the car. To be sure, there are slight differences, but for rough purposes we say “the car,” and likewise it does not matter that our points are not absolute points; for our present purposes it is not necessary to be extremely precise. Also, while we take a first look at this subject we are going to forget about the three dimensions of the world. We shall just concentrate on moving in one direction, as in a car on one road. We shall return to three dimensions after we see how to describe motion in one dimension. Now, you may say, “This is all some kind of trivia,” and indeed it is. How can we describe such a one-dimensional motion—let us say, of a car? Nothing could be simpler. Among many possible ways, one would be the following. To determine the position of the car at different times, we measure its distance from the starting point and record all the observations. In Table8–1, \(s\) represents the distance of the car, in feet, from the starting point, and \(t\) represents the time in minutes. The first line in the table represents zero distance and zero time—the car has not started yet. After one minute it has started and has gone \(1200\) feet. Then in two minutes, it goes farther—notice that it picked up more distance in the second minute—it has accelerated; but something happened between \(3\) and \(4\) and even more so at \(5\) —it stopped at a light perhaps? Then it speeds up again and goes \(13{,}000\) feet by the end of \(6\) minutes, \(18{,}000\) feet at the end of \(7\) minutes, and \(23{,}500\) feet in \(8\) minutes; at \(9\) minutes it has advanced to only \(24{,}000\) feet, because in the last minute it was stopped by a cop.

### Table Ch8-T1

Caption: Table 8–1

- \(t\) (min) | \(s\) (ft)
- \(0\) | \(\phantom{0000}0\)
- \(1\) | \(\phantom{0}1200\)
- \(2\) | \(\phantom{0}4000\)
- \(3\) | \(\phantom{0}9000\)
- \(4\) | \(\phantom{0}9500\)
- \(5\) | \(\phantom{0}9600\)
- \(6\) | \(13000\)
- \(7\) | \(18000\)
- \(8\) | \(23500\)
- \(9\) | \(24000\)


### Figure Ch8-F1
Caption: Fig. 8–1.Graph of distance versus time for the car.
Image: figures/Ch8-F1.svg
![Fig. 8–1.Graph of distance versus time for the car.](figures/Ch8-F1.svg)


That is one way to describe the motion. Another way is by means of a graph. If we plot the time horizontally and the distance vertically, we obtain a curve something like that shown in Fig.8–1. As the time increases, the distance increases, at first very slowly and then more rapidly, and very slowly again for a little while at \(4\) minutes; then it increases again for a few minutes and finally, at \(9\) minutes, appears to have stopped increasing. These observations can be made from the graph, without a table. Obviously, for a complete description one would have to know where the car is at the half-minute marks, too, but we suppose that the graph means something, that the car has some position at all the intermediate times.

### Table Ch8-T2

Caption: Table 8–2

- \(t\) (sec) | \(s\) (ft)
- \(0\) | \(\phantom{00}0\)
- \(1\) | \(\phantom{0}16\)
- \(2\) | \(\phantom{0}64\)
- \(3\) | \(144\)
- \(4\) | \(256\)
- \(5\) | \(400\)
- \(6\) | \(576\)


### Figure Ch8-F2
Caption: Fig. 8–2.Graph of distance versus time for a falling body.
Image: figures/Ch8-F2.svg
![Fig. 8–2.Graph of distance versus time for a falling body.](figures/Ch8-F2.svg)


The motion of a car is complicated. For another example we take something that moves in a simpler manner, following more simple laws: a falling ball. Table8–2gives the time in seconds and the distance in feet for a falling body. At zero seconds the ball starts out at zero feet, and at the end of \(1\) second it has fallen \(16\) feet. At the end of \(2\) seconds, it has fallen \(64\) feet, at the end of \(3\) seconds, \(144\) feet, and so on; if the tabulated numbers are plotted, we get the nice parabolic curve shown in Fig.8–2. The formula for this curve can be written as
\[
\begin{equation}
\label{Eq:I:8:1}
s=16t^2.
\end{equation}
\]
This formula enables us to calculate the distances at any time. You might say there ought to be a formula for the first graph too. Actually, one may write such a formula abstractly, as
\[
\begin{equation}
\label{Eq:I:8:2}
s=f(t),
\end{equation}
\]
meaning that \(s\) is some quantity depending on \(t\) or, in mathematical phraseology, \(s\) is a function of \(t\) . Since we do not know what the function is, there is no way we can write it in definite algebraic form.

We have now seen two examples of motion, adequately described with very simple ideas, no subtleties. However, therearesubtleties—several of them. In the first place, what do we mean bytimeandspace?It turns out that these deep philosophical questions have to be analyzed very carefully in physics, and this is not so easy to do. The theory of relativity shows that our ideas of space and time are not as simple as one might think at first sight. However, for our present purposes, for the accuracy that we need at first, we need not be very careful about defining things precisely. Perhaps you say, “That’s a terrible thing—I learned that in science we have to defineeverythingprecisely.” We cannot defineanythingprecisely! If we attempt to, we get into that paralysis of thought that comes to philosophers, who sit opposite each other, one saying to the other, “You don’t know what you are talking about!” The second one says, “What do you mean byknow?What do you mean bytalking?What do you mean byyou?,” and so on. In order to be able to talk constructively, we just have to agree that we are talking about roughly the same thing. You know as much about time as we need for the present, but remember that there are some subtleties that have to be discussed; we shall discuss them later.

Another subtlety involved, and already mentioned, is that it should be possible to imagine that the moving point we are observing is always located somewhere. (Of course when we are looking at it, there it is, but maybe when we look away it isn’t there.) It turns out that in the motion of atoms, that idea also is false—we cannot find a marker on an atom and watch it move. That subtlety we shall have to get around in quantum mechanics. But we are first going to learn what the problems are before introducing the complications, andthenwe shall be in a better position to make corrections, in the light of the more recent knowledge of the subject. We shall, therefore, take a simple point of view about time and space. We know what these concepts are in a rough way, and those who have driven a car know what speed means.

## 8–2 Speed

Even though we know roughly what “speed” means, there are still some rather deep subtleties; consider that the learned Greeks were never able to adequately describe problems involving velocity. The subtlety comes when we try to comprehend exactly what is meant by “speed.” The Greeks got very confused about this, and a new branch of mathematics had to be discovered beyond the geometry and algebra of the Greeks, Arabs, and Babylonians. As an illustration of the difficulty, try to solve this problem by sheer algebra: A balloon is being inflated so that the volume of the balloon is increasing at the rate of \(100\) cm³ per second; at what speed is the radius increasing when the volume is \(1000\) cm³? The Greeks were somewhat confused by such problems, being helped, of course, by some very confusing Greeks. To show that there were difficulties in reasoning about speed at the time, Zeno produced a large number of paradoxes, of which we shall mention one to illustrate his point that there are obvious difficulties in thinking about motion. “Listen,” he says, “to the following argument: Achilles runs \(10\) times as fast as a tortoise, nevertheless he can never catch the tortoise. For, suppose that they start in a race where the tortoise is \(100\) meters ahead of Achilles; then when Achilles has run the \(100\) meters to the place where the tortoise was, the tortoise has proceeded \(10\) meters, having run one-tenth as fast. Now, Achilles has to run another \(10\) meters to catch up with the tortoise, but on arriving at the end of that run, he finds that the tortoise is still \(1\) meter ahead of him; running another meter, he finds the tortoise \(10\) centimeters ahead, and so on,ad infinitum. Therefore, at any moment the tortoise is always ahead of Achilles and Achilles can never catch up with the tortoise.” What is wrong with that? It is that a finite amount of time can be divided into an infinite number of pieces, just as a length of line can be divided into an infinite number of pieces by dividing repeatedly by two. And so, although there are an infinite number of steps (in the argument) to the point at which Achilles reaches the tortoise, it doesn’t mean that there is an infinite amount oftime. We can see from this example that there are indeed some subtleties in reasoning about speed.

In order to get to the subtleties in a clearer fashion, we remind you of a joke which you surely must have heard. At the point where the lady in the car is caught by a cop, the cop comes up to her and says, “Lady, you were going \(60\) miles an hour!” She says, “That’s impossible, sir, I was travelling for only seven minutes. It is ridiculous—how can I go \(60\) miles an hour when I wasn’t going an hour?” How would you answer her if you were the cop? Of course, if you were really the cop, then no subtleties are involved; it is very simple: you say, “Tell that to the judge!” But let us suppose that we do not have that escape and we make a more honest, intellectual attack on the problem, and try to explain to this lady what we mean by the idea that she was going \(60\) miles an hour. Just whatdowe mean? We say, “What we mean, lady, is this: if you kept on going the same way as you are going now, in the next hour you would go \(60\) miles.” She could say, “Well, my foot was off the accelerator and the car was slowing down, so if I kept on going that way it would not go \(60\) miles.” Or consider the falling ball and suppose we want to know its speed at the time three seconds if the ball kept on going the way it is going. What does that mean—kept onaccelerating, going faster? No—kept on going with the samevelocity. But that is what we are trying to define! For if the ball keeps on going the way it is going, it will just keep on going the way it is going. Thus we need to define the velocity better. What has to be kept the same? The lady can also argue this way: “If I kept on going the way I’m going for one more hour, I would run into that wall at the end of the street!” It is not so easy to say what we mean.

Many physicists think that measurement is the only definition of anything. Obviously, then, we should use the instrument that measures the speed—the speedometer—and say, “Look, lady, your speedometer reads \(60\) .” So she says, “My speedometer is broken and didn’t read at all.” Does that mean the car is standing still? We believe that there is something to measure before we build the speedometer. Only then can we say, for example, “The speedometer isn’t working right,” or “the speedometer is broken.” That would be a meaningless sentence if the velocity had no meaning independent of the speedometer. So we have in our minds, obviously, an idea that is independent of the speedometer, and the speedometer is meant only to measure this idea. So let us see if we can get a better definition of the idea. We say, “Yes, of course, before you went an hour, you would hit that wall, but if you went one second, you would go \(88\) feet; lady, you were going \(88\) feet per second, and if you kept on going, the next second it would be \(88\) feet, and the wall down there is farther away than that.” She says, “Yes, but there’s no law against going \(88\) feet per second! There is only a law against going \(60\) miles an hour.” “But,” we reply, “it’s the same thing.” If itisthe same thing, it should not be necessary to go into this circumlocution about \(88\) feet per second. In fact, the falling ball could not keep going the same way even one second because it would be changing speed, and we shall have to define speed somehow.

Now we seem to be getting on the right track; it goes something like this: If the lady kept on going for another \(1/1000\) of an hour, she would go \(1/1000\) of \(60\) miles. In other words, she does not have to keep on going for the whole hour; the point is thatfor a momentshe is going at that speed. Now what that means is that if she went just a little bit more in time, the extra distance she goes would be the same as that of a car that goes at asteadyspeed of \(60\) miles an hour. Perhaps the idea of the \(88\) feet per second is right; we see how far she went in the last second, divide by \(88\) feet, and if it comes out \(1\) the speed was \(60\) miles an hour. In other words, we can find the speed in this way: We ask, how far do we go in a very short time? We divide that distance by the time, and that gives the speed. But the time should be made as short as possible, the shorter the better, because some change could take place during that time. If we take the time of a falling body as an hour, the idea is ridiculous. If we take it as a second, the result is pretty good for a car, because there is not much change in speed, but not for a falling body; so in order to get the speed more and more accurately, we should take a smaller and smaller time interval. What we should do is take amillionthof a second, find out how far the car has gone, and divide that distance by a millionth of a second. The result gives the distance per second, which is what we mean by the velocity, so we can define it that way. That is a successful answer for the lady, or rather, that is the definition that we are going to use.

The foregoing definition involves a new idea, an idea that was not available to the Greeks in a general form. That idea was to take aninfinitesimal distanceand the correspondinginfinitesimal time, form the ratio, and watch what happens to that ratio as the time that we use gets smaller and smaller and smaller. In other words, take a limit of the distance travelled divided by the time required, as the time taken gets smaller and smaller,ad infinitum. This idea was invented by Newton and by Leibniz, independently, and is the beginning of a new branch of mathematics, called thedifferential calculus. Calculus was invented in order to describe motion, and its first application was to the problem of defining what is meant by going “ \(60\) miles an hour.”

Let us try to define velocity a little better. Suppose that in a short time, \(\epsilon\) , the car or other body goes a short distance \(x\) ; then the velocity, \(v\) , is defined as
\[
\begin{equation*}
v=x/\epsilon,
\end{equation*}
\]
an approximation that becomes better and better as the \(\epsilon\) is taken smaller and smaller. If a mathematical expression is desired, we can say that the velocity equals the limit as the \(\epsilon\) is made to go smaller and smaller in the expression \(x/\epsilon\) , or
\[
\begin{equation}
\label{Eq:I:8:3}
v=\lim_{\epsilon\to0}\frac{x}{\epsilon}.
\end{equation}
\]
We cannot do the same thing with the lady in the car, because the table is incomplete. We know only where she was at intervals of one minute; we can get a rough idea that she was going \(5000\) ft/min during the \(7\) th minute, but we do not know, at exactly the moment \(7\) minutes, whether she had been speeding up and the speed was \(4900\) ft/min at the beginning of the \(6\) th minute, and is now \(5100\) ft/min, or something else, because we do not have the exact details in between. So only if the table were completed with an infinite number of entries could we really calculate the velocity from such a table. On the other hand, when we have a complete mathematical formula, as in the case of a falling body (Eq.8.1), then it is possible to calculate the velocity, because we can calculate the position at any time whatsoever.

Let us take as an example the problem of determining the velocity of the falling ball at the particular time \(5\) seconds. One way to do this is to see from Table8–2what it did in the \(5\) th second; it went \(400-256=144\) ft, so it is going \(144\) ft/sec; however, that is wrong, because the speed is changing;on the averageit is \(144\) ft/sec during this interval, but the ball is speeding up and is really going faster than \(144\) ft/sec. We want to find outexactly how fast. The technique involved in this process is the following: We know where the ball was at \(5\) sec. At \(5.1\) sec, the distance that it has gone all together is \(16(5.1)^2=416.16\) ft (see Eq.8.1). At \(5\) sec it had already fallen \(400\) ft; in the last tenth of a second it fell \(416.16-400=16.16\) ft. Since \(16.16\) ft in \(0.1\) sec is the same as \(161.6\) ft/sec, that is the speed more or less, but it is not exactly correct. Is that the speed at \(5\) , or at \(5.1\) , or halfway between at \(5.05\) sec, or whenisthat the speed? Never mind—the problem was to find the speedat \(5\) seconds, and we do not have exactly that; we have to do a better job. So, we take one-thousandth of a second more than \(5\) sec, or \(5.001\) sec, and calculate the total fall as
\[
\begin{gather*}
s=16(5.001)^2=16(25.010001)\\[.5ex]
=400.160016\text{ ft}.
\end{gather*}
\]
In the last \(0.001\) sec the ball fell \(0.160016\) ft, and if we divide this number by \(0.001\) sec we obtain the speed as \(160.016\) ft/sec. That is closer, very close, but it isstill not exact. It should now be evident what we must do to find the speed exactly. To perform the mathematics we state the problem a little more abstractly: to find the velocity at a special time, \(t_0\) , which in the original problem was \(5\) sec. Now the distance at \(t_0\) , which we call \(s_0\) , is \(16t_0^2\) , or \(400\) ft in this case. In order to find the velocity, we ask, “At the time \(t_0+(\text{a little bit})\) , or \(t_0+\epsilon\) , where is the body?” The new position is \(16(t_0+\epsilon)^2=16t_0^2+32t_0\epsilon+16\epsilon^2\) . So it is farther along than it was before, because before it was only \(16t_0^2\) . This distance we shall call \(s_0+(\text{a little bit more})\) , or \(s_0+x\) (if \(x\) is the extra bit). Now if we subtract the distance at \(t_0\) from the distance at \(t_0+\epsilon\) , we get \(x\) , the extra distance gone, as \(x=32t_0\cdot\epsilon+16\epsilon^2\) . Our first approximation to the velocity is
\[
\begin{equation}
\label{Eq:I:8:4}
v=\frac{x}{\epsilon}=32t_0+16\epsilon.
\end{equation}
\]
The true velocity is the value of this ratio, \(x/\epsilon\) , when \(\epsilon\) becomes vanishingly small. In other words, after forming the ratio, we take the limit as \(\epsilon\) gets smaller and smaller, that is, approaches \(0\) . The equation reduces to,
\[
\begin{equation*}
v\,(\text{at time $t_0$})=32t_0.
\end{equation*}
\]
In our problem, \(t_0=5\) sec, so the solution is \(v=\) \(32\times5=\) \(160\) ft/sec. A few lines above, where we took \(\epsilon\) as \(0.1\) and \(0.001\) sec successively, the value we got for \(v\) was a little more than this, but now we see that the actual velocity is precisely \(160\) ft/sec.

## 8–3 Speed as a derivative

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

### Table Ch8-T3

Caption: Table 8–3A Short Table of Derivatives \(s\) , \(u\) , \(v\) , \(w\) are arbitrary functions of \(t\) ; \(a\) , \(b\) , \(c\) , and \(n\) are arbitrary constants

- Function | Derivative
- \(s=t^n\) | \(\quad\displaystyle\ddt{s}{t}=nt^{n-1}\)
- \(s=cu\) | \(\quad\displaystyle\ddt{s}{t}=c\,\ddt{u}{t}\)
- \(s=u+v+w+\dotsb\quad\) | \(\quad\displaystyle\ddt{s}{t}=\ddt{u}{t}+\ddt{v}{t}+\ddt{w}{t}+\dotsb\)
- \(s=c\) | \(\quad\displaystyle\ddt{s}{t}=0\)
- \(s=u^av^bw^c\dotsm\) | \(\quad\displaystyle\ddt{s}{t}=s\biggl(\!\frac{a}{u}\ddt{u}{t}\!+\!
 \frac{b}{v}\ddt{v}{t}\!+\!\frac{c}{w}\ddt{w}{t}\!+\!\dotsb\!\biggr)\)


## 8–4 Distance as an integral

### Table Ch8-T4

Caption: Table 8–4Velocity of a Falling Ball

- \(t\) (sec) | \(v\) (ft/sec)
- \(0\) | \(\phantom{00}0\)
- \(1\) | \(\phantom{0}32\)
- \(2\) | \(\phantom{0}64\)
- \(3\) | \(\phantom{0}96\)
- \(4\) | \(128\)


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

## 8–5 Acceleration

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

### Figure Ch8-F3
Caption: Fig. 8–3.Description of the motion of a body in two dimensions and the computation of its velocity.
Image: figures/Ch8-F3.svg
![Fig. 8–3.Description of the motion of a body in two dimensions and the computation of its velocity.](figures/Ch8-F3.svg)


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

### Figure Ch8-F4
Caption: Fig. 8–4.The parabola described by a falling body with an initial horizontal velocity.
Image: figures/Ch8-F4.svg
![Fig. 8–4.The parabola described by a falling body with an initial horizontal velocity.](figures/Ch8-F4.svg)
