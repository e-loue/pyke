This is a small example of the 'forall' clause used to gather a list of
answers in both forward-chaining and backward-chaining rules.

The forward-chaining and backward-chaining rules are in two different .krb
files showing examples of use of the 'forall' clause in both cases.

Rather than finding individual siblings and cousins, these rules find all
siblings and all cousins and assert them in a single fact (as a tuple).

    >>> import driver

    # uses fc_findall.krb
    >>> driver.fc_test()
    egon has ('harald', 'claudia') as cousins
    ralf has ('harald', 'claudia') as cousins
    hilde has () as cousins
    diethelm has () as cousins
    harald has ('egon', 'ralf') as cousins
    claudia has ('egon', 'ralf') as cousins

    # uses bc_findall.krb
    >>> driver.bc_test()
    egon has ('harald', 'claudia') as cousins
    ralf has ('harald', 'claudia') as cousins
    hilde has () as cousins
    diethelm has () as cousins
    harald has ('egon', 'ralf') as cousins
    claudia has ('egon', 'ralf') as cousins

