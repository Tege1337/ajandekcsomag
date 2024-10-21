"""
1. Feladat: Ajándékcsomagoló szalag számítás
Készítsünk programot, amely ajándékok csomagolásához szükséges szalag hosszát számolja ki. 
A szalag hosszának úgy kell elegendőnek lennie, hogy kétszer körbeérje az ajándék körvonalát (téglalap alapú csomag esetén), és a masni készítéséhez további 50 cm szükséges. 
A program kérje be az ajándék hosszát, szélességét és magasságát (cm-ben), az ajándékok számát, valamint a rendelkezésre álló szalag hosszát (méterben).
Számítsa ki, hogy hány méter szalagra van szükség a megadott számú ajándék csomagolásához, és közölje a felhasználóval, hogy elegendő-e a szalag.
"""

length = int(input("Milyen hosszú a csomagod? (cm) "))
width = int(input("Milyen széles a csomagod? (cm) "))
height = int(input("Milyen magas a csomagod? (cm) "))
quantity = int(input("Hány darab csomagod van? "))
tape = float(input("Hány méter szallag van rendelkezésedre? "))

tape_req = (quantity * (2 * (width + length + (2 * height))) + 50) / 100

if tape_req < tape:
    print(f"{tape_req} méter szallagra van szükséged. ")
else:
    print(f"Nincs elég szallagod! {tape_req} méter szallag szükséges hozzá! ")