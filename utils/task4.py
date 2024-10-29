from main import HEADER, ENDC

async def dollars_to_float(d: str) -> float:
    return float(d.replace("$", ""))

async def percent_to_float(p: str) -> float:
    return float(p.replace("%", "")) / 100

async def task4():
    try:
        dollars = await dollars_to_float(input(f"{HEADER}    Cik maksā ēdiens? {ENDC}"))
        percent = await percent_to_float(input(f"{HEADER}    Kādu procentu vēlaties atstāt kā padomu? {ENDC}"))
        tip = dollars * percent
        print(f"{HEADER}    Atstājiet ${tip:.2f}{ENDC}")
    except ValueError:
        print(f"{HEADER}    Kļūda: Lūdzu ievadiet derīgu skaitli{ENDC}")
        