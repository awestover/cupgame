# Friday the 13th of March (AKA apocolypse day 1)
Bill:		Filler puts in p units of water
Bill:		Let's examine the $k$ fullest cups
Bill:		Emptier removes water from $p$ cups: $a$ of those cups remain among the $k$ fullest, and $b$ don't
Bill:		Suppose the $b$ cups that are removed were above average for the $k + b$ fullest cups
Bill:		Then the new $k$ fullest cups have avg fill
Bill:		at most as large as the avg fill of the previously $k + b$ fullest cups
Bill:		plus $b / k$ from the new units of water
Alek:		avgfill_k <= avgfill_{k+b} ish
Bill:		+ b / k
Bill:		This all works if the b cups were above average
Bill:		out of the k fullest cups (or maybe it's out of the k + b fullest cups)
Bill:		But if they're not, then it seems like maybe there's a different argument to make?
Bill:		Set b = 10
Bill:		k = 100
Bill:		If the b cups have below-avg fill for the b + k fullest cups
Bill:		then they have fill <= (n - b - k) + b / (n - b - k)
Bill:		scratch that
Bill:		I mean they have fill <= (n - b - k) + b / (k + b)
Bill:		<= (n - 110) + 10 / 110
Bill:		The a cups , on the other hand, have avg fill at most 
Bill:		(set a = 10 also)
Bill:		$n - 10$
Bill:		Now, the k fullest cups have avg fill at most
Bill:		(n - 10) * 10 / 100 + (n - 109.9) * 90 /100
Alek:		n- 99.91
Alek:		dang
Alek:		was supposed to be n-100
Bill:		When is a is small relative to b
Bill:		we actually win
Bill:		Also
Bill:		if k is really big compared to p = a+ b, then I think we also win
Bill:		Where is there room for improvement?
Bill:		If the a cups were super full, then the average fill in the remaining cups
Bill:		was actually smaller than the bound that we stated for them
Bill:		which means the b cups were actually emptier than we've analyzed them as
Bill:		and so on...


