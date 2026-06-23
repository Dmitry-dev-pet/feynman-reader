## 3–5 The circulation of a vector field

We wish now to look at the curl in somewhat the same way we looked at the divergence. We obtained Gauss’ theorem by considering the integral over a surface, although it was not obvious at the beginning that we were going to be dealing with the divergence. How did we know that we were supposed to integrate over a surface in order to get the divergence? It was not at all clear that this would be the result. And so with an apparent equal lack of justification, we shall calculate something else about a vector and show that it is related to the curl. This time we calculate what is called the circulation of a vector field. If \mathbf{C} is any vector field, we take its component along a curved line and take the integral of this component all the way around a complete loop. The integral is called the circulation of the vector field around the loop. We have already considered a line integral of \boldsymbol{\nabla}{\psi} earlier in this chapter. Now we do the same kind of thing for any vector field \mathbf{C} .

### Figure Ch3-F7
Caption: Fig. 3–7.The circulation of C\FigC around the curve Γ\Gamma is the line integral of CtC_t, the tangential component of C\FigC.
Image: figures/Ch3-F7.svg
![Fig. 3–7.The circulation of C\FigC around the curve Γ\Gamma is the line integral of CtC_t, the tangential component of C\FigC.](figures/Ch3-F7.svg)

Let \Gamma be any closed loop in space—imaginary, of course. An example is given in Fig. 3–7 . The line integral of the tangential component of \mathbf{C} around the loop is written as

\oint_\Gamma C_t\,ds=\oint_\Gamma \mathbf{C}\cdot d\mathbf{s}. (3.30)

You should note that the integral is taken all the way around, not from one point to another as we did before. The little circle on the integral sign is to remind us that the integral is to be taken all the way around. This integral is called the circulation of the vector field around the curve \Gamma . The name came originally from considering the circulation of a liquid. But the name—like flux—has been extended to apply to any field even when there is no material “circulating.”

Playing the same kind of game we did with the flux, we can show that the circulation around a loop is the sum of the circulations around two partial loops. Suppose we break up our curve of Fig. 3–7 into two loops, by joining two points (1) and (2) on the original curve by some line that cuts across as shown in Fig. 3–8 . There are now two loops, \Gamma_1 and \Gamma_2 . \Gamma_1 is made up of \Gamma_a , which is that part of the original curve to the left of (1) and (2) , plus \Gamma_{ab} , the “short cut.” \Gamma_2 is made up of the rest of the original curve plus the short cut.

### Figure Ch3-F8
Caption: Fig. 3–8.The circulation around the whole loop is the sum of the circulations around the two loops: Γ1=Γa+Γab\Gamma_1=\Gamma_a+\Gamma_{ab} and Γ2=Γb+Γab\Gamma_2=\Gamma_b+\Gamma_{ab}.
Image: figures/Ch3-F8.svg
![Fig. 3–8.The circulation around the whole loop is the sum of the circulations around the two loops: Γ1=Γa+Γab\Gamma_1=\Gamma_a+\Gamma_{ab} and Γ2=Γb+Γab\Gamma_2=\Gamma_b+\Gamma_{ab}.](figures/Ch3-F8.svg)

The circulation around \Gamma_1 is the sum of an integral along \Gamma_a and along \Gamma_{ab} . Similarly, the circulation around \Gamma_2 is the sum of two parts, one along \Gamma_b and the other along \Gamma_{ab} . The integral along \Gamma_{ab} will have, for the curve \Gamma_2 , the opposite sign from what it has for \Gamma_1 , because the direction of travel is opposite—we must take both our line integrals with the same “sense” of rotation.

Following the same kind of argument we used before, you can see that the sum of the two circulations will give just the line integral around the original curve \Gamma . The parts due to \Gamma_{ab} cancel. The circulation around the one part plus the circulation around the second part equals the circulation about the outer line. We can continue the process of cutting the original loop into any number of smaller loops. When we add the circulations of the smaller loops, there is always a cancellation of the parts on their adjacent portions, so that the sum is equivalent to the circulation around the original single loop.

### Figure Ch3-F9
Caption: Fig. 3–9.Some surface bounded by the loop Γ\Gamma is chosen. The surface is divided into a number of small areas, each approximately a square. The circulation around Γ\Gamma is the sum of the circulations around the little loops.
Image: figures/Ch3-F9.svg
![Fig. 3–9.Some surface bounded by the loop Γ\Gamma is chosen. The surface is divided into a number of small areas, each approximately a square. The circulation around Γ\Gamma is the sum of the circulations around the little loops.](figures/Ch3-F9.svg)

Now let us suppose that the original loop is the boundary of some surface. There are, of course, an infinite number of surfaces which all have the original loop as the boundary. Our results will not, however, depend on which surface we choose. First, we break our original loop into a number of small loops that all lie on the surface we have chosen, as in Fig. 3–9. No matter what the shape of the surface, if we choose our small loops small enough, we can assume that each of the small loops will enclose an area which is essentially flat. Also, we can choose our small loops so that each is very nearly a square. Now we can calculate the circulation around the big loop \Gamma by finding the circulations around all of the little squares and then taking their sum.
