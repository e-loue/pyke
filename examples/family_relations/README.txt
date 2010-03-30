This example determines the relationships between people.

family.py
    This has the primary data used by the rest of the rules.  This data is
    established as universal facts so that it remains after an engine.reset()
    is done.

fc_example.krb
    Forward-chaining example.  This only uses forward-chaining rules, which
    means that all possible relationships are determined when the rule base is
    activated.

bc_example.krb
    Backward-chaining example.  This only uses backward-chaining rules, though
    these rules are not very efficient.

bc2_example.krb
    Backward-chaining example.  This also only uses backward-chaining rules,
    but a few rule optimizations have been made which results in this rule base
    running 100 times faster than bc_example.krb.

example.krb
    Combined rule base.  This has some forward-chaining rules, some
    (unoptimized) backward-chaining rules, and produces plans that return the
    relationship when run.  (This is a poor use of plans, but demonstrates the
    syntax and underlying principles).

driver.py
    Driver program.  Read this code to see how to call Pyke!
    
    Run:

        >>> import driver

        # All of the *test functions below default to 'bruce', but I won't use
        # that here because it generates a lot of output!

        # uses fc_example.krb
        >>> driver.fc_test('michael_k')           # doctest: +ELLIPSIS
        doing proof
        michael_k, amanda are ('father', 'daughter')
        michael_k, tammy are ('father', 'daughter')
        michael_k, crystal are ('father', 'daughter')
        <BLANKLINE>
        done
        family: 9 fact names, 94 universal facts, 6920 case_specific facts
        fc_example: 20 fc_rules, 6772 triggered, 892 rerun
        fc_example: 0 bc_rules, 0 goals, 0 rules matched
                    0 successes, 0 failures
        fc time ..., ... asserts/sec

        # uses bc_example.krb
        >>> driver.bc_test('gary')                # doctest: +ELLIPSIS
        doing proof
        gary, justin_m are ('father', 'son')
        <BLANKLINE>
        done
        bc_example: 0 fc_rules, 0 triggered, 0 rerun
        bc_example: 26 bc_rules, 5034 goals, 17901 rules matched
                    3563 successes, 17901 failures
        family: 9 fact names, 94 universal facts, 0 case_specific facts
        bc time ..., ... goals/sec

        # uses bc2_example.krb
        >>> driver.bc2_test('chad')               # doctest: +ELLIPSIS
        doing proof
        chad, tyler are ('father', 'son')
        chad, tiffany are ('father', 'daughter')
        <BLANKLINE>
        done
        bc2_example: 0 fc_rules, 0 triggered, 0 rerun
        bc2_example: 29 bc_rules, 35 goals, 140 rules matched
                     10 successes, 140 failures
        family: 9 fact names, 94 universal facts, 0 case_specific facts
        bc time ..., ... goals/sec

        # uses example.krb
        >>> driver.test('paul')                   # doctest: +ELLIPSIS
        doing proof
        paul, nick are father, son
        paul, katrina are father, daughter
        <BLANKLINE>
        done
        example: 6 fc_rules, 262 triggered, 0 rerun
        example: 21 bc_rules, 2828 goals, 6221 rules matched
                 1414 successes, 6221 failures
        family: 9 fact names, 94 universal facts, 422 case_specific facts
        fc time ..., ... asserts/sec
        bc time ..., ... goals/sec
        total time ...


        # this has three parameters that all default to None:
        #     person1, person2 and relationship
        >>> driver.general(person1='bruce',             # uses bc2_example.krb
        ...             relationship=('father', 'son')) # doctest: +ELLIPSIS
        doing proof
        bruce, m_thomas are ('father', 'son')
        bruce, david_a are ('father', 'son')
        <BLANKLINE>
        done
        bc2_example: 0 fc_rules, 0 triggered, 0 rerun
        bc2_example: 29 bc_rules, 105 goals, 390 rules matched
                     82 successes, 390 failures
        family: 9 fact names, 94 universal facts, 0 case_specific facts
        bc time ... goals/sec

    The last function uses the bc2_example rule base.  You can pass whatever
    combinations of values you like.  If you want to specify person1 and/or
    person2, pass their name; otherwise any person will match.  For the
    relationship, pass a tuple.  Use '$var_name' strings in the tuple for
    pattern variables.  You can also have nested tuples (as some of the
    relationships are nested tuples).
