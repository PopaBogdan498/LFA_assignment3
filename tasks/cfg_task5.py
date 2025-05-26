# Task 5: Bonus - CFG și recunoaștere pentru L = { a^n b^n c^n | n ≥ 1 }

# Recunoaștere simplă:
def is_in_abc_language(s):
    n = len(s)
    if n < 3:
        return False
    i = 0
    while i < n and s[i] == 'a':
        i += 1
    j = i
    while j < n and s[j] == 'b':
        j += 1
    k = j
    while k < n and s[k] == 'c':
        k += 1
    # Toate caracterele trebuie să fie consumate și numărul de a, b, c să fie egal și >= 1
    if i > 0 and (i == (j - i)) and (i == (k - j)) and k == n:
        return True
    return False

# Exemplu de utilizare:
if __name__ == "__main__":
    sir = input("Introdu un șir pentru a verifica dacă este de forma a^n b^n c^n: ")
    if is_in_abc_language(sir):
        print("Șirul aparține limbajului L = { a^n b^n c^n | n ≥ 1 }.")
    else:
        print("Șirul NU aparține limbajului L = { a^n b^n c^n | n ≥ 1 }.")

# Explicație:
# Limbajul L = { a^n b^n c^n | n ≥ 1 } nu este context-free deoarece necesită
# "sincronizarea" a trei secvențe de simboluri, ceea ce nu se poate face cu o singură stivă.
# Un CFG nu poate genera acest limbaj pentru orice n, dar recunoașterea pentru n mic se poate simula.