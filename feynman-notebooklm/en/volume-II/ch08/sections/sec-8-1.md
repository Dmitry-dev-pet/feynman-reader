## 8–1 The electrostatic energy of charges. A uniform sphere

In the study of mechanics, one of the most interesting and useful discoveries was the law of the conservation of energy. The expressions for the kinetic and potential energies of a mechanical system helped us to discover connections between the states of a system at two different times without having to look into the details of what was occurring in between. We wish now to consider the energy of electrostatic systems. In electricity also the principle of the conservation of energy will be useful for discovering a number of interesting things.

The law of the energy of interaction in electrostatics is very simple; we have, in fact, already discussed it. Suppose we have two charges q_1 and q_2 separated by the distance r_{12} . There is some energy in the system, because a certain amount of work was required to bring the charges together. We have already calculated the work done in bringing two charges together from a large distance. It is

\frac{q_1q_2}{4\pi\epsilon_0 r_{12}}. (8.1)

We also know, from the principle of superposition, that if we have many charges present, the total force on any charge is the sum of the forces from the others. It follows, therefore, that the total energy of a system of a number of charges is the sum of terms due to the mutual interaction of each pair of charges. If q_i and q_j are any two of the charges and r_{ij} is the distance between them (Fig. 8–1 ), the energy of that particular pair is

\frac{q_iq_j}{4\pi\epsilon_0 r_{ij}}. (8.2)

The total electrostatic energy U is the sum of the energies of all possible pairs of charges:

U=\underset{\text{all pairs}}{\sum} \frac{q_iq_j}{4\pi\epsilon_0 r_{ij}}. (8.3)

If we have a distribution of charge specified by a charge density \rho , the sum of Eq. ( 8.3) is, of course, to be replaced by an integral.

### Figure Ch8-F1
Caption: Fig. 8–1.The electrostatic energy of a system of particles is the sum of the electrostatic energy of each pair.
Image: figures/Ch8-F1.svg
![Fig. 8–1.The electrostatic energy of a system of particles is the sum of the electrostatic energy of each pair.](figures/Ch8-F1.svg)

We shall concern ourselves with two aspects of this energy. One is the application of the concept of energy to electrostatic problems; the other is the evaluation of the energy in different ways. Sometimes it is easier to compute the work done for some special case than to evaluate the sum in Eq. ( 8.3), or the corresponding integral. As an example, let us calculate the energy required to assemble a sphere of charge with a uniform charge density. The energy is just the work done in gathering the charges together from infinity.

### Figure Ch8-F2
Caption: Fig. 8–2.The energy of a uniform sphere of charge can be computed by imagining that it is assembled from successive spherical shells.
Image: figures/Ch8-F2.svg
![Fig. 8–2.The energy of a uniform sphere of charge can be computed by imagining that it is assembled from successive spherical shells.](figures/Ch8-F2.svg)

Imagine that we assemble the sphere by building up a succession of thin spherical layers of infinitesimal thickness. At each stage of the process, we gather a small amount of charge and put it in a thin layer from r to r+dr . We continue the process until we arrive at the final radius a (Fig. 8–2 ). If Q_r is the charge of the sphere when it has been built up to the radius r , the work done in bringing a charge dQ to it is

dU=\frac{Q_r\,dQ}{4\pi\epsilon_0 r}. (8.4)

If the density of charge in the sphere is \rho , the charge Q_r is

Q_r=\rho\cdot\frac{4}{3}\,\pi r^3,

and the charge dQ is

dQ=\rho\cdot4\pi r^2\,dr.

Equation ( 8.4) becomes

dU=\frac{4\pi\rho^2r^4\,dr}{3\epsilon_0}. (8.5)

The total energy required to assemble the sphere is the integral of dU from r=0 to r=a , or

U=\frac{4\pi\rho^2a^5}{15\epsilon_0}. (8.6)

Or if we wish to express the result in terms of the total charge Q of the sphere,

U=\frac{3}{5}\,\frac{Q^2}{4\pi\epsilon_0 a}. (8.7)

The energy is proportional to the square of the total charge and inversely proportional to the radius. We can also interpret Eq. ( 8.7) as saying that the average of (1/r_{ij}) for all pairs of points in the sphere is 6/5a .
