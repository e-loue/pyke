This is the knapsack example taken from:

    http://www.ise.gmu.edu/~duminda/classes/fall03/set3.ppt starting on page 19

knapsack.krb
    This uses backward-chaining to solve the knapsack problem (see link above).
    The top-level goal is:

        legal_knapsack($Pantry, $Capacity, $Knapsack)

    $Pantry is a tuple of food items.  Each food item is: (name, weight,
    calories).

    $Capacity is the maximum weight capacity of the knapsack.

    $Knapsack is a subset of $Pantry whose total weight is <= $Capacity.

driver.py
    run(pantry, capacity)
        Uses the legal_knapsack goal to enumerate all of the possible
        knapsacks within the stated capacity.  Returns the total_calories and
        knapsack of the answer with most calories.

        The final example on page 36 at the site above would be:

        >>> import driver
        >>> driver.run((('bread',4,9200),
        ...          ('pasta',2,4500),
        ...          ('peanutButter',1,6700),
        ...          ('babyFood',3,6900)),
        ...         4)
        (13600, (('peanutButter', 1, 6700), ('babyFood', 3, 6900)))

