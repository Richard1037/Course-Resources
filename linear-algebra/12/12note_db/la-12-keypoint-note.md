# 第 12 讲要点笔记：简化行阶梯型与矩阵的秩
**（Reduced Row Echelon Form & Rank of a Matrix）**

> 本讲核心：研究矩阵 $A$ 经过高斯-约当消元（Gauss-Jordan elimination）化为简化行阶梯型 $R$ 之后，$R$ 如何"编码"了 $A$ 的列之间的线性关系，并由此构造零空间的基、定义矩阵的秩。

---

## 0. 复习要点（Recap）

| 中文 | English |
|---|---|
| 零空间（核） | Null space (kernel)，记作 $N(A)=\{x:Ax=0\}$ |
| 主元变量 / 自由变量 | Pivot variables / Free variables |
| 特解 | Particular solution（这里指 $Ax=0$ 的 basis vector） |
| 列空间 | Column space，记作 $C(A)$ |
| 行空间 | Row space |
| 张成 / 线性张成 | Span，$S(u,v)=\operatorname{span}\{u,v\}$ |

---

## 1. 简化行阶梯型与 $A$ 的列的关系

### 1.1 核心结论（最重要）

$A \xrightarrow{G-J} R$（简化行阶梯型），等价于存在**可逆矩阵** $P$（即一系列行变换的乘积）使得

$$PA = R.$$

按列写就是 $Pa_i = r_i$（$a_i$ 是 $A$ 的第 $i$ 列，$r_i$ 是 $R$ 的第 $i$ 列）。

> **Key fact**：因为 $P$ 可逆（invertible），$\{a_i\}$ 之间的任何线性关系（linear dependence）在 $\{r_i\}$ 之间被**完全原样保留**。
>
> 即：$a_j = c_1 a_{k_1}+\cdots+c_s a_{k_s} \iff r_j = c_1 r_{k_1}+\cdots+c_s r_{k_s}$。
>
> 直观理解：可逆变换不改变"谁是谁的线性组合"，只是换了一组坐标基底。

### 1.2 主元列 vs 自由列（Pivot columns vs Free columns）

以例 1 为例：

$$
A=\begin{bmatrix}1&1&2&4\\1&2&2&5\\1&3&2&6\end{bmatrix},
\qquad
R=\begin{bmatrix}1&0&2&3\\0&1&0&1\\0&0&0&0\end{bmatrix}.
$$

观察 $R$ 的列关系：

- $r_1 \neq 0$；$r_2$ 不是 $r_1$ 的倍数；
- $r_3 = 2r_1$；$r_4 = 3r_1 + r_2$。

把这个关系**直接搬运**到 $A$：

- $a_1,a_2$ 是**主元列（pivot columns）**：它们**不能**表示为其左边列的线性组合（linearly independent from columns to the left）。
- $a_3,a_4$ 是**自由列（free columns）**：它们**总能且唯一**地表示为其左边主元列的线性组合：
  $$a_3 = 2a_1,\qquad a_4 = 3a_1+a_2.$$

> **为什么？** 因为自由列中非零元素所在的行一定是主元行，该行必有一个主元为 1，因此系数可以直接从 $R$ 读出。

### 1.3 主元列在 $R$ 中的标准形式

$a_{k_i}$ 是第 $i$ 个主元列 $\iff$ 在 $R$ 中它就是标准单位向量：

$$r_{k_i} = \begin{bmatrix}0\\ \vdots\\ 1\\ \vdots\\ 0\end{bmatrix} = e_i.$$

自由列 $a_j$ 在 $R$ 中长这样（上方是系数，下方全是 0）：

$$r_j = \begin{bmatrix}r_{1j}\\ \vdots\\ r_{i-1,j}\\ 0\\ \vdots\\ 0\end{bmatrix}
\quad\Longrightarrow\quad
a_j = r_{1j}a_{k_1}+\cdots+r_{i-1,j}a_{k_{i-1}}.$$

**推论（Corollary）**：$A$ 的简化行阶梯型 $R$ 是**唯一的（unique）**。

---

## 2. 特解的构造（Construction of Null Space Basis）

仍以 $R$ 为例，把它按"主元列在前、自由列在后"分块：

$$
R = \left[\begin{array}{c|c} I & F \\ \hline 0 & 0 \end{array}\right],
\qquad
F = \begin{bmatrix}2&3\\0&1\end{bmatrix}.
$$

对每个自由变量取"一个为 1、其余为 0"，得到 $Ax=0$ 的特解：

$$
u=\begin{bmatrix}-2\\0\\1\\0\end{bmatrix}\ (x_3=1,x_4=0),
\qquad
v=\begin{bmatrix}-3\\-1\\0\\1\end{bmatrix}\ (x_3=0,x_4=1).
$$

把它们并成矩阵 $N=[u\ v]$：

$$
N=\begin{bmatrix}-2&-3\\0&-1\\1&0\\0&1\end{bmatrix}
=\boxed{\begin{bmatrix}-F\\ I\end{bmatrix}}.
$$

验证：$RN=0 \iff AN=0$（因为 $A=P^{-1}R$，$P$ 可逆）。

> **记忆点**：零空间矩阵的"自由变量对应块"是单位阵 $I$，"主元变量对应块"就是 $-F$。

---

## 3. 零空间的完整刻画（Null Space = Column Space of N）

$$
\boxed{N(A) = S(u,v) = \operatorname{span}\{u,v\}}
$$

**证明思路**：

1. $u,v\in N(A)$，所以 $S(u,v)\subseteq N(A)$。
2. 任取 $x\in N(A)$，则 $Rx=0$。分块写：
   $$
   \begin{bmatrix}I&F\\0&0\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}=0
   \iff x_1 = -F x_2.
   $$
3. 于是
   $$
   x=\begin{bmatrix}x_1\\x_2\end{bmatrix}
   =\begin{bmatrix}-F x_2\\x_2\end{bmatrix}
   =\begin{bmatrix}-F\\I\end{bmatrix}x_2 = N x_2.
   $$
   即 $x\in S(u,v)$，所以 $N(A)\subseteq S(u,v)$。
4. 双向包含 $\Rightarrow$ 等号成立。

---

## 4. 矩阵的秩（Rank of a Matrix）

### 定义 1（最常用）

矩阵 $A$ 的**主元个数（number of pivots）**称为 $A$ 的秩，记作 $r(A)$ 或 $\operatorname{rank}(A)$。

等价地：$r(A)=$ $R$ 中**非零行的行数**。

> 直观：$r(A)$ 代表方程 $Ax=0$ 中"本质上独立的方程个数"。非主元行都能被主元行消成 0，即它们是主元行的线性组合。

### 定义 2（从行的角度）

若 $A$ 有 $r$ 个**线性无关的行（linearly independent rows）**，则 $r$ 就是秩。

### 定义 3（从空间维数的角度）

- $r = \dim C(A)$（列空间的维数 dimension of column space）
- $r = \dim$（行空间）（dimension of row space）
- **$n-r = \dim N(A)$**（零空间的维数，称为零化度 nullity）

> 三个定义互相等价；背后的关键事实是：**主元行数 = 主元列数 = 主元个数**。

### 重要关系（Fundamental Theorem of LA 之一）

$$
\boxed{\dim C(A) + \dim N(A) = n}
\qquad\text{即}\qquad
r(A) + \operatorname{nullity}(A) = n.
$$

---

## 5. 秩 1 矩阵（Rank-1 Matrices）

### 例子

$$
A=\begin{bmatrix}1&2&3\\2&4&6\\3&6&9\end{bmatrix}
\longrightarrow
R=\begin{bmatrix}1&2&3\\0&0&0\\0&0&0\end{bmatrix},
\quad r(A)=1.
$$

注意到 $a_2=2a_1,\ a_3=3a_1$，并且

$$
A = \underbrace{\begin{bmatrix}1\\2\\3\end{bmatrix}}_{u}\underbrace{\begin{bmatrix}1&2&3\end{bmatrix}}_{v^\top} = uv^\top.
$$

### 性质（Rank-1 factorization）

若 $A_{m\times n}$ 的秩为 1，则存在非零向量 $u\in\mathbb{R}^m$、$v\in\mathbb{R}^n$ 使得

$$
\boxed{A = u v^\top.}
$$

**直观理解**：秩 1 意味着 $R$ 只有一行主元，$A$ 的每一行都是这一行的某个倍数。$v^\top$ 就是那个"基准行"，$u$ 记录每一行对应的倍数。

> **怎么找 $u, v$？**
> - $v^\top$ 可以取 $R$ 中唯一的非零行（或 $A$ 中任意一个非零行）；
> - $u$ 的第 $i$ 个分量 = $A$ 的第 $i$ 行是 $v^\top$ 的多少倍。

---

## 6. 一图流总结（Cheat Sheet）

```
A (m×n)
 │  Gauss-Jordan
 ▼
R = [ I  F ]   ← r 个主元行
    [ 0  0 ]
 │
 ├── 列关系：R 中各列的线性关系 = A 中各列的线性关系（P 可逆）
 │     · 主元列 = R 中的标准单位向量 e_i
 │     · 自由列 = 左边主元列的线性组合，系数直接读 R
 │
 ├── 零空间基：N = [ -F ]  (n × (n-r))
 │                 [  I ]
 │     N(A) = span{ N 的各列 }
 │
 └── 秩：r(A) = #pivots = #非零行 = dim C(A) = dim row space
         dim N(A) = n - r
```

---

## 7. 本讲关键术语英中对照

| English | 中文 |
|---|---|
| Reduced Row Echelon Form (RREF) | 简化行阶梯型 / 简化阶梯型 |
| Pivot / Pivot position | 主元 / 主元位置 |
| Pivot column / Free column | 主元列 / 自由列 |
| Pivot variable / Free variable | 主元变量 / 自由变量 |
| Linear combination | 线性组合 |
| Linearly independent / dependent | 线性无关 / 线性相关 |
| Invertible matrix | 可逆矩阵 |
| Column space $C(A)$ / Row space | 列空间 / 行空间 |
| Null space $N(A)$ (kernel) | 零空间（核） |
| Basis | 基 |
| Dimension | 维数 |
| Rank $r(A)$ | 秩 |
| Nullity | 零化度（$=\dim N(A)=n-r$） |
| Span | 张成 |
| Gauss-Jordan elimination | 高斯-约当消元 |
| Rank-1 factorization $A=uv^\top$ | 秩 1 分解 |
| Particular solution | 特解 |
| Standard basis vector $e_i$ | 标准单位向量 |

---

## 8. 课后习题提示（Hints）

1. **题 1**：先化 $R$，按"主元列 / 自由列"分块读出 $F$，再写 $N=\begin{bmatrix}-F\\I\end{bmatrix}$ 的各列作为特解。
2. **题 2**：$N(A)$ 是 1 维 $\Rightarrow$ $n-r=1$，$n=4$ 故 $r=3$。把给定特解 $u=(2,1,0,1)^\top$ 与 $N=\begin{bmatrix}-F\\I\end{bmatrix}$ 的结构对照，反推哪些列是自由列、$F$ 长什么样。
3. **题 3**：对 $\lambda$ 作分情况讨论（case analysis），看秩何时从 3 降到 2（甚至 1）。
4. **题 4**：秩 1 $\Leftrightarrow$ 任意两行成比例、任意两列成比例。用已知元素按比例填 $\Box$。
5. **题 5**：取 $A$ 中任意一个非零行作为 $v^\top$，再用每行与该行的比值填 $u$。

---

*生成自 la-12-slide.pdf，整理日期：2026-10-20*
