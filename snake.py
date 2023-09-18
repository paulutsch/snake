import pygame

# starte Pygame
pygame.init()

# Bildschirm-Maße erstellen
bildschirm_breite = 800
bildschirm_höhe = 400

# Farben
SCHWARZ = (0, 0, 0)
WEIß = (255, 255, 255)
PINK = (255, 192, 203)
GRÜN = (0, 255, 0)
ROT = (255, 0, 0)
BLAU = (0, 0, 255)

hintergrund_farbe = SCHWARZ

# Bildschirm mit Maßen erstellen
bildschirm = pygame.display.set_mode((bildschirm_breite, bildschirm_höhe))


# ein Punkt auf dem Bildschirm
punkt_breite = 10
punkt_höhe = 10

pixel_pro_tick = punkt_breite // 2

schlange_körper = pygame.Surface((punkt_breite, punkt_höhe))
schlange_körper.fill(PINK)

apfel_körper = pygame.Surface((punkt_breite, punkt_höhe))
apfel_körper.fill(ROT)

# Position der Schlange
# Auf "links-rechts"-Achse vom Bildschirm soll die Schlange genau auf der Hälfte sein
schlange_x = bildschirm_breite // 2
# Auf "unten-oben"-Achse vom Bildschirm soll die Schlange auch genau auf der Hälfte sein
schlange_y = bildschirm_höhe // 2
# Schlangen-Position ist Kombi auf schlange_x und schlange_y
schlange_pos = [schlange_x, schlange_y]


RICHTUNG = "RECHTS"

# Schlange bewegen
uhr = pygame.time.Clock()

# Hauptteil des Spiels: Spiel wird immer wieder aktualisiert
while True:
    # Events durchschauen, ob ein Event namens "Beenden" dabei ist. Wenn ja, dann beenden!
    for event in pygame.event.get():
        # Ist das Event das Beenden-Event? Wenn ja, dann beende das Programm.
        if event.type == pygame.QUIT:
            print("Nutzer beendet das Spiel.")
            pygame.quit()
            quit()
        # Ansonsten, wenn Taste gedrückt wurde, dann...:
        elif event.type == pygame.KEYDOWN:
            # Wenn Nutzer Pfeiltaste "Oben" gedrückt hat, dann setze RICHTUNG = "OBEN"
            if event.key == pygame.K_UP:
                RICHTUNG = "OBEN"
            # Ansonsten, wenn Nutzer Pfeiltaste "Rechts" gedrückt hat, dann setze RICHTUNG = "RECHTS"
            elif event.key == pygame.K_RIGHT:
                RICHTUNG = "RECHTS"
            # Ansonsten, wenn Nutzer Pfeiltaste "Links" gedrückt hat, dann setze RICHTUNG = "LINKS"
            elif event.key == pygame.K_LEFT:
                RICHTUNG = "LINKS"
            # Ansonsten, wenn Nutzer Pfeiltaste "Unten" gedrückt hat, dann setze RICHTUNG = "Unten"
            elif event.key == pygame.K_DOWN:
                RICHTUNG = "UNTEN"

    print("Richtung: ", RICHTUNG)

    # Schlange bewegt sich in RICHTUNG
    # Wenn Richtung = OBEN ist, soll Schlange sich nach oben bewegen
    if RICHTUNG == "OBEN":
        schlange_y = schlange_y - pixel_pro_tick
    # Wenn Richtung = RECHTS ist, soll Schlange sich nach rechts bewegen
    elif RICHTUNG == "RECHTS":
        schlange_x = schlange_x + pixel_pro_tick
    # Wenn Richtung = LINKS ist, soll Schlange sich nach links bewegen
    elif RICHTUNG == "LINKS":
        schlange_x = schlange_x - pixel_pro_tick
    # Wenn Richtung = UNTEN ist, soll Schlange sich nach unten bewegen
    elif RICHTUNG == "UNTEN":
        schlange_y = schlange_y + pixel_pro_tick

    schlange_pos = [schlange_x, schlange_y]

    # Bildschirm "reinigen": alle Alte löschen und nur Hintergrundfarbe reinsetzen
    bildschirm.fill(hintergrund_farbe)

    # Schlange in Bildschirm reinsetzen
    bildschirm.blit(schlange_körper, schlange_pos)

    # Bildschirm anzeigen
    pygame.display.flip()

    # 20 Bilder pro Sekunde einstellen
    uhr.tick(20)
