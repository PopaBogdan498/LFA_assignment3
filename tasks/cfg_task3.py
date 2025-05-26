# Task 3: Derivarea unui șir dat pentru CFG-ul S → aSb | ε

def derive_steps(target, current='S', steps=None):
    if steps is None:
        steps = [current]
    # Dacă am ajuns la șirul țintă, returnează pașii
    if current == target:
        return steps
    # Dacă nu mai există S în șir, dar nu am ajuns la țintă
    if 'S' not in current:
        return None
    # Dacă prefixul până la primul S nu se potrivește cu ținta
    idx = current.find('S')
    prefix = current[:idx]
    suffix = current[idx+1:]
    if not target.startswith(prefix) or not target.endswith(suffix):
        return None
    # Înlocuiește primul S cu epsilon
    new_str = prefix + '' + suffix
    result = derive_steps(target, new_str, steps + [new_str])
    if result is not None:
        return result
    # Înlocuiește primul S cu aSb
    new_str = prefix + 'aSb' + suffix
    result = derive_steps(target, new_str, steps + [new_str])
    if result is not None:
        return result
    # Dacă niciuna nu merge
    return None

# Exemplu de utilizare:
if __name__ == "__main__":
    sir = input("Introdu un șir pentru a vedea derivarea: ")
    derivare = derive_steps(sir)
    if derivare:
        print("Derivare:")
        for pas in derivare:
            print(pas)
    else:
        print("Șirul nu poate fi derivat cu această gramatică.")