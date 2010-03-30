This is a small example of the 'notany' clause used to verify that none of
the elements of a list meet a certain requirement.  This is done in both
forward-chaining and backward-chaining rules.

The forward-chaining and backward-chaining rules are in two different .krb
files showing examples of use of the 'notany' clause in both cases.

These rules find all people who have no aunts all people with no uncles.

    >>> import driver

    # uses fc_notany.krb
    >>> driver.fc_test()
    egon has no uncle
    ralf has no uncle
    anton has no uncle
    elisabeth has no uncle
    karin has no uncle
    sabine has no uncle
    anton has no aunt
    elisabeth has no aunt
    karin has no aunt
    sabine has no aunt

    # uses bc_notany.krb
    >>> driver.bc_test()
    anton has no aunt
    elisabeth has no aunt
    karin has no aunt
    sabine has no aunt
    egon has no uncle
    ralf has no uncle
    anton has no uncle
    elisabeth has no uncle
    karin has no uncle
    sabine has no uncle

