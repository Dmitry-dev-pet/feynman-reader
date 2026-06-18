SOURCE: Feynman Lectures on Physics, Volume I, Chapter 6
LANGUAGE: en
SECTION: 6–1 Chance and likelihood
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_06.html

# 6–1 Chance and likelihood

“Chance” is a word which is in common use in everyday living. The radio reports speaking of tomorrow’s weather may say: “There is a sixty percent chance of rain.” You might say: “There is a small chance that I shall live to be one hundred years old.” Scientists also use the word chance. A seismologist may be interested in the question: “What is the chance that there will be an earthquake of a certain size in Southern California next year?” A physicist might ask the question: “What is the chance that a particular geiger counter will register twenty counts in the next ten seconds?” A politician or statesman might be interested in the question: “What is the chance that there will be a nuclear war within the next ten years?” You may be interested in the chance that you will learn something from this chapter.
Bychance, we mean something like a guess. Why do we make guesses? We make guesses when we wish to make a judgment but have incomplete information or uncertain knowledge. We want to make a guess as to what things are, or what things are likely to happen. Often we wish to make a guess because we have to make a decision. For example: Shall I take my raincoat with me tomorrow? For what earth movement should I design a new building? Shall I build myself a fallout shelter? Shall I change my stand in international negotiations? Shall I go to class today?
Sometimes we make guesses because we wish, with our limited knowledge, to say as much as wecanabout some situation. Really, any generalization is in the nature of a guess. Any physical theory is a kind of guesswork. There are good guesses and there are bad guesses. The theory of probability is a system for making better guesses. The language of probability allows us to speak quantitatively about some situation which may be highly variable, but which does have some consistent average behavior.
Let us consider the flipping of a coin. If the toss—and the coin—are “honest,” we have no way of knowing what to expect for the outcome of any particular toss. Yet we would feel that in a large number of tosses there should be about equal numbers of heads and tails. We say: “The probability that a toss will land heads is \(0.5\) .”
We speak of probability only for observations that we contemplate being made in the future.By the “probability” of a particular outcome of an observation we mean our estimate for the most likely fraction of a number of repeated observations that will yield that particular outcome. If we imagine repeating an observation—such as looking at a freshly tossed coin— \(N\) times, and if we call \(N_A\) our estimateof the most likely number of our observations that will give some specified result \(A\) , say the result “heads,” then by \(P(A)\) , the probability of observing \(A\) , we mean
\[
\begin{equation}
\label{Eq:I:6:1}
P(A)=N_A/N.
\end{equation}
\]
Our definition requires several comments. First of all, we may speak of a probability of something happening only if the occurrence is a possible outcome of somerepeatableobservation. It is not clear that it would make any sense to ask: “What is the probability that there is a ghost in that house?”
You may object that no situation isexactlyrepeatable. That is right. Every different observation must at least be at a different time or place. All we can say is that the “repeated” observations should, for our intended purposes,appear to be equivalent. We should assume, at least, that each observation was made from an equivalently prepared situation, and especially with the same degree of ignorance at the start. (If we sneak a look at an opponent’s hand in a card game, our estimate of our chances of winning are different than if we do not!)
We should emphasize that \(N\) and \(N_A\) in Eq. (6.1) arenotintended to represent numbers based on actual observations. \(N_A\) is our bestestimateof whatwouldoccur in \(N\) imaginedobservations. Probability depends, therefore, on our knowledge and on our ability to make estimates. In effect, on our common sense! Fortunately, there is a certain amount of agreement in the common sense of many things, so that different people will make the same estimate. Probabilities need not, however, be “absolute” numbers. Since they depend on our ignorance, they may become different if our knowledge changes.
You may have noticed another rather “subjective” aspect of our definition of probability. We have referred to \(N_A\) as “our estimate of the most likely number …” We do not mean that we expect to observeexactly \(N_A\) , but that we expect a numbernear \(N_A\) , and that the number \(N_A\) ismore likelythan any other number in the vicinity. If we toss a coin, say, \(30\) times, we should expect that the number of heads would not be very likely to be exactly \(15\) , but rather only some number near to \(15\) , say \(12\) , \(13\) , \(14\) , \(15\) , \(16\) , or \(17\) . However, if wemustchoose, we would decide that \(15\) heads ismore likelythan any other number. We would write \(P(\text{heads})=0.5\) .
Why did we choose \(15\) as more likely than any other number? We must have argued with ourselves in the following manner: If the most likely number of heads is \(N_H\) in a total number of tosses \(N\) , then the most likely number of tails \(N_T\) is \((N-N_H)\) . (We are assuming that every toss giveseitherheadsortails, and no “other” result!) But if the coin is “honest,” there is no preference for heads or tails. Until we have some reason to think the coin (or toss) is dishonest, we must give equal likelihoods for heads and tails. So we must set \(N_T=N_H\) . It follows that \(N_T=\) \(N_H=\) \(N/2\) , or \(P(H)=\) \(P(T)=\) \(0.5\) .
We can generalize our reasoning toanysituation in which there are \(m\) different but “equivalent” (that is, equally likely) possible results of an observation. If an observation can yield \(m\) different results, and we have reason to believe that any one of them is as likely as any other, then the probability of aparticularoutcome \(A\) is \(P(A)=1/m\) .
If there are seven different-colored balls in an opaque box and we pick one out “at random” (that is, without looking), the probability of getting a ball of a particular color is \(\tfrac{1}{7}\) . The probability that a “blind draw” from a shuffled deck of \(52\) cards will show the ten of hearts is \(\tfrac{1}{52}\) . The probability of throwing a double-one with dice is \(\tfrac{1}{36}\) .
In Chapter5we described the size of a nucleus in terms of its apparent area, or “cross section.” When we did so we were really talking about probabilities. When we shoot a high-energy particle at a thin slab of material, there is some chance that it will pass right through and some chance that it will hit a nucleus. (Since the nucleus is so small that we cannotseeit, we cannot aim right at a nucleus. We must “shoot blind.”) If there are \(n\) atoms in our slab and the nucleus of each atom has a cross-sectional area \(\sigma\) , then the total area “shadowed” by the nuclei is \(n\sigma\) . In a large number \(N\) of random shots, we expect that the number of hits \(N_C\) ofsomenucleus will be in the ratio to \(N\) as the shadowed area is to the total area of the slab:
\[
\begin{equation}
\label{Eq:I:6:2}
N_C/N=n\sigma/A.
\end{equation}
\]
We may say, therefore, that theprobabilitythat any one projectile particle will suffer a collision in passing through the slab is
\[
\begin{equation}
\label{Eq:I:6:3}
P_C=\frac{n}{A}\,\sigma,
\end{equation}
\]
where \(n/A\) is the number of atoms per unit area in our slab.
