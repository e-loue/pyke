This is a small example of the 'forall'/'require' clause used to verify that
all of the elements a list meet some requirement.  This example is done in
both forward-chaining and backward-chaining rules.

The forward-chaining and backward-chaining rules are in two different .krb
files showing examples of use of the 'forall'/'require' clause in both cases.

These rules find all people who have no step brothers or sisters.

    >>> import run

    # uses fc_forall.krb
    >>> run.fc_test()
    arthur2 has no step brothers or sisters
    helen has no step brothers or sisters
    roberta has no step brothers or sisters

    # uses bc_forall.krb
    >>> run.bc_test()
    arthur2
    helen
    roberta

