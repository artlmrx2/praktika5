from main import HEADER, ENDC

async def task2():
    text = input(f"{HEADER}    Ievadiet tekstu: {ENDC}")
    print(f"{HEADER}    Rezultāts: {ENDC}", text.lower())