## 7–4 Colloidal particles in an electrolyte

We turn to another phenomenon in which the locations of charges are governed by a potential that arises in part from the same charges. The resulting effects influence in an important way the behavior of colloids. A colloid consists of a suspension in water of small charged particles which, though microscopic, from an atomic point of view are still very large. If the colloidal particles were not charged, they would tend to coagulate into large lumps; but because of their charge, they repel each other and remain in suspension.

Now if there is also some salt dissolved in the water, it will be dissociated into positive and negative ions. (Such a solution of ions is called an electrolyte.) The negative ions are attracted to the colloid particles (assuming their charge is positive) and the positive ions are repelled. We will determine how the ions which surround such a colloidal particle are distributed in space.

To keep the ideas simple, we will again solve only a one-dimensional case. If we think of a colloidal particle as a sphere having a very large radius—on an atomic scale!—we can then treat a small part of its surface as a plane. (Whenever one is trying to understand a new phenomenon it is a good idea to take a somewhat oversimplified model; then, having understood the problem with that model, one is better able to proceed to tackle the more exact calculation.)

We suppose that the distribution of ions generates a charge density \rho(x) , and an electrical potential \phi , related by the electrostatic law \nabla^2\phi=-\rho/\epsilon_0 or, for fields that vary in only one dimension, by

\frac{d^2\phi}{dx^2}=-\frac{\rho}{\epsilon_0}. (7.28)

Now supposing there were such a potential \phi(x) , how would the ions distribute themselves in it? This we can determine by the principles of statistical mechanics. Our problem then is to determine \phi so that the resulting charge density from statistical mechanics also satisfies ( 7.28).

According to statistical mechanics (see Chapter 40, Vol. I), particles in thermal equilibrium in a force field are distributed in such a way that the density n of particles at the position x is given by

n(x)=n_0e^{-U(x)/kT}, (7.29)

where U(x) is the potential energy, k is Boltzmann’s constant, and T is the absolute temperature.

We assume that the ions carry one electronic charge, positive or negative. At the distance x from the surface of a colloidal particle, a positive ion will have potential energy q_e\phi(x) , so that

U(x)=q_e\phi(x).

The density of positive ions, n_+ , is then

n_+(x)=n_0e^{-q_e\phi(x)/kT}.

Similarly, the density of negative ions is

n_-(x)=n_0e^{+q_e\phi(x)/kT}.

The total charge density is

\rho =q_en_+-q_en_-,

or

\rho =q_en_0(e^{-q_e\phi/kT}-e^{+q_e\phi/kT}). (7.30)

Combining this with Eq. ( 7.28), we find that the potential \phi must satisfy

\frac{d^2\phi}{dx^2}=-\frac{q_en_0}{\epsilon_0} (e^{-q_e\phi/kT}-e^{+q_e\phi/kT}). (7.31)

This equation is readily solved in general [multiply both sides by 2(d\phi/dx) , and integrate with respect to x ], but to keep the problem as simple as possible, we will consider here only the limiting case in which the potentials are small or the temperature T is high. The case where \phi is small corresponds to a dilute solution. For these cases the exponent is small, and we can approximate

e^{\pm q_e\phi/kT}=1\pm\frac{q_e\phi}{kT}. (7.32)

Equation ( 7.31) then gives

\frac{d^2\phi}{dx^2}=+\frac{2n_0q_e^2}{\epsilon_0 kT}\phi(x). (7.33)

Notice that this time the sign on the right is positive. The solutions for \phi are not oscillatory, but exponential.

The general solution of Eq. ( 7.33) is

\phi=Ae^{-x/D}+Be^{+x/D}, (7.34)

with

D^2=\frac{\epsilon_0 kT}{2n_0q_e^2}. (7.35)

The constants A and B must be determined from the conditions of the problem. In our case, B must be zero; otherwise the potential would go to infinity for large x . So we have that

\phi=Ae^{-x/D}, (7.36)

in which A is the potential at x=0 , the surface of the colloidal particle.

### Figure Ch7-F7
Caption: Fig. 7–7.The variation of the potential near the surface of a colloidal particle. DD is the Debye length.
Image: figures/Ch7-F7.svg
![Fig. 7–7.The variation of the potential near the surface of a colloidal particle. DD is the Debye length.](figures/Ch7-F7.svg)

The potential decreases by a factor 1/e each time the distance increases by D , as shown in the graph of Fig. 7–7. The number D is called the Debye length, and is a measure of the thickness of the ion sheath that surrounds a large charged particle in an electrolyte. Equation ( 7.35) says that the sheath gets thinner with increasing concentration of the ions ( n_0 ) or with decreasing temperature.

The constant A in Eq. ( 7.36) is easily obtained if we know the surface charge density \sigma on the colloid particle. We know that

E_n=E_x(0)=\frac{\sigma}{\epsilon_0}. (7.37)

But \mathbf{E} is also the gradient of -\phi :

E_x(0)=-\left.\frac{\partial \phi}{\partial x}\right|_0=+\frac{A}{D}, (7.38)

from which we get

A=\frac{\sigma D}{\epsilon_0}. (7.39)

Using this result in ( 7.36), we find (by taking x=0 ) that the potential of the colloidal particle is

\phi(0)=\frac{\sigma D}{\epsilon_0}. (7.40)

You will notice that this potential is the same as the potential difference across a condenser with a plate spacing D and a surface charge density \sigma .

We have said that the colloidal particles are kept apart by their electrical repulsion. But now we see that the field a little way from the surface of a particle is reduced by the ion sheath that collects around it. If the sheaths get thin enough, the particles have a good chance of knocking against each other. They will then stick, and the colloid will coagulate and precipitate out of the liquid. From our analysis, we understand why adding enough salt to a colloid should cause it to precipitate out. The process is called “salting out a colloid.”

Another interesting example is the effect that a salt solution has on protein molecules. A protein molecule is a long, complicated, and flexible chain of amino acids. The molecule has various charges on it, and it sometimes happens that there is a net charge, say negative, which is distributed along the chain. Because of mutual repulsion of the negative charges, the protein chain is kept stretched out. Also, if there are other similar chain molecules present in the solution, they will be kept apart by the same repulsive effects. We can, therefore, have a suspension of chain molecules in a liquid. But if we add salt to the liquid we change the properties of the suspension. As salt is added to the solution, decreasing the Debye distance, the chain molecules can approach one another, and can also coil up. If enough salt is added to the solution, the chain molecules will precipitate out of the solution. There are many chemical effects of this kind that can be understood in terms of electrical forces.
