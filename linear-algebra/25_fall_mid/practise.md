# 高等代数 I · 期中复习练习题（第 1–5 节）

> **编制依据**
> - 课件：第 1 节（`1.md` 向量引论）、第 2–5 节（`la-02-slide` ~ `la-05-slide`，向量引论 / 线性方程组两种观点 / 高斯消元法 / 矩阵运算法则）
> - 试卷：2025 年第一学期期中考试（`25fall_mid.pdf`），本练习按试卷 8 道大题的题型逐一编制变式题。
>
> **使用建议**：先独立完成，再对照解答；每道题末尾标注了「涉及知识点」与「对应考试题」。

---

## 一、知识点清单（第 1–5 节）

| 节次 | 核心内容 |
|---|---|
| 第 1 节 | 向量与向量空间 $\mathbb F^n$；维数、数域、坐标；加法与数乘；线性组合与张成空间 $S(v_1,\dots,v_m)$；内积、模长、正交；施瓦茨不等式、三角不等式、夹角余弦 |
| 第 2 节 | 矩阵与线性方程组；矩阵向量乘法（**列观点**、**行观点**）；可逆矩阵定义（$Ax=b$ 有唯一解 $x=A^{-1}b$）；线性相关 / 线性无关及其几何意义 |
| 第 3 节 | 线性方程组的行观点（直线/平面）与列观点（线性组合）；有解 / 无解 / 无穷多解的判定；特殊矩阵：单位阵、对角阵、上 / 下三角阵 |
| 第 4 节 | 高斯消元法：主元、消元、回代；增广矩阵；行交换产生主元；**主元个数与解的情况** |
| 第 5 节 | 初等矩阵 $E_{ij}(\lambda)$ 与置换矩阵 $P_{ij}$；矩阵加法、数乘；矩阵乘法（列-列 / 行-列两种角度）；结合律、分配律、**乘法不满足交换律**；矩阵幂 $A^n$、$A^0=I$ |

**考试延伸概念**（试卷涉及、练习中同步覆盖）：列空间 $C(A)$、行空间 $C(A^\top)$、零空间 $N(A)$、维数 $\dim$、最简行阶梯形（RREF）、秩 $\mathrm{rank}$、LDU 分解、分块矩阵乘法与可逆性、秩不等式。

---

## 二、考试题型 → 练习题对照表

| 考试题 | 题型 | 对应练习题 |
|---|---|---|
| 一 | 数乘 $aA$；$\dim C(A)$、$\dim C(A^\top)$；span 是否为子空间 | 练习 1、14 |
| 二 | 矩阵幂 $A^2, A^3, A^4$ | 练习 4 |
| 三 | 证明 $C(AB)\subset C(A)$，$B$ 可逆时相等 | 练习 11 |
| 四 | 分块矩阵乘法 | 练习 6 |
| 五 | LDU 分解；$L^{-1},D^{-1},U^{-1},A^{-1}$ | 练习 10 |
| 六 | 最简行阶梯形；$C(A)$、$N(A)$ 的基；$Ax=b$ 有解条件与全解 | 练习 9 |
| 七 | 证明 $\mathrm{rank}(AB)\le\min\{\mathrm{rank}\,A,\mathrm{rank}\,B\}$ | 练习 12 |
| 八 | 分块矩阵可逆性；$I_m-AB$ 与 $I_n-BA$ | 练习 13 |

---

# 第一部分　向量与子空间（对应第 1、2 节）

## 练习 1　矩阵数乘与子空间判定

设
$$
A=\begin{pmatrix}1&-1&2\\2&0&1\\-1&3&1\end{pmatrix}=\big(\alpha_1\ \ \alpha_2\ \ \alpha_3\big).
$$

1. 对任意 $a\in\mathbb R$，求 $aA$；并求 $2A-I_3$；
2. 判断 $\mathrm{span}\{\alpha_1,\alpha_2\}$ 是否为 $\mathbb R^3$ 的子空间，并说明理由；
3. 判断集合 $W=\{(x,y,z)^\top\in\mathbb R^3:\ x+y-z=0\}$ 是否为 $\mathbb R^3$ 的子空间。

【涉及知识点】向量的数乘、矩阵的数乘（第 5 节）；张成空间 $\mathrm{span}$（第 1 节）；子空间的判定（加法、数乘封闭）。
【对应考试题】第一题第 1、3 问。

**【解答】**

1. 数乘逐元素进行：
$$
aA=\begin{pmatrix}a&-a&2a\\2a&0&a\\-a&3a&a\end{pmatrix},\qquad
2A-I_3=\begin{pmatrix}2&-2&4\\4&0&2\\-2&6&2\end{pmatrix}-\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}
=\begin{pmatrix}1&-2&4\\4&-1&2\\-2&6&1\end{pmatrix}.
$$

2. 是子空间。理由：$\mathrm{span}\{\alpha_1,\alpha_2\}=\{\lambda_1\alpha_1+\lambda_2\alpha_2:\lambda_1,\lambda_2\in\mathbb R\}$。对任意 $u,v\in\mathrm{span}$ 与 $c\in\mathbb R$，$u+v$ 与 $cu$ 仍是 $\alpha_1,\alpha_2$ 的线性组合（系数分别相加 / 放大 $c$ 倍），故对加法和数乘封闭；且 $0=0\cdot\alpha_1+0\cdot\alpha_2$ 属于其中。一般结论：**任意有限个向量的张成空间都是子空间**。

3. 是子空间。验证：
   - $0=(0,0,0)^\top\in W$（$0+0-0=0$）；
   - 加法封闭：设 $x_1+y_1-z_1=0$、$x_2+y_2-z_2=0$，则 $(x_1+x_2)+(y_1+y_2)-(z_1+z_2)=0$；
   - 数乘封闭：$c(x+y-z)=0$。
   
   也可写为 $W=\mathrm{span}\{(1,0,1)^\top,(0,1,1)^\top\}$，由第 2 问结论直接得是子空间。

> **小结**：判定子空间三要素——含零向量、加法封闭、数乘封闭；而「形如 $x+y-z=0$ 的齐次线性方程的解集」天然是子空间（自由变量参数化的张成空间）。

---

## 练习 2　内积、模长与施瓦茨不等式

设
$$
u=\begin{pmatrix}1\\2\\2\end{pmatrix},\qquad v=\begin{pmatrix}2\\1\\-1\end{pmatrix}.
$$

1. 求 $u\cdot v$、$\|u\|$、$\|v\|$，并判断 $u$ 与 $v$ 是否正交；
2. 验证施瓦茨不等式 $|u\cdot v|\le \|u\|\,\|v\|$；
3. 求 $u$ 与 $v$ 夹角 $\theta$ 的余弦值。

【涉及知识点】内积、模长、正交（第 1 节）；施瓦茨不等式、夹角余弦。
【对应考试题】第一题（数乘/内积运算背景）。

**【解答】**

1. $u\cdot v=1\cdot2+2\cdot1+2\cdot(-1)=2+2-2=2$；
$$
\|u\|=\sqrt{1^2+2^2+2^2}=3,\qquad \|v\|=\sqrt{2^2+1^2+(-1)^2}=\sqrt6.
$$
因 $u\cdot v=2\ne0$，$u$ 与 $v$ **不正交**。

2. $|u\cdot v|=2$，而 $\|u\|\|v\|=3\sqrt6\approx7.35$，故 $|u\cdot v|=2<3\sqrt6$，施瓦茨不等式成立（等号当且仅当两向量线性相关时取得）。

3. $\cos\theta=\dfrac{u\cdot v}{\|u\|\,\|v\|}=\dfrac{2}{3\sqrt6}=\dfrac{\sqrt6}{9}$。

> **小结**：$\langle u,v\rangle=0\iff u\perp v$；$\cos\theta=\dfrac{u\cdot v}{\|u\|\|v\|}$；施瓦茨不等式等价于 $|\cos\theta|\le1$。

---

## 练习 3　线性相关与线性无关

1. 判断向量组 $a_1=(1,1,1)^\top,\ a_2=(1,2,3)^\top,\ a_3=(1,4,9)^\top$ 是线性相关还是线性无关；
2. 设 $a_1,a_2,a_3$ 线性无关，证明向量组
$$
b_1=2a_1+a_2,\qquad b_2=a_2+3a_3,\qquad b_3=3a_1-a_3
$$
也线性无关。

【涉及知识点】线性相关 / 无关的定义（第 2 节）；由定义转化为齐次方程组。
【对应考试题】第一题第 3 问（子空间/独立性背景）、第二题（列向量性质）。

**【解答】**

1. 令 $x_1a_1+x_2a_2+x_3a_3=0$，即
$$
\begin{pmatrix}1&1&1\\1&2&4\\1&3&9\end{pmatrix}\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}=0.
$$
行化简：$R_2\leftarrow R_2-R_1$，$R_3\leftarrow R_3-R_1$ 得
$$
\begin{pmatrix}1&1&1\\0&1&3\\0&2&8\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-2R_2}
\begin{pmatrix}1&1&1\\0&1&3\\0&0&2\end{pmatrix}.
$$
三个主元，只有零解 $x=0$，故 $a_1,a_2,a_3$ **线性无关**。（几何上：三向量不共面。）

2. 设 $c_1b_1+c_2b_2+c_3b_3=0$，代入展开：
$$
c_1(2a_1+a_2)+c_2(a_2+3a_3)+c_3(3a_1-a_3)=0
$$
$$
\Longrightarrow\ (2c_1+3c_3)a_1+(c_1+c_2)a_2+(3c_2-c_3)a_3=0.
$$
因 $a_1,a_2,a_3$ 线性无关，各系数必为 $0$：
$$
\begin{cases}2c_1+3c_3=0\\c_1+c_2=0\\3c_2-c_3=0\end{cases}
\Longrightarrow c_1=-c_2,\ c_3=3c_2,\ 2(-c_2)+3(3c_2)=7c_2=0
\Longrightarrow c_1=c_2=c_3=0.
$$
故 $b_1,b_2,b_3$ 线性无关。$\blacksquare$

> **小结**：判线性无关的通用流程——设 $\sum c_iv_i=0$，利用已知无关性把问题化为齐次线性方程组，证明只有零解。注意消元得到 3 个主元 ⟺ 列向量线性无关。

---

# 第二部分　矩阵运算（对应第 5 节）

## 练习 4　矩阵的幂

1. 设
$$
A=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
$$
分别求 $A^2,A^3,A^4$；
2. 设
$$
B=\begin{pmatrix}0&2&0&0\\0&0&2&0\\0&0&0&2\\0&0&0&0\end{pmatrix},
$$
分别求 $B^2,B^3,B^4$。

【涉及知识点】矩阵幂 $A^n=A\cdots A$、$A^0=I$（第 5 节）；列-列乘法视角、幂零矩阵。
【对应考试题】第二题（4×4 循环矩阵求幂）。

**【解答】**

1. 记 $A=\big(a_1\ a_2\ a_3\big)$，其中 $a_1=e_3,\ a_2=e_1,\ a_3=e_2$（单位坐标向量 $e_1=(1,0,0)^\top,e_2=(0,1,0)^\top,e_3=(0,0,1)^\top$）。用列观点 $A^2=\big(Aa_1\ Aa_2\ Aa_3\big)$：
$$
A^2=\big(Ae_3\ \ Ae_1\ \ Ae_2\big)=\big(a_3\ \ a_1\ \ a_2\big)
=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.
$$
$$
A^3=A\cdot A^2=\big(Aa_3\ \ Aa_1\ \ Aa_2\big)=\big(a_2\ \ a_3\ \ a_1\big)
=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}=I_3.
$$
$$
A^4=A\cdot A^3=A\cdot I_3=A.
$$
（几何意义：$A$ 是把基向量循环右移一位的置换矩阵，作用 3 次回到自身。）

2. 记 $N$ 为单位上移位矩阵，则 $B=2N$。由矩阵幂的性质 $(kN)^m=k^mN^m$：
$$
B^2=4N^2=4\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix}
=\begin{pmatrix}0&0&4&0\\0&0&0&4\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$
$$
B^3=8N^3=8\begin{pmatrix}0&0&0&1\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}
=\begin{pmatrix}0&0&0&8\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
$$
$$
B^4=16N^4=\boldsymbol 0.
$$
（$B$ 是幂零矩阵：移位 4 次后元素全部移出矩阵，故 $B^4=0$。）

> **小结**：求幂两大利器——①列观点 $A^2=[Aa_1,\dots,Aa_n]$；②观察结构：置换/移位矩阵（若干次幂回到 $I$）与幂零矩阵（某次幂为 $0$，类似考试二的循环移位矩阵 $A^4=16I_4$）。

---

## 练习 5　矩阵乘法：列-列与行-列视角

1. 设 $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$，$B=\begin{pmatrix}5&6\\7&8\end{pmatrix}$，分别用**列-列**和**行-列**两种观点计算 $AB$；
2. 设 $A=\begin{pmatrix}0&0\\1&0\end{pmatrix}$，$B=\begin{pmatrix}0&1\\0&0\end{pmatrix}$，计算 $AB$ 与 $BA$，说明矩阵乘法不满足交换律；
3. 计算 $\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}2&5&3\end{pmatrix}$（列向量 × 行向量）。

【涉及知识点】矩阵乘法的等价定义：列-列、行-列（第 5 节）；$AB\ne BA$；外积。
【对应考试题】第四题（分块乘法的基础）、第五题（分解求逆的基础运算）。

**【解答】**

1. **列-列观点**：$B$ 的列 $b_1=(5,7)^\top,\ b_2=(6,8)^\top$，$AB$ 的第 $j$ 列 $=A$ 的所有列按 $b_j$ 的分量作线性组合：
$$
Ab_1=5\begin{pmatrix}1\\3\end{pmatrix}+7\begin{pmatrix}2\\4\end{pmatrix}
=\begin{pmatrix}19\\43\end{pmatrix},\qquad
Ab_2=6\begin{pmatrix}1\\3\end{pmatrix}+8\begin{pmatrix}2\\4\end{pmatrix}
=\begin{pmatrix}22\\50\end{pmatrix},
$$
故 $AB=\begin{pmatrix}19&22\\43&50\end{pmatrix}$。

   **行-列观点**：$(AB)(i,j)=A$ 第 $i$ 行 $\cdot\ B$ 第 $j$ 列：
$$
AB=\begin{pmatrix}1\cdot5+2\cdot7&1\cdot6+2\cdot8\\3\cdot5+4\cdot7&3\cdot6+4\cdot8\end{pmatrix}
=\begin{pmatrix}19&22\\43&50\end{pmatrix}.
$$

2. 
$$
AB=\begin{pmatrix}0&0\\1&0\end{pmatrix}\begin{pmatrix}0&1\\0&0\end{pmatrix}
=\begin{pmatrix}0&0\\0&1\end{pmatrix},
\qquad
BA=\begin{pmatrix}0&1\\0&0\end{pmatrix}\begin{pmatrix}0&0\\1&0\end{pmatrix}
=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
$$
$AB\ne BA$，故**矩阵乘法不满足交换律**（即使两矩阵都是方阵）。

3. 列向量乘行向量得 $3\times3$ 矩阵（外积）：
$$
\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}2&5&3\end{pmatrix}
=\begin{pmatrix}2&5&3\\4&10&6\\6&15&9\end{pmatrix}.
$$

> **小结**：$A_{m\times n}B_{n\times p}=(AB)_{m\times p}$；列-列观点说明「$AB$ 的每一列都是 $A$ 的列的线性组合」，这是证明 $C(AB)\subset C(A)$ 的关键（见练习 11）。

---

## 练习 6　分块矩阵乘法

将矩阵按 $2\times2$ 分块：
$$
A=\begin{pmatrix}I_2&O\\A_1&I_2\end{pmatrix},\qquad
A_1=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad O=\begin{pmatrix}0&0\\0&0\end{pmatrix},
$$
$$
B=\begin{pmatrix}B_{11}&B_{12}\\B_{21}&B_{22}\end{pmatrix}
=\left(\begin{array}{cc|cc}1&1&0&1\\2&0&1&2\\ \hline 1&0&1&1\\0&1&1&0\end{array}\right).
$$
求 $AB$。

【涉及知识点】分块矩阵乘法（把分块视为「块元素」作普通乘法）；单位阵与零矩阵的作用。
【对应考试题】第四题（$I_2/O/A_1/I_2$ 分块结构）。

**【解答】**
按分块乘法 $AB=\begin{pmatrix}I_2B_{11}+OB_{21}&I_2B_{12}+OB_{22}\\A_1B_{11}+I_2B_{21}&A_1B_{12}+I_2B_{22}\end{pmatrix}$：

- 左上块：$I_2B_{11}+OB_{21}=B_{11}=\begin{pmatrix}1&1\\2&0\end{pmatrix}$；
- 右上块：$I_2B_{12}+OB_{22}=B_{12}=\begin{pmatrix}0&1\\1&2\end{pmatrix}$；
- 左下块：
$$
A_1B_{11}+B_{21}=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&1\\2&0\end{pmatrix}+\begin{pmatrix}1&0\\0&1\end{pmatrix}
=\begin{pmatrix}3&1\\2&0\end{pmatrix}+\begin{pmatrix}1&0\\0&1\end{pmatrix}
=\begin{pmatrix}4&1\\2&1\end{pmatrix};
$$
- 右下块：
$$
A_1B_{12}+B_{22}=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}0&1\\1&2\end{pmatrix}+\begin{pmatrix}1&1\\1&0\end{pmatrix}
=\begin{pmatrix}1&3\\1&2\end{pmatrix}+\begin{pmatrix}1&1\\1&0\end{pmatrix}
=\begin{pmatrix}2&4\\2&2\end{pmatrix}.
$$

故
$$
AB=\left(\begin{array}{cc|cc}1&1&0&1\\2&0&1&2\\ \hline 4&1&2&4\\2&1&2&2\end{array}\right).
$$

> **小结**：只要各块维度相容，分块矩阵乘法完全照搬普通乘法公式；其中「单位块 $I$ 乘任何块不变、零块 $O$ 乘任何块为 $O$」可大幅化简。考试四的 $A$ 正是这种「下分块单位三角」结构。

---

# 第三部分　线性方程组（对应第 3、4 节）

## 练习 7　高斯消元法解方程组

用增广矩阵与高斯消元法求解：
$$
\begin{cases}2x+3y+z=8\\4x+7y+5z=20\\-2y+2z=0\end{cases}
$$

【涉及知识点】增广矩阵、主元、消元、回代（第 4 节）；上三角化后回代。
【对应考试题】第六题（消元与行阶梯形的基础）。

**【解答】**
增广矩阵：
$$
[A\mid b]=\left(\begin{array}{ccc|c}2&3&1&8\\4&7&5&20\\0&-2&2&0\end{array}\right).
$$
消元：$R_2\leftarrow R_2-2R_1$，再用 $R_2$ 消 $R_3$：
$$
\left(\begin{array}{ccc|c}2&3&1&8\\0&1&3&4\\0&-2&2&0\end{array}\right)
\xrightarrow{R_3\leftarrow R_3+2R_2}
\left(\begin{array}{ccc|c}2&3&1&8\\0&1&3&4\\0&0&8&8\end{array}\right).
$$
系数矩阵为上三角，主元为 $2,1,8$（共 3 个主元，有唯一解）。回代：
$$
z=\frac88=1,\qquad y+3z=4\Rightarrow y=1,\qquad 2x+3y+z=8\Rightarrow x=2.
$$
故唯一解为 $(x,y,z)=(2,1,1)$。

> **小结**：主元个数 $=$ 未知数个数 ⟹ 唯一解；消元过程只改变系数与右端，不改变解集。**三个主元 ⟺ 系数矩阵可逆 ⟺ 列向量线性无关 ⟺ 对任意 $b$ 有唯一解**。

---

## 练习 8　含参数方程组的解

已知方程组
$$
\begin{cases}3x+2y=10\\6x+4y=c\end{cases}
$$
其中 $c$ 为参数。讨论：(a) $c$ 满足什么条件时无解？(b) $c$ 满足什么条件时有无穷多解？写出任意两个解。

【涉及知识点】消元后 $0=0$（恒成立，无穷多解）与 $0=c\ne0$（矛盾，无解）（第 4 节）；自由变量。
【对应考试题】第六题第 4 问（有解条件与全解）的二维版本。

**【解答】**
增广矩阵：
$$
\left(\begin{array}{cc|c}3&2&10\\6&4&c\end{array}\right)
\xrightarrow{R_2\leftarrow R_2-2R_1}
\left(\begin{array}{cc|c}3&2&10\\0&0&c-20\end{array}\right).
$$
- (a) 若 $c-20\ne0$，出现矛盾方程 $0=c-20\ne0$，方程组**无解**（此时两方程对应两平行直线，行观点：不相交；列观点：$(3,6)^\top$ 与 $(2,4)^\top$ 共线但 $b$ 不在其上）。
- (b) 若 $c=20$，第二行为 $0=0$ 恒成立，只有 1 个主元 < 2 个未知数，**无穷多解**。令 $x=t$（自由变量），则 $3t+2y=10\Rightarrow y=5-\tfrac32t$，通解
$$
\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}t\\5-\frac32t\end{pmatrix},\quad t\in\mathbb R.
$$
取 $t=0$ 得 $(0,5)$，取 $t=2$ 得 $(2,2)$，均为解。

> **小结**：消元后主元个数小于未知数个数时，无解或无穷多解——区别在于是否出现 $0=c\ne0$ 的矛盾行；自由变量个数 $=$ 未知数个数 $-$ 主元个数。

---

## 练习 9　最简行阶梯形、列空间、零空间与全解（对应考试六）

设
$$
A=\begin{pmatrix}1&2&0&1\\0&1&1&2\\1&3&1&3\end{pmatrix}.
$$

1. 求 $A$ 的最简行阶梯形（RREF）$R$；
2. 求 $C(A)$ 的一组基；
3. 求 $N(A)$ 的一组基；
4. 对 $b=(1,2,3)^\top$，判断 $Ax=b$ 是否有解；若有解，写出方程的全解。

【涉及知识点】高斯消元到最简行阶梯形（第 4 节延伸）；主元列张成 $C(A)$；自由变量参数化 $N(A)$；非齐次方程全解 $=$ 特解 $+$ 齐次通解。
【对应考试题】第六题（RREF、$C(A)$ 基、$N(A)$ 基、有解条件与全解）。

**【解答】**

1. 消元：
$$
\left(\begin{array}{cccc}1&2&0&1\\0&1&1&2\\1&3&1&3\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_1}
\left(\begin{array}{cccc}1&2&0&1\\0&1&1&2\\0&1&1&2\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_2}
\left(\begin{array}{cccc}1&2&0&1\\0&1&1&2\\0&0&0&0\end{array}\right)
$$
$$
\xrightarrow{R_1\leftarrow R_1-2R_2}
\left(\begin{array}{cccc}1&0&-2&-3\\0&1&1&2\\0&0&0&0\end{array}\right)=R.
$$
主元列是第 1、2 列（rank $A=2$）。

2. $C(A)$ 由主元列对应的**原矩阵列**张成：
$$
C(A)=\mathrm{span}\left\{\begin{pmatrix}1\\0\\1\end{pmatrix},\ \begin{pmatrix}2\\1\\3\end{pmatrix}\right\},
$$
这两列线性无关（对应 RREF 中主元列），故为 $C(A)$ 的一组基，$\dim C(A)=2$。

3. 解 $Ax=0$。由 $R$ 得自由变量 $x_3=s,\ x_4=t$：
$$
x_1-2s-3t=0\Rightarrow x_1=2s+3t,\qquad x_2+s+2t=0\Rightarrow x_2=-s-2t,
$$
$$
x=\begin{pmatrix}x_1\\x_2\\x_3\\x_4\end{pmatrix}
=s\begin{pmatrix}2\\-1\\1\\0\end{pmatrix}+t\begin{pmatrix}3\\-2\\0\\1\end{pmatrix}.
$$
故 $N(A)$ 的一组基为
$$
\left\{\begin{pmatrix}2\\-1\\1\\0\end{pmatrix},\ \begin{pmatrix}3\\-2\\0\\1\end{pmatrix}\right\},\qquad \dim N(A)=2.
$$
（验证：$\dim C(A)+\dim N(A)=2+2=4=n$ ✓）

4. $b=(1,2,3)^\top$。$Ax=b$ 有解 ⟺ $b\in C(A)$ ⟺ 增广矩阵消元后无矛盾行。将 $b$ 并入增广矩阵：
$$
\left(\begin{array}{cccc|c}1&2&0&1&1\\0&1&1&2&2\\1&3&1&3&3\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_1}
\left(\begin{array}{cccc|c}1&2&0&1&1\\0&1&1&2&2\\0&1&1&2&2\end{array}\right)
\xrightarrow{R_3\leftarrow R_3-R_2}
\left(\begin{array}{cccc|c}1&2&0&1&1\\0&1&1&2&2\\0&0&0&0&0\end{array}\right).
$$
无矛盾行，有解（也可直接看出 $b$ 的第 3 分量 $3=1+2$ 恰为前两行之和，$b\in C(A)$）。取特解：令 $x_3=x_4=0$，解
$$
\begin{cases}x_1+2x_2=1\\x_2=2\end{cases}\Rightarrow x_2=2,\ x_1=-3,
$$
得特解 $x_p=(-3,2,0,0)^\top$。全解 $=$ 特解 $+$ 齐次通解：
$$
x=x_p+s\begin{pmatrix}2\\-1\\1\\0\end{pmatrix}+t\begin{pmatrix}3\\-2\\0\\1\end{pmatrix}
=\begin{pmatrix}-3+2s+3t\\2-s-2t\\s\\t\end{pmatrix},\qquad s,t\in\mathbb R.
$$

> **小结**：① RREF 中主元列对应原矩阵中线性无关的列，构成 $C(A)$ 的基；② 自由变量个数 $=\dim N(A)=n-\mathrm{rank}\,A$；③ 非齐次全解 $=$ 特解 $+$ 齐次通解；④ 有解条件：$b$ 落在 $C(A)$（消元无矛盾行）。

---

# 第四部分　LDU 分解与求逆（对应考试五）

## 练习 10　LDU 分解与矩阵求逆

设
$$
A=\begin{pmatrix}4&2&0\\2&3&1\\0&1&2\end{pmatrix}.
$$

1. 求 $A$ 的 LDU 分解（$A=LDU$，$L$ 为单位下三角，$D$ 为对角阵，$U$ 为单位上三角）；
2. 求 $L^{-1},D^{-1},U^{-1}$；
3. 求 $A^{-1}$。

【涉及知识点】高斯消元的矩阵化（第 5 节初等矩阵）；三角矩阵求逆；LDU 分解（考试延伸）。
【对应考试题】第五题。

**【解答】**

1. 对 $A$ 作高斯消元（不换行，主元均非零）：
$$
A=\begin{pmatrix}4&2&0\\2&3&1\\0&1&2\end{pmatrix}
\xrightarrow{R_2\leftarrow R_2-\frac12R_1}
\begin{pmatrix}4&2&0\\0&2&1\\0&1&2\end{pmatrix}
\xrightarrow{R_3\leftarrow R_3-\frac12R_2}
\begin{pmatrix}4&2&0\\0&2&1\\0&0&\frac32\end{pmatrix}.
$$
上三角部分提出对角元 $D=\mathrm{diag}\left(4,\ 2,\ \frac32\right)$，得单位上三角
$$
U=\begin{pmatrix}1&\frac12&0\\0&1&\frac12\\0&0&1\end{pmatrix},
$$
消元乘子（负号取反、下三角排列）构成单位下三角
$$
L=\begin{pmatrix}1&0&0\\\frac12&1&0\\0&\frac12&1\end{pmatrix}.
$$
验证：$LDU=A$（主元 $4,2,\frac32$ 非零，故分解唯一）。

2. **单位下三角求逆**（回代）：
$$
L^{-1}=\begin{pmatrix}1&0&0\\-\frac12&1&0\\\frac14&-\frac12&1\end{pmatrix},
$$
**对角阵求逆**（取倒数）：
$$
D^{-1}=\mathrm{diag}\left(\frac14,\ \frac12,\ \frac23\right),
$$
**单位上三角求逆**（对称地向前代入）：
$$
U^{-1}=\begin{pmatrix}1&-\frac12&\frac14\\0&1&-\frac12\\0&0&1\end{pmatrix}.
$$

3. 由 $A^{-1}=U^{-1}D^{-1}L^{-1}$，先算
$$
D^{-1}L^{-1}=\begin{pmatrix}\frac14&0&0\\-\frac14&\frac12&0\\\frac16&-\frac13&\frac23\end{pmatrix},
$$
再左乘 $U^{-1}$：
$$
A^{-1}=U^{-1}\big(D^{-1}L^{-1}\big)
=\begin{pmatrix}\frac{5}{12}&-\frac13&\frac16\\[2pt]-\frac13&\frac23&-\frac13\\[2pt]\frac16&-\frac13&\frac23\end{pmatrix}.
$$
**验证**：$A\cdot A^{-1}=I_3$（如第一行：$4\cdot\frac{5}{12}+2\cdot\left(-\frac13\right)=1$；$4\cdot\left(-\frac13\right)+2\cdot\frac23=0$；$4\cdot\frac16+2\cdot\left(-\frac13\right)=0$ ✓）。

> **小结**：LDU 三步走——①消元得 $U$ 与乘子 $l_{ij}$；②提出对角元得 $D$ 与单位三角 $U$；③逆序求逆：$A^{-1}=U^{-1}D^{-1}L^{-1}$。三角矩阵的逆仍是同型三角矩阵，可快速写出。

---

# 第五部分　子空间、秩与证明（对应考试一、三、六、七、八）

## 练习 11　列空间的包含关系（对应考试三）

1. 对任意 $A\in\mathbb R^{m\times n}$，$B\in\mathbb R^{n\times p}$，证明 $C(AB)\subset C(A)$；
2. 在 (1) 的条件下，若 $B$ 可逆，证明 $C(AB)=C(A)$；
3. 证明：$N(B)\subset N(AB)$。

【涉及知识点】列空间定义、矩阵乘法列-列观点（第 5 节）；子空间包含的证明。
【对应考试题】第三题。

**【解答】**

1. 设 $B=(b_1\ \cdots\ b_p)$，$A=(a_1\ \cdots\ a_n)$。由矩阵乘法的**列-列观点**，$AB$ 的第 $j$ 列
$$
(AB)_j=A\,b_j=b_{1j}a_1+b_{2j}a_2+\cdots+b_{nj}a_n,
$$
是 $A$ 的各列 $a_1,\dots,a_n$ 的线性组合，故 $(AB)_j\in C(A)$。因此 $C(AB)$ 中任意向量（各列的线性组合）都属于 $C(A)$，即
$$
C(AB)\subset C(A).\quad\blacksquare
$$

2. 由 (1) 已有 $C(AB)\subset C(A)$。因 $B$ 可逆，令 $C=B^{-1}$，对矩阵对 $(AB,\,B^{-1})$ 再用 (1)：
$$
C(A)=C\big((AB)B^{-1}\big)\subset C(AB).
$$
两边包含互为相反方向，故 $C(AB)=C(A)$。$\blacksquare$

3. 若 $x\in N(B)$，即 $Bx=0$，则 $(AB)x=A(Bx)=A\cdot0=0$，故 $x\in N(AB)$。因此 $N(B)\subset N(AB)$。$\blacksquare$

> **小结**：$C(AB)\subset C(A)$ 的直觉——左乘 $A$ 只可能「压缩」列空间；右乘可逆矩阵不改变列空间（可逆变换不损失信息）。$N(B)\subset N(AB)$ 是零空间版本的「压缩」。

---

## 练习 12　秩不等式（对应考试七）

对任意 $A\in\mathbb R^{m\times n}$，$B\in\mathbb R^{n\times p}$，证明：
$$
\mathrm{rank}(AB)\le\min\{\mathrm{rank}(A),\ \mathrm{rank}(B)\}.
$$

【涉及知识点】$\mathrm{rank}\,X=\dim C(X)$（考试延伸）；列空间包含与维数；$\mathrm{rank}X=\mathrm{rank}X^\top$。
【对应考试题】第七题。

**【解答】**
由练习 11(1)，$C(AB)\subset C(A)$，取维数得
$$
\mathrm{rank}(AB)=\dim C(AB)\le\dim C(A)=\mathrm{rank}(A).
$$
另一方面，转置不改变秩，且 $(AB)^\top=B^\top A^\top$。对矩阵对 $\big(B^\top,A^\top\big)$ 再用练习 11(1)：
$$
\mathrm{rank}(AB)=\mathrm{rank}\big((AB)^\top\big)
=\mathrm{rank}\big(B^\top A^\top\big)
\le\mathrm{rank}\big(B^\top\big)=\mathrm{rank}(B).
$$
两个不等式合并即得
$$
\mathrm{rank}(AB)\le\min\{\mathrm{rank}(A),\mathrm{rank}(B)\}.\quad\blacksquare
$$

> **小结**：核心链条——「列空间包含 $\Rightarrow$ 维数（秩）不等式」；转置技巧把对 $B$ 的约束转化为对 $B^\top$ 的列空间约束。考试七正是练习 11 与本题的组合。

---

## 练习 13　分块矩阵的可逆性（对应考试八）

1. 证明：分块矩阵 $\begin{pmatrix}I&O\\B&C\end{pmatrix}$ 可逆，当且仅当 $C$ 可逆；并求其逆矩阵；
2. 对任意 $A\in\mathbb R^{m\times n}$、$B\in\mathbb R^{n\times m}$，证明：$I_m-AB$ 可逆当且仅当 $I_n-BA$ 可逆；且当可逆时
$$
\big(I_n-BA\big)^{-1}=I_n+B\big(I_m-AB\big)^{-1}A.
$$

【涉及知识点】可逆的定义（$Ax=b$ 有唯一解，第 2 节）；分块矩阵乘法（练习 6）；恒等式验证。
【对应考试题】第八题。

**【解答】**

1. **（充分性）** 若 $C$ 可逆，对任意右端 $\begin{pmatrix}u\\v\end{pmatrix}$，方程
$$
\begin{pmatrix}I&O\\B&C\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}u\\v\end{pmatrix}
\iff\begin{cases}x=u\\Bx+Cy=v\end{cases}
$$
有唯一解 $x=u$，$y=C^{-1}(v-Bu)$。故 $\begin{pmatrix}I&O\\B&C\end{pmatrix}$ 可逆，且
$$
\begin{pmatrix}I&O\\B&C\end{pmatrix}^{-1}
=\begin{pmatrix}I&O\\-C^{-1}B&C^{-1}\end{pmatrix}.
$$
**（必要性）** 若整体矩阵可逆，则方程对任意右端有唯一解；特别地，取 $u=0$，由 $x=0$ 得 $Cy=v$ 对任意 $v$ 有唯一解 $y$，这正是「$C$ 可逆」的定义。$\blacksquare$

2. 先证「$\Leftarrow$」：设 $I_m-AB$ 可逆，验证 $I_n+B(I_m-AB)^{-1}A$ 是 $I_n-BA$ 的逆：
$$
\big(I_n-BA\big)\big[I_n+B(I_m-AB)^{-1}A\big]
$$
$$
=I_n-BA+B(I_m-AB)^{-1}A-BAB(I_m-AB)^{-1}A
$$
$$
=I_n-BA+B\big[I_m-AB\big](I_m-AB)^{-1}A
=I_n-BA+BA=I_n.
$$
（第三个等号用到分配律：$B(I_m-AB)^{-1}A-BAB(I_m-AB)^{-1}A=B[I_m-AB](I_m-AB)^{-1}A$。）

同理，若 $I_n-BA$ 可逆，由对称性（把 $A,B$ 的地位对调，$m,n$ 互换）知 $I_m-AB$ 也可逆，且
$$
\big(I_m-AB\big)^{-1}=I_m+A(I_n-BA)^{-1}B.
$$
故二者同时可逆，结论成立。$\blacksquare$

> **小结**：①「可逆 ⟺ 对任意右端有唯一解」是考试八第 1 问的钥匙；② 第 2 问的关键恒等式——若 $I_m-AB$ 可逆则 $I_n-BA$ 可逆，逆矩阵显式给出；这是 Sherman–Morrison–Woodbury 公式的特例，证明只需「构造逆并验证」。

---

## 练习 14　列空间、行空间与零空间的维数（对应考试一）

设
$$
A=\begin{pmatrix}1&2&3\\2&4&6\\0&1&1\\1&3&4\end{pmatrix}.
$$

1. 求 $\dim C(A)$ 与 $\dim C(A^\top)$；
2. 求 $C(A)$ 的一组基；
3. 求 $N(A)$ 的一组基，并验证 $\dim C(A)+\dim N(A)=n$。

【涉及知识点】列空间与行空间的维数、最简行阶梯形（考试延伸）；零空间参数化。
【对应考试题】第一题第 2 问（$\dim C(A)$、$\dim C(A^\top)$）、第六题。

**【解答】**
对 $A$ 作行化简：
$$
\begin{pmatrix}1&2&3\\2&4&6\\0&1&1\\1&3&4\end{pmatrix}
\xrightarrow{R_2\leftarrow R_2-2R_1}
\begin{pmatrix}1&2&3\\0&0&0\\0&1&1\\1&3&4\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-R_1}
\begin{pmatrix}1&2&3\\0&0&0\\0&1&1\\0&1&1\end{pmatrix}
$$
$$
\xrightarrow{R_3\leftrightarrow R_2}
\begin{pmatrix}1&2&3\\0&1&1\\0&0&0\\0&1&1\end{pmatrix}
\xrightarrow{R_4\leftarrow R_4-R_2}
\begin{pmatrix}1&2&3\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}
\xrightarrow{R_1\leftarrow R_1-2R_2}
\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\\0&0&0\end{pmatrix}.
$$
RREF 有两个非零行、主元在第 1、2 列，故 $\mathrm{rank}\,A=2$。

1. $\dim C(A)=\mathrm{rank}\,A=2$；$\dim C(A^\top)=\mathrm{rank}\,A^\top=\mathrm{rank}\,A=2$（**行空间与列空间维数相等**）。
2. $C(A)$ 的基取主元列对应的原矩阵列：
$$
\left\{\begin{pmatrix}1\\2\\0\\1\end{pmatrix},\ \begin{pmatrix}2\\4\\1\\3\end{pmatrix}\right\}.
$$
3. 解 $Ax=0$：由 RREF，$x_3=t$ 自由，
$$
x_1+t=0\Rightarrow x_1=-t,\qquad x_2+t=0\Rightarrow x_2=-t,
$$
$$
x=t\begin{pmatrix}-1\\-1\\1\end{pmatrix},
$$
故 $N(A)$ 的一组基为 $\left\{\begin{pmatrix}-1\\-1\\1\end{pmatrix}\right\}$，$\dim N(A)=1$。验证：
$$
\dim C(A)+\dim N(A)=2+1=3=n.\quad\checkmark
$$

> **小结**：① 列空间与行空间维数相等（都等于主元个数 / rank）；② 主元列（原矩阵列）构成 $C(A)$ 的基；③ 秩-零化度定理 $\dim C(A)+\dim N(A)=n$ 是自检答案的利器。考试一第 2 问即直接运用 $\dim C(A)=\dim C(A^\top)=\mathrm{rank}\,A$。

---

## 附：自我检验清单

- [ ] 能否从「列-列」与「行-列」两个角度解释矩阵乘法与 $Ax=b$？
- [ ] 能否写出判定子空间的完整三要素，并判断 $\mathrm{span}$ 与齐次方程解集？
- [ ] 能否用「主元个数」快速判断方程组唯一解 / 无解 / 无穷多解？
- [ ] 能否从高斯消元过程读出 $L$（乘子）与 $U$（上三角），完成 LDU 分解并求逆？
- [ ] 能否不查资料证明 $C(AB)\subset C(A)$、$\mathrm{rank}(AB)\le\min\{\mathrm{rank}A,\mathrm{rank}B\}$？
- [ ] 能否从 RREF 读出 $C(A)$ 基、$N(A)$ 基，并写出 $Ax=b$ 的全解？
