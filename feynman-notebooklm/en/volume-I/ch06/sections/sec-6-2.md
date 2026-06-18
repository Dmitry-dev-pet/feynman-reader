SOURCE: Feynman Lectures on Physics, Volume I, Chapter 6
LANGUAGE: en
SECTION: 6–2 Fluctuations
SOURCE_URL: https://www.feynmanlectures.caltech.edu/I_06.html

# 6–2 Fluctuations

FIGURE Ch6-F1: Fig. 6–1.Observed sequences of heads and tails in three games of 30 tosses each.
We would like now to use our ideas about probability to consider in some greater detail the question: “How many heads do I reallyexpectto get if I toss a coin \(N\) times?” Before answering the question, however, let us look at what does happen in such an “experiment.” Figure6–1shows the results obtained in the first three “runs” of such an experiment in which \(N=30\) . The sequences of “heads” and “tails” are shown just as they were obtained. The first game gave \(11\) heads; the second also \(11\) ; the third \(16\) . In three trials we did not once get \(15\) heads. Should we begin to suspect the coin? Or were we wrong in thinking that the most likely number of “heads” in such a game is \(15\) ? Ninety-seven more runs were made to obtain a total of \(100\) experiments of \(30\) tosses each. The results of the experiments are given in Table6–1.1
TABLE Ch6-T1: Table 6–1Number of heads in successive trials of 30 tosses of a coin.
Looking at the numbers in Table6–1, we see that most of the results are “near” \(15\) , in that they are between \(12\) and \(18\) . We can get a better feeling for the details of these results if we plot a graph of thedistributionof the results. We count the number of games in which a score of \(k\) was obtained, and plot this number for each \(k\) . Such a graph is shown in Fig.6–2. A score of \(15\) heads was obtained in \(13\) games. A score of \(14\) heads was also obtained \(13\) times. Scores of \(16\) and \(17\) were each obtainedmorethan \(13\) times. Are we to conclude that there is some bias toward heads? Was our “best estimate” not good enough? Should we conclude now that the “most likely” score for a run of \(30\) tosses is really \(16\) heads? But wait! In all the games taken together, there were \(3000\) tosses. And the total number of heads obtained was \(1493\) . The fraction of tosses that gave heads is \(0.498\) , very nearly, but slightlylessthan half. We should certainlynotassume that the probability of throwing heads is greater than \(0.5\) ! The fact that oneparticularset of observations gave \(16\) heads most often, is afluctuation. We still expect that themost likelynumber of heads is \(15\) .
FIGURE Ch6-F2: Fig. 6–2.Summary of the results of 100 games of 30 tosses each. The vertical bars show the number of games in which a score of \(k\) heads was obtained. The dashed curve shows the expected numbers of games with the score \(k\) obtained by a probability computation.
We may ask the question: “Whatisthe probability that a game of \(30\) tosses will yield \(15\) heads—or \(16\) , or any other number?” We have said that in a game of one toss, the probability of obtainingonehead is \(0.5\) , and the probability of obtaining no head is \(0.5\) . In a game of two tosses there arefourpossible outcomes: \(HH\) , \(HT\) , \(TH\) , \(TT\) . Since each of these sequences is equally likely, we conclude that (a) the probability of a score of two heads is \(\tfrac{1}{4}\) , (b) the probability of a score of one head is \(\tfrac{2}{4}\) , (c) the probability of a zero score is \(\tfrac{1}{4}\) . There aretwoways of obtaining one head, but only one of obtaining either zero or two heads.
Consider now a game of \(3\) tosses. The third toss is equally likely to be heads or tails. There is only one way to obtain \(3\) heads: wemusthave obtained \(2\) heads on the first two tosses, and then heads on the last. There are, however,threeways of obtaining \(2\) heads. We could throw tails after having thrown two heads (one way) or we could throw heads after throwing only one head in the first two tosses (two ways). So for scores of \(3\) - \(H\) , \(2\) - \(H\) , \(1\) - \(H\) , \(0\) - \(H\) we have that the number of equally likely ways is \(1\) , \(3\) , \(3\) , \(1\) , with a total of \(8\) different possible sequences. The probabilities are \(\tfrac{1}{8}\) , \(\tfrac{3}{8}\) , \(\tfrac{3}{8}\) , \(\tfrac{1}{8}\) .
FIGURE Ch6-F3: Fig. 6–3.A diagram for showing the number of ways a score of 0, 1, 2, or 3 heads can be obtained in a game of 3 tosses.
FIGURE Ch6-F4: Fig. 6–4.A diagram like that of Fig.6–3, for a game of 6 tosses.
The argument we have been making can be summarized by a diagram like that in Fig.6–3. It is clear how the diagram should be continued for games with a larger number of tosses. Figure6–4shows such a diagram for a game of \(6\) tosses. The number of “ways” to any point on the diagram is just the number of different “paths” (sequences of heads and tails) which can be taken from the starting point. The vertical position gives us the total number of heads thrown. The set of numbers which appears in such a diagram is known asPascal’s triangle. The numbers are also known as thebinomial coefficients, because they also appear in the expansion of \((a+b)^n\) . If we call \(n\) the number of tosses and \(k\) the number of heads thrown, then the numbers in the diagram are usually designated by the symbol \(\tbinom{n}{k}\) . We may remark in passing that the binomial coefficients can also be computed from
\[
\begin{equation}
\label{Eq:I:6:4}
\binom{n}{k}=\frac{n!}{k!(n-k)!},
\end{equation}
\]
where \(n!\) , called “ \(n\) -factorial,” represents the product \((n)(n-1)(n-2)\dotsm(3)(2)(1)\) .
We are now ready to compute the probability \(P(k,n)\) of throwing \(k\) heads in \(n\) tosses, using our definition Eq. (6.1). The total number of possible sequences is \(2^n\) (since there are \(2\) outcomes for each toss), and the number of ways of obtaining \(k\) heads is \(\tbinom{n}{k}\) , all equally likely, so we have
\[
\begin{equation}
\label{Eq:I:6:5}
P(k,n)=\frac{\tbinom{n}{k}}{2^n}.
\end{equation}
\]
Since \(P(k,n)\) is the fraction of games which we expect to yield \(k\) heads, then in \(100\) games we should expect to find \(k\) heads \(100\cdot P(k,n)\) times. The dashed curve in Fig.6–2passes through the points computed from \(100\cdot P(k,30)\) . We see that weexpectto obtain a score of \(15\) heads in \(14\) or \(15\) games, whereas this score was observed in \(13\) games. Weexpecta score of \(16\) in \(13\) or \(14\) games, but we obtained that score in \(15\) games. Such fluctuations are “part of the game.”
The method we have just used can be applied to the most general situation in which there are only two possible outcomes of a single observation. Let us designate the two outcomes by \(W\) (for “win”) and \(L\) (for “lose”). In the general case, the probability of \(W\) or \(L\) in a single event need not be equal. Let \(p\) be the probability of obtaining the result \(W\) . Then \(q\) , the probability of \(L\) , is necessarily \((1-p)\) . In a set of \(n\) trials, the probability \(P(k,n)\) that \(W\) will be obtained \(k\) times is
\[
\begin{equation}
\label{Eq:I:6:6}
P(k,n)=\tbinom{n}{k}p^kq^{n-k}.
\end{equation}
\]
This probability function is called theBernoullior, also, thebinomialprobability.
