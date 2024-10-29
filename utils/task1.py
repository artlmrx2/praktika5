from main import HEADER, ENDC
from utils.prime_factor import prime_factors

async def task1():
    try:
        num = int(input(f"{HEADER}    Ievadiet skaitli: {ENDC}"))
        if num <= 1:
            print(f"{HEADER}    Skaitlim jābūt lielākam par 1{ENDC}")
            return
            
        factors = await prime_factors(num)
        print(f"{HEADER}    Pirmreizinātāji: {ENDC}", "*".join(map(str, factors)))
    except ValueError:
        print(f"{HEADER}    Kļūda: Lūdzu ievadiet derīgu skaitli{ENDC}")