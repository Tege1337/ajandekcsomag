"""
2. Feladat: Festék mennyiségének számítása
Készítsünk programot, amely egy szoba falainak kifestéséhez szükséges festék mennyiségét számolja ki.
A program kérje be a szoba szélességét, hosszát és magasságát méterben, valamint azt, hogy hány liter festéket vásároltunk már. 
Tegyük fel, hogy 1 liter festék 10 négyzetmétert fed le.
Számolja ki, hogy hány liter festékre van szükség a szoba kifestéséhez, és közölje, hogy elegendő-e a festék, vagy szükség van-e további mennyiség beszerzésére.
"""

width = input("Milyen széles a szoba? (m) ")
length = input("Milyen hosszú a szoba? (m) ")
height = input("Milyen magas a szoba? (m) ")

paint = input("Mennyi festék áll rendelkezésedre? (l) ")

# egy liter festék 10 m2-t fed le

