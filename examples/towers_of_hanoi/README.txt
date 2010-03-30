This solves the Towers of Hanoi puzzle through brute force but with the
restrictions of never repeating a board position and never moving the
same disc twice in a row.  Running this, you'll see the following pattern:

    1 disc has 1 solution
    2 discs has 2 solutions
    3 discs has 12 solutions
    4 discs has 1872 solutions

Sure enough, if the number of solutions for n discs is N, the number of
solutions for n+1 discs is: N**3 + N**2.  (I leave the explanation of why this
is so to the reader! :-)

This would mean that 5 discs has 6,563,711,232 solutions, but I haven't run
this to verify the answer...

    >>> import driver
    >>> driver.test(2)    # test takes the number of disks as an argument
    got 1: ((0, 1), (0, 2), (1, 2))
    got 2: ((0, 2), (0, 1), (2, 0), (1, 2), (0, 2))

