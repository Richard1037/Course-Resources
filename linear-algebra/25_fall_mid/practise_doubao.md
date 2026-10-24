# 高等代数 I · 配套练习题（la-02 ~ la-12）

> 解答见 `sol_doubao.md`。每题下方留空作答。

---

**1.**　设 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix},\ x=\begin{pmatrix}-1\\2\end{pmatrix}$。分别用列观点和行观点计算 $Ax$。

<br><br><br><br><br><br>

---

**2.**　判断下列矩阵是否可逆，说明理由：
$$(a)\ \begin{pmatrix}1&2\\2&4\end{pmatrix};\qquad (b)\ \begin{pmatrix}1&0&2\\0&1&3\\0&0&1\end{pmatrix};\qquad (c)\ \begin{pmatrix}0&1\\1&0\end{pmatrix}.$$

<br><br><br><br><br><br>

---

**3.**　设 $A=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix}$。对任意 $b=(b_1,b_2,b_3)^\top$，解 $Ax=b$，写出 $A^{-1}$，并验证 $AA^{-1}=I_3$。

<br><br><br><br><br><br><br><br>

---

**4.**　(1) 判断 $u=(1,2,3)^\top,\ v=(2,4,6)^\top,\ w=(3,6,9)^\top$ 是否线性相关；
(2) 证明：若 $a_1,a_2,a_3$ 线性无关，则 $a_1+a_2,\ a_2+a_3,\ a_3+a_1$ 也线性无关。

<br><br><br><br><br><br><br><br>

---

**5.**　对方程组 $\begin{cases}x+2y=5\\2x-y=0\end{cases}$：
(1) 行观点：写出两直线法向量并求交点；
(2) 列观点：令 $u=(1,2)^\top,\ v=(2,-1)^\top,\ b=(5,0)^\top$，把 $b$ 写成 $u,v$ 的线性组合；
(3) 求系数矩阵 $A=\begin{pmatrix}1&2\\2&-1\end{pmatrix}$ 的逆，并用 $x=A^{-1}b$ 验证。

<br><br><br><br><br><br><br><br>

---

**6.**　判断下列方程组解的个数（唯一解 / 无解 / 无穷多解），并用行观点解释：
$$(a)\ \begin{cases}x-y=1\\2x-2y=2\end{cases};\qquad (b)\ \begin{cases}x-y=1\\2x-2y=3\end{cases};\qquad (c)\ \begin{cases}x-y=1\\x+y=3\end{cases}.$$

<br><br><br><br><br><br>

---

**7.**　给定 $x=(1,2,-1)^\top$，分别计算 $Dx,\ Lx,\ Ux$，其中
$$D=\begin{pmatrix}3&0&0\\0&-1&0\\0&0&2\end{pmatrix},\quad
L=\begin{pmatrix}1&0&0\\2&1&0\\0&3&1\end{pmatrix},\quad
U=\begin{pmatrix}1&2&0\\0&1&3\\0&0&1\end{pmatrix}.$$

<br><br><br><br><br><br>

---

**8.**　写出增广矩阵，用高斯消元法求解 $\begin{cases}2x-y=3\\x+3y=5\end{cases}$。

<br><br><br><br><br><br><br><br>

---

**9.**　已知 $\begin{cases}x+2y=3\\2x+(4+k)y=6\end{cases}$。讨论 $k$ 取何值时方程组有唯一解、无解或无穷多解，并写出通解。

<br><br><br><br><br><br><br><br>

---

**10.**　用高斯消元法求解
$$\begin{cases}x+y+z=6\\2x-y+z=3\\x+2y-z=5\end{cases}.$$

<br><br><br><br><br><br><br><br><br><br>

---

**11.**　设 $A=\begin{pmatrix}a&b\\c&d\\e&f\end{pmatrix}$。
(1) 写出 $E_{21}(2)$，并计算 $E_{21}(2)A$；
(2) 写出 $P_{13}$，并计算 $P_{13}A$。

<br><br><br><br><br><br>

---

**12.**　设 $A=\begin{pmatrix}1&0\\1&1\end{pmatrix},\ B=\begin{pmatrix}1&1\\0&1\end{pmatrix}$，计算 $AB$ 与 $BA$。

<br><br><br><br><br><br>

---

**13.**　设 $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$。计算 $A^2$，并猜想 $A^n$ 的一般形式（用归纳法验证）。

<br><br><br><br><br><br><br><br>

---

**14.**　用行-列角度和列-列角度分别计算
$$A=\begin{pmatrix}1&0&2\\0&1&1\end{pmatrix},\quad B=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}.$$

<br><br><br><br><br><br><br><br>

---

**15.**　将矩阵按 $2\times2$ 分块：
$$A=\begin{pmatrix}I_2&O\\A_{21}&I_2\end{pmatrix},\quad A_{21}=\begin{pmatrix}1&0\\0&2\end{pmatrix},$$
$$B=\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix},\
B_{11}=\begin{pmatrix}1&1\\0&1\end{pmatrix},\ B_{12}=\begin{pmatrix}2&0\\1&1\end{pmatrix},\
B_{21}=\begin{pmatrix}1&0\\0&1\end{pmatrix},\ B_{22}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$
用分块乘法计算 $AB$。

<br><br><br><br><br><br><br><br><br><br>

---

**16.**　证明：若 $A,B$ 均为 $n$ 阶上三角矩阵，则 $AB$ 也是上三角矩阵，且 $(AB)_{ii}=A_{ii}B_{ii}$。

<br><br><br><br><br><br><br><br><br><br>

---

**17.**　用增广矩阵 $[A\mid I]$ 的 Gauss-Jordan 消元求 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ 的逆，并验证。

<br><br><br><br><br><br><br><br><br><br>

---

**18.**　判断下列矩阵是否可逆；若可逆，写出逆矩阵：
$$(a)\ \begin{pmatrix}2&0&0\\0&3&0\\0&0&4\end{pmatrix};\qquad
(b)\ \begin{pmatrix}0&0&2\\0&3&0\\4&0&0\end{pmatrix};\qquad
(c)\ \begin{pmatrix}1&2&3\\2&4&6\\1&2&3\end{pmatrix}.$$

<br><br><br><br><br><br><br><br>

---

**19.**　(1) 若 $A,B$ 均可逆，证明 $AB$ 可逆且 $(AB)^{-1}=B^{-1}A^{-1}$；
(2) 若 $AB=I_n$，证明 $BA=I_n$。

<br><br><br><br><br><br><br><br><br><br>

---

**20.**　对 $A=\begin{pmatrix}1&1&0\\4&6&1\\-2&2&0\end{pmatrix}$，写出高斯消元过程，得到 $A=LU$，并验证。

<br><br><br><br><br><br><br><br><br><br><br><br>

---

**21.**　设 $A=\begin{pmatrix}1&1&1\\1&2&2\\1&2&3\end{pmatrix}$。
(1) 求 $A$ 的 LU 分解；
(2) 求 $L^{-1}$ 和 $U^{-1}$；
(3) 求 $A^{-1}=U^{-1}L^{-1}$，并验证 $AA^{-1}=I_3$。

<br><br><br><br><br><br><br><br><br><br><br><br>

---

**22.**　沿用第 21 题的 $A$，分别求解：
(1) $Ax=\begin{pmatrix}3\\5\\6\end{pmatrix}$；
(2) $Ax=\begin{pmatrix}4\\5\\6\end{pmatrix}$。

<br><br><br><br><br><br><br><br>

---

**23.**　设 $A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix},\ B=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}$。
(1) 写出 $A^\top$；
(2) 计算 $AB$ 与 $(AB)^\top$，验证 $(AB)^\top=B^\top A^\top$。

<br><br><br><br><br><br><br><br>

---

**24.**　判断下列矩阵是否对称：
$$(a)\ \begin{pmatrix}1&2\\2&3\end{pmatrix};\qquad (b)\ \begin{pmatrix}1&2\\3&4\end{pmatrix}.$$
证明：对任意 $A$，$A^\top A$ 与 $AA^\top$ 都是对称矩阵。

<br><br><br><br><br><br><br><br><br><br>

---

**25.**　对对称矩阵 $S=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$ 进行 $LDL^\top$ 分解（写出 $L,D$）。

<br><br><br><br><br><br><br><br><br><br>

---

**26.**　设 $P=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}$。
(1) $PA$ 对 $A$ 的行做了什么？
(2) 求 $P^{-1}$；
(3) 计算 $P^3$。

<br><br><br><br><br><br><br><br>

---

**27.**　判断下列集合是否为 $\mathbb R^2$ 的子空间，说明理由：
$$(a)\ W=\{(x,y):x+y=0\};\qquad
(b)\ W=\{(x,y):x+y=1\};$$
$$(c)\ W=\{(x,y):xy\ge0\};\qquad
(d)\ W=\{2\times2\text{ 对称矩阵全体}\}.$$

<br><br><br><br><br><br><br><br><br><br>

---

**28.**　设 $A=\begin{pmatrix}1&2\\2&4\\1&2\end{pmatrix}$。
(1) 求 $C(A)$ 的一组基和 $\dim C(A)$；
(2) 判断 $b=(3,6,3)^\top$ 是否在 $C(A)$ 中；
(3) 判断 $b=(1,0,0)^\top$ 是否在 $C(A)$ 中。

<br><br><br><br><br><br><br><br>

---

**29.**　设 $v_1=(1,0,0)^\top,\ v_2=(0,1,0)^\top,\ v_3=(1,1,0)^\top$。$S(v_1,v_2,v_3)$ 是什么几何图形？它是 $\mathbb R^3$ 的子空间吗？$\dim$ 是多少？

<br><br><br><br><br><br><br><br>

---

**30.**　设 $A=\begin{pmatrix}1&2&3\\2&4&6\end{pmatrix}$。
(1) 用高斯消元将 $A$ 化为行阶梯形；
(2) 找出自由变量；
(3) 写出 $N(A)$ 的一组基。

<br><br><br><br><br><br><br><br><br><br>

---

**31.**　设 $A=\begin{pmatrix}1&1&2&3\\2&2&8&10\\3&3&10&13\end{pmatrix}$。
(1) 将 $A$ 化为最简行阶梯形 $R$；
(2) 指出主元列与自由列；
(3) 写出 $N(A)$ 的一组基。

<br><br><br><br><br><br><br><br><br><br><br><br>

---

**32.**　设 $A$ 是 $3\times5$ 矩阵。证明：$Ax=0$ 必有非零解。若 $\mathrm{rank}\,A=2$，求 $\dim N(A)$。

<br><br><br><br><br><br><br><br>

---

**33.**　设 $A=\begin{pmatrix}2&0&4&6\\-1&1&2&2\\1&1&6&8\end{pmatrix}$。
(1) 化为最简行阶梯形 $R$；
(2) 求 $\mathrm{rank}\,A$；
(3) 写出 $N(A)$ 的一组基。

<br><br><br><br><br><br><br><br><br><br><br><br>

---

**34.**　设 $A=\begin{pmatrix}3&6&6\\1&2&2\\4&8&8\end{pmatrix}$。
(1) 求 $\mathrm{rank}\,A$；
(2) 找非零向量 $u\in\mathbb R^3,\ v\in\mathbb R^3$ 使 $A=uv^\top$。

<br><br><br><br><br><br><br><br>

---

**35.**　证明：对任意可乘矩阵 $A_{m\times n},\ B_{n\times p}$，
$$\mathrm{rank}(AB)\le\min\{\mathrm{rank}\,A,\ \mathrm{rank}\,B\}.$$

<br><br><br><br><br><br><br><br><br><br>

---

**36.**　设 $A$ 是 $m\times n$ 矩阵，$\mathrm{rank}\,A=r$。写出 $\dim C(A)$、$\dim C(A^\top)$、$\dim N(A)$，并验证 $\dim C(A)+\dim N(A)=n$。

<br><br><br><br><br><br><br><br>

---

**37.**　证明：对任意 $A_{m\times n},\ B_{n\times p}$，$C(AB)\subset C(A)$；若 $B$ 可逆，则 $C(AB)=C(A)$。

<br><br><br><br><br><br><br><br><br><br>

---

**38.**　(1) 证明 $\begin{pmatrix}I&O\\B&C\end{pmatrix}$ 可逆当且仅当 $C$ 可逆，并求其逆；
(2) 证明：$I_m-AB$ 可逆当且仅当 $I_n-BA$ 可逆。

<br><br><br><br><br><br><br><br><br><br><br><br>
