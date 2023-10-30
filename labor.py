# 26.10.23
a = True
b = True

elemente = [a, b]

for element in elemente:
    if element:
        print("Ausgeführt")
        
# Ziel: Schlange erweitern bei Apfel essen
## Liste aus Schlangenpositionen
schlange_pos = [[schlange_x, schlange_y]]
## mit jedem Apfel wird Liste um aktuelle Position erweitert, danach die an Index 0 in RICHTUNG geändert
## für jede Position wird Schlangenkörper geblittet

# Ziel: Schlange körper größer machen#
schlangen_länge = 1
schlangen_körper[(schlange_x, schlange,y)]
if schlange_x == apfel_x and schlange_y == apfel_y:
    schlangen_länge += 1

if len(schlangen_körper) > schlangen_länge:
    del schlangen_körper[0]
