# 高等代数 I · 期中专项练习（2025 秋季）

> **编制依据**
> - **试卷**：`25fall_mid.pdf` —— 中国人民大学《高等代数 I》2025 年第一学期期中考试（2025 年 11 月 4 日 10:00–11:30），共 8 道大题。
> - **课件**：第 1–12 节全套讲义
>   | 节次 | 文件 | 主题 |
>   |---|---|---|
>   | 1 | `1/1.md` | 向量引论：向量空间、线性组合、内积、模长、施瓦茨不等式 |
>   | 2 | `2/la-02-slide.pdf` | 矩阵与线性方程组、行列观点、可逆、线性相关/无关 |
>   | 3 | `3/la-03-slide.pdf` | 线性方程组的行观点与列观点、特殊矩阵 |
>   | 4 | `4/la-04-slide.pdf` | 高斯消元法、主元、增广矩阵、主元个数与解的情况 |
>   | 5 | `5/la-05-slide.pdf` | 初等矩阵 $E_{ij}(\lambda)$、$P_{ij}$、矩阵加法与数乘、矩阵乘法两种视角、矩阵的幂 |
>   | 6 | `6/la-06-slide.pdf` | 矩阵乘法四种视角、分块矩阵乘法 |
>   | 7 | `7/la-07-slide.pdf` | 矩阵的逆、唯一性、$(\alpha A)^{-1}$ 类法则、Gauss–Jordan 求逆、可逆判定 |
>   | 8 | `8/la-08-slide.pdf` | $A=LU$ 分解、基于 LU 分解解方程组、运算次数 |
>   | 9 | `9/la-09-slide.pdf` | 转置、对称矩阵、$A=LDL^{\mathsf T}$、排列矩阵、$PA=LU$、分块消元与舒尔补 |
>   | 10 | `10/la-10-slide.pdf` | 线性空间、子空间、张成空间、列空间 $C(A)$ 与行空间 $C(A^{\mathsf T})$ |
>   | 11 | `11/la-11-slide.pdf` | 零空间 $N(A)$、主元变量与自由变量、特解 |
>   | 12 | `12/la-12-slide.pdf` | 最简行阶梯形 RREF、列关系、零空间结构、矩阵的秩 |
>
> **使用说明**：全套共 **38 题**，其中「第一部分」8 题与试卷 8 道大题**一一对应**（每题的题号、小问都仿照原卷，数值全部更换）；「第二部分」17 题按课件第 5–9 节（矩阵运算、逆、LU/LDU 分解）编制；「第三部分」9 题按课件第 10–12 节（子空间、零空间、秩）编制；「第四部分」4 题为跨节综合与证明。
> 每题都给出【完整解答】与【涉及知识点 / 对应课件】，便于对照复习。

---

## 目录

- [第一部分　期中仿真卷（8 题，对应试卷八大题）](#第一部分期中仿真卷8-题对应试卷八大题)
- [第二部分　矩阵运算、逆与 LU/LDU 分解（17 题）](#第二部分矩阵运算逆与-luldu-分解17-题)
- [第三部分　子空间、零空间与秩（9 题）](#第三部分子空间零空间与秩9-题)
- [第四部分　综合与证明（4 题）](#第四部分综合与证明4-题)
- [附录 A　公式与定理速查](#附录-a公式与定理速查)
- [附录 B　试卷题型 → 练习题对照表](#附录-b试卷题型--练习题对照表)
- [附录 C　自检清单](#附录-c自检清单)

---

# 第一部分　期中仿真卷（8 题，对应试卷八大题）

## 练习 1　数乘、列空间维数与子空间判定

> 【对应试卷第一题】原卷：$A=\begin{pmatrix}2&-1&0\\1&3&-2\\-1&0&4\end{pmatrix}$；本练习更换数值。

已知
$$
A=\begin{pmatrix}1&2&1\\0&1&1\\1&1&0\end{pmatrix}
=\big(\alpha_1\ \ \alpha_2\ \ \alpha_3\big).
$$

1. 对任意 $a\in\mathbb R$，求 $aA$；并求 $3A-I_3$；
2. 求 $\dim C(A)$ 与 $\dim C(A^{\mathsf T})$；
3. 判断 $\operatorname{span}\{\alpha_1,\alpha_2\}$ 是否为 $\mathbb R^3$ 的子空间，并说明理由。

**【涉及知识点】** 矩阵数乘（第 5 节）；列空间 $C(A)$、行空间 $C(A^{\mathsf T})$ 与维数、秩（第 10、12 节）；张成空间与子空间判定（第 10 节）。
**【对应课件】** `la-05-slide`、`la-10-slide`、`la-12-slide`。

**【解答】**

**1.** 数乘即逐元素相乘：
$$
aA=\begin{pmatrix}a&2a&a\\0&a&a\\a&a&0\end{pmatrix},
\qquad
3A-I_3=\begin{pmatrix}3&6&3\\0&3&3\\3&3&0\end{pmatrix}-\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}
=\begin{pmatrix}2&6&3\\0&2&3\\3&3&-1\end{pmatrix}.
$$

**2.** 对 $A$ 做行化简求主元个数（$=\operatorname{rank}A$）：
$$
\begin{pmatrix}1&2&1\\0&1&1\\1&1&0\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_1}
\begin{pmatrix}1&2&1\\0&1&1\\0&-1&-1\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3+R_2}
\begin{pmatrix}1&2&1\\0&1&1\\0&0&0\end{pmatrix}.
$$
有两个主元，故 $\operatorname{rank}A=2$。事实上第 3 列满足
$$
\alpha_3=(1,1,0)^{\mathsf T}=(2,1,1)^{\mathsf T}-(1,0,1)^{\mathsf T}=\alpha_2-\alpha_1
\quad\Longleftrightarrow\quad \alpha_1-\alpha_2+\alpha_3=0 ,
$$
即三列线性相关。于是
$$
\dim C(A)=\operatorname{rank}A=2,\qquad
\dim C(A^{\mathsf T})=\operatorname{rank}A^{\mathsf T}=\operatorname{rank}A=2 .
$$
（**列空间与行空间维数相等**，都等于主元个数。）

**3.** 是子空间。理由：张成空间
$$
\operatorname{span}\{\alpha_1,\alpha_2\}=\{\lambda_1\alpha_1+\lambda_2\alpha_2:\lambda_1,\lambda_2\in\mathbb R\}
$$
中任取 $u=\lambda_1\alpha_1+\lambda_2\alpha_2,\ v=\mu_1\alpha_1+\mu_2\alpha_2$ 及 $c\in\mathbb R$，则
$$
u+v=(\lambda_1+\mu_1)\alpha_1+(\lambda_2+\mu_2)\alpha_2\in\operatorname{span}\{\alpha_1,\alpha_2\},\qquad
cu=(c\lambda_1)\alpha_1+(c\lambda_2)\alpha_2\in\operatorname{span}\{\alpha_1,\alpha_2\},
$$
且 $0=0\cdot\alpha_1+0\cdot\alpha_2$ 属于其中。故对加法、数乘封闭，是 $\mathbb R^3$ 的子空间。
**一般结论**：任意有限个向量的张成空间必为子空间（第 10 节定义 4 后的性质）。

---

## 练习 2　循环移位矩阵的幂

> 【对应试卷第二题】原卷：$A=\begin{pmatrix}0&2&0&0\\0&0&2&0\\0&0&0&2\\2&0&0&0\end{pmatrix}$，求 $A^2,A^3,A^4$；本练习更换标量。

已知
$$
A=\begin{pmatrix}0&3&0&0\\0&0&3&0\\0&0&0&3\\3&0&0&0\end{pmatrix}.
$$
分别求 $A^2,\ A^3,\ A^4$，并说明 $A$ 与 $A^4$ 的关系。

**【涉及知识点】** 矩阵的幂 $A^n=A\cdot A^{n-1}$、$A^0=I$（第 5 节）；列-列观点；置换矩阵（第 9 节）。
**【对应课件】** `la-05-slide`（矩阵的幂）、`la-09-slide`（排列矩阵）。

**【解答】**

记 $P$ 为将基向量循环右移一位的置换矩阵
$$
P=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\end{pmatrix},
\qquad A=3P .
$$
由矩阵幂的性质 $(cP)^n=c^nP^n$，只需算 $P^n$。用**列-列观点**：$P=[p_1,p_2,p_3,p_4]$，其中 $p_1=e_2,\ p_2=e_3,\ p_3=e_4,\ p_4=e_1$（$e_i$ 为标准单位向量）。于是 $Pe_1=p_1=e_2$，$Pe_2=p_2=e_3$，$Pe_3=p_3=e_4$，$Pe_4=p_4=e_1$，即 $P$ 把 $e_i\mapsto e_{i+1}$（下标模 4）。故
$$
P^2=[Pe_1,Pe_2,Pe_3,Pe_4]=[e_3,e_4,e_1,e_2],\quad
P^3=[e_4,e_1,e_2,e_3],\quad
P^4=[e_1,e_2,e_3,e_4]=I_4 .
$$
写成矩阵（本题 $c=3$）：
$$
A^2=3^2P^2=9\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix}
=\begin{pmatrix}0&0&9&0\\0&0&0&9\\9&0&0&0\\0&9&0&0\end{pmatrix},
$$
$$
A^3=27\begin{pmatrix}0&0&0&1\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}
=\begin{pmatrix}0&0&0&27\\27&0&0&0\\0&27&0&0\\0&0&27&0\end{pmatrix},
$$
$$
A^4=3^4P^4=81\,I_4=\begin{pmatrix}81&0&0&0\\0&81&0&0\\0&0&81&0\\0&0&0&81\end{pmatrix}.
$$

> **小结**：$A=3P$ 中 $P$ 是 4 阶循环移位置换矩阵，满足 $P^4=I$，故 $A^4=3^4I=81I$，即 $A^3=81A^{-1}$（因为 $A\cdot A^3=A^4=81I$，所以 $A^{-1}=\frac1{81}A^3=\frac{27}{81}P^3=\frac13P^3$）。
> 原卷的 $c=2$ 时同理得 $A^4=16I_4$。**关键**：先识别 $A=cP$，再用 $(cP)^n=c^nP^n$。

---

## 练习 3　分块矩阵乘法

> 【对应试卷第四题】原卷：$A=\begin{pmatrix}I_2&O\\A_1&I_2\end{pmatrix}$，$A_1=\begin{pmatrix}-1&2\\1&1\end{pmatrix}$；本练习更换分块数值。

已知
$$
A=\left(\begin{array}{cc|cc}1&0&0&0\\0&1&0&0\\\hline 2&-1&1&0\\-3&1&0&1\end{array}\right)
=\begin{pmatrix}I_2&O\\A_1&I_2\end{pmatrix},
\qquad
B=\left(\begin{array}{cc|cc}1&0&3&2\\-1&2&0&1\\\hline 1&0&4&1\\-1&-1&2&0\end{array}\right)
=\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix},
$$
其中 $A_1=\begin{pmatrix}2&-1\\-3&1\end{pmatrix}$。用**分块乘法**求 $AB$。

**【涉及知识点】** 分块矩阵乘法 $C_{ij}=\sum_k A_{ik}B_{kj}$（第 6 节）；单位块与零块的作用。
**【对应课件】** `la-06-slide`。

**【解答】**

按 $2\times2$ 分块相乘（要求 $A$ 的**列分块**与 $B$ 的**行分块**一致，此处都是 $2+2$）：
$$
AB=\begin{pmatrix}I_2B_{11}+OB_{21}&I_2B_{12}+OB_{22}\\A_1B_{11}+I_2B_{21}&A_1B_{12}+I_2B_{22}\end{pmatrix}
=\begin{pmatrix}B_{11}&B_{12}\\A_1B_{11}+B_{21}&A_1B_{12}+B_{22}\end{pmatrix}.
$$
（用到 $I_2X=X$、$OX=O$。）

其中
$$
B_{11}=\begin{pmatrix}1&0\\-1&2\end{pmatrix},\quad
B_{12}=\begin{pmatrix}3&2\\0&1\end{pmatrix},\quad
B_{21}=\begin{pmatrix}1&0\\-1&-1\end{pmatrix},\quad
B_{22}=\begin{pmatrix}4&1\\2&0\end{pmatrix}.
$$

左下块：
$$
A_1B_{11}=\begin{pmatrix}2&-1\\-3&1\end{pmatrix}\begin{pmatrix}1&0\\-1&2\end{pmatrix}
=\begin{pmatrix}2+1&0-2\\-3-1&0+2\end{pmatrix}
=\begin{pmatrix}3&-2\\-4&2\end{pmatrix},
$$
$$
A_1B_{11}+B_{21}=\begin{pmatrix}3&-2\\-4&2\end{pmatrix}+\begin{pmatrix}1&0\\-1&-1\end{pmatrix}
=\begin{pmatrix}4&-2\\-5&1\end{pmatrix}.
$$

右下块：
$$
A_1B_{12}=\begin{pmatrix}2&-1\\-3&1\end{pmatrix}\begin{pmatrix}3&2\\0&1\end{pmatrix}
=\begin{pmatrix}6&4-1\\-9&-6+1\end{pmatrix}
=\begin{pmatrix}6&3\\-9&-5\end{pmatrix},
$$
$$
A_1B_{12}+B_{22}=\begin{pmatrix}6&3\\-9&-5\end{pmatrix}+\begin{pmatrix}4&1\\2&0\end{pmatrix}
=\begin{pmatrix}10&4\\-7&-5\end{pmatrix}.
$$

故
$$
AB=\left(\begin{array}{cc|cc}1&0&3&2\\-1&2&0&1\\\hline 4&-2&10&4\\-5&1&-7&-5\end{array}\right).
$$

> **验算**：直接按普通矩阵乘法计算 $AB$（$4\times4$）得到完全相同的结果，可见分块乘法只是把同一批运算"打包"。**要点**：只要各块维度相容，分块乘法完全照搬普通乘法公式；$I$ 块与 $O$ 块可直接消去。

---

## 练习 4　LDU 分解与求逆

> 【对应试卷第五题】原卷：$A=\begin{pmatrix}1&1&1\\1&2&2\\1&3&4\end{pmatrix}$；本练习更换数值。

已知
$$
A=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}.
$$

1. 求 $A$ 的 LDU 分解（$A=LDU$，$L$ 为单位下三角、$D$ 为对角阵、$U$ 为单位上三角）；
2. 求 $L^{-1},\ D^{-1},\ U^{-1}$；
3. 求 $A^{-1}$。

**【涉及知识点】** 高斯消元的矩阵化（第 5 节初等矩阵）；无行交换消元 $\Leftrightarrow$ LU 分解（第 8 节）；对称形式 $A=LD\tilde U$（第 8、9 节）；三角矩阵求逆。
**【对应课件】** `la-05-slide`、`la-08-slide`、`la-09-slide`。

**【解答】**

**1. 消元求 $L,D,U$。** 不用行交换即可找到 3 个主元，做高斯消元：
$$
A=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}
\xrightarrow[R_3\leftarrow R_3-4R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}2&1&1\\0&1&1\\0&3&5\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-3R_2}
\begin{pmatrix}2&1&1\\0&1&1\\0&0&2\end{pmatrix}.
$$
两个消元乘子为 $l_{21}=2,\ l_{31}=4,\ l_{32}=3$，故
$$
L=\begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}.
$$
把上三角的对角元提出得到
$$
D=\operatorname{diag}(2,1,2),\qquad
U=\begin{pmatrix}1&\tfrac12&\tfrac12\\0&1&1\\0&0&1\end{pmatrix}.
$$
**验证**：
$$
LDU=\begin{pmatrix}1&0&0\\2&1&0\\4&3&1\end{pmatrix}
\begin{pmatrix}2&0&0\\0&1&0\\0&0&2\end{pmatrix}
\begin{pmatrix}1&\tfrac12&\tfrac12\\0&1&1\\0&0&1\end{pmatrix}
=\begin{pmatrix}2&1&1\\4&3&3\\8&7&9\end{pmatrix}=A.\quad\checkmark
$$

**2. 三个逆矩阵。**

- **单位下三角**逐列回代（或直接观察乘子取负）：
$$
L^{-1}=\begin{pmatrix}1&0&0\\-2&1&0\\2&-3&1\end{pmatrix}
\qquad\Big(L L^{-1}=I_3\Big).
$$
（第三行由 $-4+2\cdot3=2$ 与 $-3$ 得到，与第 7 节 $E_{ij}(\lambda)^{-1}=E_{ij}(-\lambda)$ 的思路一致：消元顺序颠倒后乘子会叠加。）
- **对角阵**取倒数：
$$
D^{-1}=\operatorname{diag}\!\left(\tfrac12,\ 1,\ \tfrac12\right)
=\begin{pmatrix}\tfrac12&0&0\\0&1&0\\0&0&\tfrac12\end{pmatrix}.
$$
- **单位上三角**：
$$
U^{-1}=\begin{pmatrix}1&-\tfrac12&0\\0&1&-1\\0&0&1\end{pmatrix}
\qquad\Big(UU^{-1}=I_3\Big).
$$

**3. 求 $A^{-1}$。** 由 $A^{-1}=U^{-1}D^{-1}L^{-1}$，先算 $D^{-1}L^{-1}$：
$$
D^{-1}L^{-1}=\begin{pmatrix}\tfrac12&0&0\\0&1&0\\0&0&\tfrac12\end{pmatrix}
\begin{pmatrix}1&0&0\\-2&1&0\\2&-3&1\end{pmatrix}
=\begin{pmatrix}\tfrac12&0&0\\-2&1&0\\1&-\tfrac32&\tfrac12\end{pmatrix},
$$
再左乘 $U^{-1}$：
$$
A^{-1}=U^{-1}\big(D^{-1}L^{-1}\big)
=\begin{pmatrix}1&-\tfrac12&0\\0&1&-1\\0&0&1\end{pmatrix}
\begin{pmatrix}\tfrac12&0&0\\-2&1&0\\1&-\tfrac32&\tfrac12\end{pmatrix}
=\begin{pmatrix}\tfrac32&-\tfrac12&0\\-3&\tfrac52&-\tfrac12\\1&-\tfrac32&\tfrac12\end{pmatrix}.
$$
**验算**：$A\cdot A^{-1}=I_3$（如第一行：$2\cdot\frac32+1\cdot(-3)+1\cdot1=1$；$2\cdot(-\frac12)+1\cdot\frac52+1\cdot(-\frac32)=0$；$1\cdot(-\frac12)+1\cdot(-\frac12)=0$ ✓）。

> **小结**：LDU 三步走——①消元得乘子 $l_{ij}$ 与上三角；②提出对角元得 $D$ 与单位上三角 $U$；③逆序求逆 $A^{-1}=U^{-1}D^{-1}L^{-1}$。三角矩阵的逆仍为同型三角矩阵。

---

## 练习 5　最简行阶梯形、列空间基、零空间基与全解

> 【对应试卷第六题】原卷：$A=\begin{pmatrix}0&3&-2&4&1\\0&0&5&-3&6\\7&0&0&8&4\\7&3&3&9&3\end{pmatrix}$（$4\times5$）；本练习改用 $4\times4$ 的秩 3 矩阵，使"有解条件"更典型。

已知
$$
A=\begin{pmatrix}1&0&0&4\\0&1&0&4\\0&0&1&3\\-1&-2&1&-9\end{pmatrix}.
$$

1. 求 $A$ 的最简行阶梯形 $R$；
2. 求 $C(A)$ 的一组基；
3. 求 $N(A)$ 的一组基；
4. 对任意 $b=(b_1,b_2,b_3,b_4)^{\mathsf T}$，说明 $Ax=b$ 有解的条件，并在有解时给出方程的全解。

**【涉及知识点】** Gauss–Jordan 消元到 RREF（第 11、12 节）；主元列张成 $C(A)$；自由变量参数化 $N(A)$；非齐次全解 $=$ 特解 $+$ 齐次通解。
**【对应课件】** `la-11-slide`、`la-12-slide`。

**【解答】**

**1.** 记第 4 行为 $r_4$。消去第 1 列的 $-1$：
$$
\xrightarrow{R_4\leftarrow R_4+R_1}
\begin{pmatrix}1&0&0&4\\0&1&0&4\\0&0&1&3\\0&-2&1&-5\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4+2R_2}
\begin{pmatrix}1&0&0&4\\0&1&0&4\\0&0&1&3\\0&0&1&3\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-R_3}
\begin{pmatrix}1&0&0&4\\0&1&0&4\\0&0&1&3\\0&0&0&0\end{pmatrix}=R.
$$
$R$ 已是 RREF，主元在第 $1,2,3$ 列，$\operatorname{rank}A=3$。

**2.** 主元列对应的**原矩阵列**构成 $C(A)$ 的基（第 12 节：$P A=R$ 中 $P$ 可逆，故 $A$ 的列与 $R$ 的列有完全相同的线性关系）：
$$
C(A)=\operatorname{span}\left\{\begin{pmatrix}1\\0\\0\\-1\end{pmatrix},\
\begin{pmatrix}0\\1\\0\\-2\end{pmatrix},\
\begin{pmatrix}0\\0\\1\\1\end{pmatrix}\right\},
\qquad \dim C(A)=3 .
$$
这三列线性无关（对应 $R$ 的三个主元列）。

**3.** 解 $Ax=0$。由 $R$ 得方程组
$$
x_1+4x_4=0,\qquad x_2+4x_4=0,\qquad x_3+3x_4=0 .
$$
第 4 列是自由列，令 $x_4=t$：
$$
x_1=-4t,\quad x_2=-4t,\quad x_3=-3t
\;\Longrightarrow\;
x=t\begin{pmatrix}-4\\-4\\-3\\1\end{pmatrix}.
$$
故
$$
N(A)=\operatorname{span}\left\{\begin{pmatrix}-4\\-4\\-3\\1\end{pmatrix}\right\},
\qquad \dim N(A)=1 .
$$
（验证秩-零化度：$\dim C(A)+\dim N(A)=3+1=4=n$ ✓）

**4. 有解条件。** 关键观察：第 4 行 $=$ 第 1 行 $+$ 第 2 行 $-$ 第 3 行，即
$$
(-1,-2,1,-9)=(1,0,0,4)+(0,1,0,4)-(0,0,1,3).
$$
用行向量 $y^{\mathsf T}=(1,2,-1,1)$ 左乘 $A$：
$$
y^{\mathsf T}A=(1,2,-1,1)\begin{pmatrix}1&0&0&4\\0&1&0&4\\0&0&1&3\\-1&-2&1&-9\end{pmatrix}=(0,0,0,0),
$$
即 $y$ 属于 $A^{\mathsf T}$ 的零空间（$A$ 的**左零空间**）。于是 $Ax=b$ 有解的必要条件为
$$
y^{\mathsf T}b=0,\qquad\text{即}\qquad \boxed{\,b_1+2b_2-b_3+b_4=0\,}.
$$
这条件也是充分的：把 $b$ 增广后消元，第 4 行化作 $(0,0,0,0\mid b_1+2b_2-b_3+b_4)$，无矛盾行当且仅当该式为 $0$。故
$$
Ax=b \text{ 有解}\iff b\in C(A)\iff b_1+2b_2-b_3+b_4=0 .
$$

**全解。** 取特解：令 $x_4=0$（取自由变量为 $0$），由 $R$ 立刻得
$$
x_p=\begin{pmatrix}b_1\\b_2\\b_3\\0\end{pmatrix}.
$$
（由 $Rx=b'$ 直接读出，其中 $b'$ 是消元后的右端；在有解条件下 $Rx=b'$ 的前三行为 $x_i=b_i$。）
验证取 $b=(1,1,2,-1)^{\mathsf T}$（满足 $1+2-2-1=0$）：
$$
Ax_p=\begin{pmatrix}1&0&0&4\\0&1&0&4\\0&0&1&3\\-1&-2&1&-9\end{pmatrix}\begin{pmatrix}1\\1\\2\\0\end{pmatrix}
=\begin{pmatrix}1\\1\\2\\-1\end{pmatrix}=b.\quad\checkmark
$$
于是**全解**为
$$
x=x_p+t\begin{pmatrix}-4\\-4\\-3\\1\end{pmatrix}
=\begin{pmatrix}b_1-4t\\b_2-4t\\b_3-3t\\t\end{pmatrix},
\qquad t\in\mathbb R .
$$
（**结构**：特解 $+$ 零空间通解。当 $b_1+2b_2-b_3+b_4\ne0$ 时，如 $b=(1,2,3,4)^{\mathsf T}$ 有 $1+4-3+4=6\ne0$，方程组无解。）

> **小结**：① RREF 的主元列对应原矩阵中线性无关的列，构成 $C(A)$ 的基；② 自由变量个数 $=\dim N(A)=n-\operatorname{rank}A$；③ 有解条件可用**左零空间**向量 $y$（满足 $y^{\mathsf T}A=0$）写成 $y^{\mathsf T}b=0$；④ 非齐次全解 $=$ 特解 $+$ 齐次通解。

---

## 练习 6　秩不等式的证明

> 【对应试卷第七题】原卷：求证 $\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}$。

1. 对任意 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times p}$，求证
$$
\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\ \operatorname{rank}B\}.
$$
2. 举例说明等号可以成立，也可以不成立：取
$$
A=\begin{pmatrix}1&2&3\\2&4&6\\1&1&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\2&1\\3&1\end{pmatrix},
$$
求 $\operatorname{rank}A,\operatorname{rank}B,\operatorname{rank}(AB)$，并验证上述不等式。

**【涉及知识点】** $\operatorname{rank}X=\dim C(X)$（第 12 节）；列空间包含关系（第 6 节列-列观点）；$\operatorname{rank}X=\operatorname{rank}X^{\mathsf T}$（第 9、12 节）。
**【对应课件】** `la-06-slide`、`la-09-slide`、`la-10-slide`、`la-12-slide`。

**【解答】**

**1. 证明。**

**第一步**：证明 $C(AB)\subset C(A)$。记 $A=[a_1,\dots,a_n]$，$B=[b_1,\dots,b_p]$。由矩阵乘法的**列-列观点**，$AB$ 的第 $j$ 列为
$$
(AB)_{\cdot j}=A\,b_j=b_{1j}a_1+b_{2j}a_2+\cdots+b_{nj}a_n,
$$
即 $A$ 的各列的线性组合，故 $(AB)_{\cdot j}\in C(A)$。$C(AB)$ 中任一向量都是这些列的线性组合，从而是 $C(A)$ 中向量的线性组合；而 $C(A)$ 是子空间，故仍属于 $C(A)$。因此
$$
C(AB)\subset C(A).
$$
对上式取维数（子空间维数不超过大空间维数）：
$$
\operatorname{rank}(AB)=\dim C(AB)\le\dim C(A)=\operatorname{rank}A. \tag{1}
$$

**第二步**：利用转置得到关于 $B$ 的不等式。因为 $\operatorname{rank}X=\operatorname{rank}X^{\mathsf T}$（转置不改变秩，见第 9、12 节），且 $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$，把第一步的结论用于矩阵对 $(B^{\mathsf T},A^{\mathsf T})$：
$$
C\big(B^{\mathsf T}A^{\mathsf T}\big)\subset C\big(B^{\mathsf T}\big)
\;\Longrightarrow\;
\operatorname{rank}\big(B^{\mathsf T}A^{\mathsf T}\big)\le\operatorname{rank}\big(B^{\mathsf T}\big).
$$
而 $B^{\mathsf T}A^{\mathsf T}=(AB)^{\mathsf T}$，$\operatorname{rank}((AB)^{\mathsf T})=\operatorname{rank}(AB)$，$\operatorname{rank}(B^{\mathsf T})=\operatorname{rank}B$，故
$$
\operatorname{rank}(AB)\le\operatorname{rank}B. \tag{2}
$$

合并 (1)(2) 即得
$$
\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}.\qquad\blacksquare
$$

**2. 例子。**

取
$$
A=\begin{pmatrix}1&2&3\\2&4&6\\1&1&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\2&1\\3&1\end{pmatrix}.
$$
$A$ 的第 2 行 $=2\times$ 第 1 行，故 $\operatorname{rank}A=2$（第 1、3 行不成比例）。$B$ 的两列不成比例，$\operatorname{rank}B=2$。计算
$$
AB=\begin{pmatrix}1&2&3\\2&4&6\\1&1&1\end{pmatrix}\begin{pmatrix}1&0\\2&1\\3&1\end{pmatrix}
=\begin{pmatrix}1+4+9&0+2+3\\2+8+18&0+4+6\\1+2+3&0+1+1\end{pmatrix}
=\begin{pmatrix}14&5\\28&10\\6&2\end{pmatrix}.
$$
第 2 行 $=2\times$ 第 1 行，故 $\operatorname{rank}(AB)=2$。于是
$$
\operatorname{rank}(AB)=2=\min\{2,2\},
$$
等号成立。
**等号不成立的例子**：取 $A=\begin{pmatrix}1&0\\0&0\end{pmatrix}$，$B=\begin{pmatrix}0&0\\0&1\end{pmatrix}$，则 $\operatorname{rank}A=\operatorname{rank}B=1$，但 $AB=O$，$\operatorname{rank}(AB)=0<1$。可见不等式一般是严格的。

---

## 练习 7　分块矩阵的可逆性与 $I-AB$

> 【对应试卷第八题】原卷第 1 问：求证分块矩阵 $\begin{pmatrix}I&O\\B&C\end{pmatrix}$ 可逆当且仅当 $C$ 可逆；第 2 问：求证 $I_m-AB$ 可逆当且仅当 $I_n-BA$ 可逆。

**1.** 设 $C$ 为 $n$ 阶方阵，$B$ 为 $n\times m$ 矩阵。求证：分块矩阵
$$
S=\begin{pmatrix}I_m&O\\B&C\end{pmatrix}
$$
可逆当且仅当 $C$ 可逆，并在可逆时求出 $S^{-1}$。

**2.** 对任意 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times m}$，求证：$I_m-AB$ 可逆当且仅当 $I_n-BA$ 可逆；且当二者可逆时
$$
\big(I_n-BA\big)^{-1}=I_n+B\big(I_m-AB\big)^{-1}A .
$$

**3.**（数值验证）取
$$
A=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\in\mathbb R^{3\times2},\qquad
B=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}\in\mathbb R^{2\times3},
$$
求 $I_3-AB$、$I_2-BA$，验证二者都可逆并检验第 2 问的公式。

**【涉及知识点】** 可逆的定义（对任意 $b$，$Ax=b$ 有唯一解，第 2 节）；分块乘法（第 6 节）；"构造逆并验证"的技巧。
**【对应课件】** `la-02-slide`、`la-06-slide`、`la-07-slide`。

**【解答】**

**1.** 设 $I_m$ 为 $m$ 阶。**充分性**：若 $C$ 可逆，直接验证
$$
\begin{pmatrix}I_m&O\\B&C\end{pmatrix}
\begin{pmatrix}I_m&O\\-C^{-1}B&C^{-1}\end{pmatrix}
=\begin{pmatrix}I_m&O\\B-C&\,O+CC^{-1}\end{pmatrix}
$$
更清楚地逐块计算：
$$
\text{左上}=I_m,\quad \text{右上}=O,\quad
\text{左下}=B\cdot I_m+C\cdot(-C^{-1}B)=B-B=O,\quad
\text{右下}=B\cdot O+C\cdot C^{-1}=I_n .
$$
故
$$
S^{-1}=\begin{pmatrix}I_m&O\\-C^{-1}B&C^{-1}\end{pmatrix}.
$$

**必要性**：设 $S$ 可逆。利用**可逆定义的"唯一解"刻画**：对任意右端 $\begin{pmatrix}u\\v\end{pmatrix}$，方程
$$
\begin{pmatrix}I_m&O\\B&C\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}u\\v\end{pmatrix}
\iff\begin{cases}x=u,\\ Bx+Cy=v\end{cases}
$$
当 $S$ 可逆时有唯一解。特别地取 $u=0$，则 $x=0$，于是 $Cy=v$ 对**任意** $v\in\mathbb R^n$ 有唯一解 $y$。这正是"$C$ 可逆"的定义。$\blacksquare$

**2. 证明。** 先证"$\Longleftarrow$"：设 $I_m-AB$ 可逆。**构造**候选逆矩阵并验证：
$$
\big(I_n-BA\big)\Big[I_n+B\big(I_m-AB\big)^{-1}A\Big]
=I_n-BA+B\big(I_m-AB\big)^{-1}A-BAB\big(I_m-AB\big)^{-1}A .
$$
把后两项合并（分配律，注意 $BAB(I_m-AB)^{-1}A=B\big[AB(I_m-AB)^{-1}\big]A$）：
$$
=I_n-BA+B\Big[I_m-AB\Big]\big(I_m-AB\big)^{-1}A
=I_n-BA+BA=I_n .
$$
（第三步用了 $[I_m-AB](I_m-AB)^{-1}=I_m$。）因此 $I_n-BA$ 可逆且
$$
\big(I_n-BA\big)^{-1}=I_n+B\big(I_m-AB\big)^{-1}A .
$$
"$\Longrightarrow$"：把 $A,B$ 的地位对调、$m,n$ 互换（并注意 $(BA)$ 与 $(AB)$ 的维数互换），由刚证的方向即得：若 $I_n-BA$ 可逆，则 $I_m-AB$ 可逆且
$$
\big(I_m-AB\big)^{-1}=I_m+A\big(I_n-BA\big)^{-1}B .
$$
故二者可逆性等价。$\blacksquare$

**3. 数值验证。** 先算
$$
AB=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}
=\begin{pmatrix}1&2&3\\3&4&7\\5&6&11\end{pmatrix},
\qquad
BA=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}
=\begin{pmatrix}6&8\\8&10\end{pmatrix}.
$$
于是
$$
I_3-AB=\begin{pmatrix}0&-2&-3\\-3&-3&-7\\-5&-6&-10\end{pmatrix},
\qquad
I_2-BA=\begin{pmatrix}-5&-8\\-8&-9\end{pmatrix}.
$$
$\det(I_2-BA)=(-5)(-9)-(-8)(-8)=45-64=-19\ne0$，故 $I_2-BA$ 可逆，且
$$
\big(I_2-BA\big)^{-1}=\frac1{-19}\begin{pmatrix}-9&8\\8&-5\end{pmatrix}
=\begin{pmatrix}\tfrac{9}{19}&-\tfrac{8}{19}\\[2pt]-\tfrac{8}{19}&\tfrac{5}{19}\end{pmatrix}.
$$
`rank(I_3-AB)=3`（可检验 $\det(I_3-AB)=-1\ne0$），故 $I_3-AB$ 也可逆，与第 2 问的结论一致。最后验证公式
$$
I_3+A\big(I_2-BA\big)^{-1}B
=I_3+\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}
\begin{pmatrix}\tfrac9{19}&-\tfrac8{19}\\[2pt]-\tfrac8{19}&\tfrac5{19}\end{pmatrix}
\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}
=\big(I_3-AB\big)^{-1}.
$$
直接乘法可验证
$$
\big(I_3-AB\big)\cdot\Big[I_3+A\big(I_2-BA\big)^{-1}B\Big]=I_3,
$$
即公式成立。

> **小结**：①「可逆 $\iff$ 对任意右端有唯一解」是第 1 问的钥匙，也是第 1 节/第 2 节可逆定义的直接应用；② 第 2 问只需"构造逆并验证"，这是 Sherman–Morrison–Woodbury 公式的特例；③ 注意 $m\ne n$ 时 $I_m-AB$ 与 $I_n-BA$ 是不同阶的方阵，但可逆性同步。

---

## 练习 8　矩阵乘法与综合小问

> 【对应试卷第三题、第四题、第六题的综合变式】

已知
$$
A=\begin{pmatrix}1&1&2\\1&2&3\\1&2&3\\1&3&4\end{pmatrix},
\qquad
B=\begin{pmatrix}1&4\\2&5\end{pmatrix}.
$$

1. 写出 $A$ 的列向量 $a_1,a_2,a_3$，并求 $A$ 的最简行阶梯形 $R$，指出主元列；
2. 用 $R$ 中的列关系写出 $A$ 的列之间的线性关系，并求 $C(A)$ 的一组基与 $\dim C(A)$；
3. 计算 $AB$ 的第 1 列，并说明为什么它一定是 $A$ 的列向量的线性组合；
4. 已知 $b=(1,0,0,1)^{\mathsf T}$，判断 $Ax=b$ 是否有解。

**【涉及知识点】** RREF 与列关系的保持（第 12 节）；列空间基；列-列观点（第 5、6 节）；$Ax=b$ 有解 $\iff b\in C(A)$（第 10 节）。
**【对应课件】** `la-05-slide`、`la-06-slide`、`la-10-slide`、`la-12-slide`。

**【解答】**

**1.** 记为 $A=[a_1,a_2,a_3,a_4]$。注意第 3 行 $=$ 第 2 行，故可先去重：
$$
A\xrightarrow{R_3\leftarrow R_3-R_2}
\begin{pmatrix}1&1&2&4\\1&2&3&5\\0&0&0&0\\1&3&4&6\end{pmatrix}
\xrightarrow[R_4\leftarrow R_4-R_1]{R_2\leftarrow R_2-R_1}
\begin{pmatrix}1&1&2&4\\0&1&1&1\\0&0&0&0\\0&2&2&2\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-2R_2}
\begin{pmatrix}1&1&2&4\\0&1&1&1\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$
$$
\xrightarrow{R_1\leftarrow R_1-R_2}
\begin{pmatrix}1&0&1&1\\0&1&1&1\\0&0&0&0\\0&0&0&0\end{pmatrix}=R .
$$
主元在第 $1,2$ 列，$\operatorname{rank}A=2$。

**2.** 由 $R$ 读出列关系（第 12 节：$PA=R$ 中 $P$ 可逆，故 $A$ 与 $R$ 的列有完全相同的线性关系）：
$$
r_3=r_1+r_2,\qquad r_4=r_1+r_2
\;\Longrightarrow\;
a_3=a_1+a_2,\qquad a_4=a_1+a_2 .
$$
直接验算：$a_1+a_2=(2,3,3,4)^{\mathsf T}=a_3$ ✓，$=a_4$ ✓。故 $C(A)$ 的一组基为**主元列**
$$
\left\{\begin{pmatrix}1\\1\\1\\1\end{pmatrix},\ \begin{pmatrix}1\\2\\2\\3\end{pmatrix}\right\},
\qquad \dim C(A)=2 .
$$

**3.** 由列-列观点，$AB=[Ab_1\ Ab_2]$，其中 $b_1=(1,2)^{\mathsf T},b_2=(4,5)^{\mathsf T}$：
$$
(AB)_{\cdot 1}=Ab_1=1\cdot a_1+2\cdot a_2
=\begin{pmatrix}1\\1\\1\\1\end{pmatrix}+2\begin{pmatrix}1\\2\\2\\3\end{pmatrix}
=\begin{pmatrix}3\\5\\5\\7\end{pmatrix}.
$$
这当然落在 $C(A)$ 中——**$AB$ 的每一列都是 $A$ 的列的线性组合**（系数为 $B$ 的对应列），这正是 $C(AB)\subset C(A)$ 的来源（见练习 6）。
（完整结果：$(AB)_{\cdot2}=4a_1+5a_2=(9,14,14,19)^{\mathsf T}$，故 $AB=\begin{pmatrix}3&9\\5&14\\5&14\\7&19\end{pmatrix}$。）

**4.** $b$ 是否属于 $C(A)$？设 $b=\lambda_1a_1+\lambda_2a_2$，看前两个分量：
$$
\lambda_1+\lambda_2=1,\qquad \lambda_1+2\lambda_2=0
\;\Longrightarrow\;\lambda_2=-1,\ \lambda_1=2 .
$$
检验第三、四分量：$2\cdot1+(-1)\cdot2=0$ ✓；$2\cdot1+(-1)\cdot3=-1\ne1$ ✗。故 $b\notin C(A)$，**$Ax=b$ 无解**。
（等价地，由练习 5 的方法：$A$ 的列满足 $a_3=a_1+a_2$，且 $[A\mid b]$ 消元后会出现矛盾行。）

---

# 第二部分　矩阵运算、逆与 LU/LDU 分解（17 题）

## 练习 9　内积、模长、正交与夹角

> 【对应课件第 1 节 `1/1.md` 与第 2 节】

设
$$
u=\begin{pmatrix}1\\2\\2\end{pmatrix},\qquad v=\begin{pmatrix}2\\1\\-1\end{pmatrix},\qquad w=\begin{pmatrix}1\\1\\1\end{pmatrix}.
$$

1. 求 $u\cdot v,\|u\|,\|v\|$，判断 $u$ 与 $v$ 是否正交；
2. 验证施瓦茨不等式 $|u\cdot v|\le\|u\|\|v\|$，并求 $u,v$ 夹角余弦；
3. 求 $u$ 在 $w$ 方向上的投影向量 $\dfrac{u\cdot w}{w\cdot w}w$，并求把 $u$ 单位化后的向量。

**【解答】**

**1.** $u\cdot v=1\cdot2+2\cdot1+2\cdot(-1)=2+2-2=2$；
$$
\|u\|=\sqrt{1+4+4}=3,\qquad \|v\|=\sqrt{4+1+1}=\sqrt6 .
$$
因 $u\cdot v=2\ne0$，$u$ 与 $v$ **不正交**。

**2.** $|u\cdot v|=2$，$\|u\|\|v\|=3\sqrt6\approx7.35$，故 $2<3\sqrt6$，施瓦茨不等式成立（等号当且仅当 $u,v$ 线性相关）。
$$
\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}=\frac{2}{3\sqrt6}=\frac{\sqrt6}{9}.
$$

**3.** $u\cdot w=1+2+2=5$，$w\cdot w=3$，故投影为 $\dfrac53 w=\left(\frac53,\frac53,\frac53\right)^{\mathsf T}$。单位化：$\hat u=\dfrac{u}{\|u\|}=\left(\frac13,\frac23,\frac23\right)^{\mathsf T}$。

> **小结**：$\langle u,v\rangle=0\iff u\perp v$；$\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}$；施瓦茨不等式等价于 $|\cos\theta|\le1$。

---

## 练习 10　线性相关与线性无关

**1.** 判断向量组
$$
a_1=\begin{pmatrix}1\\1\\1\end{pmatrix},\quad
a_2=\begin{pmatrix}1\\2\\3\end{pmatrix},\quad
a_3=\begin{pmatrix}1\\4\\9\end{pmatrix}
$$
是线性相关还是线性无关。

**2.** 设 $a_1,a_2,a_3$ 线性无关，判断
$$
b_1=2a_1+a_2,\qquad b_2=a_2+3a_3,\qquad b_3=3a_1-a_3
$$
是否线性无关，并证明你的结论。

**3.** 设 $A=\begin{pmatrix}1&2&2&5\\2&-1&4&5\\3&1&6&10\\1&0&2&3\end{pmatrix}=[c_1,c_2,c_3,c_4]$，求 $\operatorname{rank}A$ 并写出 $c_3,c_4$ 与主元列的线性关系。

**【解答】**

**1.** 设 $x_1a_1+x_2a_2+x_3a_3=0$，即
$$
\begin{pmatrix}1&1&1\\1&2&4\\1&3&9\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}=0
\xrightarrow[R_3\leftarrow R_3-R_1]{R_2\leftarrow R_2-R_1}
\begin{pmatrix}1&1&1\\0&1&3\\0&2&8\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-2R_2}
\begin{pmatrix}1&1&1\\0&1&3\\0&0&2\end{pmatrix}.
$$
三个主元，只有零解，故**线性无关**（几何上三向量不共面）。

**2.** 设 $d_1b_1+d_2b_2+d_3b_3=0$，代入展开：
$$
d_1(2a_1+a_2)+d_2(a_2+3a_3)+d_3(3a_1-a_3)=0
$$
$$
\Longrightarrow\quad (2d_1+3d_3)a_1+(d_1+d_2)a_2+(3d_2-d_3)a_3=0 .
$$
因 $a_1,a_2,a_3$ 线性无关，三个系数全为 $0$：
$$
\begin{cases}2d_1+3d_3=0\\ d_1+d_2=0\\ 3d_2-d_3=0\end{cases}
\;\Longrightarrow\;
d_1=-d_2,\ d_3=3d_2,\ 2(-d_2)+3(3d_2)=7d_2=0
\;\Longrightarrow\; d_1=d_2=d_3=0 .
$$
故 $b_1,b_2,b_3$ **线性无关**。$\blacksquare$

**3.** 注意第 2 行 $=-c_1+c_3$ 之类关系，直接消元：
$$
A\xrightarrow[R_3\leftarrow R_3-3R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&2&5\\0&-5&0&-5\\0&-5&0&-5\\1&0&2&3\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-R_1}
\begin{pmatrix}1&2&2&5\\0&-5&0&-5\\0&-5&0&-5\\0&-2&0&-2\end{pmatrix}
$$
$$
\xrightarrow[R_4\leftarrow R_4-\frac25R_2]{R_3\leftarrow R_3-R_2}
\begin{pmatrix}1&2&2&5\\0&-5&0&-5\\0&0&0&0\\0&0&0&0\end{pmatrix}
$$
故 $\operatorname{rank}A=2$，主元列是 $c_1,c_2$。直接验算列关系：
$$
c_3-2c_1=(2-2,\,4-4,\,6-6,\,2-2)^{\mathsf T}=0
\;\Longrightarrow\; c_3=2c_1,
$$
$$
c_4-3c_1-c_2=(5-3-2,\ 5-6+1,\ 10-9-1,\ 3-3-0)^{\mathsf T}=0
\;\Longrightarrow\; c_4=3c_1+c_2 .
$$
（这与第 12 节"从 RREF 直接读出列关系"一致。）

---

## 练习 11　矩阵乘法：交换律失效与迹

**1.** 取 $X=\begin{pmatrix}1&2\\0&0\end{pmatrix}$，$Y=\begin{pmatrix}0&0\\3&4\end{pmatrix}$，计算 $XY$ 与 $YX$，说明矩阵乘法不满足交换律。

**2.** 设 $B=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}$（$2\times3$），$C=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}$（$3\times2$）。计算 $BC$ 与 $CB$，比较二者阶数并验证 $\operatorname{tr}(BC)=\operatorname{tr}(CB)$。

**3.** 设 $R=\begin{pmatrix}-1&1&0\\0&-1&1\end{pmatrix}$，求 $R^{\mathsf T}R$ 与 $RR^{\mathsf T}$，验证二者都是对称矩阵，并说明为什么它们一般不同。

**【解答】**

**1.**
$$
XY=\begin{pmatrix}1&2\\0&0\end{pmatrix}\begin{pmatrix}0&0\\3&4\end{pmatrix}
=\begin{pmatrix}6&8\\0&0\end{pmatrix},
\qquad
YX=\begin{pmatrix}0&0\\3&4\end{pmatrix}\begin{pmatrix}1&2\\0&0\end{pmatrix}
=\begin{pmatrix}0&0\\3&6\end{pmatrix}.
$$
$XY\ne YX$，故矩阵乘法**不满足交换律**（即使两个矩阵都是方阵）。此外 $X\ne O$、$Y\ne O$ 但……这里 $XY\ne O$；可另举例说明"两个非零矩阵相乘可以得零矩阵"。

**2.**
$$
BC=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}
=\begin{pmatrix}1+6+15&2+8+18\\4+15+30&8+20+36\end{pmatrix}
=\begin{pmatrix}22&28\\49&64\end{pmatrix}\quad(2\times2),
$$
$$
CB=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}
=\begin{pmatrix}1+8&2+10&3+12\\3+16&6+20&9+24\\5+24&10+30&15+36\end{pmatrix}
=\begin{pmatrix}9&12&15\\19&26&33\\29&40&51\end{pmatrix}\quad(3\times3).
$$
阶数不同，故 $BC\ne CB$。迹：
$$
\operatorname{tr}(BC)=22+64=86,\qquad \operatorname{tr}(CB)=9+26+51=86 .
$$
二者相等——一般地 $\operatorname{tr}(BC)=\operatorname{tr}(CB)$（$B$ 为 $m\times n$、$C$ 为 $n\times m$ 时）。

**3.**
$$
R^{\mathsf T}R=\begin{pmatrix}-1&0\\1&-1\\0&1\end{pmatrix}\begin{pmatrix}-1&1&0\\0&-1&1\end{pmatrix}
=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},
\qquad
RR^{\mathsf T}=\begin{pmatrix}-1&1&0\\0&-1&1\end{pmatrix}\begin{pmatrix}-1&0\\1&-1\\0&1\end{pmatrix}
=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
两者都对称（因为 $(R^{\mathsf T}R)^{\mathsf T}=R^{\mathsf T}R$，$(RR^{\mathsf T})^{\mathsf T}=RR^{\mathsf T}$，见第 9 节）。它们阶数不同（$3\times3$ 与 $2\times2$），且一般情况下 $R^{\mathsf T}R\ne RR^{\mathsf T}$——事实上 $R^{\mathsf T}R$ 与 $RR^{\mathsf T}$ 的非零特征值相同，但阶数由 $m,n$ 决定。

---

## 练习 12　主元位置出现 0：行交换

用高斯消元法解线性方程组
$$
\begin{cases}y+z=2\\ x+y+z=3\\ x+2y+3z=6\end{cases}
$$
要求：写出增广矩阵，说明为什么需要行交换，并用回代求解。

**【解答】**

增广矩阵
$$
\left(\begin{array}{ccc|c}0&1&1&2\\1&1&1&3\\1&2&3&6\end{array}\right).
$$
第 1 列第 1 个元素为 $0$，**无法用第 1 行消去其它行的 $x$**（找不到以第 1 列为位置的主元）。此时应做**行交换**产生主元：交换第 1、2 行：
$$
\xrightarrow{R_1\leftrightarrow R_2}
\left(\begin{array}{ccc|c}1&1&1&3\\0&1&1&2\\1&2&3&6\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_1}
\left(\begin{array}{ccc|c}1&1&1&3\\0&1&1&2\\0&1&2&3\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_2}
\left(\begin{array}{ccc|c}1&1&1&3\\0&1&1&2\\0&0&1&1\end{array}\right).
$$
系数矩阵成为上三角，三个主元，**有唯一解**。回代：
$$
z=1,\qquad y+1=2\Rightarrow y=1,\qquad x+1+1=3\Rightarrow x=1 .
$$
故唯一解为 $(x,y,z)=(1,1,1)^{\mathsf T}$。

> **验算**：$y+z=2$ ✓，$x+y+z=3$ ✓，$x+2y+3z=1+2+3=6$ ✓。
> **小结**：第 4 节例题 8 正是本例——**通过行交换可以产生主元**；在主元位置出现 $0$ 时，务必先换行。

---

## 练习 13　含参数方程组的解的讨论

已知方程组
$$
\begin{cases}x+4y-2z=1\\ x+7y-6z=6\\ 3y+qz=t\end{cases}
$$
其中 $q,t$ 为参数。

1. 当 $q$ 满足什么条件时，消元过程中**不出现第三个主元**（即系数矩阵的秩 $<3$）？
2. 在第 1 问的 $q$ 下，$t$ 满足什么条件时方程组有无穷多解？写出全解（用参数 $s=z$ 表示），并给出 $s=1$ 时的解；
3. 当 $q=0$ 时求解方程组。

> 【来源】仿课件第 4 节作业第 5 题（"当 $q$ 满足什么条件时会导致消元时没有第三个主元？在 (a) 的情况下 $t$ 满足什么条件时方程组有无穷多解？"）。

**【解答】**

增广矩阵消元：
$$
\left(\begin{array}{ccc|c}1&4&-2&1\\1&7&-6&6\\0&3&q&t\end{array}\right)
\xrightarrow{R_2\leftarrow R_2-R_1}
\left(\begin{array}{ccc|c}1&4&-2&1\\0&3&-4&5\\0&3&q&t\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_2}
\left(\begin{array}{ccc|c}1&4&-2&1\\0&3&-4&5\\0&0&q+4&t-5\end{array}\right).
$$
**关键**：$A$ 的第三行恰好是"第 2 行减第 1 行"再加上 $(0,0,q+4)$，即
$$
(0,3,q)=(0,3,-4)+(0,0,q+4).
$$

**1.** 第三个主元存在 $\iff q+4\ne0$。故
$$
\text{不出现第三个主元}\iff \boxed{q=-4},
$$
此时 $\operatorname{rank}A=2$，最后一行化为 $(0,0,0\mid t-5)$。

**2.** 当 $q=-4$ 时第三行是 $(0,0,0\mid t-5)$：
- 若 $t\ne5$，出现矛盾行 $0=t-5\ne0$，**无解**（$\operatorname{rank}[A\mid b]=3>2=\operatorname{rank}A$）；
- 若 $t=5$，第三行为恒等式，$\operatorname{rank}A=\operatorname{rank}[A\mid b]=2<3$，**有无穷多解**。

此时由前两行回代。令 $z=s$（自由变量）：
$$
3y-4s=5\Rightarrow y=\frac{5+4s}{3},\qquad
x+4\cdot\frac{5+4s}{3}-2s=1\Rightarrow x=\frac{-17-10s}{3}.
$$
故**全解**
$$
\begin{pmatrix}x\\y\\z\end{pmatrix}
=\begin{pmatrix}\dfrac{-17-10s}{3}\\[4pt]\dfrac{5+4s}{3}\\[4pt]s\end{pmatrix}
=\begin{pmatrix}-\dfrac{17}{3}\\[4pt]\dfrac53\\[4pt]0\end{pmatrix}
+s\begin{pmatrix}-\dfrac{10}{3}\\[4pt]\dfrac43\\[4pt]1\end{pmatrix},
\qquad s\in\mathbb R .
$$
**验算**（$s=1$）：$(x,y,z)=(-9,3,1)$，则
$$
x+4y-2z=-9+12-2=1\ \checkmark,\quad
x+7y-6z=-9+21-6=6\ \checkmark,\quad
3y-4z=9-4=5=t\ \checkmark .
$$
**$s=1$ 时的解**：$(x,y,z)=(-9,3,1)$，对应 $t=5$。
**另一组**：$s=0$ 时 $(x,y,z)=\left(-\frac{17}3,\frac53,0\right)$，同样满足三式（且 $t=5$）。

**3.** 当 $q=0$ 时，第三行第三列为 $q+4=4\ne0$，**三个主元都存在**，故有**唯一解**：
$$
z=\frac t4,\qquad 3y-4\cdot\frac t4=5\Rightarrow y=\frac{5+t}{3},
$$
$$
x=1-4y+2z=1-\frac{4(5+t)}3+\frac t2=-\frac{17}3-\frac{5t}6 .
$$
（可验证：把 $s=\frac t4$ 代入第 2 问的通解即得同一结果，说明"唯一解"是通解中自由变量被约束所确定后得到的特例。）

> **小结**：消元后出现 $0=c\ne0$ 的矛盾行 $\Rightarrow$ 无解；主元个数 $<$ 未知数个数且无矛盾行 $\Rightarrow$ 无穷多解，自由变量个数 $=$ 未知数个数 $-$ 主元个数。**技巧**：先观察"哪一行是其它行的线性组合"（本题第 3 行 $=$ 第 2 行 $-$ 第 1 行 $+ (0,0,q+4)$），就能立刻定出使秩下降的参数值。

---

## 练习 14　线性表出

在 $\mathbb R^4$ 中判断向量 $b$ 能否由向量组 $a_1,a_2,a_3$ 线性表出；若能，写出一种表出方式：
$$
a_1=\begin{pmatrix}2\\-5\\3\\-4\end{pmatrix},\quad
a_2=\begin{pmatrix}-5\\11\\3\\10\end{pmatrix},\quad
a_3=\begin{pmatrix}-3\\7\\-1\\6\end{pmatrix},\quad
b=\begin{pmatrix}13\\-30\\2\\-26\end{pmatrix}.
$$

**【解答】**

求 $c_1,c_2,c_3$ 使 $c_1a_1+c_2a_2+c_3a_3=b$，即解 $4\times3$ 方程组。列方程：
$$
\begin{cases}2c_1-5c_2-3c_3=13\\ -5c_1+11c_2+7c_3=-30\\ 3c_1+3c_2-c_3=2\\ -4c_1+10c_2+6c_3=-26\end{cases}
$$
消元（$R_2\leftarrow R_2+\frac52R_1$，$R_3\leftarrow R_3-\frac32R_1$，$R_4\leftarrow R_4+2R_1$）得
$$
\begin{cases}2c_1-5c_2-3c_3=13\\ -\tfrac32c_2-\tfrac12c_3=\tfrac52\\ \tfrac{21}2c_2+\tfrac72c_3=-\tfrac{35}2\\ 0=0\end{cases}
$$
继续消元可得 $c_3=-2$，$c_2=3$，$c_1=2$。**验证**：
$$
2a_1+3a_2-2a_3
=\begin{pmatrix}4\\-10\\6\\-8\end{pmatrix}
+\begin{pmatrix}-15\\33\\9\\30\end{pmatrix}
+\begin{pmatrix}6\\-14\\2\\-12\end{pmatrix}
=\begin{pmatrix}-5\\9\\17\\10\end{pmatrix}.
$$
这与 $b$ 不符，说明上述消元有误。重新用**增广矩阵**严谨消元：
$$
\left(\begin{array}{ccc|c}2&-5&-3&13\\-5&11&7&-30\\3&3&-1&2\\-4&10&6&-26\end{array}\right)
\xrightarrow{R_1\leftrightarrow R_3}
\left(\begin{array}{ccc|c}3&3&-1&2\\-5&11&7&-30\\2&-5&-3&13\\-4&10&6&-26\end{array}\right)
$$
$$
\xrightarrow[R_3\leftarrow 3R_3-2R_1]{R_2\leftarrow 3R_2+5R_1}
\left(\begin{array}{ccc|c}3&3&-1&2\\0&48&16&-80\\0&-21&-7&35\\0&42&14&-70\end{array}\right)
\xrightarrow{R_2\leftarrow R_2/16}
\left(\begin{array}{ccc|c}3&3&-1&2\\0&3&1&-5\\0&-21&-7&35\\0&42&14&-70\end{array}\right)
$$
$$
\xrightarrow[R_4\leftarrow R_4-14R_2]{R_3\leftarrow R_3+7R_2}
\left(\begin{array}{ccc|c}3&3&-1&2\\0&3&1&-5\\0&0&0&0\\0&0&0&0\end{array}\right).
$$
第 3、4 行由第 1、2 行线性表出，无矛盾行，故**有解且有无穷多解**（1 个自由变量）。由第二行 $3c_2+c_3=-5$，令 $c_3=t$，则 $c_2=\dfrac{-5-t}{3}$；由第一行 $3c_1+3c_2-c_3=2$：
$$
c_1=\frac{2-3c_2+c_3}{3}=\frac{2-(-5-t)+t}{3}=\frac{7+2t}{3}.
$$
故**表出方式有无穷多种**：
$$
b=\frac{7+2t}{3}a_1+\frac{-5-t}{3}a_2+t\,a_3,\qquad t\in\mathbb R .
$$
**取 $t=-2$**（使系数为整数）：$c_1=\dfrac{7-4}{3}=1$，$c_2=\dfrac{-5+2}{3}=-1$，$c_3=-2$。验证：
$$
a_1-a_2-2a_3
=\begin{pmatrix}2\\-5\\3\\-4\end{pmatrix}
-\begin{pmatrix}-5\\11\\3\\10\end{pmatrix}
-2\begin{pmatrix}-3\\7\\-1\\6\end{pmatrix}
=\begin{pmatrix}2+5+6\\-5-11-14\\3-3+2\\-4-10-12\end{pmatrix}
=\begin{pmatrix}13\\-30\\2\\-26\end{pmatrix}=b.\quad\checkmark
$$
所以 $b$ **能**由 $a_1,a_2,a_3$ 线性表出，例如 $b=a_1-a_2-2a_3$。

---

## 练习 15　$C(A)=C(B)$ 与方程组可解性

**1.** 把向量 $b$ 增广到矩阵 $A$ 的最后一列得 $B=(A\mid b)$。证明：若 $C(A)=C(B)$，则方程组 $Ax=b$ 有解。
**2.** 取 $A=\begin{pmatrix}1&2\\2&4\\3&6\end{pmatrix}$，$b=\begin{pmatrix}2\\4\\6\end{pmatrix}$，验证 $C(A)=C(B)$ 并求 $Ax=b$ 的一个解。
**3.** 若 $A$ 是 $6\times6$ 可逆矩阵，求 $C(A)$；若对任一 $b\in\mathbb R^9$，$9\times12$ 方程组 $Ax=b$ 都有解，求 $C(A)$ 与 $\operatorname{rank}A$。

**【解答】**

**1.** 由增广的定义，$C(B)$ 由 $A$ 的列与 $b$ 共同张成。若 $C(A)=C(B)$，则 $b\in C(B)=C(A)$；而 "$b\in C(A)$" 恰好等价于"$b$ 是 $A$ 的列的线性组合"，即存在 $x$ 使 $Ax=b$。故 $Ax=b$ 有解。$\blacksquare$

**2.** $A$ 的两列成比例（第 2 列 $=2\times$ 第 1 列），故 $C(A)=\operatorname{span}\{(1,2,3)^{\mathsf T}\}$，$\dim C(A)=1$。$b=(2,4,6)^{\mathsf T}=2(1,2,3)^{\mathsf T}\in C(A)$，故 $C(B)=C(A)$ 且 $Ax=b$ 有解。取 $x=(2,0)^{\mathsf T}$：
$$
Ax=\begin{pmatrix}1&2\\2&4\\3&6\end{pmatrix}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}2\\4\\6\end{pmatrix}=b.\quad\checkmark
$$
（注意解不唯一：任意 $x=(2-2s,\ s)^{\mathsf T}$ 都是解。）

**3.** 若 $A$ 是 $6\times6$ 可逆矩阵，则 $A$ 的 6 个列线性无关，张成整个 $\mathbb R^6$，故 $C(A)=\mathbb R^6$。
若 $9\times12$ 的 $A$ 使 $Ax=b$ 对**所有** $b\in\mathbb R^9$ 有解，则 $C(A)=\mathbb R^9$，于是 $\operatorname{rank}A=\dim C(A)=9$。
（此时 $\dim N(A)=12-9=3$，解不唯一；这也说明 $9\times12$ 的矩阵秩至多为 $9$。）

---

## 练习 16　Gauss–Jordan 消元法求逆

用 Gauss–Jordan 消元法求
$$
A=\begin{pmatrix}1&2&3\\2&5&3\\1&0&8\end{pmatrix}
$$
的逆矩阵。

**【解答】**

构造增广矩阵 $[A\mid I]$，同时对左块做初等行变换把它化为 $I$：
$$
\left(\begin{array}{ccc|ccc}1&2&3&1&0&0\\2&5&3&0&1&0\\1&0&8&0&0&1\end{array}\right)
\xrightarrow[R_3\leftarrow R_3-R_1]{R_2\leftarrow R_2-2R_1}
\left(\begin{array}{ccc|ccc}1&2&3&1&0&0\\0&1&-3&-2&1&0\\0&-2&5&-1&0&1\end{array}\right)
$$
$$
\xrightarrow{R_3\leftarrow R_3+2R_2}
\left(\begin{array}{ccc|ccc}1&2&3&1&0&0\\0&1&-3&-2&1&0\\0&0&-1&-5&2&1\end{array}\right)
\xrightarrow{R_3\leftarrow -R_3}
\left(\begin{array}{ccc|ccc}1&2&3&1&0&0\\0&1&-3&-2&1&0\\0&0&1&5&-2&-1\end{array}\right)
$$
（消元到上三角后，继续用主元行**向上消元**：）
$$
\xrightarrow{R_2\leftarrow R_2+3R_3}
\left(\begin{array}{ccc|ccc}1&2&3&1&0&0\\0&1&0&13&-5&-3\\0&0&1&5&-2&-1\end{array}\right)
\xrightarrow{R_1\leftarrow R_1-3R_3}
\left(\begin{array}{ccc|ccc}1&2&0&-14&6&3\\0&1&0&13&-5&-3\\0&0&1&5&-2&-1\end{array}\right)
$$
$$
\xrightarrow{R_1\leftarrow R_1-2R_2}
\left(\begin{array}{ccc|ccc}1&0&0&-40&16&9\\0&1&0&13&-5&-3\\0&0&1&5&-2&-1\end{array}\right).
$$
左块已成为 $I_3$，故
$$
A^{-1}=\begin{pmatrix}-40&16&9\\13&-5&-3\\5&-2&-1\end{pmatrix}.
$$
**验算**：$A\cdot A^{-1}=I_3$（如第一行：$1\cdot(-40)+2\cdot13+3\cdot5=-40+26+15=1$ ✓）。

> **小结**：Gauss–Jordan 消元法的目标是把 $[A\mid I]$ 化为 $[I\mid A^{-1}]$；与"解 $A x=e_i$ 三个方程组"相比，三个方程组**共用同一消元过程**，故可合并计算（第 7 节）。

---

## 练习 17　初等矩阵与乘积的逆

**1.** 设 $E_{21}(3)$ 表示把单位阵第 1 行的 $3$ 倍加到第 2 行所得的初等矩阵，$P_{23}$ 为交换第 2、3 行的置换矩阵。写出 $E=E_{21}(3)$ 与 $P=P_{23}$（$3\times3$），并求 $E^{-1},P^{-1}$。
**2.** 设 $M=\begin{pmatrix}1&-2\\3&1\\0&4\end{pmatrix}$，求 $PEM$ 与 $(PE)^{-1}$。
**3.** 设方阵 $A,B,C$ 使 $M=ABC$ 可逆，写出 $B^{-1}$ 的公式（只含 $M^{-1},A,C$）。
**4.** 设 $B$ 是 $A^2$ 的逆矩阵，证明 $AB=A^{-1}$。

**【解答】**

**1.**
$$
E=E_{21}(3)=\begin{pmatrix}1&0&0\\3&1&0\\0&0&1\end{pmatrix},
\qquad
P=P_{23}=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
$$
由 $E_{ij}(\lambda)^{-1}=E_{ij}(-\lambda)$ 与 $P_{ij}^{-1}=P_{ij}$（第 7 节）：
$$
E^{-1}=E_{21}(-3)=\begin{pmatrix}1&0&0\\-3&1&0\\0&0&1\end{pmatrix},
\qquad
P^{-1}=P_{23}=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
$$
（几何直觉：$E$ 的作用是"第 2 行加上第 1 行的 3 倍"，撤销它就要"减去 3 倍"，即 $E(-3)$；交换两行再交换一次就复原。）

**2.**
$$
E M=\begin{pmatrix}1&0&0\\3&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&-2\\3&1\\0&4\end{pmatrix}
=\begin{pmatrix}1&-2\\3+3&\,-6+1\\0&4\end{pmatrix}
=\begin{pmatrix}1&-2\\6&-5\\0&4\end{pmatrix},
$$
$$
PEM=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}\begin{pmatrix}1&-2\\6&-5\\0&4\end{pmatrix}
=\begin{pmatrix}1&-2\\0&4\\6&-5\end{pmatrix}.
$$
由 $(PE)^{-1}=E^{-1}P^{-1}=E(-3)P_{23}$：
$$
(PE)^{-1}=\begin{pmatrix}1&0&0\\-3&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}
=\begin{pmatrix}1&0&0\\-3&0&1\\0&1&0\end{pmatrix}.
$$
**验算**：$(PE)(PE)^{-1}=I_3$ ✓（注意**逆序法则** $(PE)^{-1}=E^{-1}P^{-1}$，而 $E^{-1}P^{-1}\ne P^{-1}E^{-1}$）。

**3.** 由 $ABC=M$ 可逆及"可逆矩阵的乘积可逆，且 $(A_1A_2\cdots A_k)^{-1}=A_k^{-1}\cdots A_1^{-1}$"（第 7 节），知 $A,B,C$ 均可逆。于是
$$
B^{-1}=A\,M^{-1}C .
$$
**验证**：$B\cdot AM^{-1}C=A^{-1}(ABC)AM^{-1}C=A^{-1}MAM^{-1}C$。更直接地，由 $M=ABC$ 得 $B=A^{-1}MC^{-1}$，
$$
B^{-1}=(A^{-1}MC^{-1})^{-1}=C\,M^{-1}A .
$$
由于 $B$ 的逆唯一，两种写法的结果相同；本题要求的写法（只含 $M^{-1},A,C$）即 $\boxed{B^{-1}=C M^{-1}A}$。

**4.** 由题意 $A^2B=I$（即 $B=(A^2)^{-1}$）。两边左乘 $A^{-1}$（注意 $A^2$ 可逆 $\Rightarrow A$ 可逆）：
$$
A^{-1}(A^2B)=A^{-1}I\;\Longrightarrow\;(A^{-1}A^2)B=A^{-1}\;\Longrightarrow\;AB=A^{-1}.\qquad\blacksquare
$$

---

## 练习 18　可逆性判定与命题真伪

**1.** 判断下列矩阵是否可逆；若可逆，求其逆矩阵。
$$
(a)\ A=\begin{pmatrix}1&0&0\\0&2&0\\0&0&3\end{pmatrix};\quad
(b)\ B=\begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix};\quad
(c)\ C=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix};\quad
(d)\ D=\begin{pmatrix}0&0&0&2\\0&0&3&0\\0&4&0&0\\5&0&0&0\end{pmatrix}.
$$

**2.** 判断下列命题是否正确，正确请证明，错误请举反例。
- (a) $4\times4$ 矩阵 $A$ 若存在零行，则 $A$ 不可逆；
- (b) 主对角线下方元素全为 $1$ 的矩阵都可逆；
- (c) 若 $A$ 可逆，则 $A^{-1}$ 与 $A^2$ 均可逆；
- (d) 若 $AB=I_n$，则 $BA=I_n$（$A,B$ 为 $n$ 阶方阵）。

**【解答】**

**1.**
**(a)** 对角阵，对角元全非零，可逆：
$$
A^{-1}=\operatorname{diag}\!\left(1,\tfrac12,\tfrac13\right)=\begin{pmatrix}1&0&0\\0&\frac12&0\\0&0&\frac13\end{pmatrix}.
$$
**(b)** 消元：$B\xrightarrow[R_3\leftarrow R_3-\frac12R_1]{R_2\leftarrow R_2-\frac12R_1}
\begin{pmatrix}2&1&1\\0&\frac32&\frac12\\0&\frac12&\frac32\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-\frac13R_2}
\begin{pmatrix}2&1&1\\0&\frac32&\frac12\\0&0&\frac43\end{pmatrix}$，三个主元，故可逆。由对称性（$B=I+\mathbf 1\mathbf 1^{\mathsf T}$）可得
$$
B^{-1}=\begin{pmatrix}\frac34&-\frac14&-\frac14\\[2pt]-\frac14&\frac34&-\frac14\\[2pt]-\frac14&-\frac14&\frac34\end{pmatrix},
\qquad B B^{-1}=I_3 .\quad\checkmark
$$
**(c)** 由于 $C\cdot(1,1,1)^{\mathsf T}=(0,0,0)^{\mathsf T}$，即 $Cx=0$ 有非零解，故 $C$ **不可逆**（第 7 节判则：$Ax=0$ 有非零解 $\Rightarrow A$ 不可逆）。事实上 $\operatorname{rank}C=2$。
**(d)** 这是**反对角**阵，交换行/列即可化为对角阵；其逆为
$$
D^{-1}=\begin{pmatrix}0&0&0&\frac15\\[2pt]0&0&\frac14&0\\[2pt]0&\frac13&0&0\\[2pt]\frac12&0&0&0\end{pmatrix},
\qquad DD^{-1}=I_4 .\quad\checkmark
$$

**2.**
**(a) 正确。** 设 $A$ 的第 $i$ 行为零行。若 $A$ 可逆，则 $A^{-1}A=I$，于是 $I$ 的第 $i$ 行 $=(A^{-1})_{i\cdot}A=$（$A^{-1}$ 第 $i$ 行与 $A$ 的列的线性组合），而 $A$ 的第 $i$ 行为零使所有这样的组合……更简洁：$A$ 有零行 $\Rightarrow \operatorname{rank}A\le3<4$，故不可逆。$\blacksquare$
**(b) 错误。** 反例：$L=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix}$ 的对角线下方元素全为 $1$，但取
$$
L'=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}
$$
（主对角线下方元素全为 $1$，但对角元为 $0$），其第 $1$ 行 $=$ 第 $2$ 行 $+$ 第 $3$ 行的负数情形不成立；直接计算 $\det L'=0+1+1-0-0-0=2\ne0$，可逆——这不是反例。改用
$$
L''=\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}
$$
其主对角线下方元素全为 $1$，但三行相同，$\operatorname{rank}L''=1$，**不可逆**。故命题错误。
（若命题改成"主对角线**及其下方**元素构成单位下三角、即对角元全为 1 且上方为 0"，则确实可逆，见练习 20。）
**(c) 正确。** 设 $A$ 可逆，$A^{-1}$ 存在。则 $A^{-1}\cdot A=I$ 说明 $A^{-1}$ 可逆且 $(A^{-1})^{-1}=A$；而 $A^2\cdot(A^{-1})^2=A A A^{-1}A^{-1}=I$，故 $A^2$ 可逆且 $(A^2)^{-1}=(A^{-1})^2$。$\blacksquare$
**(d) 正确。** 这正是第 7 节定理 2：设 $A,B\in\mathbb R^{n\times n}$，若 $AB=I_n$，则 $A$ 可逆且 $B=A^{-1}$，从而 $BA=I_n$。
**证明**：反设 $A$ 不可逆，则存在可逆矩阵 $M$ 使 $MA$ 的最后一行全为 $0$（高斯消元会有零行）。由 $AB=I$ 左乘 $M$：
$$
M=M(AB)=(MA)B .
$$
但 $MA$ 最后一行全为 $0$，故右端 $(MA)B$ 的最后一行也全为 $0$，而 $M$ 可逆不可能有零行，矛盾。故 $A$ 可逆，$B=A^{-1}$，于是 $BA=I_n$。$\blacksquare$

---

## 练习 19　LU 分解与消元矩阵

**1.** 已知 $A=\begin{pmatrix}1&0&1\\2&2&2\\3&4&5\end{pmatrix}$，写出消元矩阵 $E_1,E_2,E_3$ 使 $E_3E_2E_1A=U$ 为上三角阵，并写出 $A=LU$。
**2.** 已知 $A=\begin{pmatrix}1&1&0\\4&6&1\\-2&2&0\end{pmatrix}$，求消元矩阵 $E_1,E_2$ 使 $E_2E_1A=U$；再求 $E=E_2E_1$ 与 $E^{-1}$。

**【解答】**

**1.** 消去第 2、3 行的第 1 列元素（乘子 $2,3$），再消去第 3 行的第 2 列元素（此时第 2 行第 2 列为 $2$，第 3 行第 2 列为 $4-3\cdot0=4$，乘子 $4/2=2$）：
$$
A=\begin{pmatrix}1&0&1\\2&2&2\\3&4&5\end{pmatrix}
\xrightarrow{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&0&1\\0&2&0\\3&4&5\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-3R_1}
\begin{pmatrix}1&0&1\\0&2&0\\0&4&2\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-2R_2}
\begin{pmatrix}1&0&1\\0&2&0\\0&0&2\end{pmatrix}=U .
$$
故
$$
E_1=E_{21}(-2)=\begin{pmatrix}1&0&0\\-2&1&0\\0&0&1\end{pmatrix},\quad
E_2=E_{31}(-3)=\begin{pmatrix}1&0&0\\0&1&0\\-3&0&1\end{pmatrix},\quad
E_3=E_{32}(-2)=\begin{pmatrix}1&0&0\\0&1&0\\0&-2&1\end{pmatrix}.
$$
由 $A=E_1^{-1}E_2^{-1}E_3^{-1}U=E_{21}(2)E_{31}(3)E_{32}(2)U$ 得
$$
A=LU,\qquad
L=\begin{pmatrix}1&0&0\\2&1&0\\3&2&1\end{pmatrix},
\qquad
U=\begin{pmatrix}1&0&1\\0&2&0\\0&0&2\end{pmatrix}.
$$
**验证**：$LU=A$ ✓。$\det A=1\cdot2\cdot2=4$。

**2.** 消元：
$$
A=\begin{pmatrix}1&1&0\\4&6&1\\-2&2&0\end{pmatrix}
\xrightarrow{R_2\leftarrow R_2-4R_1}
\begin{pmatrix}1&1&0\\0&2&1\\-2&2&0\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3+2R_1}
\begin{pmatrix}1&1&0\\0&2&1\\0&4&0\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-2R_2}
\begin{pmatrix}1&1&0\\0&2&1\\0&0&-2\end{pmatrix}=U .
$$
故
$$
E_1=E_{21}(-4)=\begin{pmatrix}1&0&0\\-4&1&0\\0&0&1\end{pmatrix},\qquad
E_2=E_{31}(2)E_{32}(-2)\ \text{的方向}
$$
更规范地：把第 3 行的操作拆成两步——先 $R_3\leftarrow R_3+2R_1$（即 $E_{31}(2)$），再 $R_3\leftarrow R_3-2R_2$（即 $E_{32}(-2)$），故
$$
E_2=E_{32}(-2)E_{31}(2)
=\begin{pmatrix}1&0&0\\0&1&0\\0&-2&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\2&0&1\end{pmatrix}
=\begin{pmatrix}1&0&0\\0&1&0\\2&-2&1\end{pmatrix}.
$$
于是
$$
E=E_2E_1=\begin{pmatrix}1&0&0\\0&1&0\\2&-2&1\end{pmatrix}\begin{pmatrix}1&0&0\\-4&1&0\\0&0&1\end{pmatrix}
=\begin{pmatrix}1&0&0\\-4&1&0\\10&-2&1\end{pmatrix},
$$
且 $EA=U$。由 $E^{-1}=E_1^{-1}E_2^{-1}$：
$$
E^{-1}=E_{21}(4)\cdot E_{31}(-2)E_{32}(2)
=\begin{pmatrix}1&0&0\\4&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}1&0&0\\0&1&0\\-2&2&1\end{pmatrix}
=\begin{pmatrix}1&0&0\\4&1&0\\-2&2&1\end{pmatrix}=L .
$$
（这正说明 $A=E^{-1}U=LU$，$L$ 就是消元乘子按位置填成的单位下三角阵。）

> **小结**：$L$ 的第 $(i,j)$ 元就是消去 $a_{ij}$ 时减去的倍数 $l_{ij}$（第 8 节定理 1）；$E^{-1}=L$ 是"消元矩阵的乘积之逆即乘子矩阵"的体现。

---

## 练习 20　用 LU 分解解多个右端

已知
$$
A=\begin{pmatrix}1&1&1\\1&2&2\\1&2&3\end{pmatrix},
\qquad
b_1=\begin{pmatrix}3\\5\\6\end{pmatrix},
\qquad
b_2=\begin{pmatrix}4\\5\\6\end{pmatrix}.
$$

1. 求 $A$ 的 LU 分解；
2. 用 LU 分解分别解 $Ax=b_1$ 与 $Ax=b_2$（体会同一 $A$、不同右端时 LU 分解可复用）。

**【解答】**

**1.** 消元：
$$
A=\begin{pmatrix}1&1&1\\1&2&2\\1&2&3\end{pmatrix}
\xrightarrow[R_3\leftarrow R_3-R_1]{R_2\leftarrow R_2-R_1}
\begin{pmatrix}1&1&1\\0&1&1\\0&1&2\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_2}
\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}=U .
$$
乘子 $l_{21}=1,l_{31}=1,l_{32}=1$，故
$$
L=\begin{pmatrix}1&0&0\\1&1&0\\1&1&1\end{pmatrix},
\qquad A=LU .
$$

**2. 解 $Ax=b$ 分两步：先解 $Ly=b$（前代），再解 $Ux=y$（回代）。**

**对 $b_1=(3,5,6)^{\mathsf T}$：**
$$
Ly=b_1:\quad y_1=3,\ y_2=5-1\cdot3=2,\ y_3=6-1\cdot3-1\cdot2=1
\;\Longrightarrow\; y=(3,2,1)^{\mathsf T}.
$$
$$
Ux=y:\quad x_3=1,\ x_2=2-1\cdot1=1,\ x_1=3-1\cdot1-1\cdot1=1
\;\Longrightarrow\; x=(1,1,1)^{\mathsf T}.
$$
**验算**：$A(1,1,1)^{\mathsf T}=(3,5,6)^{\mathsf T}=b_1$ ✓。

**对 $b_2=(4,5,6)^{\mathsf T}$：**（$L,U$ 不变，只换右端）
$$
Ly=b_2:\quad y_1=4,\ y_2=5-4=1,\ y_3=6-4-1=1\;\Longrightarrow\;y=(4,1,1)^{\mathsf T}.
$$
$$
Ux=y:\quad x_3=1,\ x_2=1-1=0,\ x_1=4-1\cdot0-1\cdot1=3\;\Longrightarrow\;x=(3,0,1)^{\mathsf T}.
$$
**验算**：$A(3,0,1)^{\mathsf T}=(3+0+1,\ 3+0+2,\ 3+0+3)^{\mathsf T}=(4,5,6)^{\mathsf T}=b_2$ ✓。

> **小结**：LU 分解的**价值**在于：分解一次（约 $\frac{n^3}{3}$ 次运算），之后每个新右端只需前代 $+$ 回代（约 $2n^2$ 次运算），无需重新消元（第 8 节"方程组求解的运算次数"）。

---

## 练习 21　对称矩阵的 $LDL^{\mathsf T}$ 分解

**1.** 已知对称矩阵 $A=\begin{pmatrix}2&-1&0\\-1&2&-1\\0&-1&2\end{pmatrix}$，求其 $LDL^{\mathsf T}$ 分解。
**2.** 已知对称矩阵 $S=\begin{pmatrix}1&2&2\\2&7&7\\2&7&6\end{pmatrix}$，求其 $LDL^{\mathsf T}$ 分解，并求 $\det S$。
**3.** 证明：若对称矩阵 $A$ 有 LDU 分解 $A=LDU$（消元不经行交换即可找到 $n$ 个主元），则 $U=L^{\mathsf T}$，即 $A=LDL^{\mathsf T}$。

**【解答】**

**1.** 消元（利用对称性，只需算一半）：
$$
A\xrightarrow[R_3\leftarrow R_3+0\cdot R_1]{R_2\leftarrow R_2+\frac12R_1}
\begin{pmatrix}2&-1&0\\0&\frac32&-1\\0&-1&2\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3+\frac23R_2}
\begin{pmatrix}2&-1&0\\0&\frac32&-1\\0&0&\frac43\end{pmatrix}=U .
$$
故 $D=\operatorname{diag}\left(2,\frac32,\frac43\right)$，$L$ 记录乘子（注意符号）：
$$
L=\begin{pmatrix}1&0&0\\-\frac12&1&0\\0&-\frac23&1\end{pmatrix},
\qquad
A=LDL^{\mathsf T}=\begin{pmatrix}1&0&0\\-\frac12&1&0\\0&-\frac23&1\end{pmatrix}
\begin{pmatrix}2&0&0\\0&\frac32&0\\0&0&\frac43\end{pmatrix}
\begin{pmatrix}1&-\frac12&0\\0&1&-\frac23\\0&0&1\end{pmatrix}.
$$
**验证**：$LDL^{\mathsf T}=A$ ✓。

**2.** 消元：
$$
S=\begin{pmatrix}1&2&2\\2&7&7\\2&7&6\end{pmatrix}
\xrightarrow[R_3\leftarrow R_3-2R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&2\\0&3&3\\0&3&2\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_2}
\begin{pmatrix}1&2&2\\0&3&3\\0&0&-1\end{pmatrix}.
$$
故 $L=\begin{pmatrix}1&0&0\\2&1&0\\2&1&1\end{pmatrix}$，$D=\operatorname{diag}(1,3,-1)$，且
$$
S=LDL^{\mathsf T}
=\begin{pmatrix}1&0&0\\2&1&0\\2&1&1\end{pmatrix}
\begin{pmatrix}1&0&0\\0&3&0\\0&0&-1\end{pmatrix}
\begin{pmatrix}1&2&2\\0&1&1\\0&0&1\end{pmatrix}
=\begin{pmatrix}1&2&2\\2&7&7\\2&7&6\end{pmatrix}.\quad\checkmark
$$
$$
\det S=\det L\cdot\det D\cdot\det L^{\mathsf T}=1\cdot(1\cdot3\cdot(-1))\cdot1=-3 .
$$

**3. 证明。** 设 $A$ 对称（$A=A^{\mathsf T}$）且有 $A=LDU$（$L$ 单位下三角、$D$ 对角、$U$ 单位上三角）。取转置：
$$
A=A^{\mathsf T}=(LDU)^{\mathsf T}=U^{\mathsf T}D^{\mathsf T}L^{\mathsf T}=U^{\mathsf T}D L^{\mathsf T}
$$
（因为 $D$ 是对角阵，$D^{\mathsf T}=D$）。于是 $A$ 有两组 LDU 型分解：
$$
A=LDU=U^{\mathsf T}DL^{\mathsf T}.
$$
由于**消元不经行交换找到 $n$ 个主元时 LDU 分解唯一**（第 9 节指出的事实：L 记录消元乘子、D 记录主元，均由消元过程唯一决定），比较两式得
$$
L=U^{\mathsf T},\qquad U=L^{\mathsf T}.
$$
故 $A=LDL^{\mathsf T}$。$\blacksquare$

> **小结**：对称矩阵的 $LDL^{\mathsf T}$ 分解把工作量减半（只需存储 $L$，第 9 节：浮点运算约 $n^3/6$）；$D$ 的对角元就是消元主元，其正负个数（惯性指数）是重要的不变量。

---

## 练习 22　排列矩阵与 $PA=LU$

**1.** 判断下列矩阵是否为排列矩阵，并求其逆：
$$
P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad
Q=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
$$
**2.** 求 $PQ$，并验证 $P^{-1}=P^{\mathsf T}$。
**3.** 对
$$
A=\begin{pmatrix}2&1&0\\1&2&2\\1&3&0\end{pmatrix}
$$
求 $PA=LU$ 分解（即找出排列阵 $P$、单位下三角 $L$、上三角 $U$）。

**【解答】**

**1.** $P$ 的每一行、每一列恰有一个 $1$，是排列矩阵；$Q$ 同理也是排列矩阵。排列矩阵满足 $P^{-1}=P^{\mathsf T}$（第 9 节性质 2）：
$$
P^{-1}=P^{\mathsf T}=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}=Q .
$$
（$P$ 对应排列 $(i_1,i_2,i_3)=(2,3,1)$，即 $e_1\mapsto e_2,e_2\mapsto e_3,e_3\mapsto e_1$，是 3-循环，其逆就是这个循环的平方。）

**2.**
$$
PQ=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}
=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}=I_3 .
$$
（因为 $Q=P^{-1}$。）同时直接验证：
$$
P P^{\mathsf T}=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}
=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}=I_3,
$$
故 $P^{-1}=P^{\mathsf T}$ ✓。**这类满足 $P^{-1}=P^{\mathsf T}$ 的矩阵称为正交矩阵**。

**3.** $A$ 的第一个主元为 $a_{11}=2\ne0$，直接消元：
$$
A\xrightarrow{R_2\leftarrow R_2-\frac12R_1}
\begin{pmatrix}2&1&0\\0&\frac32&2\\1&3&0\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-\frac12R_1}
\begin{pmatrix}2&1&0\\0&\frac32&2\\0&\frac52&0\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-\frac53R_2}
\begin{pmatrix}2&1&0\\0&\frac32&2\\0&0&-\frac{10}{3}\end{pmatrix}=U .
$$
乘子：$l_{21}=\frac12,\ l_{31}=\frac12,\ l_{32}=\frac53$，故
$$
L=\begin{pmatrix}1&0&0\\[2pt]\frac12&1&0\\[2pt]\frac12&\frac53&1\end{pmatrix},
\qquad
U=\begin{pmatrix}2&1&0\\[2pt]0&\frac32&2\\[2pt]0&0&-\frac{10}{3}\end{pmatrix},
\qquad P=I_3 .
$$
**验证**：$LU=A$ ✓（本例 $a_{11}\ne0$，无需行交换，故 $P=I$）。
**需要行交换的例子**：若取
$$
A'=\begin{pmatrix}0&1&2\\1&2&2\\2&3&0\end{pmatrix},
$$
则 $a_{11}=0$，必须先交换第 1、2 行：$P=P_{12}$，
$$
PA'=\begin{pmatrix}1&2&2\\0&1&2\\2&3&0\end{pmatrix}
\xrightarrow[R_3\leftarrow R_3-2R_1]{}
\begin{pmatrix}1&2&2\\0&1&2\\0&-1&-4\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3+R_2}
\begin{pmatrix}1&2&2\\0&1&2\\0&0&-2\end{pmatrix}=U,
$$
$$
L=\begin{pmatrix}1&0&0\\0&1&0\\2&-1&1\end{pmatrix},
\qquad PA'=LU .\quad\checkmark
$$
（这体现了第 9 节结论：对可逆矩阵 $A$，总存在排列阵 $P$ 使 $PA=LU$。）

---

## 练习 23　分块消元与舒尔补

设
$$
M=\begin{pmatrix}A&B\\C&D\end{pmatrix}
=\left(\begin{array}{cc|cc}2&1&3&2\\1&2&1&1\\\hline 3&1&16&9\\2&1&9&23\end{array}\right),
\qquad A=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
$$

1. 求 $A^{-1}$；
2. 求舒尔补 $S=D-CA^{-1}B$；
3. 写出消元矩阵 $E=\begin{pmatrix}I&O\\-CA^{-1}&I\end{pmatrix}$，验证 $EM=\begin{pmatrix}A&B\\O&S\end{pmatrix}$；
4. 求 $\det M$。

**【解答】**

**1.** $\det A=2\cdot2-1\cdot1=3$，故
$$
A^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}
=\begin{pmatrix}\frac23&-\frac13\\[2pt]-\frac13&\frac23\end{pmatrix}.
$$
**验证**：$AA^{-1}=I_2$ ✓。

**2.** 先算
$$
CA^{-1}=\begin{pmatrix}3&1\\2&1\end{pmatrix}\begin{pmatrix}\frac23&-\frac13\\[2pt]-\frac13&\frac23\end{pmatrix}
=\begin{pmatrix}2-\frac13&\,-1+\frac23\\[2pt]\frac43-\frac13&\,-\frac23+\frac23\end{pmatrix}
=\begin{pmatrix}\frac53&-\frac13\\[2pt]1&0\end{pmatrix},
$$
$$
CA^{-1}B=\begin{pmatrix}\frac53&-\frac13\\[2pt]1&0\end{pmatrix}\begin{pmatrix}3&2\\1&1\end{pmatrix}
=\begin{pmatrix}5-\frac13&\ \frac{10}3-\frac13\\[2pt]3&2\end{pmatrix}
=\begin{pmatrix}\frac{14}3&3\\[2pt]3&2\end{pmatrix}.
$$
故
$$
S=D-CA^{-1}B=\begin{pmatrix}16&9\\9&23\end{pmatrix}-\begin{pmatrix}\frac{14}3&3\\[2pt]3&2\end{pmatrix}
=\begin{pmatrix}\frac{34}3&6\\[2pt]6&21\end{pmatrix}.
$$

**3.** 直接计算 $EM$ 的左下块：$-CA^{-1}\cdot A+I\cdot C=-C+C=O$，而右下块为 $D-CA^{-1}B=S$，左上、右上块不变，故
$$
EM=\left(\begin{array}{cc|cc}2&1&3&2\\1&2&1&1\\\hline 0&0&\frac{34}3&6\\0&0&6&21\end{array}\right)=\begin{pmatrix}A&B\\O&S\end{pmatrix}.\quad\checkmark
$$
**要点**：分块消元用**逆矩阵**对整个分块（如整列）做消元，$-CA^{-1}$ 就是"整块的乘子"。

**4.** 由于 $E$ 为单位分块下三角（对角块是 $I$），$\det E=1$，故
$$
\det M=\det(EM)=\det A\cdot\det S
=3\cdot\left(\frac{34}3\cdot21-6\cdot6\right)=3\cdot(238-36)=3\cdot202=606 .
$$
**验算思路**：也可直接对 $M$ 做消元，得到相同结论。**关键恒等式**：$\det\begin{pmatrix}A&B\\C&D\end{pmatrix}=\det A\cdot\det(D-CA^{-1}B)$（$A$ 可逆时）。

---

## 练习 24　零空间与自由变量

设
$$
A=\begin{pmatrix}0&1&1\\0&2&5\\0&0&1\\0&1&1\end{pmatrix}.
$$

1. 求 $A$ 的行阶梯形 $U$ 与最简行阶梯形 $R$，指出哪些变量是自由变量；
2. 求 $N(A)$ 的一组基与 $\dim N(A)$；
3. 验证秩-零化度关系。

**【解答】**

**1.** 消元：
$$
A=\begin{pmatrix}0&1&1\\0&2&5\\0&0&1\\0&1&1\end{pmatrix}
\xrightarrow[R_4\leftarrow R_4-R_2]{R_3\leftarrow R_3-\frac12R_2}
\begin{pmatrix}0&1&1\\0&2&5\\0&0&1\\0&1&1\end{pmatrix}
\xrightarrow{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}0&1&1\\0&0&3\\0&0&1\\0&0&0\end{pmatrix}
$$
$$
\xrightarrow{R_3\leftarrow R_3-\frac13R_2}
\begin{pmatrix}0&1&1\\0&0&3\\0&0&0\\0&0&0\end{pmatrix}=U .
$$
继续 Jordan 消元（主元化为 $1$、主元上方化为 $0$）：
$$
U\to\begin{pmatrix}0&1&0\\0&0&1\\0&0&0\\0&0&0\end{pmatrix}=R .
$$
第 1 列无主元，第 2、3 列是主元列，故**自由变量为 $x_1$**，主元变量为 $x_2,x_3$。

**2.** 由 $R$ 得 $x_2=0,\ x_3=0$，$x_1$ 任意。令 $x_1=1$：
$$
N(A)=\operatorname{span}\left\{\begin{pmatrix}1\\0\\0\end{pmatrix}\right\},
\qquad \dim N(A)=1 .
$$
**验证**：$A(1,0,0)^{\mathsf T}=0$ ✓。

**3.** $\operatorname{rank}A=2$（$R$ 有两个非零行），$n=3$，故
$$
\dim C(A)+\dim N(A)=2+1=3=n .\quad\checkmark
$$

> **小结**：第 11 节的"主元变量/自由变量"判据——**主元列对应主元变量，自由列对应自由变量**；对每个自由变量取 $1$、其余自由变量取 $0$，即得 $N(A)$ 的一组基。**推论**：若 $m<n$，则 $Ax=0$ 必有非零解（因为主元个数 $r\le m<n$，至少有一个自由列）。

---

## 练习 25　RREF 保持列关系

设
$$
A=\begin{pmatrix}1&1&2\\1&2&3\\1&2&3\\1&3&4\end{pmatrix}.
$$

1. 求 $A$ 的最简行阶梯形 $R$ 与 $\operatorname{rank}A$；
2. 验证 $A$ 与 $R$ 的列之间保持**完全相同**的线性关系；
3. 若 $N(A)=\{x=\lambda(2,1,0,1)^{\mathsf T}\}$，问 $A$ 的 RREF 是什么？秩是多少？

**【解答】**

**1.** 消元（第 3 行 $=$ 第 2 行）：
$$
A\xrightarrow[R_3\leftarrow R_3-R_2]{R_2\leftarrow R_2-R_1}
\begin{pmatrix}1&1&2\\0&1&1\\0&0&0\\1&3&4\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-R_1}
\begin{pmatrix}1&1&2\\0&1&1\\0&0&0\\0&2&2\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-2R_2}
\begin{pmatrix}1&1&2\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}
$$
$$
\xrightarrow{R_1\leftarrow R_1-R_2}
\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}=R .
$$
主元在第 1、2 列，$\operatorname{rank}A=2$。

**2.** 由 $R$ 读出 $r_3=r_1+r_2$。因为消元过程相当于左乘可逆矩阵 $P$（$PA=R$），故对每个 $i$ 有 $Pa_i=r_i$：
$$
a_3-a_1-a_2=(2-1-1,\ 3-1-2,\ 3-1-2,\ 4-1-3)^{\mathsf T}=(0,0,0,0)^{\mathsf T},
$$
即 $a_3=a_1+a_2$，与 $r_3=r_1+r_2$ 形式完全一致。**结论**：$A$ 的 RREF 存储了 $A$ 各列从左至右的线性关系。

**3.** 若 $N(A)=\operatorname{span}\{(2,1,0,1)^{\mathsf T}\}$，则 $n=4$、$\dim N(A)=1$，故 $\operatorname{rank}A=4-1=3$，$R$ 有 3 个非零行。由 $Ax=0$ 的解 $x=(2\lambda,\lambda,0,\lambda)$ 知：$x_3$ 是自由变量（$x_3=0$），而 $2a_1+a_2+a_4=0$，即 $a_4=-2a_1-a_2$。故 RREF 中第 4 列为 $(-2,-1,0)^{\mathsf T}$（对应主元列 $1,2,3$）：
$$
R=\begin{pmatrix}1&0&0&-2\\0&1&0&-1\\0&0&1&0\\0&0&0&0\end{pmatrix},
\qquad \operatorname{rank}A=3 .
$$
（**验证**：$R\cdot(2,1,0,1)^{\mathsf T}=(2-2,\ 1-1,\ 0,\ 0)^{\mathsf T}=0$ ✓。）

---

## 练习 26　含参数的秩

对不同的 $\lambda$，讨论下述矩阵的秩：
$$
A=\begin{pmatrix}-1&2&\lambda\\1&-6&1\\10&1&\lambda\\5&-1&2\end{pmatrix}.
$$

**【解答】**

先找出使秩下降的 $\lambda$。观察**行之间的关系**：尝试 $r_3=5r_1-r_2$：
$$
5(-1,2,\lambda)-(1,-6,1)=(-6,10,5\lambda-1),
$$
与 $r_3=(10,1,\lambda)$ 不符。改试 $r_3=-r_1+?$：
$$
r_3+r_1=(9,3,\lambda+\lambda)=(9,3,2\lambda),\qquad
r_3-r_1=(11,-1,0).
$$
再看 $r_3$ 与 $r_1,r_2$ 的关系：设 $r_3=\alpha r_1+\beta r_2$，由前两个分量
$$
-\alpha+\beta=10,\qquad 2\alpha-6\beta=1
\;\Longrightarrow\;
\alpha=-\frac{61}{4},\ \beta=-\frac{21}{4},
$$
第三个分量要求 $\lambda=\alpha\lambda+\beta\cdot1$，即 $\lambda\left(1+\frac{61}4\right)=-\frac{21}4$，得 $\lambda=-\frac{21}{65}$——这说明用行关系找 $\lambda$ 不方便。

**改用列关系**（更快）：比较第 1、3 列
$$
a_1=\begin{pmatrix}-1\\1\\10\\5\end{pmatrix},\qquad
a_3=\begin{pmatrix}\lambda\\1\\\lambda\\2\end{pmatrix}.
$$
当 $\lambda=1$ 时 $a_3=(1,1,1,2)^{\mathsf T}$，$a_1+a_3=(0,2,11,7)^{\mathsf T}$ 与 $\lambda$ 无关；但更重要的是观察**第 1、3 列成比例**的条件：$a_3=\mu a_1$ 要求 $\lambda=\mu(-1)$、$1=\mu$、$\lambda=10\mu$、$2=5\mu$，矛盾。故第 1、3 列不成比例。

**系统做法**：对 $A$ 做行化简，考察第 3 列消元后是否出现零行。用第 1、2 行消去第 3、4 行的第 1 列：
$$
A\xrightarrow[R_4\leftarrow R_4+5R_1]{R_2\leftarrow R_2+R_1,\ R_3\leftarrow R_3+10R_1}
\begin{pmatrix}-1&2&\lambda\\0&-4&1+\lambda\\0&21&11\lambda\\0&9&2+5\lambda\end{pmatrix}.
$$
用第 2 行（主元 $-4$）消去第 3、4 行的第 2 列：
$$
\xrightarrow[R_4\leftarrow R_4+\frac94R_2]{R_3\leftarrow R_3+\frac{21}{4}R_2}
\begin{pmatrix}-1&2&\lambda\\0&-4&1+\lambda\\0&0&11\lambda+\frac{21}4(1+\lambda)\\0&0&2+5\lambda+\frac94(1+\lambda)\end{pmatrix}.
$$
计算两个右下元：
$$
c_3=11\lambda+\frac{21}4+\frac{21}4\lambda=\frac{65}4\lambda+\frac{21}4=\frac{65\lambda+21}{4},
$$
$$
c_4=2+5\lambda+\frac94+\frac94\lambda=\frac{17}4+\frac{29}4\lambda=\frac{29\lambda+17}{4}.
$$
当 $\lambda=-2$ 时：$c_3=\frac{-130+21}4=-\frac{109}4\ne0$，故第 3 个主元出现；继续消元后第 4 行会变成 $0$，故 $\operatorname{rank}A=3$。
为使第 4 行化为零要求 $c_4=\frac{29}4c_3$ 之外的消元结果为零，即
$$
c_4-\frac{29}{65}c_3=0
\;\Longleftrightarrow\;
\frac{29\lambda+17}4=\frac{29}{65}\cdot\frac{65\lambda+21}4
\;\Longleftrightarrow\;
29\lambda+17=29\lambda+\frac{609}{65}
\;\Longleftrightarrow\;
17=\frac{609}{65},
$$
不成立——说明**这个 $4\times3$ 矩阵的第 3 个主元总是存在**，即 $\operatorname{rank}A=3$ 对一切 $\lambda$ 成立。

**结论**：对任意 $\lambda\in\mathbb R$，$\operatorname{rank}A=3$。
**理由（更简洁）**：取 $A$ 的第 1、2 行与第 1、2 列构成的 $2\times2$ 子式
$$
\begin{vmatrix}-1&2\\1&-6\end{vmatrix}=6-2=4\ne0,
$$
再取第 1、2、4 行与第 1、2、3 列构成的 $3\times3$ 子式：
$$
\begin{vmatrix}-1&2&\lambda\\1&-6&1\\5&-1&2\end{vmatrix}
$$
按第 3 列展开，$\lambda$ 的系数为 $\begin{vmatrix}1&-6\\5&-1\end{vmatrix}=(-1)+30=29$，常数项为 $-\begin{vmatrix}-1&2\\5&-1\end{vmatrix}\cdot1+\begin{vmatrix}-1&2\\1&-6\end{vmatrix}\cdot2=-(1-10)+2(6-2)=9+8=17$，
故该子式 $=29\lambda+17$。当 $\lambda=-\frac{17}{29}$ 时它为零，但此时可用另一个 $3\times3$ 子式（如第 1、2、3 行）验证非零。由于总能找到非零的 $3$ 阶子式，故 $\operatorname{rank}A=3$ 恒成立。

> **小结**：讨论含参数矩阵的秩，通用流程是"**消元 + 考察主元**"，或"**找非零子式的最高阶**"。若把本题改为第 3 行为第 1、2 行之和（如练习 5 的 $A_6$），则可得到 $\lambda$ 取某值时秩下降的结论——这正是第 12 节习题 3 的设计思路。

---

## 练习 27　秩 1 矩阵

**1.** 求 $A=\begin{pmatrix}3&6&6\\1&2&2\\4&8&8\end{pmatrix}$ 的秩，并把它写成 $uv^{\mathsf T}$ 的形式。
**2.** 对 $B=\begin{pmatrix}2&2&6&4\\-1&-1&-3&-2\end{pmatrix}$，判断其秩并写成 $uv^{\mathsf T}$。
**3.** 证明：若 $m\times n$ 矩阵 $A$ 的秩为 $1$，则存在非零向量 $u\in\mathbb R^m$、$v\in\mathbb R^n$ 使 $A=uv^{\mathsf T}$。

**【解答】**

**1.** $A$ 的第 2、3 行分别是第 1 行的 $\frac13$、$\frac43$ 倍，且第 1 行各列成比例 $(3,6,6)=3(1,2,2)$，故 $\operatorname{rank}A=1$。取
$$
u=\begin{pmatrix}3\\1\\4\end{pmatrix},\qquad v=\begin{pmatrix}1\\2\\2\end{pmatrix},
\qquad
uv^{\mathsf T}=\begin{pmatrix}3\\1\\4\end{pmatrix}\begin{pmatrix}1&2&2\end{pmatrix}
=\begin{pmatrix}3&6&6\\1&2&2\\4&8&8\end{pmatrix}=A .\quad\checkmark
$$
（另一组取法：$u=(3,1,4)^{\mathsf T}$、$v=(1,2,2)^{\mathsf T}$ 是最自然的；一般 $u$ 可取 $A$ 的任一非零列，$v$ 为对应的比例系数向量。）

**2.** 第 2 行 $=-\frac12\times$ 第 1 行，故 $\operatorname{rank}B=1$。取
$$
u=\begin{pmatrix}2\\-1\end{pmatrix},\qquad v=\begin{pmatrix}1\\1\\3\\2\end{pmatrix},
\qquad
uv^{\mathsf T}=\begin{pmatrix}2&2&6&4\\-1&-1&-3&-2\end{pmatrix}=B .\quad\checkmark
$$

**3. 证明。** 设 $\operatorname{rank}A=1$。于是 $\dim C(A)=1$，$C(A)$ 由某一个非零向量张成，记为 $u\in\mathbb R^m\setminus\{0\}$。$A$ 的每一列 $a_j\in C(A)$，故存在 $v_j\in\mathbb R$ 使 $a_j=v_j u$。令 $v=(v_1,\dots,v_n)^{\mathsf T}$，则
$$
A=[a_1,\dots,a_n]=[v_1u,\dots,v_nu]=u\,v^{\mathsf T}.
$$
若 $v=0$，则 $A=0$，秩为 $0$，与秩为 $1$ 矛盾，故 $v\ne0$。$\blacksquare$
**直观**：秩 1 意味着 RREF 只有一个非零行，即 $A$ 的所有行都是同一行的倍数——$v^{\mathsf T}$ 记录那一行，$u$ 记录各行对应的倍数。

---

## 练习 28　$C(AB)\subset C(A)$ 的数值体会

**1.** 对 $A=\begin{pmatrix}1&2\\0&1\\3&1\end{pmatrix}$，$B=\begin{pmatrix}1&4\\2&5\end{pmatrix}$，计算 $AB$，并验证 $AB$ 的每一列都是 $A$ 的列的线性组合。
**2.** 设 $A$ 为 $m\times n$、$B$ 为 $n\times p$，证明 $N(B)\subset N(AB)$。
**3.** 在 (2) 的条件下，若 $B$ 可逆，证明 $C(AB)=C(A)$。

**【解答】**

**1.**
$$
AB=\begin{pmatrix}1&2\\0&1\\3&1\end{pmatrix}\begin{pmatrix}1&4\\2&5\end{pmatrix}
=\begin{pmatrix}1+4&4+10\\0+2&0+5\\3+2&12+5\end{pmatrix}
=\begin{pmatrix}5&14\\2&5\\5&17\end{pmatrix}.
$$
**验证列关系**：$A$ 的列为 $a_1=(1,0,3)^{\mathsf T}$，$a_2=(2,1,1)^{\mathsf T}$。
$$
1\cdot a_1+2\cdot a_2=(1+4,\ 0+2,\ 3+2)^{\mathsf T}=(5,2,5)^{\mathsf T}=(AB)_{\cdot 1}\ \checkmark
$$
$$
4\cdot a_1+5\cdot a_2=(4+10,\ 0+5,\ 12+5)^{\mathsf T}=(14,5,17)^{\mathsf T}=(AB)_{\cdot 2}\ \checkmark
$$
即 $(AB)_{\cdot j}=Ab_j=b_{1j}a_1+b_{2j}a_2$，正是列-列观点。

**2. 证明。** 设 $x\in N(B)$，即 $Bx=0$。则
$$
(AB)x=A(Bx)=A\cdot0=0,
$$
故 $x\in N(AB)$。因此 $N(B)\subset N(AB)$。$\blacksquare$

**3. 证明。** 由 (1)（及其一般形式）已有 $C(AB)\subset C(A)$。反过来，若 $B$ 可逆，令 $C=B^{-1}$，对矩阵对 $(AB,\,B^{-1})$ 再用同一结论：
$$
C(A)=C\big((AB)B^{-1}\big)\subset C(AB).
$$
两个包含方向相反，故 $C(AB)=C(A)$。$\blacksquare$
**直观**：左乘 $A$ 只可能"压缩"列空间；右乘可逆矩阵不损失信息，列空间不变。

---

# 第三部分　子空间、零空间与秩（9 题）

## 练习 29　子空间判定

判断下列集合是否为所指线性空间的子空间，并说明理由：
1. $W_1=\{(x,y)^{\mathsf T}\in\mathbb R^2:y=2x\}$，是否为 $\mathbb R^2$ 的子空间？
2. $W_2=\{(x,y)^{\mathsf T}\in\mathbb R^2:y=x+1\}$，是否为 $\mathbb R^2$ 的子空间？
3. $W_3=\{(x,y)^{\mathsf T}\in\mathbb R^2:xy\ge0\}$，是否为 $\mathbb R^2$ 的子空间？
4. $W_4=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}\in M_2(\mathbb R):a+d=0\right\}$（迹为零的 $2\times2$ 矩阵），是否为 $M_2(\mathbb R)$ 的子空间？
5. $W_5=\left\{(a_1,a_2,\dots,a_r,0,\dots,0)^{\mathsf T}\in\mathbb R^n:a_i\in\mathbb R,\ 1\le r<n\right\}$，是否为 $\mathbb R^n$ 的子空间？

**【解答】**

**判定三要素**：含零元、对加法封闭、对数乘封闭（第 10 节定义 2）。

**1. 是。** $W_1=\operatorname{span}\{(1,2)^{\mathsf T}\}$（过原点的直线）。$0\in W_1$；若 $(x_1,2x_1),(x_2,2x_2)\in W_1$，则其和为 $(x_1+x_2,\ 2(x_1+x_2))\in W_1$，数乘 $c(x_1,2x_1)=(cx_1,2cx_1)\in W_1$。故是子空间。

**2. 不是。** 因为 $(0,0)^{\mathsf T}\notin W_2$（$0\ne0+1$）——**子空间必含零向量**（第 10 节性质 2）。几何上是不过原点的直线。

**3. 不是。** 用**加法不封闭**来找反例：取
$$
v=(1,0)^{\mathsf T}\in W_3\ (\text{因 }1\cdot0=0\ge0),\qquad
w=(0,-1)^{\mathsf T}\in W_3\ (\text{因 }0\cdot(-1)=0\ge0).
$$
但
$$
v+w=(1,-1)^{\mathsf T},\qquad (1)(-1)=-1<0\ \Longrightarrow\ v+w\notin W_3 .
$$
故 $W_3$ **对加法不封闭**，不是子空间。
（几何上 $W_3$ 是第一、三象限之并，是两条互相垂直的射线的并集，显然不封闭；注意**数乘**对它其实是封闭的——取 $v=(x,y)$ 且 $xy\ge0$，则 $(cx)(cy)=c^2xy\ge0$——所以必须用加法找反例。）

**4. 是。** $W_4=\{A:\operatorname{tr}A=0\}$。$0$ 矩阵的迹为 $0$；若 $\operatorname{tr}A=\operatorname{tr}B=0$，则 $\operatorname{tr}(A+B)=0$，$\operatorname{tr}(cA)=c\operatorname{tr}A=0$（迹是线性的）。故是子空间。
更具体地，
$$
W_4=\left\{\begin{pmatrix}a&b\\c&-a\end{pmatrix}:a,b,c\in\mathbb R\right\},
\qquad \dim W_4=3 .
$$

**5. 是。** 显然 $0\in W_5$（取所有 $a_i=0$）。若 $x=(a_1,\dots,a_r,0,\dots,0)$、$y=(b_1,\dots,b_r,0,\dots,0)\in W_5$，则
$$
x+y=(a_1+b_1,\dots,a_r+b_r,0,\dots,0)\in W_5,\qquad
cx=(ca_1,\dots,ca_r,0,\dots,0)\in W_5 .
$$
故 $W_5$ 是 $\mathbb R^n$ 的子空间，且
$$
W_5=\operatorname{span}\{e_1,e_2,\dots,e_r\},\qquad \dim W_5=r .
$$

---

## 练习 30　张成空间与子空间的运算

**1.** 在 $\mathbb R^4$ 中，设 $v_1=(1,1,1,1)^{\mathsf T}$、$v_2=(1,1,1,0)^{\mathsf T}$。证明 $W=\operatorname{span}\{v_1,v_2\}$ 是 $\mathbb R^4$ 的子空间，并求 $\dim W$。
**2.** 设 $U_1,U_2$ 是线性空间 $V$ 的两个子空间。证明：$U_1\cup U_2$ 是子空间 $\iff$ $U_1\subset U_2$ 或 $U_2\subset U_1$。
**3.** 设 $X\subseteq V$ 是线性空间 $V$ 的任意子集，$S(X)$ 为 $X$ 中有限个元素的所有线性组合之集。证明 $S(X)$ 是 $V$ 的子空间。

**【解答】**

**1.** 一般结论：**任意有限个向量的张成空间都是子空间**（第 10 节定义 4 后的性质）。证明：设 $u=\lambda_1v_1+\lambda_2v_2$、$w=\mu_1v_1+\mu_2v_2\in W$，则
$$
u+w=(\lambda_1+\mu_1)v_1+(\lambda_2+\mu_2)v_2\in W,\qquad
cu=(c\lambda_1)v_1+(c\lambda_2)v_2\in W,
$$
且 $0=0v_1+0v_2\in W$。
又 $v_1,v_2$ 不成比例（第 4 分量 $1$ 与 $0$），故线性无关，
$$
\dim W=2 .
$$

**2. 证明。**
**（$\Leftarrow$）** 若 $U_2\subset U_1$，则 $U_1\cup U_2=U_1$ 是子空间；对称地，若 $U_1\subset U_2$ 则并集 $=U_2$ 也是子空间。

**（$\Rightarrow$）** 设 $U_1\cup U_2$ 是子空间。反设 $U_1\not\subset U_2$ 且 $U_2\not\subset U_1$，则可取 $u\in U_1\setminus U_2$（故 $u\notin U_2$）与 $v\in U_2\setminus U_1$（故 $v\notin U_1$）。
考虑 $u+v$。因 $U_1\cup U_2$ 对加法封闭，$u+v\in U_1\cup U_2$。
- 若 $u+v\in U_1$：由 $u\in U_1$ 得 $v=(u+v)-u\in U_1$，与 $v\notin U_1$ 矛盾；
- 若 $u+v\in U_2$：由 $v\in U_2$ 得 $u=(u+v)-v\in U_2$，与 $u\notin U_2$ 矛盾。

两者都不可能，故假设不成立，必有 $U_1\subset U_2$ 或 $U_2\subset U_1$。$\blacksquare$

**3. 证明。** 由定义
$$
S(X)=\Big\{\sum_{i=1}^{m}\lambda_i x_i:\ x_i\in X,\ m\in\mathbb N,\ \lambda_i\in\mathbb R\Big\}.
$$
**含零元**：取 $m=1,\lambda_1=0$（或空组合取 $0$），得 $0\in S(X)$。
**加法封闭**：设 $u=\sum_{i=1}^m\lambda_ix_i$、$w=\sum_{j=1}^{k}\mu_jy_j$，则
$$
u+w=\sum_{i=1}^m\lambda_ix_i+\sum_{j=1}^{k}\mu_jy_j
$$
仍是 $X$ 中有限个元素的线性组合，故属于 $S(X)$。
**数乘封闭**：$cu=\sum_{i=1}^m(c\lambda_i)x_i\in S(X)$。
故 $S(X)$ 是 $V$ 的子空间。$\blacksquare$

---

## 练习 31　列空间与行空间

设
$$
A=\begin{pmatrix}1&2&3\\2&4&6\\0&1&1\\1&3&4\end{pmatrix}.
$$

1. 求 $C(A)$ 的一组基与 $\dim C(A)$；
2. 求 $C(A^{\mathsf T})$ 的一组基与 $\dim C(A^{\mathsf T})$；
3. 在 $\mathbb R^4$ 中判断 $b_1=(1,0,0,9)^{\mathsf T}$、$b_2=(1,2,1,3)^{\mathsf T}$ 能否由 $A$ 的列线性表出。

**【解答】**

**1.** 行化简：
$$
A\xrightarrow[R_4\leftarrow R_4-R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&3\\0&0&0\\0&1&1\\0&1&1\end{pmatrix}
\xrightarrow{R_2\leftrightarrow R_3}
\begin{pmatrix}1&2&3\\0&1&1\\0&0&0\\0&1&1\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-R_2}
\begin{pmatrix}1&2&3\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}
$$
$$
\xrightarrow{R_1\leftarrow R_1-2R_2}
\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}=R .
$$
主元列是第 1、2 列，故 $C(A)$ 的基取**原矩阵的主元列**：
$$
C(A)=\operatorname{span}\left\{\begin{pmatrix}1\\2\\0\\1\end{pmatrix},\ \begin{pmatrix}2\\4\\1\\3\end{pmatrix}\right\},
\qquad \dim C(A)=2 .
$$
**2.** $C(A^{\mathsf T})$ 是 $A$ 的行空间，维数 $\dim C(A^{\mathsf T})=\operatorname{rank}A^{\mathsf T}=\operatorname{rank}A=2$。由 $R$ 的非零行读出 $C(A^{\mathsf T})$ 的一组基（行空间不因行变换改变）：
$$
C(A^{\mathsf T})=\operatorname{span}\left\{(1,0,1)^{\mathsf T},\ (0,1,1)^{\mathsf T}\right\},
\qquad \dim C(A^{\mathsf T})=2 .
$$
（也可取 $A$ 原来的第 1、3 行——它们线性无关且张成同一空间。）
**3.** 由 $R$ 得 $a_3=a_1+a_2$，故 $C(A)=\operatorname{span}\{a_1,a_2\}$。
- $b_1=(1,0,0,9)^{\mathsf T}$：设 $b_1=\lambda_1a_1+\lambda_2a_2$，由后两个分量 $\lambda_2=0$、$\lambda_1+\lambda_2=9$，得 $\lambda_1=9$，但第一分量应为 $9\cdot1+0=9\ne1$，矛盾。故 $b_1\notin C(A)$，**不能**表出。
- $b_2=(1,2,1,3)^{\mathsf T}$：设 $b_2=\lambda_1a_1+\lambda_2a_2$，由第 3、4 分量 $\lambda_2=1$、$\lambda_1+\lambda_2=3$，得 $\lambda_1=2$。检验前两个分量：$2\cdot1+1\cdot2=4\ne1$ ✗。故 $b_2\notin C(A)$，**不能**表出。
（若要 $b\in C(A)$，需满足消元后无矛盾行；可对 $[A\mid b]$ 消元检验。）

---

## 练习 32　零空间与特解

**1.** 求 $A=\begin{pmatrix}1&2\\3&6\end{pmatrix}$ 的零空间 $N(A)$，并给出几何描述。
**2.** 设 $A=\begin{pmatrix}1&2&3&4\\2&4&6&8\\1&1&1&1\end{pmatrix}$，求 $N(A)$ 的一组基。
**3.** 设 $A=\begin{pmatrix}1&1&2&3\\2&2&8&10\\3&3&10&13\end{pmatrix}$，求 $Ax=0$ 的解集，并指出主元变量与自由变量。

**【解答】**

**1.** $Ax=0$ 即 $x_1+2x_2=0$（第 2 行 $=3\times$ 第 1 行）。令 $x_2=t$（自由变量），则 $x_1=-2t$：
$$
N(A)=\operatorname{span}\left\{\begin{pmatrix}-2\\1\end{pmatrix}\right\}
=\left\{t\begin{pmatrix}-2\\1\end{pmatrix}:t\in\mathbb R\right\}.
$$
**几何**：过原点、方向为 $(-2,1)^{\mathsf T}$ 的直线。也可从列直接观察：$-2a_1+a_2=0$，即 $a_2=2a_1$。

**2.** 第 2 行 $=2\times$ 第 1 行，先消元：
$$
A\xrightarrow[R_3\leftarrow R_3-R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&3&4\\0&0&0&0\\0&-1&-2&-3\end{pmatrix}
\xrightarrow{R_2\leftrightarrow R_3}
\begin{pmatrix}1&2&3&4\\0&-1&-2&-3\\0&0&0&0\end{pmatrix}
\xrightarrow{R_1\leftarrow R_1+2R_2}
\begin{pmatrix}1&0&-1&-2\\0&-1&-2&-3\\0&0&0&0\end{pmatrix}
$$
$$
\xrightarrow{R_2\leftarrow -R_2}
\begin{pmatrix}1&0&-1&-2\\0&1&2&3\\0&0&0&0\end{pmatrix}=R .
$$
主元列第 1、2 列，自由变量 $x_3=s,\ x_4=t$：
$$
x_1=s+2t,\qquad x_2=-2s-3t,
$$
$$
x=s\begin{pmatrix}1\\-2\\1\\0\end{pmatrix}+t\begin{pmatrix}2\\-3\\0\\1\end{pmatrix}.
$$
故 $N(A)$ 的一组基为 $\left\{(1,-2,1,0)^{\mathsf T},\ (2,-3,0,1)^{\mathsf T}\right\}$，$\dim N(A)=2=n-\operatorname{rank}A=4-2$。

**3.** 消元：
$$
A\xrightarrow[R_3\leftarrow R_3-3R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&1&2&3\\0&0&4&4\\0&0&4&4\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_2}
\begin{pmatrix}1&1&2&3\\0&0&4&4\\0&0&0&0\end{pmatrix}
$$
$$
\xrightarrow[R_2\leftarrow \frac14R_2]{}
\begin{pmatrix}1&1&2&3\\0&0&1&1\\0&0&0&0\end{pmatrix}
\xrightarrow{R_1\leftarrow R_1-2R_2}
\begin{pmatrix}1&1&0&1\\0&0&1&1\\0&0&0&0\end{pmatrix}=R .
$$
**主元列**是第 1、3 列，故**主元变量**为 $x_1,x_3$，**自由变量**为 $x_2,x_4$。令 $x_2=s,x_4=t$：
$$
x_1=-s-t,\qquad x_3=-t,
$$
$$
x=s\begin{pmatrix}-1\\1\\0\\0\end{pmatrix}+t\begin{pmatrix}-1\\0\\-1\\1\end{pmatrix}.
$$
故
$$
N(A)=\operatorname{span}\left\{\begin{pmatrix}-1\\1\\0\\0\end{pmatrix},\ \begin{pmatrix}-1\\0\\-1\\1\end{pmatrix}\right\},
\qquad \dim N(A)=2 .
$$
（这正与第 11 节"对于每个自由列 $i$ 构造特解 $s_i$"的规则一致。）

---

## 练习 33　秩的计算与性质

**1.** 求 $A=\begin{pmatrix}2&0&4&6\\-1&1&2&2\\1&1&6&8\end{pmatrix}$ 的最简行阶梯形与秩，并根据 $R$ 写出 $Ax=0$ 的特解。
**2.** 分别选择向量 $u,v$ 使得 $A=uv^{\mathsf T}$：
$$
A_1=\begin{pmatrix}3&6&6\\1&2&2\\4&8&8\end{pmatrix},
\qquad
A_2=\begin{pmatrix}2&2&6&4\\-1&-1&-3&-2\end{pmatrix}.
$$
**3.** 证明：$A^{\mathsf T}A$ 的对角线元素必非负。

**【解答】**

**1.** 消元：
$$
A\xrightarrow[R_3\leftarrow R_3+R_1]{R_2\leftarrow R_2+\frac12R_1}
\begin{pmatrix}2&0&4&6\\0&1&4&5\\0&1&8&11\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_2}
\begin{pmatrix}2&0&4&6\\0&1&4&5\\0&0&4&6\end{pmatrix}
$$
$$
\xrightarrow[R_2\leftarrow R_2-R_3]{R_1\leftarrow R_1-R_3}
\begin{pmatrix}2&0&0&0\\0&1&0&-1\\0&0&4&6\end{pmatrix}
\xrightarrow{R_1\leftarrow \frac12R_1,\ R_3\leftarrow\frac14R_3}
\begin{pmatrix}1&0&0&0\\0&1&0&-1\\0&0&1&\frac32\end{pmatrix}=R .
$$
$\operatorname{rank}A=3$，主元列第 $1,2,3$ 列，自由变量 $x_4=t$：
$$
x_1=0,\qquad x_2=t,\qquad x_3=-\frac32t
\;\Longrightarrow\;
x=t\begin{pmatrix}0\\1\\-\frac32\\1\end{pmatrix}
\;\text{或}\;
t'\begin{pmatrix}0\\2\\-3\\2\end{pmatrix}.
$$
故 $\dim N(A)=1$，特解可取 $(0,2,-3,2)^{\mathsf T}$。

**2.**
$$
A_1=\begin{pmatrix}3\\1\\4\end{pmatrix}\begin{pmatrix}1&2&2\end{pmatrix},
\qquad
A_2=\begin{pmatrix}2\\-1\end{pmatrix}\begin{pmatrix}1&1&3&2\end{pmatrix}.
$$
（验证见练习 27。）

**3. 证明。** 设 $A$ 为 $m\times n$，记 $A$ 的列为 $a_1,\dots,a_n$，则 $A^{\mathsf T}A$ 的第 $i$ 行第 $j$ 列元为 $(A^{\mathsf T}A)_{ij}=a_i^{\mathsf T}a_j$。取 $i=j$：
$$
(A^{\mathsf T}A)_{ii}=a_i^{\mathsf T}a_i=\sum_{k=1}^{m}a_{ki}^2\ge0 .
$$
每个平方项非负，故对角线元素非负；且 $(A^{\mathsf T}A)_{ii}=0\iff a_i=0$（第 $i$ 列为零列）。$\blacksquare$
（另：$A^{\mathsf T}A$ 是对称矩阵，因为 $(A^{\mathsf T}A)^{\mathsf T}=A^{\mathsf T}A$。）

---

## 练习 34　秩与可逆性

**1.** 设 $A$ 为 $n$ 阶方阵。证明：$A$ 可逆 $\iff$ $\operatorname{rank}A=n$。
**2.** 设 $A$ 为 $4\times4$ 矩阵，$A$ 存在零行。判断 $A$ 是否可逆并说明理由。
**3.** 设 $A=\begin{pmatrix}1&2&3\\2&5&3\\1&0&8\end{pmatrix}$，用"主元个数"判断可逆性并求 $A^{-1}$。

**【解答】**

**1. 证明。**
**（$\Rightarrow$）** 若 $A$ 可逆，则对任意 $b\in\mathbb R^n$，$Ax=b$ 有唯一解 $x=A^{-1}b$。特别地取 $b=e_1,\dots,e_n$，得 $A x_i=e_i$，即 $e_i\in C(A)$。于是 $C(A)$ 包含 $\mathbb R^n$ 的一组基 $\{e_1,\dots,e_n\}$，故 $C(A)=\mathbb R^n$，$\operatorname{rank}A=\dim C(A)=n$。

**（$\Leftarrow$）** 若 $\operatorname{rank}A=n$，则 $A$ 有 $n$ 个主元（第 7 节定理 1）。由第 7 节"$A$ 可逆 $\iff$ 高斯消元能找到 $n$ 个主元"即得 $A$ 可逆。
也可直接论证：$n$ 个主元意味着齐次方程 $Ax=0$ 只有零解（自由变量个数 $=n-n=0$），故 $\dim N(A)=0$。……更直接地引用第 7 节定理 1 即可。$\blacksquare$

**2.** 设 $A$ 的第 $i$ 行为零行，则任一 $4$ 阶子式（只有 $4$ 阶子式，即 $\det A$）为零，因为按第 $i$ 行展开每项都含因子 $0$。故 $\operatorname{rank}A\le3<4$，由第 1 问知 $A$ **不可逆**。
**另一证法**：$Ae_i$ 的第……取 $b=e_i$（第 $i$ 个标准基向量），若 $Ax=b$ 有解则 $b$ 是 $A$ 的列的线性组合，但 $A$ 的每一列的第 $i$ 个分量都是 $0$，故任何线性组合的第 $i$ 个分量都是 $0\ne1$，矛盾。故 $Ax=e_i$ 无解，$A$ 不可逆。

**3.** 消元：
$$
A\xrightarrow[R_3\leftarrow R_3-R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&3\\0&1&-3\\0&-2&5\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3+2R_2}
\begin{pmatrix}1&2&3\\0&1&-3\\0&0&-1\end{pmatrix}.
$$
对角线元素均非零，**找到 3 个主元**，故 $A$ 可逆。由练习 16 的计算
$$
A^{-1}=\begin{pmatrix}-40&16&9\\13&-5&-3\\5&-2&-1\end{pmatrix}.
$$
（**验算**：$AA^{-1}=I_3$ ✓。也可先算 $\det A=1\cdot1\cdot(-1)=-1\ne0$ 判断可逆。）

---

## 练习 35　转置与对称矩阵

**1.** 设 $A=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}$，$B=\begin{pmatrix}1&0\\2&3\end{pmatrix}$。验证 $(AB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}$。
**2.** 设 $C=\begin{pmatrix}2&1\\1&3\end{pmatrix}$，验证 $(C^{\mathsf T})^{-1}=(C^{-1})^{\mathsf T}$，并说明 $C^{-1}$ 也是对称的。
**3.** 判断下列命题是否正确。
- (a) 若 $A,B$ 都对称，则 $A^2-B^2$ 对称；
- (b) 若 $A,B$ 都对称，则 $(A+B)(A-B)$ 对称；
- (c) 若 $A,B$ 都对称，则 $ABA$ 对称；
- (d) 若 $A,B$ 都对称，则 $ABAB$ 对称；
- (e) 给定任意方阵 $A$，分块矩阵 $\begin{pmatrix}O&A\\A&O\end{pmatrix}$ 必为对称矩阵；
- (f) 若 $A,B,C$ 都对称，则 $(ABC)^{\mathsf T}=CBA$。

**【解答】**

**1.**
$$
AB=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}\begin{pmatrix}1&0\\2&3\end{pmatrix}
=\begin{pmatrix}5&6\\11&12\\17&18\end{pmatrix},
\qquad
(AB)^{\mathsf T}=\begin{pmatrix}5&11&17\\6&12&18\end{pmatrix}.
$$
$$
B^{\mathsf T}A^{\mathsf T}=\begin{pmatrix}1&2\\0&3\end{pmatrix}\begin{pmatrix}1&3&5\\2&4&6\end{pmatrix}
=\begin{pmatrix}1+4&3+8&5+12\\0+6&0+12&0+18\end{pmatrix}
=\begin{pmatrix}5&11&17\\6&12&18\end{pmatrix}=(AB)^{\mathsf T}.\quad\checkmark
$$

**2.** $\det C=6-1=5$，故
$$
C^{-1}=\frac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}=\begin{pmatrix}\frac35&-\frac15\\[2pt]-\frac15&\frac25\end{pmatrix},
\qquad
(C^{-1})^{\mathsf T}=C^{-1}\ (\text{对称}).
$$
又
$$
(C^{\mathsf T})^{-1}=\left(\begin{pmatrix}2&1\\1&3\end{pmatrix}\right)^{-1}=C^{-1}=(C^{-1})^{\mathsf T}.\quad\checkmark
$$
**一般结论**：对称矩阵若可逆，其逆矩阵也对称（第 9 节性质 3）——因为 $(A^{-1})^{\mathsf T}=(A^{\mathsf T})^{-1}=A^{-1}$。

**3.**
**(a) 正确。** $(A^2-B^2)^{\mathsf T}=(A^2)^{\mathsf T}-(B^2)^{\mathsf T}=(A^{\mathsf T})^2-(B^{\mathsf T})^2=A^2-B^2$。
数值例：$A=\begin{pmatrix}1&2\\2&3\end{pmatrix},B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$，$A^2-B^2=\begin{pmatrix}5&8\\8&13\end{pmatrix}-\begin{pmatrix}1&0\\0&1\end{pmatrix}=\begin{pmatrix}4&8\\8&12\end{pmatrix}$，对称 ✓。

**(b) 错误。** 展开：
$$
(A+B)(A-B)=A^2-AB+BA-B^2 .
$$
它对称需要 $AB-BA$ 反对称且 $A^2-B^2$ 对称，即需要 $AB=BA$ 之外的额外条件；一般 $AB\ne BA$，故结果一般**不对称**。
**反例**：取上面的 $A,B$：
$$
(A+B)(A-B)=\begin{pmatrix}1&3\\3&3\end{pmatrix}\begin{pmatrix}1&1\\1&3\end{pmatrix}
=\begin{pmatrix}4&10\\6&12\end{pmatrix},
$$
而它的转置 $\begin{pmatrix}4&6\\10&12\end{pmatrix}\ne\begin{pmatrix}4&10\\6&12\end{pmatrix}$，故不对称。

**(c) 正确。** $(ABA)^{\mathsf T}=A^{\mathsf T}B^{\mathsf T}A^{\mathsf T}=ABA$。
数值例：$ABA=\begin{pmatrix}1&2\\2&3\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&2\\2&3\end{pmatrix}=\begin{pmatrix}2&1\\3&2\end{pmatrix}\begin{pmatrix}1&2\\2&3\end{pmatrix}=\begin{pmatrix}4&7\\7&12\end{pmatrix}$，对称 ✓。

**(d) 错误。** 一般 $(ABAB)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}B^{\mathsf T}A^{\mathsf T}=BABA\ne ABAB$（除非 $AB=BA$）。
**反例**：同上 $A,B$，$AB=\begin{pmatrix}2&1\\3&2\end{pmatrix}$，$(AB)^2=\begin{pmatrix}2&1\\3&2\end{pmatrix}^2=\begin{pmatrix}7&4\\12&7\end{pmatrix}$，其转置为 $\begin{pmatrix}7&12\\4&7\end{pmatrix}\ne\begin{pmatrix}7&4\\12&7\end{pmatrix}$，不对称。

**(e) 正确。** 记 $S=\begin{pmatrix}O&A\\A&O\end{pmatrix}$。转置逐块进行：$S^{\mathsf T}=\begin{pmatrix}O^{\mathsf T}&A^{\mathsf T}\\A^{\mathsf T}&O^{\mathsf T}\end{pmatrix}=\begin{pmatrix}O&A\\A&O\end{pmatrix}=S$（这里 $A$ 是方阵，两个 $A$ 互换位置后形式不变）。故 $S$ 对称。$\blacksquare$
**注**：这一结构正是第 9 节例 7 的"鞍点矩阵"的简化版本。

**(f) 正确。** 由转置的反序性质（第 9 节性质 2 的推论）
$$
(ABC)^{\mathsf T}=C^{\mathsf T}B^{\mathsf T}A^{\mathsf T}=CBA
$$
（因为 $A,B,C$ 对称）。$\blacksquare$

---

## 练习 36　$A^n$ 的递推计算

设
$$
A=\begin{pmatrix}3&-2\\1&0\end{pmatrix}.
$$

1. 验证 $A^2=3A-2I_2$；
2. 由此证明 $A^n=C+2^nD$，其中 $C=2I-A,\ D=A-I$；
3. 用 (2) 求 $A^5$，并与直接计算比较。

**【解答】**

**1.**
$$
A^2=\begin{pmatrix}3&-2\\1&0\end{pmatrix}\begin{pmatrix}3&-2\\1&0\end{pmatrix}
=\begin{pmatrix}9-2&-6+0\\3+0&-2+0\end{pmatrix}
=\begin{pmatrix}7&-6\\3&-2\end{pmatrix},
$$
$$
3A-2I_2=\begin{pmatrix}9&-6\\3&0\end{pmatrix}-\begin{pmatrix}2&0\\0&2\end{pmatrix}
=\begin{pmatrix}7&-6\\3&-2\end{pmatrix}=A^2.\quad\checkmark
$$

**2. 证明。** 由 $A^2=3A-2I$ 变形得
$$
A^2-3A+2I=O\;\Longrightarrow\;(A-I)(A-2I)=O
$$
直接计算验证：$(A-I)(A-2I)=A^2-3A+2I=O$ ✓。
记
$$
C=2I-A=\begin{pmatrix}-1&2\\-1&2\end{pmatrix},
\qquad D=A-I=\begin{pmatrix}2&-2\\1&-1\end{pmatrix}.
$$
则
$$
C+D=I,\qquad C+2D=(2I-A)+2(A-I)=A .
$$
**用归纳法证明 $A^n=C+2^nD$**：
- $n=0$：$C+2^0D=C+D=I=A^0$ ✓；
- $n=1$：$C+2D=A=A^1$ ✓；
- 设 $A^k=C+2^kD$。由 $A^2=3A-2I$ 得 $A^{k+1}=3A^k-2A^{k-1}$。代入归纳假设：
$$
A^{k+1}=3(C+2^kD)-2(C+2^{k-1}D)=C+3\cdot2^kD-2^kD=C+2^{k+1}D .
$$
故对一切 $n\ge0$，$A^n=C+2^nD$。$\blacksquare$
**（另一视角）** 上式说明 $A$ 的特征值为 $1,2$：$C$ 对应特征值 $1$ 的"投影"，$D$ 对应特征值 $2$ 的"投影"，$A^n$ 把 $2$ 的方向放大 $2^n$ 倍。

**3.**
$$
A^5=C+2^5D=\begin{pmatrix}-1&2\\-1&2\end{pmatrix}+32\begin{pmatrix}2&-2\\1&-1\end{pmatrix}
=\begin{pmatrix}-1+64&2-64\\-1+32&2-32\end{pmatrix}
=\begin{pmatrix}63&-62\\31&-30\end{pmatrix}.
$$
**直接验证**：
$$
A^2=\begin{pmatrix}7&-6\\3&-2\end{pmatrix},\quad
A^3=A^2A=\begin{pmatrix}15&-14\\7&-6\end{pmatrix},\quad
A^4=\begin{pmatrix}31&-30\\15&-14\end{pmatrix},\quad
A^5=\begin{pmatrix}63&-62\\31&-30\end{pmatrix}.\quad\checkmark
$$
（与练习 2 用"幂的递推 $A^n=A\cdot A^{n-1}$"的结果一致。）

---

## 练习 37　线性空间的判定

**1.** 判断下列集合在给定的加法与数乘下是否为**实线性空间**：
- (a) $M_{2}(\mathbb R)$（全体 $2\times2$ 实矩阵）；
- (b) $P_n=\{a_0+a_1x+\cdots+a_nx^n:a_i\in\mathbb R\}$（次数不超过 $n$ 的实系数多项式）；
- (c) $C(\mathbb R)$（$\mathbb R$ 上全体连续函数）；
- (d) $V=\left\{\begin{pmatrix}a&b\\c&d\end{pmatrix}:a,b,c,d\in\mathbb R,\ a+d=1\right\}$。
**2.** 写出 $M_2(\mathbb R)$ 中的一个子空间链 $D\subset U\subset M_2(\mathbb R)$，并给出各空间的维数，其中
$$
D=\left\{\begin{pmatrix}a&0\\0&d\end{pmatrix}\right\},
\qquad
U=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}\right\}.
$$
**3.** 在 $\mathbb R^2$ 中，分别记第一象限和第三象限的向量集合为 $A$ 与 $B$。判断 $A$ 与 $A\cup B$ 是否为 $\mathbb R^2$ 的子空间。

**【解答】**

**1.**
**(a) 是。** $M_2(\mathbb R)$ 中加法和数乘按元素定义，满足 8 条公理（第 10 节例 1）。$\dim M_2(\mathbb R)=4$。
**(b) 是。** 定义 $(f+g)(x)=f(x)+g(x)$、$(\lambda f)(x)=\lambda f(x)$，可逐条验证 8 条公理。$\dim P_n=n+1$（基 $1,x,\dots,x^n$）。
**(c) 是。** 连续函数之和、数乘仍连续。它是**无穷维**空间。
**(d) 不是。** $V$ 不含零元：$O$ 的对角元和为 $0\ne1$，故 $O\notin V$。**子空间（乃至线性空间）必含零元**，故 $V$ 不是线性空间。

**2.** 包含关系与维数：
$$
D=\left\{\begin{pmatrix}a&0\\0&d\end{pmatrix}:a,d\in\mathbb R\right\}
\;\subset\;
U=\left\{\begin{pmatrix}a&b\\0&d\end{pmatrix}:a,b,d\in\mathbb R\right\}
\;\subset\;
M_2(\mathbb R),
$$
$$
\dim D=2,\qquad \dim U=3,\qquad \dim M_2(\mathbb R)=4 .
$$
（$D$ 的基 $\left\{\begin{pmatrix}1&0\\0&0\end{pmatrix},\begin{pmatrix}0&0\\0&1\end{pmatrix}\right\}$；$U$ 的基再加 $\begin{pmatrix}0&1\\0&0\end{pmatrix}$。）

**3.** $A$（第一象限，含坐标轴正方向）**不是**子空间：取 $v=(1,1)^{\mathsf T}\in A$，但 $-1\cdot v=(-1,-1)^{\mathsf T}\notin A$，**对负数标量不封闭**（第 10 节例 11(a)）。
$A\cup B$ **不是**子空间：取 $u=(1,0)^{\mathsf T}\in A$、$v=(-1,-1)^{\mathsf T}\in B$，但
$$
u+v=(0,-1)^{\mathsf T}\notin A\cup B
$$
（第四象限），**对加法不封闭**（例 11(b)）。

---

# 第四部分　综合与证明（4 题）

## 练习 38　综合证明

**1.** 设 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times p}$、$C\in\mathbb R^{p\times q}$。证明：$\operatorname{rank}(ABC)\le\operatorname{rank}(AB)$，并由此推出 $\operatorname{rank}(ABC)\le\operatorname{rank}(B)$。
**2.** 设 $A$ 可逆。证明：$\operatorname{rank}(AB)=\operatorname{rank}B$。
**3.** 设 $A\in\mathbb R^{m\times n}$，$S\in\mathbb R^{m\times m}$ 对称。证明 $A^{\mathsf T}SA$ 对称，并确定其形状（阶数）。

**【解答】**

**1. 证明。** 把 $ABC$ 看作 $(AB)C$，由练习 6 的不等式
$$
\operatorname{rank}(ABC)=\operatorname{rank}\big((AB)C\big)\le\operatorname{rank}(AB).
$$
另一方面，把 $ABC$ 看作 $A(BC)$，由同一不等式
$$
\operatorname{rank}(ABC)=\operatorname{rank}\big(A(BC)\big)\le\operatorname{rank}(BC)\le\operatorname{rank}B
$$
（最后一步再用一次不等式）。故
$$
\operatorname{rank}(ABC)\le\min\{\operatorname{rank}(AB),\operatorname{rank}B\}\le\operatorname{rank}B.\qquad\blacksquare
$$
**2. 证明。** 由练习 6 已证 $C(AB)\subset C(A)$ 与 $\operatorname{rank}(AB)\le\operatorname{rank}B$。
另一方面，$B=A^{-1}(AB)$，由 $C(XY)\subset C(X)$ 得
$$
C(B)=C\big(A^{-1}(AB)\big)\subset C(AB),
$$
取维数得 $\operatorname{rank}B\le\operatorname{rank}(AB)$。两个不等式合并即 $\operatorname{rank}(AB)=\operatorname{rank}B$。$\blacksquare$
**直观**：左乘可逆矩阵是可逆变换，不改变列空间的维数（"可逆变换不损失信息"）。

**3. 证明。** 转置：
$$
(A^{\mathsf T}SA)^{\mathsf T}=A^{\mathsf T}S^{\mathsf T}(A^{\mathsf T})^{\mathsf T}=A^{\mathsf T}SA
$$
（用了 $S^{\mathsf T}=S$ 与 $(A^{\mathsf T})^{\mathsf T}=A$）。故 $A^{\mathsf T}SA$ 对称。$\blacksquare$
**形状**：$A$ 是 $m\times n$ ⟹ $A^{\mathsf T}$ 是 $n\times m$，$SA$ 是 $m\times n$，故
$$
A^{\mathsf T}SA\ \text{是}\ n\times n\ \text{方阵}.
$$
**特别地**（取 $S=I_m$）：$A^{\mathsf T}A$ 是 $n\times n$ 对称矩阵，其对角元非负（练习 33）。

---

## 练习 39　$I-AB$ 的可逆性与行列式

**1.** 证明：对任意 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times m}$，
$$
\det(I_m-AB)=\det(I_n-BA).
$$
（提示：当 $I_m-AB$ 可逆时，验证分块矩阵的恒等式
$\begin{pmatrix}I_m&A\\B&I_n\end{pmatrix}
=\begin{pmatrix}I_m&O\\B&I_n\end{pmatrix}
\begin{pmatrix}I_m&O\\O&I_m-AB\end{pmatrix}
\begin{pmatrix}I_m&A\\O&I_n\end{pmatrix}$ 之类；也可用分块行列式公式。）
**2.** 用 (1) 验证练习 7 的数值例子中的行列式关系。

**【解答】**

**1. 证明（用分块矩阵的两种消元方式计算同一个分块矩阵的行列式）。**
考虑
$$
M=\begin{pmatrix}I_m&A\\B&I_n\end{pmatrix}.
$$
**方式一**：对第一块施行消元（$R_2\leftarrow R_2-BR_1$），即左乘 $E_1=\begin{pmatrix}I_m&O\\-B&I_n\end{pmatrix}$（$\det E_1=1$）：
$$
E_1M=\begin{pmatrix}I_m&A\\O&I_n-BA\end{pmatrix}
\;\Longrightarrow\;
\det M=\det\begin{pmatrix}I_m&A\\O&I_n-BA\end{pmatrix}=\det(I_n-BA)
$$
（分块上三角阵的行列式 $=$ 对角块行列式之积）。

**方式二**：对第二块施行消元（$R_1\leftarrow R_1-AR_2$），即左乘 $E_2=\begin{pmatrix}I_m&-A\\O&I_n\end{pmatrix}$（$\det E_2=1$）：
$$
E_2M=\begin{pmatrix}I_m-AB&O\\B&I_n\end{pmatrix}
\;\Longrightarrow\;
\det M=\det\begin{pmatrix}I_m-AB&O\\B&I_n\end{pmatrix}=\det(I_m-AB)
$$
（分块下三角阵同理）。两次算的是同一个 $\det M$，故
$$
\det(I_n-BA)=\det M=\det(I_m-AB).\qquad\blacksquare
$$
**推论**：$I_m-AB$ 可逆 $\iff\det(I_m-AB)\ne0\iff\det(I_n-BA)\ne0\iff I_n-BA$ 可逆。这给出了练习 7 第 2 问的**另一个证明**（用行列式而非构造逆矩阵）。

**2. 验证。** 练习 7 中 $A=\begin{pmatrix}1&2\\3&4\\5&6\end{pmatrix}$（$3\times2$）、$B=\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}$（$2\times3$），已算得
$$
I_3-AB=\begin{pmatrix}0&-2&-3\\-3&-3&-7\\-5&-6&-10\end{pmatrix},
\qquad
I_2-BA=\begin{pmatrix}-5&-8\\-8&-9\end{pmatrix}.
$$
$$
\det(I_2-BA)=(-5)(-9)-(-8)(-8)=45-64=-19 .
$$
直接展开 $\det(I_3-AB)$（按第一行）：
$$
0\cdot\begin{vmatrix}-3&-7\\-6&-10\end{vmatrix}
-(-2)\begin{vmatrix}-3&-7\\-5&-10\end{vmatrix}
+(-3)\begin{vmatrix}-3&-3\\-5&-6\end{vmatrix}
$$
$$
=2\big(30-35\big)-3\big(18-15\big)=2(-5)-3(3)=-10-9=-19 .
$$
故 $\det(I_3-AB)=-19=\det(I_2-BA)$ ✓，与 (1) 的结论一致。

---

## 练习 40　秩的界与 $C(A)=C(B)$

**1.** 设 $A,B$ 均为 $m\times n$ 矩阵。证明：$C(A)=C(B)$ $\iff$ 存在可逆矩阵 $P$（$m$ 阶）使 $B=PA$。
**2.** 设 $A$ 为 $m\times n$、$B$ 为 $n\times p$。证明：
$$
\operatorname{rank}(AB)\ge\operatorname{rank}A+\operatorname{rank}B-n .
$$
（**Sylvester 秩不等式**；提示：对 $B$ 用秩-零化度定理，考察 $B$ 在 $N(AB)$ 上的限制，或利用 $N(AB)/N(B)\cong C(B)\cap N(A)$。）
**3.** 用练习 6 的数值例子检验 (2)。

**【解答】**

**1. 证明。**
**（$\Leftarrow$）** 若 $B=PA$ 且 $P$ 可逆，则由练习 28(3)（或练习 38(2)）$C(PA)=C(A)$，故 $C(B)=C(A)$。

**（$\Rightarrow$）** 设 $C(A)=C(B)=:W$，$\dim W=r$。取 $W$ 的一组基 $w_1,\dots,w_r$，把它分别补充成 $A$ 的列与 $B$ 的列……更简洁的论证：
$A,B$ 的列都张成 $W$，故 $A$ 的每一列都是 $B$ 的列的线性组合。设 $A=BX$（$X$ 为 $p\times n$ 的系数矩阵，这里 $B$ 是 $m\times n$……）——为避免记号混乱，改用如下论证：
$C(A)=C(B)$ 时 $\operatorname{rank}A=\operatorname{rank}B=r$。设 $A$ 的主元列为 $a_{i_1},\dots,a_{i_r}$，$B$ 的主元列为 $b_{j_1},\dots,b_{j_r}$。因两组都是 $W$ 的基，存在可逆的 $r\times r$ 矩阵 $Q$ 使 $(b_{j_1},\dots,b_{j_r})=(a_{i_1},\dots,a_{i_r})Q$。把"把主元列映到目标基"的线性变换扩充即可构造出可逆矩阵 $P$ 使 $B=PA$。
**更简单的做法**：由 $A,B$ 都有 $r$ 个主元，存在可逆矩阵 $P_1,P_2$（$m$ 阶，由消元过程给出）使
$$
P_1A=\begin{pmatrix}R_A\\O\end{pmatrix},\qquad P_2B=\begin{pmatrix}R_B\\O\end{pmatrix},
$$
其中 $R_A,R_B$ 都是 $r\times n$ 的 RREF，而 **RREF 由行空间唯一决定**；$C(A)=C(B)$ 等价于行空间相同，故 $R_A=R_B$。于是 $P_1A=P_2B$，取 $P=P_2^{-1}P_1$（可逆）得 $B=PA$。$\blacksquare$

**2. 证明。** 记 $r_A=\operatorname{rank}A$，$r_B=\operatorname{rank}B$，$r_{AB}=\operatorname{rank}(AB)$。
由秩-零化度定理（第 12 节）$\dim N(AB)=p-r_{AB}$，$\dim N(B)=p-r_B$。
因 $N(B)\subset N(AB)$（练习 28(2)），故
$$
\dim\big(N(AB)/N(B)\big)=\dim N(AB)-\dim N(B)=r_B-r_{AB} .
$$
**关键**：由 $x\in N(AB)\iff Bx\in N(A)$，映射
$$
\varphi:\ N(AB)\longrightarrow N(A),\qquad x\longmapsto Bx
$$
是良定义的线性映射，其核恰为 $N(B)$。故由同态基本定理
$$
N(AB)/N(B)\cong \operatorname{Im}\varphi\subseteq N(A)
\;\Longrightarrow\;
\dim\big(N(AB)/N(B)\big)\le\dim N(A)=n-r_A .
$$
于是
$$
r_B-r_{AB}\le n-r_A
\;\Longrightarrow\;
r_{AB}\ge r_A+r_B-n .\qquad\blacksquare
$$

**3. 检验。** 例中 $m=n=p$ 的情形：$A=\begin{pmatrix}1&2&3\\2&4&6\\1&1&1\end{pmatrix}$，$B=\begin{pmatrix}1&0\\2&1\\3&1\end{pmatrix}$ 不是方阵（$3\times2$），取 $n=3,p=2$：$r_A=2,\ r_B=2,\ r_{AB}=2$，则
$$
r_A+r_B-n=2+2-3=1\le2=r_{AB}\quad\checkmark
$$
不等式成立。**等号成立的条件**是 $\operatorname{Im}\varphi=N(A)$，即 $C(B)\cap N(A)=N(A)$，也就是 $N(A)\subset C(B)$。

> **小结**：Sylvester 秩不等式与练习 6 的 $\operatorname{rank}(AB)\le\min\{r_A,r_B\}$ 一起给出了乘积秩的**上下界**：
> $$\max\{0,\ r_A+r_B-n\}\le\operatorname{rank}(AB)\le\min\{r_A,r_B\}.$$

---

## 练习 41　综合模拟（期中仿真卷 B）

> 本题按试卷八大题的顺序各编一个小问，用于考前限时自测（建议 90 分钟）。

**1.** 已知 $A=\begin{pmatrix}0&1&2\\2&1&0\\1&0&1\end{pmatrix}=\big(\alpha_1\ \alpha_2\ \alpha_3\big)$。对任意 $a\in\mathbb R$ 求 $aA$；求 $\dim C(A)$；判断 $\operatorname{span}\{\alpha_1,\alpha_2\}$ 是否为 $\mathbb R^3$ 的子空间。

**2.** 已知 $A=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\end{pmatrix}$，求 $A^2,A^3,A^4,A^{100}$。

**3.** 对任意 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times p}$，证明 $N(B)\subset N(AB)$，并说明 $B$ 可逆时 $N(AB)=N(A)$。

**4.** 已知 $A=\begin{pmatrix}I_2&O\\A_1&I_2\end{pmatrix}$，$A_1=\begin{pmatrix}1&2\\0&1\end{pmatrix}$，$B=\begin{pmatrix}1&1&1&0\\0&1&0&1\\1&0&1&1\\0&1&1&0\end{pmatrix}$（按 $2\times2$ 分块）。求 $AB$。

**5.** 已知 $A=\begin{pmatrix}1&2&3\\2&5&7\\3&7&11\end{pmatrix}$。求 $A$ 的 LDU 分解及 $A^{-1}$（若存在）。

**6.** 已知 $A=\begin{pmatrix}1&1&2\\2&2&4\\1&0&1\end{pmatrix}$。求 RREF $R$、$C(A)$ 的一组基、$N(A)$ 的一组基；对 $b=(1,2,1)^{\mathsf T}$ 判断 $Ax=b$ 是否有解。

**7.** 对任意 $m\times n$ 矩阵 $A$，证明 $\operatorname{rank}(A)=\operatorname{rank}(A^{\mathsf T}A)$。

**8.** 证明 $\begin{pmatrix}I&O\\B&C\end{pmatrix}$ 可逆当且仅当 $C$ 可逆；并求 $I_2-AB$ 与 $I_3-BA$ 的可逆性关系，其中 $A=\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}^{\mathsf T}$ 型矩阵任取（写出你所用的一般结论即可）。

**【解答摘要】**

**1.** $aA=\begin{pmatrix}0&a&2a\\2a&a&0\\a&0&a\end{pmatrix}$。消元：$R_2\leftrightarrow R_1$ 后 $R_3\leftarrow R_3-\frac12R_1$，$R_3\leftarrow R_3-\frac14R_2$ 可得 3 个主元（$0\cdot$……），具体为
$$
\begin{pmatrix}0&1&2\\2&1&0\\1&0&1\end{pmatrix}\xrightarrow{R_1\leftrightarrow R_2}
\begin{pmatrix}2&1&0\\0&1&2\\1&0&1\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-\frac12R_1}
\begin{pmatrix}2&1&0\\0&1&2\\0&-\frac12&1\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3+\frac12R_2}
\begin{pmatrix}2&1&0\\0&1&2\\0&0&2\end{pmatrix},
$$
三个主元，故 $\operatorname{rank}A=3$，$\dim C(A)=3$。$\operatorname{span}\{\alpha_1,\alpha_2\}$ 是子空间（张成空间必为子空间）。

**2.** $A$ 是 4 阶循环移位置换矩阵，$A^4=I_4$，故
$$
A^2=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
A^3=\begin{pmatrix}0&0&0&1\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix},\quad
A^4=I_4,\quad
A^{100}=A^{4\cdot25}=(A^4)^{25}=I_4 .
$$

**3.** 若 $x\in N(B)$ 即 $Bx=0$，则 $(AB)x=A(Bx)=0$，故 $x\in N(AB)$，即 $N(B)\subset N(AB)$。
若 $B$ 可逆：$x\in N(AB)\Rightarrow A(Bx)=0\Rightarrow Bx\in N(A)$；令 $y=Bx$，则 $x=B^{-1}y$。反之 $y\in N(A)\Rightarrow A y=0\Rightarrow (AB)(B^{-1}y)=0$。故 $x\in N(AB)\iff Bx\in N(A)$。因为 $B$ 可逆给出 $\mathbb R^n\to\mathbb R^n$ 的双射，$x\mapsto Bx$ 是双射，故 $\dim N(AB)=\dim N(A)$；又 $N(A)\subset N(AB)$（因为 $B$ 可逆时……）——更直接：$N(AB)=B^{-1}(N(A))$，而可逆线性变换保持维数，且 $N(A)\subset N(AB)$ 成立，故两者维数相同且 $N(A)\subset N(AB)$ 给出 $N(A)=N(AB)$。$\blacksquare$

**4.** 按块乘法：
$$
AB=\begin{pmatrix}B_{11}&B_{12}\\A_1B_{11}+B_{21}&A_1B_{12}+B_{22}\end{pmatrix}.
$$
$B_{11}=\begin{pmatrix}1&1\\0&1\end{pmatrix}$，$B_{12}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$，$B_{21}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$，$B_{22}=\begin{pmatrix}1&1\\1&0\end{pmatrix}$。
$$
A_1B_{11}=\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}
=\begin{pmatrix}1&3\\0&1\end{pmatrix},\qquad
A_1B_{11}+B_{21}=\begin{pmatrix}2&3\\0&2\end{pmatrix},
$$
$$
A_1B_{12}=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
A_1B_{12}+B_{22}=\begin{pmatrix}2&3\\1&1\end{pmatrix}.
$$
故
$$
AB=\left(\begin{array}{cc|cc}1&1&1&0\\0&1&0&1\\\hline 2&3&2&3\\0&2&1&1\end{array}\right).
$$

**5.** 注意第 3 行 $=$ 第 1 行 $+$ 第 2 行（$1+2=3,\ 2+5=7,\ 3+7=10\ne11$）——第 3 列为 $10\ne11$，故第 3 行**不是**前两行之和。消元：
$$
A\xrightarrow[R_3\leftarrow R_3-3R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&3\\0&1&1\\0&1&2\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-R_2}
\begin{pmatrix}1&2&3\\0&1&1\\0&0&1\end{pmatrix},
$$
主元 $1,1,1$ 均非零，故 $A$ 可逆。$L=\begin{pmatrix}1&0&0\\2&1&0\\3&1&1\end{pmatrix}$，$D=\operatorname{diag}(1,1,1)=I$，$U=\begin{pmatrix}1&2&3\\0&1&1\\0&0&1\end{pmatrix}$，故 $A=LDU=LU$。
由 $A^{-1}=U^{-1}D^{-1}L^{-1}=U^{-1}L^{-1}$：
$$
U^{-1}=\begin{pmatrix}1&-2&-1\\0&1&-1\\0&0&1\end{pmatrix},
\qquad
L^{-1}=\begin{pmatrix}1&0&0\\-2&1&0\\-1&-1&1\end{pmatrix},
$$
$$
A^{-1}=U^{-1}L^{-1}.
$$
逐项计算 $U^{-1}L^{-1}$ 的第 1 行（用 $U^{-1}$ 的第 1 行 $=(1,-2,-1)$ 与 $L^{-1}$ 的各列作内积）：
$$
(U^{-1}L^{-1})_{11}=1\cdot1+(-2)(-2)+(-1)(-1)=6,\quad
(U^{-1}L^{-1})_{12}=1\cdot0+(-2)\cdot1+(-1)(-1)=-1,
$$
$$
(U^{-1}L^{-1})_{13}=1\cdot0+(-2)\cdot0+(-1)\cdot1=-1 .
$$
第 2 行（$U^{-1}$ 的第 2 行 $=(0,1,-1)$）：
$$
(U^{-1}L^{-1})_{21}=0+1\cdot(-2)+(-1)(-1)=-1,\quad
(U^{-1}L^{-1})_{22}=0+1\cdot1+(-1)(-1)=2,
$$
$$
(U^{-1}L^{-1})_{23}=0+0+(-1)\cdot1=-1 .
$$
第 3 行（$U^{-1}$ 的第 3 行 $=(0,0,1)$）：
$$
(U^{-1}L^{-1})_{31}=0+0+1\cdot(-1)=-1,\quad
(U^{-1}L^{-1})_{32}=0+0+1\cdot(-1)=-1,\quad
(U^{-1}L^{-1})_{33}=0+0+1\cdot1=1 .
$$
故
$$
A^{-1}=\begin{pmatrix}6&-1&-1\\-1&2&-1\\-1&-1&1\end{pmatrix}.
$$
**验算**：$A A^{-1}$ 第一行 $=(1\cdot6+2\cdot(-1)+3\cdot(-1),\ 1\cdot(-1)+2\cdot2+3\cdot(-1),\ 1\cdot(-1)+2\cdot(-1)+3\cdot1)=(1,0,0)$ ✓；第二行 $=(2\cdot6+5\cdot(-1)+7\cdot(-1),\ \cdots)=(0,1,0)$ ✓；第三行 $=(3\cdot6+7\cdot(-1)+11\cdot(-1),\ \cdots)=(0,0,1)$ ✓。

**6.** 消元：
$$
A=\begin{pmatrix}1&1&2\\2&2&4\\1&0&1\end{pmatrix}
\xrightarrow[R_3\leftarrow R_3-R_1]{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&1&2\\0&0&0\\0&-1&-1\end{pmatrix}
\xrightarrow{R_2\leftrightarrow R_3}
\begin{pmatrix}1&1&2\\0&-1&-1\\0&0&0\end{pmatrix}
\xrightarrow[R_2\leftarrow -R_2]{}
\begin{pmatrix}1&1&2\\0&1&1\\0&0&0\end{pmatrix}
$$
$$
\xrightarrow{R_1\leftarrow R_1-R_2}
\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\end{pmatrix}=R .
$$
主元列第 1、2 列，$\operatorname{rank}A=2$。
- $C(A)$ 的基（取原矩阵主元列）：$\left\{(1,2,1)^{\mathsf T},\ (1,2,0)^{\mathsf T}\right\}$。
- $N(A)$：自由变量 $x_3=t$，$x_1=-t,x_2=-t$，故基为 $\left\{(-1,-1,1)^{\mathsf T}\right\}$。
- $b=(1,2,1)^{\mathsf T}$：设 $b=\lambda_1a_1+\lambda_2a_2$，由第 3 分量 $\lambda_1=1$，由第 1 分量 $\lambda_1+\lambda_2=1\Rightarrow\lambda_2=0$，检验第 2 分量：$1\cdot2+0=2$ ✓。故 $b=(1,2,1)^{\mathsf T}=a_1\in C(A)$，**有解**，且特解 $x_p=(1,0,0)^{\mathsf T}$，全解 $x=(1-t,\ -t,\ t)^{\mathsf T}$（$t\in\mathbb R$）。

**7. 证明。** 只需证 $N(A)=N(A^{\mathsf T}A)$，再由秩-零化度定理 $n-\operatorname{rank}A=n-\operatorname{rank}(A^{\mathsf T}A)$ 即得。
- $N(A)\subset N(A^{\mathsf T}A)$：若 $Ax=0$，则 $A^{\mathsf T}Ax=A^{\mathsf T}0=0$。
- $N(A^{\mathsf T}A)\subset N(A)$：若 $A^{\mathsf T}Ax=0$，则
$$
0=x^{\mathsf T}(A^{\mathsf T}Ax)=(Ax)^{\mathsf T}(Ax)=\|Ax\|^2\;\Longrightarrow\;Ax=0 .
$$
故二者相等，从而 $\operatorname{rank}A=\operatorname{rank}(A^{\mathsf T}A)$。$\blacksquare$
（同理 $\operatorname{rank}A=\operatorname{rank}(AA^{\mathsf T})$。）

**8.** $\begin{pmatrix}I&O\\B&C\end{pmatrix}$ 可逆 $\iff C$ 可逆：见练习 7 第 1 问，且逆为 $\begin{pmatrix}I&O\\-C^{-1}B&C^{-1}\end{pmatrix}$。
一般结论：对任意 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times m}$，$I_m-AB$ 可逆 $\iff I_n-BA$ 可逆，且此时
$$
(I_n-BA)^{-1}=I_n+B(I_m-AB)^{-1}A .
$$
（见练习 7 第 2 问与练习 39。）

---

# 附录 A　公式与定理速查

## A.1 向量与内积（第 1 节）

| 名称 | 公式 |
|---|---|
| 内积 | $v\cdot w=v^{\mathsf T}w=\sum_i v_iw_i$ |
| 模长 | $\lVert v\rVert=\sqrt{v\cdot v}$ |
| 单位化 | $\hat v=v/\lVert v\rVert$ |
| 夹角 | $\cos\theta=\dfrac{v\cdot w}{\lVert v\rVert\lVert w\rVert}$ |
| 正交 | $v\perp w\iff v\cdot w=0$ |
| 施瓦茨不等式 | $\lvert v\cdot w\rvert\le\lVert v\rVert\lVert w\rVert$（等号 $\iff$ 线性相关） |
| 三角不等式 | $\lVert v+w\rVert\le\lVert v\rVert+\lVert w\rVert$ |

## A.2 线性方程组与高斯消元（第 2–4 节）

- 矩阵向量乘法：**列观点** $Ax=\sum_j x_ja_j$；**行观点** $(Ax)_i=a_i^{\mathsf T}x$。
- $Ax=b$ 有解 $\iff b\in C(A)$。
- **主元个数**判据（$n$ 个未知数）：

| 主元个数 | 是否出现 $0=c\ne0$ | 解的情况 |
|---|---|---|
| $n$ | 否 | 唯一解 |
| $<n$ | 是 | 无解 |
| $<n$ | 否 | 无穷多解（自由变量个数 $=n-$ 主元数） |

- $A$（$n$ 阶）可逆 $\iff$ 高斯消元能找到 $n$ 个主元 $\iff Ax=0$ 只有零解 $\iff\det A\ne0$。

## A.3 矩阵乘法与分块（第 5、6 节）

- 定义：$A_{m\times n}B_{n\times p}=(AB)_{m\times p}$，$(AB)_{ij}=\sum_k a_{ik}b_{kj}$。
- **列-列**：$AB=[Ab_1,\dots,Ab_p]$；**行-列**：$(AB)_{ij}=a_i^{\mathsf T}b_j$。
- **行-行**：$(AB)$ 的第 $i$ 行 $=a_i^{\mathsf T}B$（只与 $A$ 的第 $i$ 行有关）。
- **列-行（外积和）**：$AB=\sum_{k=1}^n a_kb_k^{\mathsf T}$。
- 分配律 $(A+B)C=AC+BC$、$C(A+B)=CA+CB$；结合律 $(AB)C=A(BC)$；**无交换律** $AB\ne BA$。
- 分块乘法：$C_{ij}=\sum_kA_{ik}B_{kj}$（$A$ 的列分块与 $B$ 的行分块一致）。
- 幂：$A^0=I$，$A^n=A\cdot A^{n-1}$，$(cA)^n=c^nA^n$。

## A.4 初等矩阵与逆（第 5、7 节）

| 初等矩阵 | 作用 | 逆 |
|---|---|---|
| $E_{ij}(\lambda)$ | 第 $i$ 行的 $\lambda$ 倍加到第 $j$ 行 | $E_{ij}(-\lambda)$ |
| $P_{ij}$ | 交换第 $i,j$ 行 | $P_{ij}$ |
| $D_i(\lambda)$ | 第 $i$ 行乘以 $\lambda\ne0$ | $D_i(1/\lambda)$ |

- $(AB)^{-1}=B^{-1}A^{-1}$；$(A_1\cdots A_k)^{-1}=A_k^{-1}\cdots A_1^{-1}$。
- $(A^{\mathsf T})^{-1}=(A^{-1})^{\mathsf T}$。
- **唯一性**：$AB=I$ 且 $CA=I$ $\Rightarrow B=C$。
- **判定**：$AB=I_n$（$A,B$ 为 $n$ 阶）$\Rightarrow BA=I_n$。
- Gauss–Jordan：$[A\mid I]\longrightarrow[I\mid A^{-1}]$。

## A.5 LU / LDU / PA=LU（第 8、9 节）

- 无行交换找到 $n$ 个主元 $\Longrightarrow A=LU$（$L$ 单位下三角，元素即消元乘子；$U$ 上三角，对角元即主元）。
- $U=D\tilde U$（$\tilde U$ 单位上三角，$D=\operatorname{diag}(u_{ii})$）$\Longrightarrow A=LD\tilde U$。
- **对称**情形：$A=LDL^{\mathsf T}$。
- 解 $Ax=b$：先解 $Ly=b$（前代），再解 $Ux=y$（回代）。
- 有行交换时：存在排列阵 $P$ 使 $PA=LU$；也存在 $\tilde P$ 使 $A=\tilde L\tilde P\tilde U$。
- 排列阵：每行每列恰一个 $1$；$P^{-1}=P^{\mathsf T}$。
- 分块消元：$\begin{pmatrix}I&O\\-CA^{-1}&I\end{pmatrix}\begin{pmatrix}A&B\\C&D\end{pmatrix}=\begin{pmatrix}A&B\\O&D-CA^{-1}B\end{pmatrix}$，$D-CA^{-1}B$ 为**舒尔补**。

## A.6 子空间、零空间与秩（第 10–12 节）

| 概念 | 定义 | 维数 |
|---|---|---|
| 列空间 $C(A)\subset\mathbb R^m$ | $A$ 的列的所有线性组合 | $\operatorname{rank}A$ |
| 行空间 $C(A^{\mathsf T})\subset\mathbb R^n$ | $A$ 的行的所有线性组合 | $\operatorname{rank}A$ |
| 零空间 $N(A)\subset\mathbb R^n$ | $\{x:Ax=0\}$ | $n-\operatorname{rank}A$ |

- 子空间判定：含零元 $+$ 对加法封闭 $+$ 对数乘封闭。
- **秩-零化度定理**：$\dim C(A)+\dim N(A)=n$。
- $C(A)$ 的基 $=$ RREF 主元列对应的**原矩阵列**；$N(A)$ 的基 $=$ 自由变量取 $1$ 的特解。
- RREF 保持列关系；RREF 唯一。
- 秩的性质：
  - $\operatorname{rank}A=\operatorname{rank}A^{\mathsf T}$；
  - $\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}$（练习 6）；
  - $\operatorname{rank}(AB)\ge\operatorname{rank}A+\operatorname{rank}B-n$（Sylvester，练习 40）；
  - $A$ 可逆 $\Rightarrow\operatorname{rank}(AB)=\operatorname{rank}B$；
  - $\operatorname{rank}A=\operatorname{rank}(A^{\mathsf T}A)$（练习 41 第 7 问）；
  - 秩 1 $\iff A=uv^{\mathsf T}$（练习 27）。
- $C(AB)\subset C(A)$；$N(B)\subset N(AB)$；$B$ 可逆 $\Rightarrow C(AB)=C(A)$。
- $\det(I_m-AB)=\det(I_n-BA)$（练习 39）。

---

# 附录 B　试卷题型 → 练习题对照表

| 试卷题号 | 试卷内容 | 本练习对应题 |
|---|---|---|
| 一 | 数乘 $aA$；$\dim C(A)$、$\dim C(A^{\mathsf T})$；$\operatorname{span}$ 是否为子空间 | **练习 1**、练习 41 第 1 问 |
| 二 | 循环移位矩阵求 $A^2,A^3,A^4$ | **练习 2**、练习 41 第 2 问 |
| 三 | 证明 $C(AB)\subset C(A)$；$B$ 可逆时相等 | **练习 6** 第 1 问、**练习 28**、练习 41 第 3 问 |
| 四 | 分块矩阵乘法 | **练习 3**、练习 41 第 4 问 |
| 五 | LDU 分解；$L^{-1},D^{-1},U^{-1},A^{-1}$ | **练习 4**、练习 21、练习 41 第 5 问 |
| 六 | RREF；$C(A)$、$N(A)$ 的基；$Ax=b$ 有解条件与全解 | **练习 5**、练习 25、练习 31、练习 32、练习 41 第 6 问 |
| 七 | 证明 $\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}$ | **练习 6**、练习 38、练习 40、练习 41 第 7 问 |
| 八 | 分块矩阵可逆性；$I_m-AB$ 与 $I_n-BA$ | **练习 7**、练习 39、练习 41 第 8 问 |

**按课件节次索引**

| 节次 | 相关练习 |
|---|---|
| 1 向量引论 | 练习 9 |
| 2 矩阵与方程组、可逆、相关无关 | 练习 7、9、10、18 |
| 3 行/列观点、特殊矩阵 | 练习 12、13 |
| 4 高斯消元法 | 练习 12、13 |
| 5 初等矩阵、矩阵运算、幂 | 练习 2、8、11、17、36 |
| 6 矩阵乘法四种视角、分块 | 练习 3、11、28、38 |
| 7 矩阵的逆、Gauss–Jordan | 练习 16、17、18、34 |
| 8 LU 分解 | 练习 19、20、21 |
| 9 转置、$LDL^{\mathsf T}$、排列阵、$PA=LU$、分块消元 | 练习 21、22、23、35 |
| 10 线性空间与子空间、$C(A)$ | 练习 1、15、29、30、31、37 |
| 11 零空间、自由变量 | 练习 24、32 |
| 12 RREF、列关系、秩 | 练习 5、8、10、25、26、27、33、34、40 |

---

# 附录 C　自检清单

做完上述练习后，请逐条确认自己能够**不查资料**完成：

- [ ] 用「列观点」和「行观点」两种方式解释 $Ax=b$ 与矩阵乘法 $AB$（练习 8、11）。
- [ ] 写出子空间判定的三要素，并判断 $\operatorname{span}$、齐次方程解集、直线/象限等集合是否为子空间（练习 29、30、37）。
- [ ] 用「主元个数」快速判断方程组唯一解 / 无解 / 无穷多解，并讨论含参数情形（练习 12、13）。
- [ ] 从高斯消元过程读出 $L$（乘子）与 $U$（上三角 / 主元），完成 $LU$、$LDU$ 分解并求逆（练习 4、19、20、21、41）。
- [ ] 对可逆矩阵完成 $PA=LU$ 分解，并说明何时必须行交换（练习 22）。
- [ ] 用 Gauss–Jordan 消元法求 $A^{-1}$（练习 16、34）。
- [ ] 用分块消元求舒尔补，并用 $\det M=\det A\cdot\det S$ 计算行列式（练习 23）。
- [ ] 从 RREF 读出 $C(A)$ 的基、$N(A)$ 的基与 $Ax=b$ 的全解，写出有解条件（练习 5、24、25、31、32）。
- [ ] 证明 $\operatorname{rank}(AB)\le\min\{\operatorname{rank}A,\operatorname{rank}B\}$ 与 Sylvester 秩不等式（练习 6、40）。
- [ ] 证明 $C(AB)\subset C(A)$、$N(B)\subset N(AB)$，以及 $B$ 可逆时 $C(AB)=C(A)$（练习 28、38）。
- [ ] 证明 $I_m-AB$ 可逆 $\iff I_n-BA$ 可逆，并写出逆矩阵的显式公式（练习 7、39）。
- [ ] 判断关于对称矩阵、转置、秩的命题真伪并给出反例（练习 18、26、35）。
- [ ] 说明 $\operatorname{rank}A=\operatorname{rank}(A^{\mathsf T}A)$ 的证明思路（练习 41 第 7 问）。
