# Tema 2: Generarea de șiruri folosind CFG
import random
import cfg_task1

# Clasa CFG
class CFG:
    def __init__(self, terminals, non_terminals, start_symbol, productions):
        self.terminals = terminals          
        self.non_terminals = non_terminals   
        self.start_symbol = start_symbol     
        self.productions = productions     

# Funcție pentru generarea aleatorie a șirurilor
def generate_strings(cfg, max_length=10, max_count=10):
    results = []  # Folosim listă, nu set

    def generate_random(symbol, current_string):
        if len(current_string) > max_length:
            return []
        if symbol in cfg.terminals:
            return [current_string + symbol]
        elif symbol in cfg.non_terminals:
            production = random.choice(cfg.productions[symbol])
            temp_strings = [current_string]
            for sym in production:
                new_strings = []
                for s in temp_strings:
                    expanded = generate_random(sym, s)
                    new_strings.extend(expanded)
                temp_strings = new_strings
            return temp_strings
        else:
            # epsilon
            return [current_string]

    attempts = 0
    while len(results) < max_count and attempts < max_count * 20:
        generated = generate_random(cfg.start_symbol, "")
        for g in generated:
            # Acceptă doar șirurile care au lungime corectă și nu au neterminale (doar a și b)
            if len(g) <= max_length and all(c in cfg.terminals for c in g):
                results.append(g) 
        attempts += 1

    return results

# Exemplu de utilizare
if __name__ == "__main__":
    # Construiește CFG-ul folosind cfg_task1.py
    cfg = CFG(
        terminals=cfg_task1.terminale,
        non_terminals=cfg_task1.non_terminale,
        start_symbol=cfg_task1.simbol_start,
        productions=cfg_task1.reguli_productie
    )

    # Generează și afișează până la 10 șiruri de lungime maximă 10
    strings = generate_strings(cfg, max_length=10, max_count=10)
    print("Exemple de șiruri generate pentru task-ul 1:")
    for s in strings:
        print(f"'{s}'")