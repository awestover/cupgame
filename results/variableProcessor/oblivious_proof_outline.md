Base case: $\rep(\randalg)$, then concentrate the fill in a known cup
  num cups: $\log^8 N$
  backlog: $\Theta(1)$ (or mass $N^2$)
  running time: $m=\Theta(N^2)$, so $\poly(N)$
  fail pr: $2^{-\Omega(\log^8 N)}$

Oblivious Amplification Lemma.
We are given $\alg(f)$ which has
  num cups: $n$
  backlog: $f(n)$ (or mass $N^2$)
  running time: $T(n)$
  fail pr: $p$, which is assumed to be $p\ge 1/2^{\lg^8 N}$.

We get $\alg(f')$ by doing $\rep(\alg(f))$ on $B$ and donating
cups to $A$, then doing $\alg(f)$ on $A$. $\alg(f')$ has
  num cups: $n$
  backlog: $f'(n) \ge (1-\delta)f(\floor{(1-\delta)n}) + f(\ceil{\delta n})$ (or mass $N^2$)
  running time: use $M = 2^{\log^{24} N}$, $T'(n) \le MnT(\floor{(1-\delta)n}) + T(\ceil{\delta n})$
  fail pr: $p' \le n p + 1/2^{\lg^8 N}$

Finally we recursively use the Oblivious Amplification Lemma to
get large backlog. Specifically, we let $f_{i+1}$ be the
amplification of $f_i$ using $\delta = \Theta(1)$ chosen as a
function of $\varepsilon$, and using $\randalg$ for $\alg(f_0)$.
In particular we get the following:
  num cups: $N$ 
  backlog: $\Omega(N^{1-\varepsilon})$
  running time: $(2^{\log^{24} N})^{\log N} = 2^{\log^{25} N}$
  fail pr: the recurrence $p_{i+1} = ap_i + b, p_1 = c$ solves to
    $p_k = b\Theta(a^{k-1}) + c \Theta(a^k)$. In our case this
    becomes $N^{\lg N} / 2^{\lg^8 N} + 2^{\lg N}/2^{\lg^8 N} = 2^{-\polylog(N)}$

