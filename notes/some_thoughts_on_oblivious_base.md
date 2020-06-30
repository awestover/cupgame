% ideas: flattening can be made to certainly work
% just continue on for long enough, which works because mu(A) can't sink too
% low (interconnected induction thing)
% $L_t$ and $U_t$ still can't lose stuff; this doesn't depend on if the emptier is changing its $p$
% consider the swapping incurred change in m(A) - m(B)
% cup in A: fill at most mu(B) + 3R_\Delta + d
% cup in B: fill at least mu(B) - R_\Delta - |D|
% fill of cup in A - fill of cup in B is less than 4R_\Delta + d + |D| \le O(1)
% lets call this f
% so m(A) has at most |A| f swap induced decrease
% m(B) has at most |A| f swap induced increase
% this lets us inductively say a) yup we can actually guarantee that all the swapping-processes work (we needed to know how long we have to keep going; lower bounding mu(A) does this), and b) can't be too many neglects per swapping process (also by lower bounding mu(A) and upper bounding mu(B))
% now for the other claim, that mu(B) never sinks below -h/2.
% consider how high a cup in A could be
% we're going to have to do some induction here
% because this is intertwined with how low mu(B) can sink
% within a swapping-process mu(B) only sinks. No cup in A can rise above mu(B) initial + 3R_\Delta + d
% what about swaps? Give the same thing.
% ok, so now there is a recursivey thing
% case: if A neglectable by the end of the swapping-processes then mu(B) is fine
% case: if A is not neglectable at the end of the swapping-processes, then  
% consider the most recent time that A became not neglectable.
% at that point it was fine, 
% after that mu(B) doesn't sink due to neglect of A but rather sinks due only to swaps
% but, a swap isn't too bad, it decreases m(B) by at most like 2h or something, 
% and B can take that kinda loss all day (its way bigger than A)

