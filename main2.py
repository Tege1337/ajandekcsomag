"""
2. Feladat: Festék mennyiségének számítása
Készítsünk programot, amely egy szoba falainak kifestéséhez szükséges festék mennyiségét számolja ki.
A program kérje be a szoba szélességét, hosszát és magasságát méterben, valamint azt, hogy hány liter festéket vásároltunk már. 
Tegyük fel, hogy 1 liter festék 10 négyzetmétert fed le.
Számolja ki, hogy hány liter festékre van szükség a szoba kifestéséhez, és közölje, hogy elegendő-e a festék, vagy szükség van-e további mennyiség beszerzésére.
"""

width = int(input("Milyen széles a szoba? (m) "))
length = int(input("Milyen hosszú a szoba? (m) "))
height = int(input("Milyen magas a szoba? (m) "))

paint = int(input("Mennyi festék áll rendelkezésedre? (l) "))

# egy liter festék 10 m2-t fed le

wall_1 = (height * length)
wall_2 = (height * width)
walls = 2 * (wall_1 + wall_2) # sqr m

paintable_surf = paint * 10
req_paint = walls / 10

if walls < paintable_surf:
    print(f"{req_paint} liter festék szükséges a szoba lefestéséhez. ")
else:
    print(f"Nincs elég festéked a szoba lefestéséhez! {req_paint} liter szükséges hozzá, és neked csak {paint} liternyid van. ")