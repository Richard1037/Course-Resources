# 《高等代数 I》期中练习题 · 解答与知识点

> **配套文件**：题目见 `exercise_qoder.md`（题号一一对应，共 32 题）。
>
> **依据**：期中卷 `25_fall_mid.pdf`（人大《高等代数 I》2025 秋期中，2025-11-04）＋ 课件 `la-02-slide.pdf`～`la-12-slide.pdf`（第 1 节按向量引论笔记）。
>
> **记号**：张成 $S(\boldsymbol v_1,\dots,\boldsymbol v_k)$；列空间 $C(A)$；行空间 $C(A^\top)$；零空间 $N(A)$；秩 $r(A)$；消元阵 $E_{ij}(\lambda)$（第 $j$ 元的 $\lambda$ 倍加到第 $i$ 行）；置换阵 $P_{ij}$；最简行阶梯形 $R$。
>
> 所有数值答案均已用精确有理数运算逐题验算（矩阵乘积、行列式、$R$、$A^{-1}$、全解代回原方程）。

---

# 第一部分　基础巩固（题 1–10）

## 题 1　内积、模长与两个不等式

设 $\boldsymbol u=(2,1,-2)^\top,\ \boldsymbol v=(1,1,1)^\top$。

**(1)** $\boldsymbol u\cdot\boldsymbol v=2\cdot1+1\cdot1+(-2)\cdot1=2+1-2=1$。
$$\|\boldsymbol u\|=\sqrt{4+1+4}=\sqrt9=3,\qquad \|\boldsymbol v\|=\sqrt{1+1+1}=\sqrt3 .$$
$$\cos\theta=\frac{\boldsymbol u\cdot\boldsymbol v}{\|\boldsymbol u\|\,\|\boldsymbol v\|}=\frac{1}{3\sqrt3}=\frac{\sqrt3}{9}>0 ,$$
内积为正，故夹角为**锐角**（$\theta\approx1.37$ 弧度，约 $78.6^\circ$）。

**(2)** 单位化：
$$\frac{\boldsymbol u}{\|\boldsymbol u\|}=\left(\tfrac23,\tfrac13,-\tfrac23\right)^\top,\qquad
\frac{\boldsymbol v}{\|\boldsymbol v\|}=\left(\tfrac{1}{\sqrt3},\tfrac{1}{\sqrt3},\tfrac{1}{\sqrt3}\right)^\top .$$
验算：$(2/3)^2+(1/3)^2+(2/3)^2=9/9=1$ ✓。

**(3)** 正交条件 $\langle\boldsymbol u+a\boldsymbol v,\boldsymbol v\rangle=0$，即
$$(\boldsymbol u\cdot\boldsymbol v)+a\|\boldsymbol v\|^2=1+3a=0\ \Longrightarrow\ a=-\frac13 .$$
此时 $\boldsymbol u-\tfrac13\boldsymbol v=\left(\tfrac53,\tfrac23,-\tfrac73\right)^\top$，与 $\boldsymbol v$ 的点积为 $\tfrac53+\tfrac23-\tfrac73=0$ ✓。

**(4)** 施瓦茨不等式：$|\boldsymbol u\cdot\boldsymbol v|=1\le\|\boldsymbol u\|\,\|\boldsymbol v\|=3\sqrt3\ (\approx5.20)$ ✓。
等号成立 $\iff$ 存在不全为零的 $\lambda_1,\lambda_2$ 使 $\lambda_1\boldsymbol u+\lambda_2\boldsymbol v=0$，即两向量**共线**（一个为另一个的倍数）。本题 $\boldsymbol u,\boldsymbol v$ 不共线，故为严格不等号。
三角不等式：$\boldsymbol u+\boldsymbol v=(3,2,-1)^\top$，$\|\boldsymbol u+\boldsymbol v\|=\sqrt{9+4+1}=\sqrt{14}\ (\approx3.74)\le 3+\sqrt3\ (\approx4.73)$ ✓。
代数验证：$\|\boldsymbol u+\boldsymbol v\|^2=\|\boldsymbol u\|^2+2\boldsymbol u\cdot\boldsymbol v+\|\boldsymbol v\|^2=9+2+3=14$，而 $(\|\boldsymbol u\|+\|\boldsymbol v\|)^2=12+6\sqrt3$，由 $14<12+6\sqrt3\iff2<6\sqrt3$ 成立。
等号成立 $\iff$ 其中一个是另一个的**非负**倍数（同向共线）；反向共线时施瓦茨取等号但三角不等式取严格号。

**涉及知识点**　第 1 节：点积 $\boldsymbol v\cdot\boldsymbol w=v_1w_1+\cdots+v_nw_n$、模长 $\|\boldsymbol v\|=\sqrt{\boldsymbol v\cdot\boldsymbol v}$、内积几何意义 $\langle\boldsymbol v,\boldsymbol w\rangle=\|\boldsymbol v\|\|\boldsymbol w\|\cos\theta$（余弦定理的向量形式）、正交判据 $\langle\cdot,\cdot\rangle=0$、施瓦茨不等式与三角不等式及其取等条件。

---

## 题 2　矩阵–向量乘的两种观点、差分阵与前缀和阵

设 $D=\begin{pmatrix}1&0&0\\ -1&1&0\\ 0&-1&1\end{pmatrix}$，其三列为
$$\boldsymbol d_1=\begin{pmatrix}1\\-1\\0\end{pmatrix},\quad \boldsymbol d_2=\begin{pmatrix}0\\1\\-1\end{pmatrix},\quad \boldsymbol d_3=\begin{pmatrix}0\\0\\1\end{pmatrix}.$$

**(1)** **列观点**：$Dx=x_1\boldsymbol d_1+x_2\boldsymbol d_2+x_3\boldsymbol d_3$，即 $Dx$ 是 $D$ 的列的以 $x_1,x_2,x_3$ 为系数的线性组合。
**行观点**：$b=Dx$ 的各分量是行与 $\boldsymbol x$ 的点积：
$$b_1=\text{row}_1\cdot x=x_1,\qquad b_2=-x_1+x_2,\qquad b_3=-x_2+x_3 .$$

**(2)** $b=(x_1,\ x_2-x_1,\ x_3-x_2)^\top$ 正是序列 $x_1,x_2,x_3$ 的一阶差分（首项保留），故 $D$ 称**一阶差分阵**。
$x=(1,4,9)^\top$ 时 $Dx=(1,\ 4-1,\ 9-4)^\top=(1,3,5)^\top$（$1,4,9$ 的差分是 $1,3,5$，即前三个奇数）。

**(3)** $Dx=0$ 给出 $x_1=0$，$x_2-x_1=0$，$x_3-x_2=0$，逐个回代得 $x_1=x_2=x_3=0$，故 $N(D)=\{0\}$，$D$ 有三个主元（秩 3），由课件定理 1（$n$ 阶方阵可逆 $\iff$ 有 $n$ 个主元）知 $D$ 可逆。
求逆即「由差分还原序列」——前缀和：
$$D^{-1}=\begin{pmatrix}1&0&0\\ 1&1&0\\ 1&1&1\end{pmatrix},\qquad D^{-1}b=\begin{pmatrix}b_1\\ b_1+b_2\\ b_1+b_2+b_3\end{pmatrix}.$$
验算 $D^{-1}D=\begin{pmatrix}1&0&0\\1-1&1&0\\1-1-1+1&-1+1&1\end{pmatrix}=I$（逐块：$D^{-1}$ 的第 $i$ 行为 $(1,\dots,1,0,\dots)$ 与 $\boldsymbol d_j$ 相点得 $\delta_{ij}$）✓。
取 $b=(1,1,1)^\top$：$D^{-1}b=(1,2,3)^\top$，再作用 $D$ 得 $D(1,2,3)^\top=(1,1,1)^\top=b$ ✓——差分与前缀和互逆。

**涉及知识点**　第 2 节：矩阵–向量乘的列观点（$Ax=$ 列的线性组合）与行观点（分量 = 点积）；第 6 节：特殊矩阵（一阶差分阵、前缀和阵）；第 7 节：$n$ 阶阵可逆 $\iff n$ 个主元 $\iff N(A)=\{0\}$；第 11 节：零空间维数与主元个数。

---

## 题 3　线性相关、线性无关与张成

**(1)** 以三者为列作矩阵并求行列式：
$$\det\begin{pmatrix}1&1&0\\ 1&0&1\\ 0&1&1\end{pmatrix}=1(0\cdot1-1\cdot1)-1(1\cdot1-0)+0=-1-1=-2\ne0 .$$
行列式非零 $\iff$ 三列线性无关（也 $\iff$ 有 3 个主元 $\iff$ 可逆）。故 $v_1,v_2,v_3$ **线性无关**。
它们是 $\mathbb R^3$ 中 3 个无关向量，故张成整个空间：$S(v_1,v_2,v_3)=\mathbb R^3$（任意 $(x_1,x_2,x_3)$ 都可唯一表出）。

**(2)** 设 $k_1(\alpha_1+\alpha_2)+k_2(\alpha_2+\alpha_3)+k_3(\alpha_3+\alpha_1)=0$，按 $\alpha_i$ 整理：
$$(k_1+k_3)\alpha_1+(k_1+k_2)\alpha_2+(k_2+k_3)\alpha_3=0 .$$
$\alpha_1,\alpha_2,\alpha_3$ 无关，故各系数为零：
$$\begin{cases}k_1+k_3=0\\ k_1+k_2=0\\ k_2+k_3=0\end{cases}
\quad\Longleftrightarrow\quad
\underbrace{\begin{pmatrix}1&0&1\\ 1&1&0\\ 0&1&1\end{pmatrix}}_{M}\,k=0 .$$
按第一行展开 $\det M=1\cdot\begin{vmatrix}1&0\\ 1&1\end{vmatrix}+1\cdot\begin{vmatrix}1&1\\ 0&1\end{vmatrix}=1+1=2\ne0$，故 $M$ 可逆，齐次方程只有零解 $k_1=k_2=k_3=0$，即三向量**线性无关**。

**(3)** 设 $c_1(\alpha_1+\alpha_2+\alpha_3)+c_2(\alpha_1-\alpha_2)=0$，按 $\alpha_i$ 合并得
$$(c_1+c_2)\alpha_1+(c_1-c_2)\alpha_2+c_1\alpha_3=0 .$$
由 $\alpha_1,\alpha_2,\alpha_3$ 无关：$c_1+c_2=0,\ c_1-c_2=0,\ c_1=0$，前两式相加得 $2c_1=0$，于是 $c_1=c_2=0$。故二者**线性无关**（即两个向量不成比例：$\alpha_1+\alpha_2+\alpha_3$ 含 $\alpha_3$ 分量，而 $\alpha_1-\alpha_2$ 不含）。

**(4)** 课件中「$u,v,w$ 共面」的例子对应存在**非零**系数使 $\lambda_1u+\lambda_2v+\lambda_3w=0$，此时其中一个可写成其余的线性组合，$S(u,v,w)$ 是一个平面（二维）；而本题 (1) 中使组合为零的只有 $\lambda\equiv0$，没有「多余」的向量，$S(v_1,v_2,v_3)$ 填满三维空间。判据即 $\det$ 是否为零 / 主元个数是否等于向量个数。

**涉及知识点**　第 1、3 节：线性组合与张成集 $S(\cdot)$、线性相关/无关的定义（组合得零的方式是否唯一）；第 2 节：$Ax=0$ 有无非零解与相关性等价；第 7 节：行列式非零 $\iff$ 可逆 $\iff$ 列无关；第 12 节：无关向量的个数 $\le$ 空间维数。

---

## 题 4　高斯消元、主元与初等矩阵

设 $A=\begin{pmatrix}1&2&1\\ 2&4&3\\ 1&3&2\end{pmatrix},\ b=(1,2,3)^\top$。

**(1)** 对增广矩阵消元（先处理第一列）：
$$(A\mid b)=\left(\begin{array}{ccc|c}1&2&1&1\\ 2&4&3&2\\ 1&3&2&3\end{array}\right)
\xrightarrow[\ r_3-r_1\ ]{\ r_2-2r_1\ }
\left(\begin{array}{ccc|c}1&2&1&1\\ 0&0&1&0\\ 0&1&1&2\end{array}\right).$$
此时第二列在主元位置 $(2,2)$ 上是 $0$，而其下方 $(3,2)=1\ne0$，**必须做行交换** $r_2\leftrightarrow r_3$，否则无法在第二列取得主元：
$$\xrightarrow{\ P_{23}\ }
\left(\begin{array}{ccc|c}1&2&1&1\\ 0&1&1&2\\ 0&0&1&0\end{array}\right)
\xrightarrow{\ r_2-r_3,\ r_1-r_3\ }
\left(\begin{array}{ccc|c}1&2&0&1\\ 0&1&0&2\\ 0&0&1&0\end{array}\right)
\xrightarrow{\ r_1-2r_2\ }
\left(\begin{array}{ccc|c}1&0&0&-3\\ 0&1&0&2\\ 0&0&1&0\end{array}\right).$$
三个主元、无自由变量 $\Rightarrow$ 唯一解。

**(2)** 第一列的消元由 $E_{21}(-2)$ 与 $E_{31}(-1)$ 实现，作用顺序为先 $E_{21}$ 后 $E_{31}$，故
$$E=E_{31}(-1)\,E_{21}(-2)=\begin{pmatrix}1&0&0\\ -2&1&0\\ -1&0&1\end{pmatrix},\qquad
EA=\begin{pmatrix}1&2&1\\ 0&0&1\\ 0&1&1\end{pmatrix}.$$
取 $P=P_{23}=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$，得
$$U=PEA=\begin{pmatrix}1&2&1\\ 0&1&1\\ 0&0&1\end{pmatrix}\ \ (\text{上三角，主元 }1,1,1).$$
消元阵的逆把操作反向：$E^{-1}=E_{21}(2)E_{31}(1)=\begin{pmatrix}1&0&0\\ 2&1&0\\ 1&0&1\end{pmatrix}$，验算 $E^{-1}E=I$ ✓。
置换阵自逆且正交：$P^{-1}=P=P^\top$ ✓。

**(3)** 回代 $Ux=Pb$，其中 $Pb=(1,3,2)^\top$：
$$x_3=0,\qquad x_2+x_3=2\Rightarrow x_2=2,\qquad x_1+2x_2+x_3=1\Rightarrow x_1=1-4=-3 .$$
即 $x=(-3,2,0)^\top$。验算 $Ax$：第一行 $-3+4+0=1$ ✓；第二行 $-6+8+0=2$ ✓；第三行 $-3+6+0=3$ ✓。

**(4)** 若先置换再消元：$PA=\begin{pmatrix}1&2&1\\ 1&3&2\\ 2&4&3\end{pmatrix}$，则只需
$$\tilde E=E_{31}(-2)\,E_{21}(-1)=\begin{pmatrix}1&0&0\\ -1&1&0\\ -2&0&1\end{pmatrix},\qquad
\tilde E P A=\begin{pmatrix}1&2&1\\ 0&1&1\\ 0&0&1\end{pmatrix}=\tilde U=U .$$
$\tilde E\ne E$（乘子从 $-2,-1$ 变为 $-1,-2$，因为被交换的两行互换了角色），但 $\tilde U=U=PEA$。这说明 $U$ 由 $A$ 本身决定（消元结果是唯一的行阶梯形，主元位置不变），而**初等阵的分解方式依赖于行交换与消元的先后次序**；对应关系为 $\tilde E=P EP^{-1}$，即共轭变换把乘子搬到了交换后的位置上（可验算 $P EP^{-1}=\tilde E^{-1}$ 型关系，此处直接乘即得 $\tilde E P=PE$）。

**涉及知识点**　第 4 节：消元法、主元（用于消元的行中第一个非零系数）、需要行交换的情形（主元位置为 0 而下方非零）；第 5 节：消元阵 $E_{ij}(\lambda)$、置换阵 $P_{ij}$、$E^{-1}=E_{ij}(-\lambda)$、$P^{-1}=P=P^\top$；第 7 节：$U=PEA$、回代、主元个数 $=n$ 时唯一解。

---

## 题 5　矩阵乘法的四种视角、不可交换与幂

**(1)** $A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\ B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$。
**行–列视角**：$(AB)_{ij}=$ 第 $i$ 行与第 $j$ 列的点积，
$$AB=\begin{pmatrix}1\cdot5+2\cdot7&1\cdot6+2\cdot8\\ 3\cdot5+4\cdot7&3\cdot6+4\cdot8\end{pmatrix}=\begin{pmatrix}19&22\\ 43&50\end{pmatrix}.$$
**列–列视角**：$AB$ 的第 $j$ 列 $=A$（的第 $j$ 列的像）$=A b_j$：
$$AB=(A\boldsymbol b_1\ \ A\boldsymbol b_2)=\left(A\binom{5}{7}\ \ A\binom{6}{8}\right)=\left(\binom{19}{43}\ \binom{22}{50}\right)\ \checkmark$$
同理 $BA=\begin{pmatrix}23&34\\31&46\end{pmatrix}$（例如 $(BA)_{11}=5\cdot1+6\cdot3=23$，$(BA)_{21}=7\cdot1+8\cdot3=31$）。
$AB\ne BA$：即使 $A,B$ 同阶方阵也不可交换。

**(2)** $N$ 的上移（super-diagonal）矩阵，$N=2S$，$S$ 在超对角线上为 1。逐次相乘：
$$N^2=\begin{pmatrix}0&0&4&0\\ 0&0&0&4\\ 0&0&0&0\\ 0&0&0&0\end{pmatrix},\quad
N^3=\begin{pmatrix}0&0&0&8\\ 0&0&0&0\\ 0&0&0&0\\ 0&0&0&0\end{pmatrix},\quad N^4=O .$$
规律：$N^k$ 把 $2^k$ 放到第 $k$ 条超对角线上（$(N^k)_{i,i+k}=2^k$），$k\ge4$ 时全部跑出矩阵外，故 $N^4=O$。
$N$ **不可逆**，两种理由：
①$N$ 的第一列全为零，故列向量组含零向量必线性相关，$r(N)\le3<4$；
②若 $N$ 可逆，则 $N^4=O$ 两边左乘 $N^{-4}$ 得 $I=O$，矛盾（可逆阵的幂不可能为零阵）。

**(3)** 设 $A,B$ 均为上三角。取 $i>j$，则
$$(AB)_{ij}=\sum_{k}a_{ik}b_{kj}.$$
项中 $b_{kj}\ne0\Rightarrow k\le j<i$，而此时 $a_{ik}$ 满足 $i>k$，由上三角性 $a_{ik}=0$；故每个乘积项都为零，$(AB)_{ij}=0$，即 $AB$ 上三角。
对角元：$(AB)_{ii}=\sum_k a_{ik}b_{ki}$ 中非零项需同时 $k\le i$（来自 $a_{ik}$）与 $k\ge i$（来自 $b_{ki}$，$b_{ki}\ne0\Rightarrow k\ge i$），故只剩 $k=i$ 项，$(AB)_{ii}=a_{ii}b_{ii}$。
**下三角**同理：$i<j$ 时 $(AB)_{ij}=0$，且对角元仍为 $a_{ii}b_{ii}$；因此三角阵的乘积保持三角性，且 $\det$（对角元之积）相乘。

**(4)** 约定 $A^0\triangleq I$ 是为了让指数律 $A^pA^q=A^{p+q}$ 在 $p=0$ 时仍成立（$A^0A=IA=A=A^{0+1}$）。
写 $N=2S$，其中 $S=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\0&0&0&0\end{pmatrix}$。$S$ 的作用是「下移一位/丢首项」：$S(x_1,x_2,x_3,x_4)^\top=(x_2,x_3,x_4,0)^\top$，即 $S\boldsymbol e_j=\boldsymbol e_{j-1}$（$\boldsymbol e_1\mapsto0$）。连续作用 4 次必把任何向量送成零，故 $S^4=O$，从而 $N^4=2^4S^4=O$；而 $S^3=\boldsymbol e_1\boldsymbol e_4^\top\ne O$，即 $S$ 是幂零指数为 4 的幂零阵。

**涉及知识点**　第 5、6 节：乘法的四种视角（行列点积、$AB$ 的列 $=Ab_j$、行组合、列–行外积和）；不可交换性；第 6 节：置换阵/移位阵的幂、幂零矩阵；第 7 节：$\det$ 与可逆性、$r(AB)\le r(A)$ 的萌芽；三角阵乘积的对角元。

---

## 题 6　行图与列图：用两种观点解释解的情况

方程组 $(\ast)\ \begin{cases}x+y+z=4\\ x+2y+3z=7.\end{cases}$

**(1)** **行观点**：每个方程是 $\mathbb R^3$ 中的一个**平面**，其法向量是该方程的系数行：$\boldsymbol n_1=(1,1,1)^\top$、$\boldsymbol n_2=(1,2,3)^\top$。两法向量不成比例，故两平面**不平行**；常数不同（$4\ne7$ 且 $(4,7)$ 不满足成比例），故不重合。两个不平行的平面相交于**一条直线**，所以解有无穷多个，且解集是一条直线（1 个自由变量）。

**(2)** **列观点**：$A=\begin{pmatrix}1&1&1\\1&2&3\end{pmatrix}$，三列
$$\boldsymbol a_1=\binom11,\quad \boldsymbol a_2=\binom12,\quad \boldsymbol a_3=\binom13,\qquad b=\binom47 .$$
$Ax=b$ 就是「$b$ 能否写成 $\boldsymbol a_1,\boldsymbol a_2,\boldsymbol a_3$ 的线性组合」。因 $\boldsymbol a_1,\boldsymbol a_2$ 不成比例（$\det\begin{pmatrix}1&1\\1&2\end{pmatrix}=1\ne0$），它们已张成 $\mathbb R^2$，故 $C(A)=\mathbb R^2$，**任意** $b\in\mathbb R^2$ 都可表出 $\Rightarrow$ 一定有解。又未知数个数 $3>$ 主元个数 $r(A)=2$，自由变量 $3-2=1$ 个 $\Rightarrow$ 解不唯一（一条直线）。

**(3)** 取 $z=0$：$x+y=4,\ x+2y=7\Rightarrow y=3,x=1$，得 $\boldsymbol p=(1,3,0)^\top$；
取 $z=1$：$x+y=3,\ x+2y=4\Rightarrow y=1,x=2$，得 $\boldsymbol q=(2,1,1)^\top$。
$\boldsymbol v=\boldsymbol q-\boldsymbol p=(1,-2,1)^\top$ 满足 $A\boldsymbol v=0$（验证：$1-2+1=0$，$1-2+3=2$……应为 $1\cdot1+1\cdot(-2)+1\cdot1=0$ ✓，$1+2(-2)+3(1)=1-4+3=0$ ✓）。
全部解：
$$x=\boldsymbol p+t\boldsymbol v=\begin{pmatrix}1+t\\ 3-2t\\ t\end{pmatrix},\qquad t\in\mathbb R,$$
即「特解 $+$ 零空间的直线」。

**(4)** 改后方程组的系数矩阵为 $A'=\begin{pmatrix}1&1&1\\2&2&2\end{pmatrix}$，第二行 $=2\times$ 第一行。
**(a)** $2x+2y+2z=7$。**行观点**：两平面法向量平行但常数不满足同比例（$7\ne 2\cdot4=8$），是**两个平行且不重合**的平面，交集为空 $\Rightarrow$ 无解。
**列观点**：$A'$ 的三列都落在直线 $S\!\left(\binom12\right)$ 上，故 $C(A')=S\!\left(\binom12\right)\subsetneq\mathbb R^2$，而 $b=\binom47\notin C(A')$（因为 $\binom47$ 不是 $(1,2)^\top$ 的倍数：$4\cdot2\ne7$）。等价地，$y=\binom{-2}{1}\in N(A'^\top)$（$A'^\top y=0$：$-2+2=0$ 三列皆然），而 $y\cdot b=-2\cdot4+1\cdot7=-1\ne0$，即 $b$ 与 $N(A^\top)$ 中的向量不正交，故 $b\notin C(A)$。
**(b)** $2x+2y+2z=8$。第二方程正是第一方程的 2 倍，两平面**重合**，$b=\binom48=4\binom12\in C(A')$ $\Rightarrow$ 有解；$r(A')=1$，未知数 3 个，自由变量 $3-1=2$ 个 $\Rightarrow$ 解集是一个平面（无穷多解，两个参数）：$x=4-y-z$，$y,z$ 自由。

**涉及知识点**　第 3 节：行图（方程 = 超平面）、列图（$Ax=b$ 能否表出）、解集 = 特解 + 零空间；第 2 节：列空间 $C(A)$；第 10 节：$b\in C(A)\iff Ax=b$ 相容；第 11–12 节：$r(A)$、自由变量个数 $n-r(A)$、$N(A^\top)$ 与相容性判据。

---

## 题 7　带参数的消元：行交换、主元缺失与解的讨论

$A=\begin{pmatrix}1&2&1\\ 2&4&3\\ 1&a&5\end{pmatrix}$。

**(1)** 第一列消元：$r_2-2r_1,\ r_3-r_1$，
$$\longrightarrow\begin{pmatrix}1&2&1\\ 0&0&1\\ 0&a-2&4\end{pmatrix}.$$
第二列的主元位置 $(2,2)$ 为 $0$。当 $a\ne2$ 时 $(3,2)=a-2\ne0$，其下方有非零元，**必须**交换 $r_2\leftrightarrow r_3$ 才能取到第二个主元；交换后矩阵为 $\begin{pmatrix}1&2&1\\ 0&a-2&4\\ 0&0&1\end{pmatrix}$，三个主元 $1,\ a-2,\ 1$ 全非零 $\Rightarrow r(A)=3$，$A$ 可逆，唯一解。
$a=3,\ b=(1,3,2)^\top$ 时（$A=\begin{pmatrix}1&2&1\\2&4&3\\1&3&5\end{pmatrix}$）：先对第一列消元并同步处理右端，
$$\left(\begin{array}{ccc|c}1&2&1&1\\ 2&4&3&3\\ 1&3&5&2\end{array}\right)
\xrightarrow[\ r_3-r_1\ ]{\ r_2-2r_1\ }
\left(\begin{array}{ccc|c}1&2&1&1\\ 0&0&1&1\\ 0&1&4&1\end{array}\right)
\xrightarrow{\ r_2\leftrightarrow r_3\ }
\left(\begin{array}{ccc|c}1&2&1&1\\ 0&1&4&1\\ 0&0&1&1\end{array}\right).$$
回代：$x_3=1$；$x_2+4x_3=1\Rightarrow x_2=-3$；$x_1+2x_2+x_3=1\Rightarrow x_1=1+6-1=6$。即 $x=(6,-3,1)^\top$，验算 $Ax$：
$$1\cdot6+2(-3)+1\cdot1=1\ \checkmark,\qquad 2\cdot6+4(-3)+3\cdot1=3\ \checkmark,\qquad 1\cdot6+3(-3)+5\cdot1=2\ \checkmark$$

**(2)** $a=2$ 时第三行变为 $(0,0,4)$：
$$\begin{pmatrix}1&2&1\\ 0&0&1\\ 0&0&4\end{pmatrix}\xrightarrow{\ r_3-4r_2\ }\begin{pmatrix}1&2&1\\ 0&0&1\\ 0&0&0\end{pmatrix}.$$
对 $b=(1,3,t)^\top$：$r_2-2r_1$ 右端 $3-2=1$；$r_3-r_1$ 右端 $t-1$；$r_3-4r_2$ 右端 $t-1-4=t-5$。
- $t\ne5$：出现 $0=t-5\ne0$，**无解**（第三行是零行却右端非零）。
- $t=5$：主元在列 1、列 3（两个主元），$x_2$ 自由，**无穷多解**。最简行阶梯形：由 $\left(\begin{smallmatrix}1&2&1&1\\0&0&1&1\end{smallmatrix}\right)$ 做 $r_1-r_2$ 得
$$R=\left(\begin{array}{ccc|c}1&2&0&0\\ 0&0&1&1\\ 0&0&0&0\end{array}\right),$$
全解 $x_1=-2s,\ x_2=s,\ x_3=1$，即
$$x=\binom{0}{0}{1}+s\binom{-2}{1}{0},\qquad s\in\mathbb R .$$
验算 $s=0$：$A(0,0,1)^\top$ 是 $A$ 的第三列 $=(1,3,5)^\top=b$ ✓（$t=5$）；$A(-2,1,0)^\top=(-2+2,\ -4+4,\ -2+2)^\top=0$ ✓。

**(3)** 归纳（$n=3$ 个未知数）：
- 3 个主元、0 个自由变量 $\Rightarrow$ 唯一解（$A$ 可逆），如 $a\ne2$；
- 2 个主元、1 个自由变量且相容 $\Rightarrow$ 无穷多解（直线），如 $a=2,t=5$；
- 主元出现在右端列（$0=c\ne0$）$\Rightarrow$ 无解，如 $a=2,t\ne5$；
- 一般地：$r(A)=r(A\mid b)$ 时有解，此时解的自由度 $=n-r(A)$；$r(A)<r(A\mid b)$ 时无解。

**(4)** 若 $(1,1)$ 元改为 $0$（首列首元素为零），第一列消元无法以第 1 行为主元行，须先把某一行（第 2 或第 3 行，其第一列元素非零）换到第 1 行——即 $P_{1j}$。这正是「**主元是用于消元的行中第一个非零系数**」的含义：主元不固定在某行某列，而是当前可用行中该列的第一个非零元；只有当该列在所有剩余行中都为零时，该列才没有主元（成为自由列），消元转向下一列。

**涉及知识点**　第 4 节：消元与主元定义、行交换；第 7 节：$r(A)$ 与 $r(A\mid b)$ 对比判定解的存在性、主元个数 = 非零行数；第 11 节：自由变量个数 $=n-r(A)$；第 12 节：最简行阶梯形 $R$ 读出全解 = 特解 + 零空间基的线性组合。

---

## 题 8　特殊矩阵左乘、右乘的效应

$A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&10\end{pmatrix}$，$D=\operatorname{diag}\!\left(2,\frac13,1\right)$，$E=E_{21}(3)$，$P=P_{23}$。

**(1)** 左乘 $D$（**按行放大**）：第 $i$ 行乘 $d_i$，
$$DA=\begin{pmatrix}2&4&6\\[2pt]\frac43&\frac53&2\\7&8&10\end{pmatrix}.$$
右乘 $D$（**按列放大**）：第 $j$ 列乘 $d_j$，
$$AD=\begin{pmatrix}2&\frac23&3\\8&\frac53&6\\14&\frac83&10\end{pmatrix}.$$
原因：$(DA)_{ij}=d_ia_{ij}$（只有 $k=i$ 项非零），$(AD)_{ij}=a_{ij}d_j$。

**(2)** 左乘消元阵 $E_{21}(3)=\begin{pmatrix}1&0&0\\3&1&0\\0&0&1\end{pmatrix}$：把第 1 行的 3 倍加到第 2 行，
$$EA=\begin{pmatrix}1&2&3\\7&11&15\\7&8&10\end{pmatrix}\quad(\text{row}_2=(4,5,6)+3(1,2,3)=(7,11,15)).$$
右乘同一矩阵是**列变换**：$AE_{21}(3)$ 把第 2 列的 3 倍加到第 **1** 列，
$$AE=\begin{pmatrix}7&2&3\\19&5&6\\31&8&10\end{pmatrix},$$
即列 1 被改写为 $\boldsymbol a_1+3\boldsymbol a_2=(1,4,7)+3(2,5,8)=(7,19,31)^\top$，列 2、列 3 不变。
一般规律：$E_{ij}(\lambda)$ **左乘** = 行变换「第 $j$ 行的 $\lambda$ 倍加到第 $i$ 行」；**右乘** = 列变换「第 $i$ 列的 $\lambda$ 倍加到第 $j$ 列」。

**(3)** 左乘 $P_{23}$ 交换 $A$ 的第 2、3 **行**：
$$PA=\begin{pmatrix}1&2&3\\7&8&10\\4&5&6\end{pmatrix};$$
右乘 $P_{23}$ 交换第 2、3 **列**：
$$AP=\begin{pmatrix}1&3&2\\4&6&5\\7&10&8\end{pmatrix}.$$
（因 $P_{23}^\top=P_{23}$，$AP=(P_{23}A^\top)^\top$，行交换转置后变列交换。）

**(4)** 「左乘初等阵不改变 $A$ 的列空间」**不正确**。反例：取 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$，$E_{21}(1)=\begin{pmatrix}1&0\\1&1\end{pmatrix}$，
$$E_{21}(1)A=\begin{pmatrix}1&0\\1&0\end{pmatrix},$$
$C(A)=S\!\left(\binom10\right)$（$x$ 轴），而 $C(E_{21}(1)A)=S\!\left(\binom11\right)$（直线 $y=x$），两者**不同**。
真正保持不变的是：**列与列之间的线性关系**，即 $N(A)=N(EA)$（$E$ 可逆时 $Ax=0\iff EAx=0$）；列空间满足 $C(EA)=E\,C(A)$（像空间被 $E$ 一起搬运，维数相同 $\dim C(EA)=\dim C(A)$ 但子空间一般不同）。
对偶地，**右乘**可逆阵保持列空间（$C(AB)\subset C(A)$，$B$ 可逆时取等，见题 13），而不保持行空间/零空间。

**涉及知识点**　第 5 节：三类初等阵（消元阵、置换阵、$D_i(\lambda)$ 缩放阵）与左乘=行变换；第 6 节：右乘=列变换、$(AB)_{ij}$ 的两类展开、对角阵缩放；第 7、10 节：可逆变换保持零空间与维数；第 10 节：列空间作为子空间可被线性映射改变位置。

---

## 题 9　乘法的可定义性、形状规则与结合律

$A=\begin{pmatrix}1&0&2\\3&1&-1\end{pmatrix}_{2\times3},\quad B=\begin{pmatrix}1&2\\0&1\\2&-1\end{pmatrix}_{3\times2}.$

**(1)** 行–列点积：
$$AB=\begin{pmatrix}1\cdot1+0\cdot0+2\cdot2&1\cdot2+0\cdot1+2\cdot(-1)\\ 3\cdot1+1\cdot0+(-1)\cdot2&3\cdot2+1\cdot1+(-1)(-1)\end{pmatrix}=\begin{pmatrix}5&0\\1&8\end{pmatrix}_{2\times2};$$
$$BA=\begin{pmatrix}7&2&0\\ 3&1&-1\\ -1&-1&5\end{pmatrix}_{3\times3}$$
（如第一行 $=1\cdot(1,0,2)+2\cdot(3,1,-1)=(7,2,0)$；第三行 $=2(1,0,2)-(3,1,-1)=(-1,-1,5)$）。
$AB$ 是 $2\times2$、$BA$ 是 $3\times3$，**阶数不同**，谈不上相等——这就是「即使两个乘积都有意义也未必能比较」。

**(2)** 记号需匹配：$A$ 为 $2\times3$、$B$ 为 $3\times2$，故只有当 $C$ 的行数 $p=2$ 时 $BC$ 才有意义。设 $C$ 为 $2\times q$：
$$BC:\ (3\times2)(2\times q)=3\times q,\qquad A(BC):\ (2\times3)(3\times q)=2\times q;$$
$$AB:\ (2\times3)(3\times2)=2\times2,\qquad (AB)C:\ (2\times2)(2\times q)=2\times q.$$
两种算法结果同为 $2\times q$，形状规则「$(m\times n)(n\times p)=m\times p$」中**中间指标 $n$ 消去**：它是「内积的长度」，只要求两侧匹配，不出现在结果形状里。

**(3)** 结合律证明（逐元素）。设 $A=(a_{ij})$ 为 $m\times n$，$B=(b_{jk})$ 为 $n\times p$，$C=(c_{k\ell})$ 为 $p\times q$。则
$$\big((AB)C\big)_{i\ell}=\sum_{k=1}^{p}(AB)_{ik}c_{k\ell}=\sum_{k=1}^{p}\Big(\sum_{j=1}^{n}a_{ij}b_{jk}\Big)c_{k\ell}
=\sum_{k}\sum_{j}a_{ij}b_{jk}c_{k\ell},$$
$$\big(A(BC)\big)_{i\ell}=\sum_{j=1}^{n}a_{ij}(BC)_{j\ell}=\sum_{j=1}^{n}a_{ij}\Big(\sum_{k=1}^{p}b_{jk}c_{k\ell}\Big)
=\sum_{j}\sum_{k}a_{ij}b_{jk}c_{k\ell}.$$
有限和可换求和次序（实数的结合律、交换律与分配律），两式相等，故 $(AB)C=A(BC)$。

**(4)** 课件提到不可交换的三种情形，各举一例：
- **$BA$ 无定义**：取 $A$ 为题中 $2\times3$ 矩阵，再取 $G$ 为 $3\times4$ 矩阵（例如 $G=(A\ B)^\top$ 型的任意 $3\times4$ 阵）。则 $AG$ 有定义，是 $2\times4$；而 $GA$ 需要 $4=2$ 才有意义，**根本无定义**，谈不上交换律。
- **都有定义但阶数不同**：本题 (1) 的 $A,B$：$AB$ 为 $2\times2$，$BA$ 为 $3\times3$。
- **同为方阵仍不等**：$A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\ B=\begin{pmatrix}1&1\\1&1\end{pmatrix}$，
$$AB=\begin{pmatrix}1&1\\0&0\end{pmatrix}\ne\begin{pmatrix}1&0\\1&0\end{pmatrix}=BA$$
（此处 $AB\ne BA$ 且二者都不对称，见题 24。）

**涉及知识点**　第 5 节：矩阵乘法的定义与形状规则、内积长度即中间指标；第 6 节：$AB$ 的列 $=Ab_j$、行 $=$ 行与 $B$ 的组合；结合律证明（第 5 节定理）；矩阵乘法不满足交换律的三种原因。

---

## 题 10　形状判据与可逆方阵的列空间、零空间

**(1)** 证明：$A$ 为 $m\times n$ 且 $m<n$。消元后主元每行至多一个，故主元个数 $r(A)\le m$。自由变量个数
$$n-r(A)\ \ge\ n-m\ >\ 0,$$
存在自由变量即可取其值为 $1$（其余自由变量 $0$，主元变量由回代确定）而得 $Ax=0$ 的**非零解**。$\blacksquare$
（列观点：$n$ 个列向量落在 $m$ 维空间 $\mathbb R^m$ 中，$n>m$ 个向量必线性相关。）

**(2)** $\mathbb R^3$ 中任意 4 个向量：以它们为列作 $3\times4$ 矩阵，$m=3<n=4$，由 (1) $Ax=0$ 有非零解，即存在非零系数使列的组合为零 $\Rightarrow$ **必线性相关**。
$\mathbb R^3$ 中 2 个向量**不必**相关：如 $\boldsymbol e_1=(1,0,0)^\top,\boldsymbol e_2=(0,1,0)^\top$ 不成比例，$c_1\boldsymbol e_1+c_2\boldsymbol e_2=0$ 只有零解，故无关。（相关 $\iff$ 两向量共线，且其中之一可为零向量。）

**(3)** $6\times6$ 可逆 $A$：由定理 1 有 6 个主元，$R=I$。
$$C(A)=\mathbb R^6\ (\dim=6),\qquad N(A)=\{0\}\ (\dim=0),$$
且 $\dim C(A)+\dim N(A)=6+0=6=$ 列数 ✓。任意 $b$ 有唯一解。

**(4)** $A$ 为 $9\times12$，且对任意 $b\in\mathbb R^9$ 都有解 $\iff$ $C(A)=\mathbb R^9$ $\iff$ $A$ 有 9 个主元（每行一个主元，无零行），故 $r(A)=9$。于是
$$\dim C(A)=9,\qquad \dim N(A)=12-9=3,$$
即 $Ax=b$ 的解集总形如「特解 + 3 维子空间」，绝不可能唯一。
注意 $m<n$（$9<12$）与 (1) 一致：零空间必非平凡。

**涉及知识点**　第 2、11 节：$Ax=0$ 有非零解 $\iff$ 有自由变量 $\iff r(A)<n$；第 4、12 节：主元个数 $\le\min\{m,n\}$、$r(A)+\dim N(A)=n$；第 7 节：可逆 $\iff n$ 个主元 $\iff N(A)=\{0\}$；第 10 节：$C(A)=\mathbb R^m\iff$ 任意 $b$ 可表出。

---

# 第二部分　仿真期中（题 11–19，逐题对应考卷八大题）

## 题 11　数乘、$\dim C(A)$ 与 $\dim C(A^\top)$、$S(\alpha_1,\alpha_2)$

$A=\begin{pmatrix}2&-1&1\\ 0&3&-2\\ 1&0&4\end{pmatrix}=(\alpha_1\ \alpha_2\ \alpha_3)$，其中 $\alpha_1=(2,0,1)^\top,\ \alpha_2=(-1,3,0)^\top,\ \alpha_3=(1,-2,4)^\top$。

**(1)** 数乘即每个元素相乘：
$$aA=\begin{pmatrix}2a&-a&a\\ 0&3a&-2a\\ a&0&4a\end{pmatrix},\qquad a\in\mathbb R .$$
（特别 $0A=O$，$(-1)A=-A$；列角度 $aA=(a\alpha_1\ \ a\alpha_2\ \ a\alpha_3)$，每列被同倍伸缩，故 $C(aA)=C(A)$（$a\ne0$ 时）。）

**(2)** 按第一列展开：
$$\det A=2\begin{vmatrix}3&-2\\0&4\end{vmatrix}-0+1\begin{vmatrix}-1&1\\3&-2\end{vmatrix}=2\cdot12+(-1)(-2)-1\cdot3=24+2-3=23\ne0 .$$
故 $A$ 可逆、有 3 个主元，$R=I_3$。于是
$$\dim C(A)=r(A)=3,\qquad \dim C(A^\top)=\text{行秩}=r(A)=3,$$
且 $C(A)=C(A^\top)=\mathbb R^3$。（行秩 $=$ 列秩是第 12 节定理；本题两者都等于 3。）

**(3)** $S(\alpha_1,\alpha_2)=\{c_1\alpha_1+c_2\alpha_2:c_1,c_2\in\mathbb R\}$ 是**子空间**：任取两向量 $c_1\alpha_1+c_2\alpha_2$ 与 $d_1\alpha_1+d_2\alpha_2$，其和仍为 $\alpha_1,\alpha_2$ 的组合 $(c_1+d_1)\alpha_1+(c_2+d_2)\alpha_2$，数乘 $k(c_1\alpha_1+c_2\alpha_2)$ 也是——对加法与数乘都封闭（课件子空间两条判别）。
$\alpha_1,\alpha_2$ 不成比例（第二个分量 $0$ 与 $3$ 不成比例），故线性无关 $\Rightarrow\dim S(\alpha_1,\alpha_2)=2$，它是过原点的一个**平面**。
平面方程：$x$ 属于该平面 $\iff x$ 与法向量正交。法向量取
$$\alpha_1\times\alpha_2=\begin{vmatrix}\boldsymbol e_1&\boldsymbol e_2&\boldsymbol e_3\\ 2&0&1\\ -1&3&0\end{vmatrix}=(0\cdot0-1\cdot3,\ 1\cdot(-1)-2\cdot0,\ 2\cdot3-0\cdot(-1))=(-3,-1,6),$$
取 $\boldsymbol n=(3,1,-6)^\top$（同向乘 $-1$），平面方程为
$$3x_1+x_2-6x_3=0 .$$
验证：$\alpha_1$: $3\cdot2+0-6\cdot1=0$ ✓；$\alpha_2$: $3(-1)+3-0=0$ ✓。
$\alpha_3$: $3\cdot1+(-2)-6\cdot4=3-2-24=-23\ne0$，故 $\alpha_3\notin S(\alpha_1,\alpha_2)$。
（这个 $-23$ 恰是 $-\det A$：$\det A=(\alpha_1\times\alpha_2)\cdot\alpha_3$，即三阶行列式 $=$ 平行六面体体积，几何上正是「$\alpha_3$ 到 $\alpha_1,\alpha_2$ 张成平面的有向距离 $\times$ 底面积」。所以三列无关 $\iff\alpha_3$ 不在前两列的平面内。）

**涉及知识点**　第 1 节：数乘与线性组合；第 2、10 节：列空间 $C(A)$、张成集 $S(\cdot)$ 是子空间及其维数；第 11 节：秩 $=$ 主元个数 $=\dim C(A)$；第 12 节：行秩 $=$ 列秩；第 7 节：$\det\ne0\iff$ 可逆 $\iff$ 列无关。

---

## 题 12　缩放置换矩阵的幂

$A=\begin{pmatrix}0&3&0&0\\ 0&0&3&0\\ 0&0&0&3\\ 3&0&0&0\end{pmatrix}=3P$，其中 $P$ 是循环置换阵（$P\boldsymbol e_1=\boldsymbol e_4,\ P\boldsymbol e_j=\boldsymbol e_{j-1}$），$Ax=3(x_2,x_3,x_4,x_1)^\top$。

**(1)** 因 $A=3P$ 且数量阵与 $P$ 可交换，$(3P)^k=3^kP^k$：
$$A^2=9P^2=\begin{pmatrix}0&0&9&0\\ 0&0&0&9\\ 9&0&0&0\\ 0&9&0&0\end{pmatrix},\quad
A^3=27P^3=\begin{pmatrix}0&0&0&27\\ 27&0&0&0\\ 0&27&0&0\\ 0&0&27&0\end{pmatrix},\quad
A^4=81P^4=81I .$$
逐点核对 $A^2$：$(A^2)_{13}=\text{row}_1(A)\cdot\text{col}_3(A)=(0,3,0,0)\cdot(0,3,0,0)=9$ ✓，其余非零元同理。

**(2)** $P^4=I\Rightarrow P^{4k}=(P^4)^k=I$，故
$$A^{4k}=3^{4k}P^{4k}=81^{\,k}I,\qquad A^8=81^2I=6561\,I .$$
一般地 $A^{4k+r}=81^kA^r\ (0\le r\le3)$，如 $A^{10}=81^2A^2$。

**(3)** 作用解释：$A$ 把 $(x_1,x_2,x_3,x_4)$ 送成 $3(x_2,x_3,x_4,x_1)$——先「循环搬位」再「放大 3 倍」。搬位是 4-循环，连续 4 次回到原向量；而每次各自贡献因子 3，四次共 $3^4=81$。所以不必做矩阵乘法即得 $A^4=81I$。（等价说法：$P$ 对应置换 $\sigma$，$\sigma^4=\mathrm{id}$。）

**(4)** 可逆：$\det A=3^4\det P=81\cdot(-1)=-81\ne0$（4-循环的符号为 $-1$），或由 $A^4=81I$ 得
$$A^{-1}=\frac1{81}A^3=\frac1{27}P^3=\begin{pmatrix}0&0&0&\frac13\\[2pt]\frac13&0&0&0\\[2pt]0&\frac13&0&0\\[2pt]0&0&\frac13&0\end{pmatrix}.$$
验算 $A^{-1}A$ 的 $(1,2)$ 元：第一行 $(0,0,0,\frac13)$ 与第二列 $(3,0,0,0)^\top$ 点积 $=0$；$(1,4)$ 元：$(0,0,0,\frac13)\cdot(0,0,3,0)=1$ ✓ 即 $A^{-1}A=I$。

**涉及知识点**　第 5、6 节：置换阵 $P_\sigma$、排列的循环分解、$P^{-1}=P^\top$；数量阵与任意同阶阵可交换 $(cA)^k=c^kA^k$；第 7 节：由 $A^k=cI$ 读出 $A^{-1}=A^{k-1}/c$、$\det(cA)=c^n\det A$；第 9 节：$\det P_\sigma=\operatorname{sgn}(\sigma)$。

---

## 题 13　$C(AB)\subset C(A)$；$B$ 可逆取等；$N(B)\subset N(AB)$

设 $A$ 为 $m\times n$，$B$ 为 $n\times p$，记 $B$ 的列为 $b_1,\dots,b_p$。

**(1)** $AB$ 的第 $j$ 列 $=Ab_j$，它是 $A$ 的各列以 $b_j$ 的分量为系数的线性组合，故 $Ab_j\in C(A)$。$C(AB)$ 由这些列张成，而 $C(A)$ 是子空间、包含这些列，就包含它们的全部线性组合，因此
$$C(AB)=S(Ab_1,\dots,Ab_p)\subset C(A).\blacksquare$$

**(2)** 若 $B$ 可逆（$n=p$）：由 (1) 有 $C(AB)\subset C(A)$。又 $A=(AB)B^{-1}$，再次用 (1) 得 $C(A)=C\big((AB)B^{-1}\big)\subset C(AB)$。两侧包含互逆 $\Rightarrow$ $C(AB)=C(A)$。$\blacksquare$
（直观：右乘可逆阵只是对列做可逆的线性组合，不改变张成的子空间；此时 $\dim C(AB)=\dim C(A)$，与题 17 的 $r(AB)=r(A)$ 一致。）

**(3)** 若 $Bx=0$，则 $(AB)x=A(Bx)=A0=0$，故 $x\in N(AB)$，即 $N(B)\subset N(AB)$。$\blacksquare$
若 $A$ 可逆（$m=n$）：反向包含取 $x\in N(AB)$，则 $ABx=0$，左乘 $A^{-1}$ 得 $Bx=0$，即 $x\in N(B)$，故 $N(AB)\subset N(B)$；结合正向得 $N(AB)=N(B)$。$\blacksquare$
（注意两个「取等」条件分工不同：**列空间取等要看右因子可逆，零空间取等要看左因子可逆。**）

**(4)** 两个严格包含的例子（同一对矩阵即可）：取
$$A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad B=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad AB=\begin{pmatrix}0&0\\0&0\end{pmatrix}=O .$$
$C(A)=S\!\left(\binom10\right)$ 而 $C(AB)=\{0\}$，故 $C(AB)\subsetneq C(A)$（$B$ 不可逆：$\det B=0$）。
$N(AB)=\mathbb R^2$（零矩阵的零空间是全空间），取 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\ B=I_2$（$B$ 可逆而 $A$ 不可逆）：$N(B)=\{0\}\subsetneq\mathbb R^2=N(A)=N(AB)$ ✓。
维数视角：本例 $r(A)=r(B)=1$ 而 $r(AB)=0$，即 $B$ 的列空间 $S(\boldsymbol e_1)$ 恰好整个落进 $A$ 的零空间 $S(\boldsymbol e_2)$ 的对偶情形里——$AB$ 把 $B$ 的像「杀光」了。

**涉及知识点**　第 2、6 节：$AB$ 的列 $=Ab_j$、列空间定义；第 6、7 节：可逆阵的列变换不改张成；第 10 节：子空间的包含与传递性；第 11 节：零空间 $N(A)$、$N(B)\subset N(AB)$；第 12 节：$\dim$ 与秩的关系（为题 17 铺垫）。

---

## 题 14　分块矩阵乘法

$A=\begin{pmatrix}I_2&O\\ A_1&I_2\end{pmatrix}$，$A_1=\begin{pmatrix}2&-1\\ 1&3\end{pmatrix}$；
$B=\begin{pmatrix}B_{11}&B_{12}\\ B_{21}&B_{22}\end{pmatrix}$，其中
$$B_{11}=\begin{pmatrix}1&0\\ -1&2\end{pmatrix},\ B_{12}=\begin{pmatrix}0&3\\ 1&-1\end{pmatrix},\ B_{21}=\begin{pmatrix}2&0\\ 0&1\end{pmatrix},\ B_{22}=\begin{pmatrix}1&2\\ -1&0\end{pmatrix}.$$

**(1)** 要求：$A$ 的**行分块**与 $B$ 的**列分块**一致（这里都按 $2+2$ 分），且每个小块乘积的形状匹配。于是按「小块当作元素」做行列点积：
$$AB=\begin{pmatrix}I_2B_{11}+OB_{21}&I_2B_{12}+OB_{22}\\ A_1B_{11}+I_2B_{21}&A_1B_{12}+I_2B_{22}\end{pmatrix}
=\begin{pmatrix}B_{11}&B_{12}\\ A_1B_{11}+B_{21}&A_1B_{12}+B_{22}\end{pmatrix}.$$
计算两个新块：
$$A_1B_{11}=\begin{pmatrix}2&-1\\1&3\end{pmatrix}\begin{pmatrix}1&0\\-1&2\end{pmatrix}=\begin{pmatrix}3&-2\\-2&6\end{pmatrix}
\Rightarrow A_1B_{11}+B_{21}=\begin{pmatrix}5&-2\\-2&7\end{pmatrix},$$
$$A_1B_{12}=\begin{pmatrix}2&-1\\1&3\end{pmatrix}\begin{pmatrix}0&3\\1&-1\end{pmatrix}=\begin{pmatrix}-1&7\\3&0\end{pmatrix}
\Rightarrow A_1B_{12}+B_{22}=\begin{pmatrix}0&9\\2&2\end{pmatrix}.$$
故
$$AB=\begin{pmatrix}1&0&0&3\\ -1&2&1&-1\\ 5&-2&0&9\\ -2&7&2&0\end{pmatrix}.$$

**(2)** 核对 $(3,1)$：$A$ 的第 3 行 $(2,-1,1,0)$ 与 $B$ 的第 1 列 $(1,-1,2,0)^\top$ 点积 $=2+1+2+0=5$ ✓；
核对 $(4,3)$：$A$ 的第 4 行 $(1,3,0,1)$ 与 $B$ 的第 3 列 $(0,1,1,-1)^\top$ 点积 $=0+3+0-1=2$ ✓（与分块结果右下块第 2 行第 2 列 $=2$ 一致）。

**(3)** 把 $A$ 换成 $\begin{pmatrix}I_2&O\\ -A_1&I_2\end{pmatrix}$，只有下左块变号，故左下、右下两块变为「减」：
$$B_{21}-A_1B_{11}=\begin{pmatrix}-1&2\\ 2&-5\end{pmatrix},\qquad
B_{22}-A_1B_{12}=\begin{pmatrix}2&-5\\ -4&0\end{pmatrix},$$
$$AB=\begin{pmatrix}1&0&0&3\\ -1&2&1&-1\\ -1&2&2&-5\\ 2&-5&-4&0\end{pmatrix}.$$
用途：两类矩阵互为逆矩阵，
$$\begin{pmatrix}I&O\\ A_1&I\end{pmatrix}^{-1}=\begin{pmatrix}I&O\\ -A_1&I\end{pmatrix}\quad\big(\text{乘积}=\begin{pmatrix}I&O\\ A_1-A_1&I\end{pmatrix}=I\big),$$
即「把某块行的倍数加到另一块行」的**分块消元阵**。左乘 $\begin{pmatrix}I&O\\ A_1&I\end{pmatrix}$ 执行加分块、左乘 $\begin{pmatrix}I&O\\ -A_1&I\end{pmatrix}$ 就是它的逆操作（消元的反向），这正是 LU 分解中 $L$ 与 $L^{-1}$（题 15、题 22）的分块版本。

**涉及知识点**　第 6 节：分块矩阵及其乘法的形状要求、把小块当元素做行列点积；第 5 节：消元阵的分块类比 $\begin{pmatrix}I&O\\ *&I\end{pmatrix}$；第 7 节：逆矩阵、$(E_{ij}(\lambda))^{-1}=E_{ij}(-\lambda)$ 的分块版。

---

## 题 15　LDU 分解及其逆

$A=\begin{pmatrix}1&1&2\\ 2&4&6\\ 1&7&11\end{pmatrix}$。

**(1)** 消元（无需行交换）：$r_2-2r_1$、$r_3-r_1$，再 $r_3-3r_2$：
$$\xrightarrow{\ r_2-2r_1,\ r_3-r_1\ }\begin{pmatrix}1&1&2\\ 0&2&2\\ 0&6&9\end{pmatrix}
\xrightarrow{\ r_3-3r_2\ }\begin{pmatrix}1&1&2\\ 0&2&2\\ 0&0&3\end{pmatrix}=U_{\text{tri}} .$$
即 $U_{\text{tri}}=E_{32}(-3)E_{31}(-1)E_{21}(-2)A$，故
$$L=\big(E_{32}(-3)E_{31}(-1)E_{21}(-2)\big)^{-1}=E_{21}(2)E_{31}(1)E_{32}(3)=\begin{pmatrix}1&0&0\\ 2&1&0\\ 1&3&1\end{pmatrix}$$
（乘子 $2,1,3$ 直接填入下三角对应位置）。把 $U_{\text{tri}}$ 的各行除以主元 $1,2,3$ 提出 $D$：
$$D=\begin{pmatrix}1&0&0\\ 0&2&0\\ 0&0&3\end{pmatrix},\qquad
U=\begin{pmatrix}1&1&2\\ 0&1&1\\ 0&0&1\end{pmatrix}.$$
验证 $LDU=A$：先 $DU=\begin{pmatrix}1&1&2\\0&2&2\\0&0&3\end{pmatrix}$，再
$$L(DU)=\begin{pmatrix}1&1&2\\ 2&4&6\\ 1&7&11\end{pmatrix}=A\ \checkmark$$

**(2)** 三个因子的逆：
$$L^{-1}=\big(E_{21}(2)E_{31}(1)E_{32}(3)\big)^{-1}=E_{32}(-3)E_{31}(-1)E_{21}(-2)=\begin{pmatrix}1&0&0\\ -2&1&0\\ 5&-3&1\end{pmatrix},$$
（$(3,1)$ 元 $=-1-3(-2)=5$，不能只写 $-1$：逆的顺序必须**反序**取逆。）
$$D^{-1}=\begin{pmatrix}1&0&0\\ 0&\frac12&0\\ 0&0&\frac13\end{pmatrix},\qquad
U^{-1}=\begin{pmatrix}1&-1&-1\\ 0&1&-1\\ 0&0&1\end{pmatrix}.$$
$U^{-1}$ 由回代或 $U^{-1}=(I+N)^{-1}=I-N+N^2$（$N=\begin{pmatrix}0&1&2\\0&0&1\\0&0&0\end{pmatrix}$ 幂零，$N^2=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix}$，$N^3=O$）求得，验算 $U^{-1}U=I$ ✓。

**(3)** 乘积的逆**反序**：
$$A^{-1}=(LDU)^{-1}=U^{-1}D^{-1}L^{-1}
=\begin{pmatrix}\frac13&\frac12&-\frac13\\[2pt]-\frac83&\frac32&-\frac13\\[2pt]\frac53&-1&\frac13\end{pmatrix}.$$
验算 $A^{-1}A$：第一行 $\times$ 第一列 $=\frac13\cdot1+\frac12\cdot2-\frac13\cdot1=1$ ✓；第一行 $\times$ 第二列 $=\frac13\cdot1+\frac12\cdot4-\frac13\cdot7=\frac13+2-\frac73=0$ ✓；第一行 $\times$ 第三列 $=\frac13\cdot2+\frac12\cdot6-\frac13\cdot11=\frac23+3-\frac{11}{3}=0$ ✓（其余元素同法可核，全部给出 $I$）。

**(4)** 用分解解 $Ax=b,\ b=(1,2,3)^\top$，三段式（不重新消元）：
$$Ly=b\Rightarrow y=(1,0,2)^\top;\qquad Dz=y\Rightarrow z=(1,0,\tfrac23)^\top;\qquad Ux=z\Rightarrow x=\Big(\tfrac13,-\tfrac23,\tfrac23\Big)^\top .$$
细节：$y_1=1$，$y_2=2-2\cdot1=0$，$y_3=3-1-3\cdot0=2$；$z=y/(1,2,3)=(1,0,\frac23)$；回代 $x_3=\frac23$，$x_2=z_2-x_3=-\frac23$，$x_1=z_1-x_2-2x_3=1+\frac23-\frac43=\frac13$。
验算 $Ax$：第一行 $\frac13-\frac23+\frac43=1$ ✓；第二行 $\frac23-\frac83+4=2$ ✓；第三行 $\frac13-\frac{14}{3}+\frac{22}{3}=3$ ✓。
（与 (3) 的 $A^{-1}b$ 一致：$\frac13+\;1\cdot\frac12\cdot2-\frac13\cdot3=\frac13+1-1=\frac13$ ✓。）

**(5)** $A$ 的**顺序主子式**全不为零：$\Delta_1=1,\ \Delta_2=\begin{vmatrix}1&1\\2&4\end{vmatrix}=2,\ \Delta_3=\det A=6$，故每一步主元 $\Delta_k/\Delta_{k-1}=1,2,3$ 非零，消元无需行交换。等价说法：$A$ 的前 $k$ 列在前 $k$ 行构成的子方阵都可逆。
反例见题 25：若 $(1,1)$ 元为 $0$（如 $A=\begin{pmatrix}0&2&1\\1&1&1\\2&1&2\end{pmatrix}$，$\Delta_1=0$），不交换行就没有 $LU$ 分解，必须引入 $P$。

**涉及知识点**　第 7 节：消元阵乘积 $U_{\text{tri}}=EA$、$L=E^{-1}$；第 8 节：LU/LDU 分解、乘子入 $L$、$D$ 为主元对角阵；第 7 节：$(XYZ)^{-1}=Z^{-1}Y^{-1}X^{-1}$、用分解求解三段式；第 9 节：顺序主子式与不需行交换的分解；第 11 节：$\det A$ 与主元之积。

---

## 题 16　最简行阶梯形、$C(A)$ 与 $N(A)$ 的基、$Ax=b$ 全解

$A=\begin{pmatrix}1&2&0&-1&0\\ 2&4&1&1&0\\ 1&2&3&8&1\\ 0&0&1&3&2\end{pmatrix}$（$4\times5$）。

**(1)** 消元与回代化简（$r_2-2r_1,\ r_3-r_1$；再处理第 3、5 列）得最简行阶梯形
$$R=\begin{pmatrix}1&2&0&-1&0\\ 0&0&1&3&0\\ 0&0&0&0&1\\ 0&0&0&0&0\end{pmatrix}.$$
主元列为 **1、3、5**（每行的第一个非零元所在列），自由列为 **2、4**；非零行数 $=3$，故 $r(A)=3$，自由变量个数 $5-3=2$。

**(2)** $C(A)$ 的基 = **$A$ 中对应主元列的那些列**（不是 $R$ 的列！行变换改变列空间，但主元列本身保持无关）：
$$\Big\{\ \alpha_1=\begin{pmatrix}1\\2\\1\\0\end{pmatrix},\ \alpha_3=\begin{pmatrix}0\\1\\3\\1\end{pmatrix},\ \alpha_5=\begin{pmatrix}0\\0\\1\\2\end{pmatrix}\ \Big\},\qquad \dim C(A)=3 .$$
$R$ 的其余列把自由列用主元列表示出来，给出 $A$ 中同样的关系（行变换保持列间线性关系）：
$$\text{col}_2(R)=2\,\text{col}_1(R)\ \Rightarrow\ \alpha_2=2\alpha_1;\qquad
\text{col}_4(R)=-\text{col}_1(R)+3\,\text{col}_3(R)\ \Rightarrow\ \alpha_4=-\alpha_1+3\alpha_3 .$$
验证：$\alpha_2=(2,4,2,0)^\top=2\alpha_1$ ✓；$-\alpha_1+3\alpha_3=(-1,-2,-1,0)+(0,3,9,3)=(-1,1,8,3)=\alpha_4$ ✓。

**(3)** 由 $R=[\,I_3\ F\,]$ 型（主元列已排成 $I_3$，$F=\begin{pmatrix}2&-1\\0&3\\0&0\end{pmatrix}$ 是第 2、4 列），零空间基按 $N=\binom{-F}{I_2}$ 读出：
$$\Big\{\ n_1=\begin{pmatrix}-2\\1\\0\\0\\0\end{pmatrix},\quad n_2=\begin{pmatrix}1\\0\\-3\\1\\0\end{pmatrix}\ \Big\},\qquad \dim N(A)=2 .$$
验证 $An_1$：$-2\alpha_1+\alpha_2=-2\alpha_1+2\alpha_1=0$ ✓；$An_2=\alpha_1-3\alpha_3+\alpha_4=\alpha_1-3\alpha_3+(-\alpha_1+3\alpha_3)=0$ ✓。
维数关系：$\dim C(A)+\dim N(A)=3+2=5=$ 列数 $n$ ✓（秩–零化度定理）。
又 $\dim N(A^\top)=4-3=1$，$N(A^\top)$ 的基由 $R(A^\top)$ 读出为 $\big(-8,\,5,\,-2,\,1\big)^\top$（见 (4)）。

**(4)** 对 $[A\mid b]$ 作同样的行变换，右端化为 $(c_1,c_2,c_3,c_4)^\top$，其中（逐行按 $A$ 的行组合系数计算，并已用具体 $b$ 验算）
$$c_1=b_1,\qquad c_2=b_2-2b_1,\qquad c_3=5b_1-3b_2+b_3,\qquad c_4=-8b_1+5b_2-2b_3+b_4 .$$
最后一行是 $0=c_4$，故
$$Ax=b\ \text{有解}\ \Longleftrightarrow\ -8b_1+5b_2-2b_3+b_4=0\ \Longleftrightarrow\ b\perp N(A^\top)\ \Longleftrightarrow\ b\in C(A).$$
有解时全解（$x_2=s,\ x_4=t$ 自由）：
$$x=\underbrace{\begin{pmatrix}b_1\\ 0\\ b_2-2b_1\\ 0\\ 5b_1-3b_2+b_3\end{pmatrix}}_{\text{特解}}
+s\begin{pmatrix}-2\\1\\0\\0\\0\end{pmatrix}+t\begin{pmatrix}1\\0\\-3\\1\\0\end{pmatrix},\qquad s,t\in\mathbb R .$$

**(5)** $b=(2,8,15,6)^\top$：条件 $-16+40-30+6=0$ ✓ 有解；特解 $(2,\,0,\,8-4,\,0,\,10-24+15)=(2,0,4,0,1)^\top$，全解
$$x=\begin{pmatrix}2\\0\\4\\0\\1\end{pmatrix}+s\begin{pmatrix}-2\\1\\0\\0\\0\end{pmatrix}+t\begin{pmatrix}1\\0\\-3\\1\\0\end{pmatrix}.$$
验算 $A(2,0,4,0,1)^\top$：第一行 $2+0+0+0+0=2$ ✓；第二行 $4+4+0+0+0=8$ ✓；第三行 $2+12+8+1=15$ ✓；第四行 $4+3+2=6$ ✓。
**条件与 $N(A^\top),C(A)$ 的关系**：$\boldsymbol y=(-8,5,-2,1)^\top$ 满足 $A^\top\boldsymbol y=0$（逐列核对：第 1 列 $-8+10-2+0=0$ ✓，第 3 列 $-8\cdot0+5\cdot1-2\cdot3+1\cdot1=0$ ✓，第 5 列 $-2+2=0$ ✓）。对任何 $x$，$\boldsymbol y\cdot Ax=(A^\top\boldsymbol y)\cdot x=0$，故 $b\in C(A)\Rightarrow \boldsymbol y\cdot b=0$；反之 $\boldsymbol y\cdot b=0$ 即 $c_4=0$，消元不再出现矛盾行，解存在。这正是 $C(A)=N(A^\top)^\perp$（第 10 节正交补观点）。

**涉及知识点**　第 4 节：消元到 $R$、主元列与自由列；第 11 节：$N(A)$ 的基 $\big(\begin{smallmatrix}-F\\I\end{smallmatrix}\big)$、自由变量个数；第 10 节：$C(A)$ 的基（$A$ 的主元列）、$b\in C(A)$ 判相容；第 12 节：$r(A)=$ 非零行数 $=\dim C(A)$、$\dim C(A)+\dim N(A)=n$、行秩=列秩、$C(A)=N(A^\top)^\perp$；第 6 节：行变换保持列间线性关系。

---

## 题 17　$\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}$

设 $A$ 为 $m\times n$，$B$ 为 $n\times p$。

**(第一个不等号，列空间)** 由题 13(1)，$C(AB)\subset C(A)$。两边取维数：
$$\operatorname{rank}(AB)=\dim C(AB)\le\dim C(A)=\operatorname{rank}(A).$$
直观：$AB$ 的每列都是 $A$ 的列的组合，列空间不可能超出 $A$ 的列空间。

**(第二个不等号，零空间)** 由题 13(3)，$N(B)\subset N(AB)$（同为 $\mathbb R^p$ 的子空间），故 $\dim N(B)\le\dim N(AB)$。对 $B$（$n\times p$）与 $AB$（$m\times p$）分别用「主元个数 $+$ 自由变量个数 $=$ 列数 $p$」：
$$\operatorname{rank}(B)=p-\dim N(B)\ \ge\ p-\dim N(AB)=\operatorname{rank}(AB),$$
即 $\operatorname{rank}(AB)\le\operatorname{rank}(B)$（注意维数不等式取负后方向翻转）。

**(3)** 两式合并：$\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}$。

**(另证第二式，转置法)** $(AB)^\top=B^\top A^\top$，对它们用第一式：
$$\operatorname{rank}(B)=\operatorname{rank}(B^\top)\ \ge\ \operatorname{rank}(B^\top A^\top)=\operatorname{rank}\big((AB)^\top\big)=\operatorname{rank}(AB),$$
其中用到了行秩 $=$ 列秩（$\operatorname{rank}(M^\top)=\operatorname{rank}(M)$）。$\blacksquare$

**(4)** 两个不等号可**同时**严格：取 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\ B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$，则 $AB=O$，
$$\operatorname{rank}(AB)=0<1=\min\{1,1\}=\min\{\operatorname{rank}A,\operatorname{rank}B\}.$$
原因：$B$ 的列空间 $S(\boldsymbol e_1)$ 经 $A$ 作用后……更准确地说，$B$ 的第 1 列 $\boldsymbol e_2$ 落在 $N(A)$ 里（$A\boldsymbol e_2=0$），$B$ 的第 2 列是零列，故像全部被杀死。
单侧严格也可各自发生：取 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$（$\operatorname{rank}=1$）、$B=\begin{pmatrix}1&0\\0&0\end{pmatrix}$（$\operatorname{rank}=1$），则 $AB=B$，$\operatorname{rank}(AB)=1=\operatorname{rank}A$ 而 $B$ 换成 $B'=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix}_{2\times3}$（$\operatorname{rank}B'=1$）时 $AB'=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix}$ 仍有 $\operatorname{rank}=1$——真正的差别在零空间：$\dim N(B')=2$、$\dim N(AB')=2$，第二式取等。要第二式严格而第一式取等，可取 $A=\begin{pmatrix}0&1\\0&0\end{pmatrix},\ B=\begin{pmatrix}1&0\\0&0\end{pmatrix}$：$AB=\begin{pmatrix}0&0\\0&0\end{pmatrix}$……直接核验更简单的是 $A=\begin{pmatrix}0&1\end{pmatrix}_{1\times2},\ B=\binom{1}{0}$：$\operatorname{rank}A=1$（第一式取等），$\operatorname{rank}B=1$，而 $AB=(0)$，$\operatorname{rank}(AB)=0$（第二式严格）。

**推论**：$A$ 可逆 $\Rightarrow\operatorname{rank}(AB)=\operatorname{rank}B$；$B$ 可逆 $\Rightarrow\operatorname{rank}(AB)=\operatorname{rank}A$（与题 13(2) 的 $C(AB)=C(A)$ 一致）。

**涉及知识点**　第 9 节：$(AB)^\top=B^\top A^\top$；第 11 节：零空间维数 $=n-r$；第 12 节：秩的三种定义（主元个数 = 非零行数 = 列空间维数）与行秩=列秩；第 10 节：子空间包含 $\Rightarrow$ 维数不等式；第 6 节：可逆阵乘积的秩。

---

## 题 18　$\begin{pmatrix}I&O\\ B&C\end{pmatrix}$ 可逆 $\iff C$ 可逆

设 $B$ 为 $n\times m$、$C$ 为 $n\times n$，$I=I_m$，记 $M=\begin{pmatrix}I_m&O\\ B&C\end{pmatrix}$。

**(充分性，构造法)** 若 $C$ 可逆，断言
$$M^{-1}=\begin{pmatrix}I_m&O\\ -C^{-1}B&C^{-1}\end{pmatrix}.$$
逐块相乘验证 $MM^{-1}$：左上 $I\cdot I+O=I_m$；右上 $I\cdot O+O\cdot C^{-1}=O$；左下 $B\cdot I+C(-C^{-1}B)=B-B=O$；右下 $B\cdot O+CC^{-1}=I_n$。故 $MM^{-1}=I$ ✓。
再验证 $M^{-1}M$：左上 $I+O=I_m$；右上 $O$；左下 $-C^{-1}B\cdot I+C^{-1}B=O$；右下 $-C^{-1}B\cdot O+C^{-1}C=I_n$ ✓。两侧皆为 $I$，故确为逆矩阵。

**(必要性)** 设 $M$ 可逆，$W=M^{-1}=\begin{pmatrix}W_{11}&W_{12}\\ W_{21}&W_{22}\end{pmatrix}$（$W_{11}$ 为 $m\times m$）。由 $MW=I$ 的**上排**块等式：
$$W_{11}=I_m,\quad W_{12}=O;$$
下排右块等式：$BW_{12}+CW_{22}=I_n$，即 $CW_{22}=I_n$。$C$ 与 $W_{22}$ 都是 $n\times n$ 方阵且 $CW_{22}=I$，由课件**定理 2**（方阵有右逆即有左逆，$AB=I\Rightarrow BA=I$）知 $C$ 可逆，且 $C^{-1}=W_{22}$。$\blacksquare$
（再由下排左块 $BW_{11}+CW_{21}=O$ 得 $CW_{21}=-B$，两边左乘 $C^{-1}$ 得 $W_{21}=-C^{-1}B$——这同时**推出**了上面构造的逆矩阵，说明逆必为那个形式。）

**(第三种证法：分块消元 + 行列式)** 用分块消元阵（题 14(3)）左乘：
$$\begin{pmatrix}I_m&O\\ -B&I_n\end{pmatrix}\begin{pmatrix}I_m&O\\ B&C\end{pmatrix}=\begin{pmatrix}I_m&O\\ O&C\end{pmatrix}.$$
左端第一个因子行列式为 $1$（单位下三角），故 $\det M=\det\begin{pmatrix}I&O\\O&C\end{pmatrix}=\det C$。于是 $M$ 可逆 $\iff\det M\ne0\iff\det C\ne0\iff C$ 可逆。$\blacksquare$
这也是题 30 的舒尔补特例：对 $M=\begin{pmatrix}A&B\\ C&D\end{pmatrix}$ 取 $A=I_m,\ B=O$，舒尔补 $D-CA^{-1}B=C-BI^{-1}O=C$。

**(变式)** 一般分块下三角：$\begin{pmatrix}A&O\\ E&D\end{pmatrix}$（$A,D$ 均方阵）可逆 $\iff A,D$ 都可逆，且
$$\begin{pmatrix}A&O\\ E&D\end{pmatrix}^{-1}=\begin{pmatrix}A^{-1}&O\\ -D^{-1}EA^{-1}&D^{-1}\end{pmatrix}.$$
分块反三角（副对角）：$\begin{pmatrix}O&A\\ B&O\end{pmatrix}^{-1}=\begin{pmatrix}O&B^{-1}\\ A^{-1}&O\end{pmatrix}$，可逆 $\iff A,B$ 都可逆。

**涉及知识点**　第 6 节：分块矩阵乘法；第 7 节：逆矩阵定义（双侧验证）、定理 2「方阵 $AB=I\Rightarrow BA=I$」；第 9 节：$\det$ 与可逆性、分块（三角）阵行列式 $=$ 对角块行列式之积；第 5 节：分块消元阵；题 30 的舒尔补。

---

## 题 19　$I_m-AB$ 可逆 $\iff I_n-BA$ 可逆

设 $A$ 为 $m\times n$、$B$ 为 $n\times m$。

**(1)** 设 $I_m-AB$ 可逆，断言
$$(I_n-BA)^{-1}=I_n+B\,(I_m-AB)^{-1}A .$$
**右侧验证**：记 $T=(I_m-AB)^{-1}$，把四项重新分组，并分别使用 $(I_m-AB)T=I_m$ 与 $T(I_m-AB)=I_m$：
$$(I_n-BA)(I_n+BTA)=I_n+BTA-BA-B(AB)TA=I_n-BA+B\,(I_m-AB)\,TA=I_n-BA+BA=I_n\ \checkmark$$
**左侧验证**：
$$(I_n+BTA)(I_n-BA)=I_n-BA+BTA-BT(AB)A=I_n-BA+BT\,(I_m-AB)\,A=I_n-BA+BA=I_n\ \checkmark$$
故 $I_n-BA$ 可逆，其逆正是 $I_n+B(I_m-AB)^{-1}A$。反向同理（$A,B$ 角色与 $m,n$ 互换）：$(I_m-AB)^{-1}=I_m+A(I_n-BA)^{-1}B$。$\blacksquare$
（注意 $AB$ 是 $m\times m$ 而 $BA$ 是 $n\times n$，阶数通常不同，故不能直接比较 $AB$ 与 $BA$，只能在两者之间「穿一件 $A,B$ 的外衣」。）

**(2)** 用 $(m+n)$ 阶分块阵 $N=\begin{pmatrix}I_m&A\\ B&I_n\end{pmatrix}$ 的两种消元：
$$\begin{pmatrix}I_m&O\\ -B&I_n\end{pmatrix}N=\begin{pmatrix}I_m&A\\ O&I_n-BA\end{pmatrix}\tag{I}$$
$$N\begin{pmatrix}I_m&-A\\ O&I_n\end{pmatrix}=\begin{pmatrix}I_m-AB&O\\ B&I_n\end{pmatrix}\tag{II}$$
（(I) 左下块：$-B\cdot I_m+I_n\cdot B=O$，右下块：$-BA+I_n$ ✓；(II) 右上块：$-A+A=O$，左上块：$I_m-AB$ ✓。）
两式左/右乘的都是行列式为 $1$ 的可逆分块三角阵，而分块三角阵可逆 $\iff$ 其对角块都可逆，故
$$N\ \text{可逆}\ \iff\ I_n-BA\ \text{可逆}\quad(\text{由 (I)}),\qquad
N\ \text{可逆}\ \iff\ I_m-AB\ \text{可逆}\quad(\text{由 (II)}),$$
两者等价，即 $I_m-AB$ 可逆 $\iff I_n-BA$ 可逆。$\blacksquare$
同时取行列式：$\det N=\det(I_n-BA)=\det(I_m-AB)$，顺带得到
$$\boxed{\det(I_m-AB)=\det(I_n-BA)}$$
（这正是「$AB$ 与 $BA$ 有相同的非零特征值，其余用 $0$ 补齐」的行列式形式）。

**(3)** 取 $A=\begin{pmatrix}1&0&0\end{pmatrix}_{1\times3}$、$B=(1,1,0)^\top_{3\times1}$：
$$AB=(1)\ \Rightarrow\ I_1-AB=(0),$$
$$BA=\begin{pmatrix}1&0&0\\ 1&0&0\\ 0&0&0\end{pmatrix}\ \Rightarrow\ I_3-BA=\begin{pmatrix}0&0&0\\ -1&1&0\\ 0&0&1\end{pmatrix}.$$
$I_1-AB$ 是零矩阵不可逆；$I_3-BA$ 第一行全为零，也没有 3 个主元，不可逆 ✓ 两侧结论一致。
（$AB$ 的特征值 $1$ 与 $BA$ 的特征值 $1$ 同时出现，使 $1$ 成为 $\det(I-\cdot)$ 的零点。）

**正例补充**：取 $A=\begin{pmatrix}1&0\end{pmatrix}_{1\times2}$、$B=\binom{2}{0}$，则 $I_1-AB=(-1)$ 可逆，$I_2-BA=\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ 可逆，而公式给出
$$I_2+B(I_1-AB)^{-1}A=\begin{pmatrix}1&0\\0&1\end{pmatrix}+\binom{2}{0}(-1)\begin{pmatrix}1&0\end{pmatrix}=\begin{pmatrix}-1&0\\0&1\end{pmatrix}=\left(I_2-BA\right)^{-1}\ \checkmark$$

**涉及知识点**　第 6、9 节：分块矩阵乘法与分块消元阵、分块三角阵的行列式；第 7 节：逆的双侧验证、可逆 $\iff$ 满秩 $\iff\det\ne0$；第 9 节：$\det(I-AB)=\det(I-BA)$；题 18 的同型技巧。

---
<!-- CONTINUE -->

