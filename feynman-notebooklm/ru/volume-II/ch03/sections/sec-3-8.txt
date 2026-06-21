SOURCE: Feynman Lectures on Physics, Volume II, Chapter 3
LANGUAGE: ru
SECTION: 3–8 Итоги
SOURCE_URL: https://www.feynmanlectures.caltech.edu/II_03.html

# 3–8 Итоги

Подытожим теперь все, что мы узнали о векторном исчислении. Вот самые существенные моменты гл. 2 и 3: 1. Операторы \(\ddpl{}{x}\) , \(\ddpl{}{y}\) и \(\ddpl{}{z}\) можно рассматривать как три составляющие векторного оператора \(\FLPnabla\) ; формулы, следующие из векторной алгебры, остаются правильными, если этот оператор считать вектором:
\[
\begin{equation*}
\FLPnabla=\biggl(\ddp{}{x},\ddp{}{y},\ddp{}{z}\biggr).
\end{equation*}
\]
2. Разность значений скалярного поля в двух точках равна криволинейному интегралу от касательной составляющей градиента этого скаляра вдоль любой кривой, соединяющей первую точку со второй:
\[
\begin{equation}
\label{Eq:II:3:42}
\psi(2)-\psi(1)=\underset{\text{any curve}}{\int_{(1)}^{(2)}}
\FLPgrad{\psi}\cdot d\FLPs.
\end{equation}
\]
3. Поверхностный интеграл от нормальной составляющей произвольного вектора по замкнутой поверхности равен интегралу от дивергенции вектора по объему, лежащему внутри этой поверхности:
\[
\begin{equation}
\label{Eq:II:3:43}
\underset{\substack{\text{closed}\\\text{surface}}}{\int}
\FLPC\cdot\FLPn\,da=
\underset{\substack{\text{volume}\\\text{inside}}}{\int}
\FLPdiv{\FLPC}\,dV.
\end{equation}
\]
4. Криволинейный интеграл от касательной составляющей произвольного вектора по замкнутому контуру равен поверхностному интегралу от нормальной составляющей ротора этого вектора по произвольной поверхности, ограниченной этим контуром:
\[
\begin{equation}
\label{Eq:II:3:44}
\underset{\text{boundary}}{\int}
\FLPC\cdot d\FLPs=
\underset{\text{surface}}{\int}
(\FLPcurl{\FLPC})\cdot\FLPn\,da.
\end{equation}
\]
