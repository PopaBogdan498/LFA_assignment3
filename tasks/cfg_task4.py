# Task 4: Tester de apartenență pentru CFG-ul S → aSb | ε

def is_in_language(s):
    # Funcție recursivă care verifică dacă șirul s poate fi generat de gramatică
    def check(subs):
        if subs == "":
            return True  # epsilon
        if len(subs) < 2:
            return False
        if subs[0] == 'a' and subs[-1] == 'b':
            return check(subs[1:-1])
        return False
    return check(s)

# Exemplu de utilizare:
if __name__ == "__main__":
    sir = input("Introdu un șir pentru a verifica apartenența: ")
    if is_in_language(sir):
        print("Șirul aparține limbajului generat de S → aSb | ε.")
    else:
        print("Șirul NU aparține limbajului generat de S → aSb | ε.")