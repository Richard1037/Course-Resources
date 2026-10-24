# 第一章 习题库（解答）

> 对应题目文件 `qs_db.md`，题号一一对应；题目按知识点顺序排列（§1.2 → §1.6）。

---

## §1.2 函数

### 1.1　答案：$[0,1)\cup(1,2]$

**解：** 各部分有意义的条件：
- $\sqrt{4-x^2}$：$4-x^2\ge0\Rightarrow x\in[-2,2]$；
- $\dfrac1{x-1}$：$x\neq1$；
- $\arcsin(x-1)$：$-1\le x-1\le1\Rightarrow x\in[0,2]$。

取交集：$[-2,2]\cap[0,2]=[0,2]$，再去掉 $x=1$，得定义域
$$
[0,1)\cup(1,2].
$$

---

### 1.2

**证：** 定义域要求 $x+\sqrt{1+x^2}>0$ 恒成立（因 $\sqrt{1+x^2}>|x|$），故定义域为 $\mathbb R$，关于原点对称。
注意到
$$
\bigl(-x+\sqrt{1+x^2}\bigr)\bigl(x+\sqrt{1+x^2}\bigr)=(1+x^2)-x^2=1,
$$
即 $-x+\sqrt{1+x^2}=\dfrac1{x+\sqrt{1+x^2}}$。于是
$$
f(-x)=\ln\!\bigl(-x+\sqrt{1+x^2}\bigr)
=\ln\frac1{x+\sqrt{1+x^2}}
=-\ln\!\bigl(x+\sqrt{1+x^2}\bigr)=-f(x).
$$
故 $f(x)$ 为奇函数。（此即反双曲正弦 $\operatorname{arsh}x$。）

---

### 1.3

**证：** 由定义
$$
\operatorname{ch}x=\frac{e^x+e^{-x}}2,\qquad \operatorname{sh}x=\frac{e^x-e^{-x}}2 .
$$
于是
$$
\operatorname{ch}^2x-\operatorname{sh}^2x
=\frac{(e^x+e^{-x})^2-(e^x-e^{-x})^2}{4}
=\frac{4}{4}=1 .
$$

---

## §1.3 数列极限

### 1.4

**证：**
$$
\left|\frac{3n+1}{2n+1}-\frac32\right|
=\left|\frac{2(3n+1)-3(2n+1)}{2(2n+1)}\right|
=\frac{1}{2(2n+1)}<\frac{1}{4n}.
$$
$\forall\varepsilon>0$，欲使上式 $<\varepsilon$，只需 $\dfrac1{4n}<\varepsilon$，即 $n>\dfrac1{4\varepsilon}$。
取 $N=\left[\dfrac1{4\varepsilon}\right]+1$，则当 $n>N$ 时恒有
$$
\left|\frac{3n+1}{2n+1}-\frac32\right|<\varepsilon .
$$
故 $\displaystyle\lim_{n\to\infty}\frac{3n+1}{2n+1}=\frac32$。

---

### 1.5　答案：$\dfrac12$

**解：** 有理化
$$
n(\sqrt{n^2+1}-n)
=\frac{n\big[(n^2+1)-n^2\big]}{\sqrt{n^2+1}+n}
=\frac{n}{\sqrt{n^2+1}+n}
=\frac{1}{\sqrt{1+\frac1{n^2}}+1}\to\frac12 .
$$

---

### 1.6　答案：$1$

**解：** 记通项第 $k$ 项为 $\dfrac1{\sqrt{n^2+k}}\ (k=1,\dots,n)$。每项满足
$$
\frac1{\sqrt{n^2+n}}\le \frac1{\sqrt{n^2+k}}\le \frac1{\sqrt{n^2+1}} .
$$
求和得
$$
\frac{n}{\sqrt{n^2+n}}\le S_n\le \frac{n}{\sqrt{n^2+1}} .
$$
两端分别为
$$
\frac{n}{\sqrt{n^2+n}}=\frac1{\sqrt{1+\frac1n}}\to1,\qquad
\frac{n}{\sqrt{n^2+1}}=\frac1{\sqrt{1+\frac1{n^2}}}\to1 .
$$
由夹逼准则，$S_n\to1$。

---

### 1.7　答案：极限为 $2$

**证：**

**（1）有界性。** $x_1=\sqrt2<2$。设 $x_n<2$，则 $x_{n+1}=\sqrt{2+x_n}<\sqrt4=2$；又 $x_{n+1}\ge\sqrt2$。故 $\sqrt2\le x_n<2$。

**（2）单调性。**
$$
x_{n+1}-x_n=\sqrt{2+x_n}-x_n .
$$
其符号由 $2+x_n-x_n^2=(2-x_n)(1+x_n)$ 决定。因 $0<x_n<2$，上式 $>0$，故 $x_{n+1}>x_n$。即 $\{x_n\}$ 单调递增且有上界 $2$，由单调有界准则，$\{x_n\}$ 收敛。

**（3）求极限。** 设 $\lim x_n=L$，对递推式两边取极限：
$$
L=\sqrt{2+L}\ \Longrightarrow\ L^2=2+L\ \Longrightarrow\ (L-2)(L+1)=0 .
$$
由 $x_n\ge\sqrt2>0$ 知 $L\ge0$，舍去 $L=-1$，得 $L=2$。

---

## §1.4 函数的极限

### 1.8

**证：** 当 $x\neq2$ 时，
$$
\frac{x^2+x-6}{x-2}=\frac{(x-2)(x+3)}{x-2}=x+3 .
$$
于是
$$
\left|\frac{x^2+x-6}{x-2}-5\right|=|(x+3)-5|=|x-2| .
$$
$\forall\varepsilon>0$，取 $\delta=\varepsilon$，则当 $0<|x-2|<\delta$ 时，恒有
$$
\left|\frac{x^2+x-6}{x-2}-5\right|<\varepsilon .
$$
故 $\displaystyle\lim_{x\to2}\frac{x^2+x-6}{x-2}=5$。

---

### 1.9　答案：D

**解析：** 由 $g(x)-\varphi(x)\to0$ 只能说明上下界“距离趋于零”，但并不能保证 $\varphi(x),g(x)$ 各自收敛。
反例：取 $\varphi(x)=g(x)=\sin x$，则 $g(x)-\varphi(x)\equiv0\to0$，取 $f(x)=\sin x$，当 $x\to\infty$ 时极限并不存在。
故 $\lim f(x)$ **不一定存在**。若额外知道 $\varphi(x),g(x)$ 趋于同一常数，则由夹逼准则可得 $f(x)$ 收敛于该常数。

---

### 1.10

**证：** 取两个都趋于 $0$ 的数列：
$$
x_n=\frac{1}{2n\pi}\to0,\qquad x_n'=\frac{1}{2n\pi+\frac\pi2}\to0 .
$$
则
$$
\cos\frac1{x_n}=\cos(2n\pi)=1\to1,\qquad
\cos\frac1{x_n'}=\cos\!\left(2n\pi+\frac\pi2\right)=0\to0 .
$$
两个子列极限不相等（$1\neq0$）。由 Heine 定理，$\displaystyle\lim_{x\to0}\cos\frac1x$ 不存在。

---

### 1.11　答案：$-2$；水平渐近线 $y=-2$

**解：** 分子分母同除以最高次 $x^2$：
$$
\frac{2x^2+5}{3x-x^2}
=\frac{2+\frac5{x^2}}{\frac3x-1}\to\frac{2}{-1}=-2 .
$$
故水平渐近线为 $y=-2$。
（一般地，$x\to\infty$ 时有理分式的极限由分子、分母最高次决定：次数相等取系数比；分子次数低则为 $0$；分子次数高则为 $\infty$。）

---

### 1.12　答案：B

**解析：**
- 取 $x_n=2n\pi$，则 $f(x_n)=2n\pi\to\infty$，故 $f$ **无界**（排除 C、D）。
- 但取 $x_n=\dfrac\pi2+n\pi$，则 $f(x_n)=0$，并不满足“$|f(x)|$ 最终大于任意给定正数”，故 $f$ **不是无穷大量**（排除 A）。

因此 $f(x)=x\cos x$ 是无界量但不是无穷大量，选 B。

---

### 1.13　答案：$1$

**解：** 有理化
$$
\frac{\sqrt{1+x}-\sqrt{1-x}}{x}
=\frac{(\sqrt{1+x}-\sqrt{1-x})(\sqrt{1+x}+\sqrt{1-x})}{x(\sqrt{1+x}+\sqrt{1-x})}
=\frac{2x}{x(\sqrt{1+x}+\sqrt{1-x})}
=\frac{2}{\sqrt{1+x}+\sqrt{1-x}}
\to \frac{2}{1+1}=1 .
$$

---

### 1.14　答案：$\dfrac12$

**解：** 当 $x\to0$ 时，$1-\cos x\sim\dfrac12 x^2$，$\sin x\sim x$，
$$
\frac{1-\cos x}{x\sin x}\sim \frac{\frac12 x^2}{x\cdot x}=\frac12 .
$$

---

### 1.15　答案：$12$

**解：** $x\to0$ 时，$\sin2x\sim2x$，$\tan3x\sim3x$，$1-\cos x\sim\dfrac12 x^2$，
$$
\frac{\sin2x\cdot\tan3x}{1-\cos x}\sim\frac{(2x)(3x)}{\frac12 x^2}=12 .
$$

---

### 1.16　答案：B

**解析：**
$$
\frac{\tan x-\sin x}{x^3}
=\frac{\tan x(1-\cos x)}{x^3}
\sim \frac{x\cdot \frac12 x^2}{x^3}=\frac12 .
$$

---

### 1.17　答案：C（四阶）

**解析：** 当 $x\to0$ 时，
$1-\cos x\sim \dfrac12 x^2$，$\ln(1+x^2)\sim x^2$，
故
$$
(1-\cos x)\ln(1+x^2)\sim \frac12 x^2\cdot x^2=\frac12 x^4,
$$
即关于 $x$ 是**四阶**无穷小。

---

### 1.18　答案：C

**解析：**
- A：$\sin2x\sim2x$；
- B：$1-\cos x\sim\dfrac12 x^2$；
- C：$\sqrt{1+x}-\sqrt{1-x}=\dfrac{2x}{\sqrt{1+x}+\sqrt{1-x}}\to\dfrac{2x}{2}=x$，与 $x$ 等价；
- D：$x-\sin x\sim\dfrac16 x^3$。

故选 C。

---

### 1.19　答案：B

**解析：** 由重要极限 $\displaystyle\lim_{x\to0}(1+x)^{1/x}=e$ 直接得 B。
A：$\to e^{-1}$；C：$\to1$；D：$\to e^2$。

---

### 1.20　答案：$e^4$

**解：**
$$
\left(\frac{x+3}{x-1}\right)^x
=\left(1+\frac{4}{x-1}\right)^x
=\left[\left(1+\frac{4}{x-1}\right)^{\frac{x-1}{4}}\right]^{\frac{4x}{x-1}} .
$$
当 $x\to\infty$ 时，括号内 $\to e$，指数 $\dfrac{4x}{x-1}\to4$，故原式 $=e^4$。

---

### 1.21　答案：$5$

**解：** 提出最大底数 $5^x$：
$$
(2^x+3^x+5^x)^{1/x}
=5\cdot\left[\left(\frac25\right)^x+\left(\frac35\right)^x+1\right]^{1/x}.
$$
括号内趋于 $1$，且 $\left(\frac25\right)^x+\left(\frac35\right)^x$ 以指数速度趋于 $0$，故括号整体的 $\frac1x$ 次方趋于 $e^{0}=1$。原式 $=5$。
（一般地，$\displaystyle\lim_{x\to+\infty}(a_1^x+\cdots+a_k^x)^{1/x}=\max\{a_i\}$。）

---

### 1.22　答案：$\dfrac32$

**解：** 拆项后分别用等价无穷小（$x\to0$）：
$$
e^{x^2}-\cos x=(e^{x^2}-1)+(1-\cos x)\sim x^2+\frac12 x^2=\frac32 x^2,
$$
分母 $x\ln(1+x)\sim x\cdot x=x^2$。故
$$
\text{原式}=\lim_{x\to0}\frac{\frac32 x^2}{x^2}=\frac32 .
$$

---

## §1.5 连续函数与间断点

### 1.23　答案：$x=1$ 为可去间断点（第一类）；$x=2$ 为无穷间断点（第二类）。

**解：**
$$
f(x)=\frac{x^2-1}{x^2-3x+2}=\frac{(x-1)(x+1)}{(x-1)(x-2)}.
$$
定义域 $x\neq1,2$。

- $x\to1$：约去 $(x-1)$，$f(x)\to\dfrac{1+1}{1-2}=-2$，极限存在但 $f(1)$ 无定义，故 $x=1$ 为**可去间断点**（第一类）。
- $x\to2$：分子 $\to3$，分母 $\to0$，故 $|f(x)|\to\infty$，$x=2$ 为**无穷间断点**（第二类）。

---

### 1.24　答案：$a=2$

**解：**
左极限 $\displaystyle f(0^-)=\lim_{x\to0^-}\frac{\sin2x}{x}=2$；
右极限及函数值 $f(0^+)=f(0)=a$。
$f$ 在 $x=0$ 连续 $\Longleftrightarrow f(0^-)=f(0^+)$，即 $a=2$。

---

### 1.25　答案：$x=0$ 为跳跃间断点（第一类）。

**解：**
- $x\to0^+$ 时 $\dfrac1x\to+\infty$，$e^{1/x}\to+\infty$，
  $$
  f(x)=\frac{e^{1/x}-1}{e^{1/x}+1}=\frac{1-e^{-1/x}}{1+e^{-1/x}}\to1 .
  $$
- $x\to0^-$ 时 $\dfrac1x\to-\infty$，$e^{1/x}\to0$，
  $$
  f(x)\to\frac{0-1}{0+1}=-1 .
  $$
左极限 $-1\neq$ 右极限 $1$，故 $x=0$ 为**跳跃间断点**（第一类）。

---

### 1.26　答案：$x=\pm1$ 均为跳跃间断点（第一类）。

**解：** $\varphi(x)=x^2-1$，代入分段函数 $f$：
$$
f[\varphi(x)]=
\begin{cases}
0,&\varphi(x)\le0\ \text{即}\ |x|\le1,\\
1,&\varphi(x)>0\ \text{即}\ |x|>1 .
\end{cases}
$$
- 在 $x=1$ 处：左极限（$x\to1^-$, $|x|<1$）$=0$，右极限（$x\to1^+$, $|x|>1$）$=1$，左右不相等 → **跳跃间断点**。
- 在 $x=-1$ 处：左极限（$x\to-1^-$, $|x|>1$）$=1$，右极限（$x\to-1^+$, $|x|<1$）$=0$，左右不相等 → **跳跃间断点**。

其余点均连续。

---

## §1.6 闭区间上连续函数的性质

### 1.27　答案：B

**解析：** 闭区间 $[a,b]$ 上连续才能保证有界、取得最值（最值定理、有界定理）。开区间不成立，例如 $f(x)=\dfrac1x$ 在 $(0,1)$ 上连续却无界、取不到最值；$f(x)=x$ 在 $(0,1)$ 上连续但既无最大值也无最小值。
A、D 是闭区间连续函数的标准定理，C 是函数极限与数列极限的关系（Heine 定理），均正确。

---

### 1.28

**证：** 令 $f(x)=x\cdot2^x-1$，它在 $[0,1]$ 上连续。
$$
f(0)=-1<0,\qquad f(1)=2-1=1>0 .
$$
由零点存在定理，存在 $\xi\in(0,1)$ 使 $f(\xi)=0$，即 $\xi\cdot2^\xi=1$。故方程在 $(0,1)$ 内至少有一个实根。

---

### 1.29

**证：** 令 $F(x)=f(x)-x$。因 $f$ 在 $[0,1]$ 上连续，故 $F$ 在 $[0,1]$ 上连续。
由 $0<f(x)<1$：
$$
F(0)=f(0)-0=f(0)>0,\qquad F(1)=f(1)-1<0 .
$$
由零点存在定理，存在 $x_0\in(0,1)$ 使 $F(x_0)=0$，即 $f(x_0)=x_0$。

---

### 1.30

**证：** $f$ 在 $[a,b]$ 上连续，故在闭子区间 $[x_1,x_n]$ 上连续，从而有最大值 $M$ 和最小值 $m$：
$$
m\le f(x_i)\le M\quad(i=1,2,\dots,n).
$$
于是
$$
m\le\frac{f(x_1)+f(x_2)+\cdots+f(x_n)}{n}\le M .
$$
由介值定理，存在 $\xi\in[x_1,x_n]\subseteq[a,b]$，使得
$$
f(\xi)=\frac{f(x_1)+f(x_2)+\cdots+f(x_n)}{n} .
$$

---

### 1.31

**证：** 令
$$
F(x)=f\!\left(x+\frac12\right)-f(x),
$$
它在 $\left[0,\tfrac12\right]$ 上连续。
$$
F(0)=f\!\left(\tfrac12\right)-f(0),\qquad
F\!\left(\tfrac12\right)=f(1)-f\!\left(\tfrac12\right)
=f(0)-f\!\left(\tfrac12\right)=-F(0).
$$

- 若 $F(0)=0$，取 $\xi=0$ 即可；
- 若 $F(0)\neq0$，则 $F(0)\cdot F(\tfrac12)=-F(0)^2<0$，由零点存在定理，存在 $\xi\in(0,\tfrac12)$ 使 $F(\xi)=0$，即
  $$
  f\!\left(\xi+\frac12\right)=f(\xi).
  $$

综上，存在 $\xi\in[0,\tfrac12]$ 使命题成立。
