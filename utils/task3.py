from main import HEADER, ENDC

async def task3():
    text = input(f"{HEADER}    Ievadiet tekstu: {ENDC}")
    print(f"{HEADER}    Rezultāts: {ENDC}", text.replace(" ", "..."))