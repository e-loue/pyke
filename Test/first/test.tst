# test.tst

    >>> from Test import test
    >>> import Test.first
    >>> from Test.first import family
    >>> test.init(family.__file__)
    >>> family.init(test.Engine)

    son_of('art', 'art2', 'nana')
    son_of('artie', 'art', 'kathleen')
    son_of('ed', 'art', 'kathleen')
    son_of('david', 'art', 'kathleen')
    son_of('justin', 'artie', 'julie')
    son_of('arthur', 'artie', 'lisa')
    son_of('keith', 'ed', 'ann')
    son_of('ramon', 'ed', 'ann')
    son_of('cody', 'david', 'colleen')

    >>> test.Engine.get_kb('family').dump_specific_facts()

    >>> test.fc_test('test')

    >>> test.Engine.get_kb('family').dump_specific_facts()
    brothers('artie', 'ed')
    brothers('ed', 'artie')
    brothers('david', 'artie')
    brothers('keith', 'ramon')
    brothers('ramon', 'keith')
    cousins('justin', 'keith')
    cousins('keith', 'justin')
    cousins('cody', 'justin')
    nephew_of('keith', 'artie', 'julie')

