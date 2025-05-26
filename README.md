# Proiect - Assignment 3 LFA

Acest proiect conține implementări pentru generarea și recunoașterea șirurilor dintr-un limbaj formal definit printr-o gramatică independentă de context (CFG).

## Descrierea Task-urilor

### Task 1: Definirea CFG-ului

- **Descriere:** Definește o reprezentare programatică a CFG-ului: S → aSb | ε.
- **Output-uri posibile:** Nu are output direct, dar definește structurile de date necesare pentru celelalte task-uri.

### Task 2: Generator de Șiruri

- **Descriere:** Implementează o funcție care generează aleatoriu șiruri din CFG-ul definit la Task 1.
- **Output-uri posibile:** O listă de șiruri generate aleatoriu, de exemplu: `['', 'ab', 'aabb', 'aaabbb']`.

### Task 3: Derivare

- **Descriere:** Implementează o funcție care, dat un șir țintă, afișează pașii de derivare a acelui șir din simbolul de start al CFG-ului.
- **Output-uri posibile:**
  ```
  Introdu un șir pentru a vedea derivarea: aabb
  Derivare:
  S
  aSb
  aaSbb
  aabb
  ```
  Sau, dacă șirul nu poate fi derivat:
  ```
  Introdu un șir pentru a vedea derivarea: abc
  Șirul nu poate fi derivat cu această gramatică.
  ```

### Task 4: Tester de Apartenență

- **Descriere:** Implementează o funcție care verifică dacă un șir dat aparține limbajului generat de CFG-ul definit.
- **Output-uri posibile:**
  ```
  Introdu un șir pentru a verifica apartenența: aabb
  Șirul aparține limbajului generat de S → aSb | ε.
  ```
  Sau:
  ```
  Introdu un șir pentru a verifica apartenența: abc
  Șirul NU aparține limbajului generat de S → aSb | ε.
  ```

### Task 5: Bonus - Extinderea CFG-ului

- **Descriere:** Extinde gramatica pentru a suporta limbajul L = { aⁿbⁿcⁿ | n ≥ 1 } și implementează un recognizer pentru acesta.
- **Output-uri posibile:**
  ```
  Introdu un șir pentru a verifica dacă este de forma a^n b^n c^n: aaabbbccc
  Șirul aparține limbajului L = { a^n b^n c^n | n ≥ 1 }.
  ```
  Sau:
  ```
  Introdu un șir pentru a verifica dacă este de forma a^n b^n c^n: aaaabbcc
  Șirul NU aparține limbajului L = { a^n b^n c^n | n ≥ 1 }.
  ```

## Atenție - Limbaj Non-Context-Free(Task 5)

 ATENȚIE: Acest limbaj NU este context-free!
 Orice implementare de CFG pentru acest limbaj este doar o simulare.
 Motiv: Pentru a recunoaște a^n b^n c^n trebuie să reții două numărători independente,
 ceea ce nu se poate cu o singură stivă (cum are un automat cu stivă, adică limbajele context-free).