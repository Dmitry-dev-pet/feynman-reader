SOURCE: Feynman Lectures on Physics, Volume II, Chapter 2
LANGUAGE: ru
SECTION: 2–5 Операции с \(\FLPnabla\)
SOURCE_URL: https://www.feynmanlectures.caltech.edu/II_02.html

# 2–5 Операции с \(\FLPnabla\)

Можно ли производить с векторным оператором \(\FLPnabla\) другие алгебраические действия? Попробуем скомбинировать его с вектором. Из двух векторов можно составить скалярное произведение, причем двоякого рода:
\[
\begin{equation*}
(\text{a vector})\cdot\FLPnabla,\quad\text{or}\quad\FLPdiv{(\text{a
vector})}.
\end{equation*}
\]
Первое выражение пока что ничего не означает — это все еще оператор. Окончательный смысл его зависит от того, на что он будет действовать. А второе произведение — это некое скалярное поле ( \(\FLPA\cdot\FLPB\) — всегда скаляр).
Попробуем составить скалярное произведение \(\FLPnabla\) на известное поле, скажем на \(\FLPh\) . Распишем покомпонентно:
\[
\begin{equation}
\label{Eq:II:2:32}
\FLPdiv{\FLPh}=\nabla_xh_x+\nabla_yh_y+\nabla_zh_z
\end{equation}
\]
или
\[
\begin{equation}
\label{Eq:II:2:33}
\FLPdiv{\FLPh}=\ddp{h_x}{x}+\ddp{h_y}{y}+\ddp{h_z}{z}.
\end{equation}
\]
Эта сумма инвариантна относительно преобразования координат. Если выбрать другую систему (отмеченную штрихами), то получилось бы
\[
\begin{equation}
\label{Eq:II:2:34}
\FLPnabla'\cdot\FLPh=\ddp{h_{x'}}{x'}+\ddp{h_{y'}}{y'}+\ddp{h_{z'}}{z'},
\end{equation}
\]
а это — то же самое число, которое получилось бы и из ( 2.33 ), хотя с виду оно выглядит иначе, т. е.
\[
\begin{equation}
\label{Eq:II:2:35}
\FLPnabla'\cdot\FLPh=\FLPdiv{\FLPh}
\end{equation}
\]
в любой точке пространства. Итак, \(\FLPdiv{\FLPh}\) — это скалярное поле, и оно должно представлять собой некоторую физическую величину. Вы должны понимать, что комбинация производных в \(\FLPdiv{\FLPh}\) имеет довольно специальный вид. Могут быть и другие комбинации всяческого вида, скажем \(\ddpl{h_y}{x}\) , которые не являются ни скалярами, ни компонентами векторов.
Скалярная величина \(\FLPdiv{(\text{a vector})}\) очень широко применяется в физике. Ей присвоили имя «дивергенция», или «расходимость». Например,
\[
\begin{equation}
\label{Eq:II:2:36}
\FLPdiv{\FLPh}=\ndiv\FLPh=\text{“divergence of $\FLPh$.”}
\end{equation}
\]
Можно было бы, как и для \(\FLPgrad{T}\) , описать физический смысл \(\FLPdiv{\FLPh}\) . Но мы отложим это до лучших времен.
Посмотрим теперь, что еще можно испечь из векторного оператора \(\FLPnabla\) . Как насчет векторного произведения? Можно ожидать, что
\[
\begin{equation}
\label{Eq:II:2:37}
\FLPcurl{\FLPh}=\text{a vector}.
\end{equation}
\]
Это вектор, компоненты которого мы можем написать, пользуясь обычным правилом для векторного произведения [см. (2.2)]:
\[
\begin{equation}
\label{Eq:II:2:38}
(\FLPcurl{\FLPh})_z=
\nabla_x h_y -\nabla_y h_x =\ddp{h_y}{x} -\ddp{h_x}{y}.
\end{equation}
\]
Аналогично,
\[
\begin{equation}
\label{Eq:II:2:39}
(\FLPcurl{\FLPh})_x =
\nabla_y h_z -\nabla_z h_y =\ddp{h_z}{y} -\ddp{h_y}{z}\phantom{.}
\end{equation}
\]
и
\[
\begin{equation}
\label{Eq:II:2:40}
(\FLPcurl{\FLPh})_y =
\nabla_z h_x -\nabla_x h_z =\ddp{h_x}{z} -\ddp{h_z}{x}.
\end{equation}
\]
Комбинацию \(\FLPcurl{\FLPh}\) называют «ротор» (пишут rot \(\FLPh\) ). Происхождение этого названия и физический смысл комбинации мы обсудим позже.
В итоге мы получили три сорта комбинаций, куда входит \(\FLPnabla\) :
\[
\begin{alignat*}{3}
&\FLPgrad{T}&&=\grad T\;&&=\text{a vector},\\[1ex]
&\FLPdiv{\FLPh}&&=\ndiv\FLPh&&=\text{a scalar},\\[1ex]
&\FLPcurl{\FLPh}\;&&=\curl\FLPh&&=\text{a vector}.
\end{alignat*}
\]
Используя эти комбинации, пространственные вариации полей можно записывать в удобном виде, т. е. в виде, не зависящем от той или иной совокупности осей координат.
В качестве примера применения нашего векторного дифференциального оператора \(\FLPnabla\) выпишем совокупность векторных уравнений, в которой содержатся те самые законы электромагнетизма, которые мы словесно изложили в гл. 1. Их называют уравнениями Максвелла.
\[
\begin{gather}
\notag
\textit{Maxwell’s Equations}\\[1ex]
\label{Eq:II:2:41}
\begin{alignedat}{2}
&(1)&\quad
\FLPdiv{\FLPE}\;&=\frac{\rho}{\epsO}\\[.5ex]
&(2)&\quad\FLPcurl{\FLPE}\;&=-\ddp{\FLPB}{t}\\[.5ex]
&(3)&\quad\FLPdiv{\FLPB}\;&=0\\[.5ex]
&(4)&\quad c^2\,\FLPcurl{\FLPB}\;&=\ddp{\FLPE}{t}+\frac{\FLPj}{\epsO}
\end{alignedat}
\end{gather}
\]
где \(\rho\) (ро) — «плотность электрического заряда» (количество заряда в единице объема), а \(\FLPj\) — «плотность электрического тока» (скорость протекания заряда сквозь единицу площади). Эти четыре уравнения содержат в себе законченную классическую теорию электромагнитного поля. Видите, какой элегантной и простой записи мы добились с помощью наших новых обозначений!
