# family.py

def init(engine):
    def son_of(son, father, mother):
        engine.add_universal_fact('family', 'son_of', (son, father, mother))
    son_of('art', 'art2', 'nana')
    son_of('artie', 'art', 'kathleen')
    son_of('ed', 'art', 'kathleen')
    son_of('david', 'art', 'kathleen')
    son_of('justin', 'artie', 'julie')
    son_of('arthur', 'artie', 'lisa')
    son_of('keith', 'ed', 'ann')
    son_of('ramon', 'ed', 'ann')
    son_of('cody', 'david', 'colleen')
