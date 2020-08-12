ok so what if we don't flatten A?
but we still know that everything in A is a whole lot better
than whatever is in B

except not

also we cant flatten A
at least not at the bottom (i.e. f_0)


you know what? mu(A) might be a freaking piece of crap.
I'm talking about randalg
randalg can dump absolute trash into A

pseudocode rep_\delta $\alg_p{f}$
  $B \gets$ all cups; $A \gets \varnothing$
  for $i \gets 1,2,\ldots, n_A$ \Comment \enquote{donation processes}
    flatten $A$ using $|A|/2$ processors (can do something super
        dumb if $|A|$ is odd (anchor a single cup, and then
          anchor a different single cup)
    $m_0$ \gets uniformly randomly chosen from $[m]$ ($m \in \poly(M)$ to be specified)
    for $j \gets 1,2,\ldots, m_0$
      flatten $B$ with the flattening procedure
      apply $\alg_p{f}$ to $B$
    donate the last cup given by $\alg_p{f}$ from $B$ to $A$

Now we establish some important properties maintained by rep.

First we condition on no extra-emptyings, and prove several
invariants.

prop 0:
all flattenings work by just doing them for a ridiculously long time
  pf
  first note that if the fill-range starts out $\ge M$ we just win.
  this is clear fo the flattening of $B$

prop 1: $B$ is always $(R_\Delta + f(n_B))$-flat
  pf since $B$ starts flat before applying $\alg_p{f}$ it stays pretty flat during the
  application by assumption. $B$ also stays pretty flat during flattening
  process. donation doesn't mess with flatness. $B$ started $R_\Delta$-flat. 
  induction.

prop 2: $\mu(B) \le \mu(AB) + \frac{\delta}{1-\delta} f(n_B) + 2R_\Delta.$
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

prop 3: $\mu(B) \ge \mu(AB) - \frac{\delta}{(1-\delta)^2}f(n_B) -\frac{\delta}{1-\delta}4R_\Delta$
  pf
  combining clm 1 and clm 2 we have that the backlog in B never
  exceeds $u_B = \mu(AB) + (1+\delta/(1-\delta)) f(n_B) + 3R_\Delta$.
  Hence, no cup in $A$ ever has fill greater than $u_A = u_B + \Delta + 1$.
  But then of course $\mu(A) \le u_A$.
  This gives the following lower bound on $\mu(B)$: 
  $$\mu(B) \ge -\frac{|A|}{|B|}\mu(A) + \frac{|AB|}{|B|}\mu(AB)$$
  $$\mu(B) \ge -\frac{|A|}{|B|}u_A + \frac{|AB|}{|B|}\mu(AB)$$
  $$\mu(B) \ge \frac{\delta}{(1-\delta)^2}f(n_B) -\frac{\delta}{1-\delta}4R_\Delta + \mu_0.$$

prop 4: if $p(n) \in \Theta(1)$ then get $n p(n)/2$ cups whp in $n$
fill at least $(1-\delta/(1-\delta)^2)f(n_B) - \frac{\delta}{1-\delta}4R_\Delta + \mu_0$
  pf set $m \in \poly(M)$ big enough that this holds. In
  particular, note that the emptier can choose to neglect the
  anchor set conditional on the progress of $\alg{f}$, so need
  to make it big enough that there are plenty of applications
  that could work.

prop 5: if $p(n) = 1-1/\poly(M) - 2^{-\Omega(n)}$ then we're comfortable union bounding
fill at least $(1-\delta/(1-\delta)^2)f(n_B) - \frac{\delta}{1-\delta}4R_\Delta + \mu_0$
pf union bound

prop 6: run time is clearly $n_A \poly(M) T(\alg{f})$
  pf this is clear

Now we consider what if there were extra-emptyings.
prop 7 we've maintained flatness the entire time.
pf we're pretty flat whenever extra emptyings happen
in particular, I'm willing to assume something like
extra-emptyings only happen to pretty darn big cups.

lem REP
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
    output: gets $n\cdot p(n)$ cups with fill at least $\mu_0 + (1-\delta)f(n_B)$ if no extra emptyings
    unconditional guarantees: cups always are $(R_\Delta + k_\Delta f(n))$-flat
    restriction: on a round where extra-empties happen, they happen to cups in $B$ with really high fill
pf 
combine prop 1234567

prop base case
there exists an alg that gets backlog 1

pf  
alg_p(f) is randalg
combine stuff to a single cup

lem oblivious amplification lemma
you can camplify a function

pf 
rep(alg_p(f)) on B
then use alg_p(f) on A

thm
can get backlog n^{1-\epsilon}

pf
basic algebra


so far:

ok so if no extra empties 
alg f_0 works

imagine that there's an extra empty somehwere

ok we're analyzing stuff within the recursive tree kind of.
I just don't see this working out too well.

we're gonna go for it anyways tho

ok say we've established that f_i works if no extra empties
happen to it, 

       imagine that an extra empty happens
       its not a big deal 
       in particular it doesn't mess with the flattness


       when an extra empty happens 



       CLAIM extra-empties don't increase fill-range
CLAIM is false, 
      because A is very not flat at the bottom




alg f0 basically has to work basically the way its going right
now
  - in particular, flattening A makes no sense in this setting


having A be flat seems kind of nice for other levels of
recursion

 but maybe there is a less strict thing that we can say

 like 




1) Base case works if no extra emptying, elsewise no guarantees on it.
2) Assume that f_i works if theres no extra emptying. consider an
instance of f_{i+1} that happens with no extra emptying. we're
repeatedly flattening B and then applying f_i to B. 
By a union bound we can say that the final times never
have neglects. so every time we donate we're donating a cup with
fill like mu(B_0) + f(|B_0|). so mu(B) is monotonitcally
decreasing. **except for skips**. if muB
never gets below mu_0 - delta f(n_B) then everytime we swap its
lit
elsewise, muB is low enough in the end that we know we're rolling
with A

hum, so its not quite mu(B) that's monotonically decreasing, 
it's more like mu(B) - mu(AB) maybe?

I think that by analysis of this we can maybe be ok?

