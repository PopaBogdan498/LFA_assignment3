# Tema 1: Definirea unui CFG

# Simboluri neterminale și terminale
non_terminale = {'S'}
terminale = {'a', 'b'}
# Simbolul de start
simbol_start = 'S'

# Regulile de producție: fiecare neterminal este asociat cu o listă de posibile părți drepte
reguli_productie = {
    'S': [
        [], # epsilon
        ['a','S','b'] # a S b
    ]
}
