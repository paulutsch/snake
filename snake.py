import pygame

# starte Pygame
pygame.init()

# Bildschirm-Maße erstellen
bildschirm_breite = 800
bildschirm_höhe = 400

# Farben
SCHWARZ = (255, 255, 255)
PINK = (255, 192, 203)
GRÜN = (0, 255, 0)
ROT = (255, 0, 0)
BLAU = (0, 0, 255)

# Bildschirm mit Maßen erstellen
bildschirm = pygame.display.set_mode((bildschirm_breite, bildschirm_höhe))
bildschirm.fill(SCHWARZ)

# ein Punkt auf dem Bildschirm
punkt_breite = 10
punkt_höhe = 10

pixel_pro_tick = punkt_breite // 2

schlange_körper = pygame.Surface((punkt_breite, punkt_höhe))
schlange_körper.fill(PINK)

apfel_körper = pygame.Surface((punkt_breite, punkt_höhe))
apfel_körper.fill(ROT)

# Position der Schlange
schlange_x = bildschirm_breite // 2
schlange_y = bildschirm_höhe // 2
schlange_pos = [schlange_x, schlange_y]


RICHTUNG = "RECHTS"


# Schlange bewegen
uhr = pygame.time.Clock()

# Spiel starten
while True:
    # Events durchschauen, ob ein Event namens "Beenden" dabei ist. Wenn ja, dann beenden!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Nutzer beendet das Spiel.")
            pygame.quit()
            quit()

    # Schlange bewegt sich in RICHTUNG
    if RICHTUNG == "RECHTS":
        # Schlange bewegt sich nach recht
        schlange_x += pixel_pro_tick
        schlange_pos = [schlange_x, schlange_y]

    bildschirm.blit(schlange_körper, schlange_pos)

    # Bildschirm anzeigen
    pygame.display.flip()

    # warte 50 ms, bevor die nächste Runde passiert
    uhr.tick(50)
