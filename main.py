import asyncio, os

HEADER = '\033[95m'
ENDC = '\033[0m'

async def main():
    while True:
        os.system("cls")
        
        print()
        print(f'    Praktiskais Darbs {HEADER}N5{ENDC}')
        print()
        print(f"    Izvēlieties {HEADER}uzdevumu{ENDC}:")
        print()
        print(f"    {HEADER}1.{ENDC} Skaitļa sadalīšana pirmreizinātājos")
        print(f"    {HEADER}2.{ENDC} Teksta pārveidošana uz mazajiem burtiem")
        print(f"    {HEADER}3.{ENDC} Atstarpes aizstāšana ar '...'")
        print(f"    {HEADER}4.{ENDC} Dzeramnaudas kalkulators")
        print(f"    {HEADER}0.{ENDC} Iziet")
        print()
        choice = input(f"{HEADER}    - {ENDC}")
        print()

        if choice == "0":
            break
        elif choice == "1":
            from utils.task1 import task1  
            await task1()
            input(f"{HEADER}    Poga Enter lai atgrieztos uz menu{ENDC}")
        elif choice == "2":
            from utils.task2 import task2 
            await task2()
            input(f"{HEADER}    Poga Enter lai atgrieztos uz menu{ENDC}")
        elif choice == "3":
            from utils.task3 import task3  
            await task3()
            input(f"{HEADER}    Poga Enter lai atgrieztos uz menu{ENDC}")
        elif choice == "4":
            from utils.task4 import task4  
            await task4()
            input(f"{HEADER}    Poga Enter lai atgrieztos uz menu{ENDC}")
        else:
            print(f"{HEADER}    Nederīga izvēle!{ENDC}")

if __name__ == "__main__":
    asyncio.run(main())