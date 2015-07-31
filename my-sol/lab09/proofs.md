---
layout: resource
title: Proofs
---
CS 61B  Lab 9
-------------
Recall the definition of big-Oh:

<pre>
  O(f(n)) is the SET of ALL functions T(n) that satisfy: 

    There exist positive constants c and N such that, for all n >= N,
                               T(n) <= c f(n)                        
</pre>

Part I:  (1 point)
------------------
Formally prove that 2^n + 1  is in  O(4^n - 16).

HINT:  You may assert without proof that, for all n >=1, 2^n >= 1.
(You may also assert without proof that 4^n and 2^n are monotonically
increasing, if you find it useful.)

**Solution**:

Let T(n) = 2^n + 1, f(n) = 4^n - 16.

Choose c = 1, and N = 3. Since 4^n and 2^n are monotonically increasing, and 

                        T(n) <= c f(n),
    or equivalently,    2^n + 1 <= 4^n - 16,                 for all n >= 3.

Thus, 2^n + 1  is in  O(4^n - 16).

Part II:  (1 point)
-------------------
Formally prove that if f(n) is in O(g(n)), and g(n) is in O(h(n)), then
f(n) is in O(h(n)).

NOTE:  The values of c and N used to prove that f(n) is in O(g(n)) are
not necessarily the same as the values used to prove that g(n) is in O(h(n)).
Hence, assume that there are positive c', N', c'', and N'' such that

    f(n) <= c' g(n)        for all n >= N', and
    g(n) <= c'' h(n)       for all n >= N''.

**Solution**:

Since if f(n) is in O(g(n)), and g(n) is in O(h(n)), then

    f(n) <= c' g(n)        for all n >= N', and
    g(n) <= c'' h(n)       for all n >= N''.

Therefore,

    f(n) <= c' g(n) <= c'c'' h(n)        for all n >= max(N', N'')

Choose c = c'c'', and N = max(N', N''). Then, 

                        f(n) <= c h(n),
    or equivalently,    f(n) <= c'c'' h(n),                 for all n >= max(N', N'').

Thus, f(n)  is in  O(h(n)).

Part III:  (2 points)
---------------------
Formally prove that 0.01 n^2 - 1  is NOT in  O(n).

We need to show that, no matter how large we choose c and N, we will never
obtain the desired inequality.  We cannot prove this by picking a specific
value of c and N.  Instead, we must study how the two functions behave as
n approaches infinity.

Let T(n) = 0.01 n^2 - 1, and let f(n) = n.  Prove that

                    c f(n)
            lim     ------ = 0,
        n->infinity  T(n)

no matter how large we choose c to be.  You will need to scale both the
numerator and the denominator by a well-chosen multiplier to get the result.

Use this result to show that there are no values c, N such that T(n) <= c f(n)
for all n >= N.

**Solution**:

                    c f(n)
            lim     ------ ,
        n->infinity  T(n)

equivalently,

                        c n                             c
            lim     -------------- =      lim     -------------- , 
        n->infinity  0.01 n^2 - 1     n->infinity  0.01 n - 1/n

We know as n goes to infinity, 1/n goes to zero and 0.01 n alse goes to inifity. 

Thus, 

                          c
            lim     -------------- = 0.
        n->infinity  0.01 n - 1/n

No matter how large we choose c to be, T(n) is greater than f(n) as n goes to inifinity. In another word, there are no values c, N such that T(n) <= c f(n) for all n >= N.

Postscript
----------
The functions |cos(n)| and |sin(n)| are interesting, because neither is
dominated by the other.  Can you informally suggest why |cos(n)| is not in
O(|sin(n)|), and |sin(n)| is not in O(|cos(n)|)?

**Solution**: 
We known that neither |cos(n)| or |sin(n)| is monotonically increasing or decreasing. 
Instead, they are periodic function and greater than or equal to zero. Whenever n is equals to kpi, 
where k is an nonnegative integer, |sin(n)| = 0 and |cos(n)| > 0. On the other hand, whenever n is equals 
kpi + pi/2, |cos(n)| = 0 and |sin(n)| > 0. Even we scale the functions, this property does not change. 
So |cos(n)| is not in O(|sin(n)|), and |sin(n)| is not in O(|cos(n)|).

How would you prove that, for all n >=1, 2^n >= 1?  (Hint:  use calculus.)

**Solution**: We know that f'(n) = n 2^(n-1) and whenever n > 0, f'(n) > 0. In another word, f(n) monotonically increases when n > 0. Moreover, f(1) = 2. So f(n) = 2^n >= 1 for all n >= 1. 