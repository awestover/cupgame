# The Cup Games

The cup game is a classic problem in computer science that models work
scheduling.  In the cup game on n cups, a filler and an emptier take turns
adding and removing water from cups (i.e. new tasks come in and the scheduler
must allocate processors to handle the incoming work). On each round the filler
will distribute some new amount of water among the cups, and the emptier will
remove some amount of water from some of the cups. The filler can distribute
the water however it wants (as long as it places at most a single unit of water
in each cup), but the emptier has an added "discretization constraint": it can
only remove water from some fixed number of cups (it removes a unit of water
from each cup). The problem is to analyze how well each player can do, that is,
how much water can the filler force to be in the fullest cup, and what is the
upper bound on this fill that an appropriate emptying strategy can guarantee?
We study several variants of the problem and answer some open questions.

# results

- Variable-Processor cup game

We ask the natural question: "what if the number of processors is
allowed to change?"
Allowing the filler to change the resources drastically alters
the game.

* An adaptive filler can achieve backlog linear in the number of
cups! Classically there is a logarithmic upper bound! Wow!
* A greedy emptier never lets backlog exceed linear
* An oblivious filler can still get polynomial backlog, in fact
polynomials with any constant exponent below one! We are only
able to prove this for "greedy-like" emptiers, but this class of
emptiers is of great interest because all known upper bound
constructions for cup games fall into this category!

- Multi-Processor Cup Game: Adaptive lower bound

We provide a simple construction that an adaptive filler can use
to get large backlog. Combined with previous work by Kuszmaul
this implies that backlog logarithmic in the number of cups is
tight for the adaptive case of the multi-processor cup game,
regardless of the number of processors, which is somewhat surprising!

