# 高等代数 I · 配套练习题解答（la-02 ~ la-12）

> 对应 `practise_doubao.md`，题号 1～38。每题标注【章节】与【知识点】。

---

**1.**　【第 2 节 · 矩阵向量乘法的列观点与行观点】

列观点：$Ax=(-1)a_1+2a_2=(-1)\begin{pmatrix}1\\3\end{pmatrix}+2\begin{pmatrix}2\\4\end{pmatrix}=\begin{pmatrix}3\\5\end{pmatrix}$。
行观点：第一行 $(1,2)\cdot(-1,2)=3$；第二行 $(3,4)\cdot(-1,2)=5$。
$Ax=(3,5)^\top$。

**2.**　【第 2 节 · 可逆矩阵判据（$Ax=0$ 是否只有零解）】

(a) 不可逆。$Ax=0$ 有非零解 $(-2,1)^\top$。
(b) 可逆。上三角对角元均非零，$Ax=0$ 只有零解。
(c) 可逆。交换矩阵 $G^2=I$，故 $G^{-1}=G$。

**3.**　【第 2 节 · 按定义求逆矩阵】

解 $Ax=b$：$x_1=b_1,\ x_2=b_2-b_1,\ x_3=b_3-b_2$。
$$A^{-1}=\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\end{pmatrix}.$$

**4.**　【第 2 节 · 线性相关 / 无关的定义与判定】

(1) $v=2u,\ w=3u$，线性相关。
(2) 设 $c_1(a_1+a_2)+c_2(a_2+a_3)+c_3(a_3+a_1)=0$，整理得 $(c_1+c_3)a_1+(c_1+c_2)a_2+(c_2+c_3)a_3=0$。由 $a_1,a_2,a_3$ 无关，系数全为 0，解得 $c_1=c_2=c_3=0$。$\blacksquare$

**5.**　【第 3 节 · 行观点与列观点、逆矩阵】

(1) 法向量 $(1,2)^\top,\ (2,-1)^\top$ 不共线，交点 $(1,2)$。
(2) $u+2v=(5,0)=b$，系数 $(1,2)$。
(3) $\det A=-5$，$A^{-1}=\begin{pmatrix}\frac15&\frac25\\[2pt]\frac25&-\frac15\end{pmatrix}$，$A^{-1}b=(1,2)$。$\checkmark$

**6.**　【第 3 节 · 三种解的情况】

(a) 无穷多解（两直线重合）；(b) 无解（平行不相交）；(c) 唯一解 $(2,1)$。

**7.**　【第 3 节 · 特殊矩阵乘向量的作用】

$$Dx=\begin{pmatrix}3\\-2\\-2\end{pmatrix},\quad Lx=\begin{pmatrix}1\\4\\5\end{pmatrix},\quad Ux=\begin{pmatrix}5\\-1\\-1\end{pmatrix}.$$

**8.**　【第 4 节 · 增广矩阵高斯消元、行交换】

$$\begin{pmatrix}2&-1&3\\1&3&5\end{pmatrix}\xrightarrow{R_1\leftrightarrow R_2}\begin{pmatrix}1&3&5\\0&-7&-7\end{pmatrix}.$$
回代：$y=1,\ x=2$。

**9.**　【第 4 节 · 含参数方程组解的讨论】

消元得 $\begin{pmatrix}1&2&3\\0&k&0\end{pmatrix}$。$k\ne0$ 唯一解 $(3,0)$；$k=0$ 无穷多解 $(3-2t,t)$。

**10.**　【第 4 节 · 三阶方程组高斯消元、回代】

消元后 $\begin{pmatrix}1&1&1&6\\0&1&-2&-1\\0&0&-7&-12\end{pmatrix}$。回代：$z=\frac{12}{7},\ y=\frac{17}{7},\ x=\frac{13}{7}$。

**11.**　【第 5 节 · 初等矩阵与置换矩阵的左乘作用】

(1) $E_{21}(2)=\begin{pmatrix}1&0&0\\2&1&0\\0&0&1\end{pmatrix}$，$E_{21}(2)A=\begin{pmatrix}a&b\\2a+c&2b+d\\e&f\end{pmatrix}$。
(2) $P_{13}=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}$，$P_{13}A=\begin{pmatrix}e&f\\c&d\\a&b\end{pmatrix}$。

**12.**　【第 5 节 · 矩阵乘法、$AB\ne BA$】

$$AB=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad BA=\begin{pmatrix}2&1\\1&1\end{pmatrix}.$$

**13.**　【第 5 节 · 矩阵幂与归纳法】

$A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}$，猜想 $A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$，归纳成立。$\blacksquare$

**14.**　【第 6 节 · 矩阵乘法的行-列视角与列-列视角】

$$AB=\begin{pmatrix}11&14\\8&10\end{pmatrix}.$$

**15.**　【第 6 节 · 分块矩阵乘法】

$$AB=\left(\begin{array}{cc|cc}1&1&2&0\\0&1&1&1\\ \hline 2&1&2&1\\0&3&3&2\end{array}\right).$$

**16.**　【第 6 节 · 上三角矩阵乘积的封闭性】

$(AB)_{ij}=\sum_k a_{ik}b_{kj}$。当 $i>j$：$k\le j$ 时 $b_{kj}=0$；$k\ge i$ 时 $a_{ik}=0$。故 $(AB)_{ij}=0$。对角元 $(AB)_{ii}=a_{ii}b_{ii}$。$\blacksquare$

**17.**　【第 7 节 · Gauss-Jordan 消元求逆】

$$A^{-1}=\begin{pmatrix}-2&1\\[2pt]\frac32&-\frac12\end{pmatrix}.$$

**18.**　【第 7 节 · 可逆性判断、对角阵与反对角阵求逆】

(a) 可逆，$A^{-1}=\mathrm{diag}(\frac12,\frac13,\frac14)$。
(b) 可逆，$A^{-1}=\begin{pmatrix}0&0&\frac14\\0&\frac13&0\\\frac12&0&0\end{pmatrix}$。
(c) 不可逆，$\mathrm{rank}\,A=1<3$。

**19.**　【第 7 节 · 乘积的逆、$AB=I\Rightarrow BA=I$】

(1) $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=I$。
(2) 若 $A$ 不可逆，则存在可逆 $M$ 使 $MA$ 末行全零，左乘 $M$ 于 $AB=I$ 得 $M=(MA)B$ 末行也全零，矛盾。$\blacksquare$

**20.**　【第 8 节 · LU 分解】

$$L=\begin{pmatrix}1&0&0\\4&1&0\\-2&2&1\end{pmatrix},\quad U=\begin{pmatrix}1&1&0\\0&2&1\\0&0&-2\end{pmatrix}.$$

**21.**　【第 8 节 · LU 分解、三角矩阵求逆、$A^{-1}=U^{-1}L^{-1}$】

$$L=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix},\quad U=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}.$$
$$L^{-1}=\begin{pmatrix}1&0&0\\-1&1&0\\0&-1&1\end{pmatrix},\quad U^{-1}=\begin{pmatrix}1&-1&0\\0&1&-1\\0&0&1\end{pmatrix}.$$
$$A^{-1}=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}.$$

**22.**　【第 8 节 · 基于 LU 的方程组求解】

(1) $y=(3,2,1)$，$x=(1,1,1)$。
(2) $y=(4,1,1)$，$x=(3,0,1)$。

**23.**　【第 9 节 · 转置定义、$(AB)^\top=B^\top A^\top$】

$$A^\top=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix},\quad AB=\begin{pmatrix}22&28\\49&64\end{pmatrix},\quad (AB)^\top=\begin{pmatrix}22&49\\28&64\end{pmatrix}=B^\top A^\top.$$

**24.**　【第 9 节 · 对称矩阵判定、$A^\top A$ 与 $AA^\top$ 对称】

(a) 对称；(b) 不对称。$(A^\top A)^\top=A^\top A$，$(AA^\top)^\top=AA^\top$。$\blacksquare$

**25.**　【第 9 节 · 对称矩阵的 $LDL^\top$ 分解】

$$L=\begin{pmatrix}1&0&0\\-\frac12&1&0\\0&-\frac23&1\end{pmatrix},\quad D=\mathrm{diag}\left(2,\frac32,\frac43\right).$$

**26.**　【第 9 节 · 排列矩阵的作用、$P^{-1}=P^\top$】

(1) $PA$ 将 $A$ 的行按 $(1,2,3)\to(3,1,2)$ 循环重排。
(2) $P^{-1}=P^\top=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}$。
(3) $P^3=I$。

**27.**　【第 10 节 · 线性子空间的判定】

(a) 是；(b) 不是（不含零向量）；(c) 不是（$(2,1)+(-1,-2)=(1,-1)\notin W$）；(d) 是。

**28.**　【第 10 节 · 列空间 $C(A)$、基与维数、$Ax=b$ 有解条件】

(1) $a_2=2a_1$，$C(A)=\mathrm{span}\{(1,2,1)^\top\}$，$\dim C(A)=1$。
(2) $(3,6,3)^\top=3a_1\in C(A)$，有解。
(3) $(1,0,0)^\top\notin C(A)$，无解。

**29.**　【第 10 节 · 张成空间、子空间维数】

$v_3=v_1+v_2$，$S(v_1,v_2,v_3)=\mathrm{span}\{v_1,v_2\}$，即 $z=0$ 的 $xy$ 平面，是 $\mathbb R^3$ 的二维子空间，$\dim=2$。

**30.**　【第 11 节 · 零空间 $N(A)$、自由变量】

$$R=\begin{pmatrix}1&2&3\\0&0&0\end{pmatrix},\quad N(A)=\mathrm{span}\left\{\begin{pmatrix}-2\\1\\0\end{pmatrix},\begin{pmatrix}-3\\0\\1\end{pmatrix}\right\}.$$

**31.**　【第 11 节 · 最简行阶梯形、主元列 / 自由列、构造特解】

$$R=\begin{pmatrix}1&1&0&1\\0&0&1&1\\0&0&0&0\end{pmatrix},\quad N(A)=\mathrm{span}\{(-1,1,0,0)^\top,\ (-1,0,-1,1)^\top\}.$$

**32.**　【第 11 节 · $m<n\Rightarrow Ax=0$ 有非零解、维数公式】

主元个数 $r\le3<5$，至少 $2$ 个自由变量，必有非零解。$\dim N(A)=5-2=3$。

**33.**　【第 12 节 · RREF、秩、零空间基】

$$R=\begin{pmatrix}1&0&2&3\\0&1&4&5\\0&0&0&0\end{pmatrix},\quad \mathrm{rank}\,A=2,\quad N(A)=\mathrm{span}\{(-2,-4,1,0)^\top,\ (-3,-5,0,1)^\top\}.$$

**34.**　【第 12 节 · 秩 1 分解 $A=uv^\top$】

(1) $\mathrm{rank}\,A=1$。
(2) $u=(3,1,4)^\top$，$v=(1,2,2)^\top$，$uv^\top=A$。

**35.**　【第 12 节 · 秩不等式 $\mathrm{rank}(AB)\le\min\{\mathrm{rank}\,A,\mathrm{rank}\,B\}$】

由 $C(AB)\subset C(A)$，$\mathrm{rank}(AB)\le\mathrm{rank}\,A$；由 $(AB)^\top=B^\top A^\top$，$\mathrm{rank}(AB)\le\mathrm{rank}\,B$。$\blacksquare$

**36.**　【第 12 节 · 秩-零化度定理】

$\dim C(A)=r$，$\dim C(A^\top)=r$，$\dim N(A)=n-r$。$r+(n-r)=n$。

**37.**　【第 10、12 节 · 列空间包含关系 $C(AB)\subset C(A)$、可逆保持列空间（考试三）】

$AB$ 的第 $j$ 列 $=Ab_j\in C(A)$，故 $C(AB)\subset C(A)$。若 $B$ 可逆，$A=(AB)B^{-1}$，同理 $C(A)\subset C(AB)$。$\blacksquare$

**38.**　【第 7、9 节 · 分块矩阵可逆性、$I_m-AB\iff I_n-BA$（考试八）】

(1) 方程等价于 $x=u,\ Cy=v-Bu$。对任意 $v$ 有唯一解 $y\iff C$ 可逆。逆矩阵 $\begin{pmatrix}I&O\\-C^{-1}B&C^{-1}\end{pmatrix}$。
(2) 若 $I_m-AB$ 可逆，令 $X=I_n+B(I_m-AB)^{-1}A$，验证 $(I_n-BA)X=I_n$。反之对称。$\blacksquare$
