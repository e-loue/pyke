# family_relations.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> new_path = os.path.join(os.path.dirname(os.path.dirname(pyke.__file__)),
    ...                         'examples/family_relations')
    >>> sys.path.append(new_path)

    >>> import driver

    >>> driver.fc_test()      # doctest: +ELLIPSIS
    doing proof
    bruce, thomas are ('son', 'father')
    bruce, norma are ('son', 'mother')
    bruce, frederik are (('grand', 'son'), ('grand', 'father'))
    bruce, mary are (('grand', 'son'), ('grand', 'mother'))
    bruce, allen are (('grand', 'son'), ('grand', 'father'))
    bruce, ismay are (('grand', 'son'), ('grand', 'mother'))
    bruce, m_thomas are ('father', 'son')
    bruce, david_a are ('father', 'son')
    bruce, fred_a are ('brother', 'brother')
    bruce, tim are ('brother', 'brother')
    bruce, vicki are ('brother', 'sister')
    bruce, jill are ('brother', 'sister')
    bruce, joyce are ('nephew', 'aunt')
    bruce, phyllis are ('nephew', 'aunt')
    bruce, john_w are ('nephew', 'uncle')
    bruce, bill are ('nephew', 'uncle')
    bruce, chuck_w are ('nephew', 'uncle')
    bruce, david_c are ('1st', 'cousins')
    bruce, danny are ('1st', 'cousins')
    bruce, dee are ('1st', 'cousins')
    bruce, mitch are ('1st', 'cousins')
    bruce, jonni are ('1st', 'cousins')
    bruce, lorri are ('1st', 'cousins')
    bruce, steve_w are ('1st', 'cousins')
    bruce, jim are ('1st', 'cousins')
    bruce, jeri are ('1st', 'cousins')
    bruce, annette are ('1st', 'cousins')
    bruce, helen_w are ('1st', 'cousins')
    bruce, mary_w are ('1st', 'cousins')
    bruce, charli are ('1st', 'cousins', 1, 'removed')
    bruce, jimjim are ('1st', 'cousins', 1, 'removed')
    bruce, johnjohn are ('1st', 'cousins', 1, 'removed')
    bruce, jamie are ('1st', 'cousins', 1, 'removed')
    bruce, david_w are ('1st', 'cousins', 1, 'removed')
    bruce, jessica are ('1st', 'cousins', 1, 'removed')
    bruce, bridget are ('1st', 'cousins', 1, 'removed')
    bruce, brian2 are ('1st', 'cousins', 1, 'removed')
    bruce, victoria are ('1st', 'cousins', 1, 'removed')
    <BLANKLINE>
    done
    family: 9 fact names, 94 universal facts, 6920 case_specific facts
    fc_example: 20 fc_rules, 6772 triggered, 892 rerun
    fc_example: 0 bc_rules, 0 goals, 0 rules matched
                0 successes, 0 failures
    fc time ..., ... asserts/sec

    >>> driver.bc_test()      # doctest: +ELLIPSIS
    doing proof
    bruce, thomas are ('son', 'father')
    bruce, norma are ('son', 'mother')
    bruce, frederik are (('grand', 'son'), ('grand', 'father'))
    bruce, mary are (('grand', 'son'), ('grand', 'mother'))
    bruce, allen are (('grand', 'son'), ('grand', 'father'))
    bruce, ismay are (('grand', 'son'), ('grand', 'mother'))
    bruce, m_thomas are ('father', 'son')
    bruce, david_a are ('father', 'son')
    bruce, fred_a are ('brother', 'brother')
    bruce, tim are ('brother', 'brother')
    bruce, vicki are ('brother', 'sister')
    bruce, jill are ('brother', 'sister')
    bruce, joyce are ('nephew', 'aunt')
    bruce, phyllis are ('nephew', 'aunt')
    bruce, john_w are ('nephew', 'uncle')
    bruce, bill are ('nephew', 'uncle')
    bruce, chuck_w are ('nephew', 'uncle')
    bruce, david_c are ('1st', 'cousins')
    bruce, danny are ('1st', 'cousins')
    bruce, dee are ('1st', 'cousins')
    bruce, mitch are ('1st', 'cousins')
    bruce, jonni are ('1st', 'cousins')
    bruce, lorri are ('1st', 'cousins')
    bruce, steve_w are ('1st', 'cousins')
    bruce, jim are ('1st', 'cousins')
    bruce, jeri are ('1st', 'cousins')
    bruce, annette are ('1st', 'cousins')
    bruce, helen_w are ('1st', 'cousins')
    bruce, mary_w are ('1st', 'cousins')
    bruce, charli are ('1st', 'cousins', 1, 'removed')
    bruce, jimjim are ('1st', 'cousins', 1, 'removed')
    bruce, johnjohn are ('1st', 'cousins', 1, 'removed')
    bruce, jamie are ('1st', 'cousins', 1, 'removed')
    bruce, david_w are ('1st', 'cousins', 1, 'removed')
    bruce, jessica are ('1st', 'cousins', 1, 'removed')
    bruce, bridget are ('1st', 'cousins', 1, 'removed')
    bruce, brian2 are ('1st', 'cousins', 1, 'removed')
    bruce, victoria are ('1st', 'cousins', 1, 'removed')
    <BLANKLINE>
    done
    bc_example: 0 fc_rules, 0 triggered, 0 rerun
    bc_example: 26 bc_rules, 31950 goals, 112099 rules matched
                17150 successes, 112099 failures
    family: 9 fact names, 94 universal facts, 0 case_specific facts
    bc time ..., ... goals/sec

    >>> driver.bc2_test()      # doctest: +ELLIPSIS
    doing proof
    bruce, thomas are ('son', 'father')
    bruce, norma are ('son', 'mother')
    bruce, frederik are (('grand', 'son'), ('grand', 'father'))
    bruce, mary are (('grand', 'son'), ('grand', 'mother'))
    bruce, allen are (('grand', 'son'), ('grand', 'father'))
    bruce, ismay are (('grand', 'son'), ('grand', 'mother'))
    bruce, m_thomas are ('father', 'son')
    bruce, david_a are ('father', 'son')
    bruce, fred_a are ('brother', 'brother')
    bruce, tim are ('brother', 'brother')
    bruce, vicki are ('brother', 'sister')
    bruce, jill are ('brother', 'sister')
    bruce, joyce are ('nephew', 'aunt')
    bruce, phyllis are ('nephew', 'aunt')
    bruce, john_w are ('nephew', 'uncle')
    bruce, bill are ('nephew', 'uncle')
    bruce, chuck_w are ('nephew', 'uncle')
    bruce, david_c are ('1st', 'cousins')
    bruce, danny are ('1st', 'cousins')
    bruce, dee are ('1st', 'cousins')
    bruce, mitch are ('1st', 'cousins')
    bruce, jonni are ('1st', 'cousins')
    bruce, lorri are ('1st', 'cousins')
    bruce, steve_w are ('1st', 'cousins')
    bruce, jim are ('1st', 'cousins')
    bruce, jeri are ('1st', 'cousins')
    bruce, annette are ('1st', 'cousins')
    bruce, helen_w are ('1st', 'cousins')
    bruce, mary_w are ('1st', 'cousins')
    bruce, charli are ('1st', 'cousins', 1, 'removed')
    bruce, jimjim are ('1st', 'cousins', 1, 'removed')
    bruce, johnjohn are ('1st', 'cousins', 1, 'removed')
    bruce, jamie are ('1st', 'cousins', 1, 'removed')
    bruce, david_w are ('1st', 'cousins', 1, 'removed')
    bruce, jessica are ('1st', 'cousins', 1, 'removed')
    bruce, bridget are ('1st', 'cousins', 1, 'removed')
    bruce, brian2 are ('1st', 'cousins', 1, 'removed')
    bruce, victoria are ('1st', 'cousins', 1, 'removed')
    <BLANKLINE>
    done
    bc2_example: 0 fc_rules, 0 triggered, 0 rerun
    bc2_example: 29 bc_rules, 315 goals, 1202 rules matched
                 272 successes, 1202 failures
    family: 9 fact names, 94 universal facts, 0 case_specific facts
    bc time ..., ... goals/sec

    >>> driver.test()      # doctest: +ELLIPSIS
    doing proof
    bruce, thomas are son, father
    bruce, norma are son, mother
    bruce, frederik are grand son, grand father
    bruce, mary are grand son, grand mother
    bruce, allen are grand son, grand father
    bruce, ismay are grand son, grand mother
    bruce, m_thomas are father, son
    bruce, david_a are father, son
    bruce, fred_a are brother, brother
    bruce, tim are brother, brother
    bruce, vicki are brother, sister
    bruce, jill are brother, sister
    bruce, joyce are nephew, aunt
    bruce, phyllis are nephew, aunt
    bruce, john_w are nephew, uncle
    bruce, bill are nephew, uncle
    bruce, chuck_w are nephew, uncle
    bruce, david_c are 1st cousins
    bruce, danny are 1st cousins
    bruce, dee are 1st cousins
    bruce, mitch are 1st cousins
    bruce, jonni are 1st cousins
    bruce, lorri are 1st cousins
    bruce, steve_w are 1st cousins
    bruce, jim are 1st cousins
    bruce, jeri are 1st cousins
    bruce, annette are 1st cousins
    bruce, helen_w are 1st cousins
    bruce, mary_w are 1st cousins
    bruce, charli are 1st cousins, 1 removed
    bruce, jimjim are 1st cousins, 1 removed
    bruce, johnjohn are 1st cousins, 1 removed
    bruce, jamie are 1st cousins, 1 removed
    bruce, david_w are 1st cousins, 1 removed
    bruce, jessica are 1st cousins, 1 removed
    bruce, bridget are 1st cousins, 1 removed
    bruce, brian2 are 1st cousins, 1 removed
    bruce, victoria are 1st cousins, 1 removed
    <BLANKLINE>
    done
    example: 6 fc_rules, 262 triggered, 0 rerun
    example: 21 bc_rules, 9600 goals, 19772 rules matched
             1542 successes, 19772 failures
    family: 9 fact names, 94 universal facts, 422 case_specific facts
    fc time ..., ... asserts/sec
    bc time ..., ... goals/sec
    total time ...

    >>> driver.general('bruce')      # doctest: +ELLIPSIS
    doing proof
    bruce, thomas are ('son', 'father')
    bruce, norma are ('son', 'mother')
    bruce, frederik are (('grand', 'son'), ('grand', 'father'))
    bruce, mary are (('grand', 'son'), ('grand', 'mother'))
    bruce, allen are (('grand', 'son'), ('grand', 'father'))
    bruce, ismay are (('grand', 'son'), ('grand', 'mother'))
    bruce, m_thomas are ('father', 'son')
    bruce, david_a are ('father', 'son')
    bruce, fred_a are ('brother', 'brother')
    bruce, tim are ('brother', 'brother')
    bruce, vicki are ('brother', 'sister')
    bruce, jill are ('brother', 'sister')
    bruce, joyce are ('nephew', 'aunt')
    bruce, phyllis are ('nephew', 'aunt')
    bruce, john_w are ('nephew', 'uncle')
    bruce, bill are ('nephew', 'uncle')
    bruce, chuck_w are ('nephew', 'uncle')
    bruce, david_c are ('1st', 'cousins')
    bruce, danny are ('1st', 'cousins')
    bruce, dee are ('1st', 'cousins')
    bruce, mitch are ('1st', 'cousins')
    bruce, jonni are ('1st', 'cousins')
    bruce, lorri are ('1st', 'cousins')
    bruce, steve_w are ('1st', 'cousins')
    bruce, jim are ('1st', 'cousins')
    bruce, jeri are ('1st', 'cousins')
    bruce, annette are ('1st', 'cousins')
    bruce, helen_w are ('1st', 'cousins')
    bruce, mary_w are ('1st', 'cousins')
    bruce, charli are ('1st', 'cousins', 1, 'removed')
    bruce, jimjim are ('1st', 'cousins', 1, 'removed')
    bruce, johnjohn are ('1st', 'cousins', 1, 'removed')
    bruce, jamie are ('1st', 'cousins', 1, 'removed')
    bruce, david_w are ('1st', 'cousins', 1, 'removed')
    bruce, jessica are ('1st', 'cousins', 1, 'removed')
    bruce, bridget are ('1st', 'cousins', 1, 'removed')
    bruce, brian2 are ('1st', 'cousins', 1, 'removed')
    bruce, victoria are ('1st', 'cousins', 1, 'removed')
    <BLANKLINE>
    done
    bc2_example: 0 fc_rules, 0 triggered, 0 rerun
    bc2_example: 29 bc_rules, 315 goals, 1202 rules matched
                 272 successes, 1202 failures
    family: 9 fact names, 94 universal facts, 0 case_specific facts
    bc time ..., ... goals/sec

