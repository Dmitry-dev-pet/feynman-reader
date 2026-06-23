## 2–7 Second derivatives of vector fields

So far we have had only first derivatives. Why not second derivatives? We could have several combinations:

\begin{alignedat}{2} &(\text{a})&\quad&\mathbf{d}iv{(\boldsymbol{\nabla}{T})}\\[.5ex] &(\text{b})&&\mathbf{c}url{(\boldsymbol{\nabla}{T})}\\[.5ex] &(\text{c})&&\boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})}\\[.5ex] &(\text{d})&&\mathbf{d}iv{(\mathbf{c}url{\FLPh})}\\[.5ex] &(\text{e})&&\mathbf{c}url{(\mathbf{c}url{\FLPh})} \end{alignedat} (2.45)

You can check that these are all the possible combinations.

Let’s look first at the second one, (b). It has the same form as

\mathbf{A}\times(\mathbf{A} T)=(\mathbf{A}\times\mathbf{A})T=\FLPzero,

since \mathbf{A}\times\mathbf{A} is always zero. So we should have

\curl(\grad T)=\mathbf{c}url{(\boldsymbol{\nabla}{T})}=\FLPzero. (2.46)

We can see how this equation comes about if we go through once with the components:

\begin{aligned} [\mathbf{c}url{(\boldsymbol{\nabla}{T})}]_z&= \nabla_x(\boldsymbol{\nabla}{T})_y-\nabla_y(\boldsymbol{\nabla}{T})_x\\[1ex] &=\frac{\partial }{\partial x}\biggl(\frac{\partial T}{\partial y}\biggr)-\frac{\partial }{\partial y}\biggl(\frac{\partial T}{\partial x}\biggr), \end{aligned} (2.47)

which is zero (by Eq. ( 2.8)). It goes the same for the other components. So \mathbf{c}url{(\boldsymbol{\nabla}{T})}=\FLPzero , for any temperature distribution—in fact, for any scalar function.

Now let us take another example. Let us see whether we can find another zero. The dot product of a vector with a cross product which contains that vector is zero:

\mathbf{A}\cdot(\mathbf{A}\times\mathbf{B})=0, (2.48)

because \mathbf{A}\times\mathbf{B} is perpendicular to \mathbf{A} , and so has no components in the direction \mathbf{A} . The same combination appears in (d) of ( 2.45), so we have

\mathbf{d}iv{(\mathbf{c}url{\FLPh})}=\ndiv(\curl\FLPh)=0. (2.49)

Again, it is easy to show that it is zero by carrying through the operations with components.

Now we are going to state two mathematical theorems that we will not prove. They are very interesting and useful theorems for physicists to know.

In a physical problem we frequently find that the curl of some quantity—say of the vector field \mathbf{A} —is zero. Now we have seen (Eq. ( 2.46)) that the curl of a gradient is zero, which is easy to remember because of the way the vectors work. It could certainly be, then, that \mathbf{A} is the gradient of some quantity, because then its curl would necessarily be zero. The interesting theorem is that if the \curl\mathbf{A} is zero, then \mathbf{A} is always the gradient of something —there is some scalar field \psi (psi) such that \mathbf{A} is equal to \grad\psi . In other words, we have the

\begin{aligned} \text{Theorem:}\\[3pt] &\text{If}&\boldsymbol{\nabla}\times\mathbf{A}&=\FLPzero\\[3pt] &\text{there is a}&\psi&\\[3pt] &\text{such that}\quad&\mathbf{A}=\boldsymbol{\nabla}\psi&. \end{aligned} (2.50)

There is a similar theorem if the divergence of \mathbf{A} is zero. We have seen in Eq. ( 2.49) that the divergence of a curl of something is always zero. If you come across a vector field \FLPD for which \ndiv\FLPD is zero, then you can conclude that \FLPD is the curl of some vector field \mathbf{C} .

\begin{aligned} \text{Theorem:}\\[3pt] &\text{If}&\boldsymbol{\nabla}\cdot\FLPD&=0\\[3pt] &\text{there is a}&\mathbf{C}&\\[3pt] &\text{such that}\quad&\FLPD=\boldsymbol{\nabla}&\times\mathbf{C}. \end{aligned} (2.51)

In looking at the possible combinations of two \boldsymbol{\nabla} operators, we have found that two of them always give zero. Now we look at the ones that are not zero. Take the combination \mathbf{d}iv{(\boldsymbol{\nabla}{T})} , which was first on our list. It is not, in general, zero. We write out the components:

\boldsymbol{\nabla}{T}=\mathbf{i}\nabla_xT+\mathbf{j}\nabla_yT+\mathbf{k}\nabla_zT.

Then

\begin{aligned} \mathbf{d}iv{(\boldsymbol{\nabla}{T})}&= \nabla_x(\nabla_xT)+\nabla_y(\nabla_yT)+\nabla_z(\nabla_zT)\\[1ex] &=\frac{\partial^2T}{\partial x^2}+\frac{\partial^2T}{\partial y^2}+ \frac{\partial^2T}{\partial z^2}, \end{aligned} (2.52)

which would, in general, come out to be some number. It is a scalar field.

You see that we do not need to keep the parentheses, but can write, without any chance of confusion,

\mathbf{d}iv{(\boldsymbol{\nabla}{T})}=\mathbf{d}iv{\boldsymbol{\nabla}{T}}=(\mathbf{d}iv{\boldsymbol{\nabla}})T=\nabla^2T. (2.53)

We look at \nabla^2 as a new operator. It is a scalar operator. Because it appears often in physics, it has been given a special name—the Laplacian.

\text{Laplacian}=\nabla^2=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+ \frac{\partial^2}{\partial z^2}. (2.54)

Since the Laplacian is a scalar operator, we may operate with it on a vector—by which we mean the same operation on each component in rectangular coordinates:

\nabla^2\FLPh=(\nabla^2h_x,\nabla^2h_y,\nabla^2h_z).

Let’s look at one more possibility: \mathbf{c}url{(\mathbf{c}url{\FLPh})} , which was (e) in the list ( 2.45). Now the curl of the curl can be written differently if we use the vector equality ( 2.6):

\mathbf{A}\times(\mathbf{B}\times\mathbf{C})=\mathbf{B}(\mathbf{A}\cdot\mathbf{C})-\mathbf{C}(\mathbf{A}\cdot\mathbf{B}). (2.55)

In order to use this formula, we should replace \mathbf{A} and \mathbf{B} by the operator \boldsymbol{\nabla} and put \mathbf{C}=\FLPh . If we do that, we get

\mathbf{c}url{(\mathbf{c}url{\FLPh})}=\boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})}- \FLPh(\mathbf{d}iv{\boldsymbol{\nabla}})\ldots\text{???}

Wait a minute! Something is wrong. The first two terms are vectors all right (the operators are satisfied), but the last term doesn’t come out to anything. It’s still an operator. The trouble is that we haven’t been careful enough about keeping the order of our terms straight. If you look again at Eq. ( 2.55), however, you see that we could equally well have written it as

\mathbf{A}\times(\mathbf{B}\times\mathbf{C})= \mathbf{B}(\mathbf{A}\cdot\mathbf{C})-(\mathbf{A}\cdot\mathbf{B})\mathbf{C}. (2.56)

The order of terms looks better. Now let’s make our substitution in ( 2.56). We get

\mathbf{c}url{(\mathbf{c}url{\FLPh})}=\boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})}- (\mathbf{d}iv{\boldsymbol{\nabla}})\FLPh. (2.57)

This form looks all right. It is, in fact, correct, as you can verify by computing the components. The last term is the Laplacian, so we can equally well write

\mathbf{c}url{(\mathbf{c}url{\FLPh})}=\boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})}-\nabla^2\FLPh. (2.58)

We have had something to say about all of the combinations in our list of double \boldsymbol{\nabla} 's, except for (c), \boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})} . It is a possible vector field, but there is nothing special to say about it. It’s just some vector field which may occasionally come up.

It will be convenient to have a table of our conclusions:

\begin{alignedat}{2} &(\text{a})&&\mathbf{d}iv{(\boldsymbol{\nabla}{T})}=\nabla^2T=\text{a scalar field}\\[.5ex] &(\text{b})&&\mathbf{c}url{(\boldsymbol{\nabla}{T})}=\FLPzero\\[.5ex] &(\text{c})&&\boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})}=\text{a vector field}\\[.5ex] &(\text{d})&&\mathbf{d}iv{(\mathbf{c}url{\FLPh})}=0\\[.5ex] &(\text{e})&&\mathbf{c}url{(\mathbf{c}url{\FLPh})}= \boldsymbol{\nabla}{(\mathbf{d}iv{\FLPh})}-\nabla^2\FLPh\\[.5ex] &(\text{f})&\quad(&\mathbf{d}iv{\boldsymbol{\nabla}})\FLPh=\nabla^2\FLPh=\text{a vector field} \end{alignedat} (2.59)

You may notice that we haven’t tried to invent a new vector operator (\mathbf{c}url{\boldsymbol{\nabla}}) . Do you see why?
