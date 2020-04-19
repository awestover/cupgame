# Some Cup Games

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

