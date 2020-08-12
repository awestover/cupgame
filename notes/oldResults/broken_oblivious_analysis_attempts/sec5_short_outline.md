different structural idea:

first describe the rep procedure
then prove some invariants that it holds (the clm s)
  e.g. mu(B) le mu(AB) + delta f(n_B) and stuff
  more invariants 
  more invariants
two separate prop s to analyze cases p(n) = O(1) and p(n) = 1-1/2^n - 1/M
(probably these go with the base case & obliv amp lem pf s)


lem **(The reps LEMMA)**

given: 
  alg_p{f}:
    input: $R_\Delta$ flat cup config with avg fill $\mu_0$
    pr: conditional on no extra-emptyings, succeeds with probability $p(n)$ vs $\Delta$-greedy-like
    output: cup with fill at least $f(n) + \mu_0$ 
    unconditional guarantee: cups always are $(R_\Delta + k_\Delta f(n))$-flat
gives:
  $\rep(\alg_p{f})$:
    parameters: $\delta$, $n_A = \ceil{n\delta}$, $n_B = n-n_A$
    input: $R_\Delta$-flat cup config with avg fill $\mu_0$
    pr: conditional on no extra emptyings, succeeds with probability $1-n_A/\poly(M)$ vs $\Delta$-greedy-like
    output: gets $n\cdot p(n)$ cups with fill at least $\mu_0 + (1-\delta)f(n_B)$
    unconditional guarantees: cups always are $(R_\Delta + k_\Delta f(n))$-flat

pf
  algorithm:
    $B \gets$ all cups; $A \gets \varnothing$
    for $i \gets 1,2,\ldots, n_A$
      $m_0$ \gets uniformly randomly chosen from $[m]$ ($m \in \poly(M)$ to be specified)
      for $j \gets 1,2,\ldots, m_0$
        flatten $B$
        apply $\alg_p{f}$ to $B$
      donate the last cup given by $\alg_p{f}$ from $B$ to $A$

  First we condition on no extra emptyings,
  clm 1: flattening always succeeds \textbf{and} $B$ is always $(R_\Delta + f(n_B))$-flat
    pf if $B$ was pretty flat, then we can flatten $B$. if $B$ starts
    flat before applying $\alg_p{f}$ it stays pretty flat during the
    application. donation doesn't mess with flatness. $B$ started $R_\Delta$-flat. 
    induction.

  clm 2: $\mu(B) \le \mu(AB) + \frac{\delta}{1-\delta} f(n_B) + 2R_\Delta.$
    pf 
    two ways for $\mu(B) - \mu(AB)$ to increase:
      case 1: skip emptying $B$
        because of greediness $\min \fil(a) > \max \fil(b) - \Delta$, so $\mu(AB) + \Delta n_A/n \ge \mu(B)$
        i.e. $\mu(B) \le \mu(AB) + \Delta \delta$
      case 2: donate a cup with fill lower than $\mu(B)$
      ---
      consider the final round when B is skipped but A is not skipped (or the first round if there are no such rounds)
      from this round on, case 2 is the only way for $\mu(B) - \mu(AB)$
      to increase. Recall that we're assuming $\mu(AB)$
      doesn't decrease (i.e. no extra-emptyings of $AB$). 
      Hence it suffices to bound how much $\mu(B)$ could increase.
      by flatness of $B$, the worst case is that $B$ donates a cup with
      fill $\mu(B) - R_\Delta - f(n_B)$ to $A$ on all $n_A$
      donation processes. But even doing this would only change
      $B$ by a little bit. In particular, removing something with
      fill $\mu(B)-x$ from $B$ does $\mu(B) \mapsto \mu(B) + x/(|B|-1)$.
      If this happened $n_A$ times, then we would still have 
      $$\mu(B) \le \mu(AB) + \Delta\delta + (R_\Delta + f(n_B))\ln(1/(1-\delta))$$
      an interesting note is that $\ln(1/(1-\delta)) \approx \delta$ for $\delta \approx 0$ 
      so this is almost saying somehting like $\mu(B) \le \mu(AB) + \delta f(n_B)$, but not quite.
      something to note is that $\ln(1/(1-\delta)) \le \frac{1}{1-\delta} -1 = \delta/(1-\delta).$

  clm 3: $\mu(B) \ge \mu(AB) - \frac{\delta}{(1-\delta)^2}f(n_B) -\frac{\delta}{1-\delta}4R_\Delta$
    pf
    combining clm 1 and clm 2 we have that the backlog in B never
    exceeds $u_B = \mu(AB) + (1+\delta/(1-\delta)) f(n_B) + 3R_\Delta$.
    Hence, no cup in $A$ ever has fill greater than $u_A = u_B + \Delta + 1$.
    But then of course $\mu(A) \le u_A$.
    This gives the following lower bound on $\mu(B)$: 
    $$\mu(B) \ge -\frac{|A|}{|B|}\mu(A) + \frac{|AB|}{|B|}\mu(AB)$$
    $$\mu(B) \ge -\frac{|A|}{|B|}u_A + \frac{|AB|}{|B|}\mu(AB)$$
    $$\mu(B) \ge \frac{\delta}{(1-\delta)^2}f(n_B) -\frac{\delta}{1-\delta}4R_\Delta + \mu_0.$$
    
  **TODO: clm 4 isnt quite right**
    probably need to break into cases, 
      $p(n) \in \Theta(1)$ then get $n p(n)/2$ cups whp in $n$
      $p(n) = 1-1/\poly(M) - 2^{-\Omega(n)}$ then we're comfortable union bounding
  clm 4: with probability at least $1 - 1/M$ we get $n\cdot p(n)$
  cups with fill at least $(1-\delta/(1-\delta)^2)f(n_B) -
  \frac{\delta}{1-\delta}4R_\Delta + \mu_0$
    pf set $m \in \poly(M)$ big enough that this holds. In
    particular, note that the emptier can choose to neglect the
    anchor set conditional on the progress of $\alg{f}$, so need
    to make it big enough that there are plenty of applications
    that could work.

  clm 5: run time is clearly $n_A \poly(M) T(\alg{f})$
    pf this is clear

  now we consider what if there were extra-emptyings
  clm 6 we've maintained flatness the entire time.
    pf well we still have clm 1, and HMMM TODO XXX

    NOT NECESSARY: can flatten for M rounds… we're union bounding
    to gurantee that all of the rounds we use work. only problem:
    mu(B) vs mu(AB) can get messed up while we're letting extra-emptyings
    happen. Actually flatnes guarantee seems crucial. or at least backlog - avg

prop base case
alg_p(f) is randalg
combine stuff to a single cup

pf  
the combining argument already written as prop whatever

lem oblivious amplification lemma
yay recursion

pf 
just need the extra + f(n_A) thing

