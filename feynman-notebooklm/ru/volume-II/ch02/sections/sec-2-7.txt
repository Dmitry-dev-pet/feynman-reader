SOURCE: Feynman Lectures on Physics, Volume II, Chapter 2
LANGUAGE: ru
SECTION: 2–7 Вторые производные векторных полей
SOURCE_URL: https://www.feynmanlectures.caltech.edu/II_02.html

# 2–7 Вторые производные векторных полей

Пока мы имели дело только с первыми производными. А почему не со вторыми? Из вторых производных можно составить несколько комбинаций:
\[
\begin{equation}
\begin{alignedat}{2}
&(\text{a})&\quad&\FLPdiv{(\FLPgrad{T})}\\[.5ex]
&(\text{b})&&\FLPcurl{(\FLPgrad{T})}\\[.5ex]
&(\text{c})&&\FLPgrad{(\FLPdiv{\FLPh})}\\[.5ex]
&(\text{d})&&\FLPdiv{(\FLPcurl{\FLPh})}\\[.5ex]
&(\text{e})&&\FLPcurl{(\FLPcurl{\FLPh})}
\end{alignedat}
\label{Eq:II:2:45}
\end{equation}
\]
Вы можете убедиться, что никаких иных комбинаций быть не может.
Посмотрим сперва на вторую комбинацию (б). Она имеет ту же форму, что и
\[
\begin{equation*}
\FLPA\times(\FLPA T)=(\FLPA\times\FLPA)T=\FLPzero,
\end{equation*}
\]
, потому что \(\FLPA\times\FLPA\) всегда нуль. Значит, мы должны получить
\[
\begin{equation}
\label{Eq:II:2:46}
\curl(\grad T)=\FLPcurl{(\FLPgrad{T})}=\FLPzero.
\end{equation}
\]
Можно понять, как это получается, если расписать одну из компонент:
\[
\begin{align}
[\FLPcurl{(\FLPgrad{T})}]_z&=
\nabla_x(\FLPgrad{T})_y-\nabla_y(\FLPgrad{T})_x\notag\\[1ex]
\label{Eq:II:2:47}
&=\ddp{}{x}\biggl(\ddp{T}{y}\biggr)-\ddp{}{y}\biggl(\ddp{T}{x}\biggr),
\end{align}
\]
что равно нулю [по уравнению (2.8)]. Это же верно и для других компонент. Стало быть, \(\FLPcurl{(\FLPgrad{T})}=\FLPzero\) для любого распределения температур, да и для всякой скалярной функции.
Возьмем второй пример. Посмотрим, нельзя ли получить нуль другим путем. Скалярное произведение вектора на векторное произведение, содержащее этот вектор, равно нулю
\[
\begin{equation}
\label{Eq:II:2:48}
\FLPA\cdot(\FLPA\times\FLPB)=0,
\end{equation}
\]
потому что \(\FLPA\times\FLPB\) перпендикулярно к \(\FLPA\) и не имеет тем самым составляющих вдоль \(\FLPA\) . Сходная комбинация стоит в списке (2.45) под номером (г), так что мы имеем
\[
\begin{equation}
\label{Eq:II:2:49}
\FLPdiv{(\FLPcurl{\FLPh})}=\ndiv(\curl\FLPh)=0.
\end{equation}
\]
В справедливости этого равенства опять-таки легко убедиться, проделав выкладки на компонентах.
Теперь мы сформулируем без доказательства две математические теоремы. Они очень интересны и весьма полезны для физиков.
В физических задачах часто оказывается, что ротор какой-то величины (скажем, векторного поля \(\FLPA\) ) равен нулю. Мы видели в уравнении (2.46), что ротор градиента равен нулю. (Это легко запоминается по свойствам векторов.) Далее, может оказаться, что \(\FLPA\) будет градиентом какой-то величины, потому что тогда ротор \(\curl\FLPA\) с необходимостью обратится в нуль. Имеется интересная теорема, утверждающая, что если \(\FLPA\) есть нуль, то тогда \(\psi\) непременно окажется чьим-то градиентом; существует некоторое скалярное поле \(\FLPA\) (пси), такое, что \(\grad\psi\) равно
\[
\begin{alignat}{2}
\kern-6em\text{Theorem:}\notag\\[3pt]
&\text{If}&\FLPnabla\times\FLPA&=\FLPzero\notag\\[3pt]
&\text{there is a}&\psi&\notag\\[3pt]
\label{Eq:II:2:50}
&\text{such that}\quad&\FLPA=\FLPnabla\psi&.
\end{alignat}
\]
. Иными словами, справедлива теорема
Сходная теорема формулируется и для случая, когда дивергенция \(\FLPA\) есть нуль. Из уравнения (2.49) видно, что дивергенция ротора любой величины равна всегда нулю. Если вам случайно встретилось векторное поле \(\FLPD\) , для которого \(\ndiv\FLPD\) — нуль, то вы имеете право заключить, что \(\FLPD\) — это ротор некоторого векторного поля \(\FLPC\) .
\[
\begin{alignat}{2}
\kern-6em\text{Theorem:}\notag\\[3pt]
&\text{If}&\FLPnabla\cdot\FLPD&=0\notag\\[3pt]
&\text{there is a}&\FLPC&\notag\\[3pt]
\label{Eq:II:2:51}
&\text{such that}\quad&\FLPD=\FLPnabla&\times\FLPC.
\end{alignat}
\]
Перебирая всевозможные сочетания двух операторов \(\FLPnabla\) , мы обнаружили, что два из них всегда дают нуль. Займемся теперь теми, которые не равны нулю. Возьмем комбинацию \(\FLPdiv{(\FLPgrad{T})}\) , первую в нашем списке. В общем случае это не нуль. Выпишем компоненты:
\[
\begin{equation*}
\FLPgrad{T}=\FLPi\nabla_xT+\FLPj\nabla_yT+\FLPk\nabla_zT.
\end{equation*}
\]
Далее
\[
\begin{align}
\FLPdiv{(\FLPgrad{T})}&=
\nabla_x(\nabla_xT)+\nabla_y(\nabla_yT)+\nabla_z(\nabla_zT)\notag\\[1ex]
\label{Eq:II:2:52}
&=\frac{\partial^2T}{\partial x^2}+\frac{\partial^2T}{\partial y^2}+
\frac{\partial^2T}{\partial z^2},
\end{align}
\]
что может, вообще говоря, быть любым числом. Это скалярное поле.
Вы видите, что скобок можно не ставить, а вместо этого писать, не рискуя ошибиться:
\[
\begin{equation}
\label{Eq:II:2:53}
\FLPdiv{(\FLPgrad{T})}=\FLPdiv{\FLPgrad{T}}=(\FLPdiv{\FLPnabla})T=\nabla^2T.
\end{equation}
\]
Можно рассматривать \(\nabla^2\) как новый оператор. Это скалярный оператор. Так как он в физике встречается часто, ему дали особое имя — лапласиан.
\[
\begin{equation}
\label{Eq:II:2:54}
\text{Laplacian}=\nabla^2=\frac{\partial^2}{\partial
x^2}+\frac{\partial^2}{\partial y^2}+ \frac{\partial^2}{\partial z^2}.
\end{equation}
\]
Поскольку оператор Лапласа является скалярным оператором, мы можем применять его к вектору, подразумевая под этим выполнение той же операции над каждой компонентой в прямоугольных координатах:
\[
\begin{equation*}
\nabla^2\FLPh=(\nabla^2h_x,\nabla^2h_y,\nabla^2h_z).
\end{equation*}
\]
Рассмотрим еще одну возможность: \(\FLPcurl{(\FLPcurl{\FLPh})}\) , что было (д) в списке (2.45). Ротор от ротора можно написать иначе, если использовать векторное равенство (2.6):
\[
\begin{equation}
\label{Eq:II:2:55}
\FLPA\times(\FLPB\times\FLPC)=\FLPB(\FLPA\cdot\FLPC)-\FLPC(\FLPA\cdot\FLPB).
\end{equation}
\]
Чтобы воспользоваться этой формулой, заменим \(\FLPA\) и \(\FLPB\) оператором \(\FLPnabla\) и положим \(\FLPC=\FLPh\) . Если мы сделаем это, то получим
\[
\begin{equation*}
\FLPcurl{(\FLPcurl{\FLPh})}=\FLPgrad{(\FLPdiv{\FLPh})}-
\FLPh(\FLPdiv{\FLPnabla})\ldots\text{???}
\end{equation*}
\]
Погодите-ка! Здесь что-то не так. Как и положено, первые два члена — векторы (операторы утолили свою жажду), но последний член совсем не такой. Он все еще оператор. Ошибка в том, что мы не были осторожны и не выдержали нужного порядка членов. Вернувшись обратно, вы увидите, что (2.55) можно с равным успехом записать в виде
\[
\begin{equation}
\label{Eq:II:2:56}
\FLPA\times(\FLPB\times\FLPC)=
\FLPB(\FLPA\cdot\FLPC)-(\FLPA\cdot\FLPB)\FLPC.
\end{equation}
\]
Такой порядок членов выглядит уже лучше. Сделаем нашу подстановку в (2.56). Получится
\[
\begin{equation}
\label{Eq:II:2:57}
\FLPcurl{(\FLPcurl{\FLPh})}=\FLPgrad{(\FLPdiv{\FLPh})}-
(\FLPdiv{\FLPnabla})\FLPh.
\end{equation}
\]
С этой формулой уже все в порядке. Она действительно правильна, в чем вы можете убедиться, расписав компоненты. Последний член — это лапласиан, так что с равным успехом можно написать
\[
\begin{equation}
\label{Eq:II:2:58}
\FLPcurl{(\FLPcurl{\FLPh})}=\FLPgrad{(\FLPdiv{\FLPh})}-\nabla^2\FLPh.
\end{equation}
\]
Мы сказали всё, что можно, обо всех комбинациях в нашем списке двойных \(\FLPnabla\) , за исключением (в), \(\FLPgrad{(\FLPdiv{\FLPh})}\) . Это возможное векторное поле, но сказать о нём ничего особенного нельзя. Это просто некое векторное поле, которое может иногда встретиться в расчетах.
Удобно будет все наши рассуждения свести теперь в таблицу:
\[
\begin{equation}
\begin{alignedat}{2}
&(\text{a})&&\FLPdiv{(\FLPgrad{T})}=\nabla^2T=\text{a scalar field}\\[.5ex]
&(\text{b})&&\FLPcurl{(\FLPgrad{T})}=\FLPzero\\[.5ex]
&(\text{c})&&\FLPgrad{(\FLPdiv{\FLPh})}=\text{a vector field}\\[.5ex]
&(\text{d})&&\FLPdiv{(\FLPcurl{\FLPh})}=0\\[.5ex]
&(\text{e})&&\FLPcurl{(\FLPcurl{\FLPh})}=
\FLPgrad{(\FLPdiv{\FLPh})}-\nabla^2\FLPh\\[.5ex]
&(\text{f})&\quad(&\FLPdiv{\FLPnabla})\FLPh=\nabla^2\FLPh=\text{a
vector field}
\end{alignedat}
\label{Eq:II:2:59}
\end{equation}
\]
Вы могли заметить, что мы не пытались изобрести новый векторный оператор \((\FLPcurl{\FLPnabla})\) . Понимаете, почему?
