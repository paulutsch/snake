import pygame
import random

from einstellungen import (
    SCHWARZ,
    WEIß,
    PINK,
    GRÜN,
    ROT,
    BLAU,
    BILDSCHIRM_BREITE,
    BILDSCHIRM_HÖHE,
    PUNKT_DURCHMESSER,
    PUNKT_BREITE,
    PUNKT_HÖHE,
    PIXEL_PRO_TICK,
    HINTERGRUND_FARBE,
    SCHLANGEN_FARBE,
    APFEL_FARBE,
)


# starte Pygame
pygame.init()

# Bildschirm mit Maßen erstellen
bildschirm = pygame.display.set_mode((BILDSCHIRM_BREITE, BILDSCHIRM_HÖHE))

schlange_körper = pygame.Surface((PUNKT_BREITE, PUNKT_HÖHE))
schlange_körper.fill(SCHLANGEN_FARBE)

apfel_körper = pygame.Surface((PUNKT_BREITE, PUNKT_HÖHE))
apfel_körper.fill(APFEL_FARBE)

# Position der Schlange
# Auf "links-rechts"-Achse vom Bildschirm soll die Schlange genau auf der Hälfte sein
schlange_x = BILDSCHIRM_BREITE // 2
# Auf "unten-oben"-Achse vom Bildschirm soll die Schlange auch genau auf der Hälfte sein
schlange_y = BILDSCHIRM_HÖHE // 2
# Schlangen-Position ist Kombi aus schlange_x und schlange_y
schlange_pos = [schlange_x, schlange_y]

apfel_x = BILDSCHIRM_BREITE - 10 * PIXEL_PRO_TICK
apfel_y = BILDSCHIRM_HÖHE - 10 * PIXEL_PRO_TICK
apfel_pos = [apfel_x, apfel_y]

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
        schlange_y = schlange_y - PIXEL_PRO_TICK
    # Wenn Richtung = RECHTS ist, soll Schlange sich nach rechts bewegen
    elif RICHTUNG == "RECHTS":
        schlange_x = schlange_x + PIXEL_PRO_TICK
    # Wenn Richtung = LINKS ist, soll Schlange sich nach links bewegen
    elif RICHTUNG == "LINKS":
        schlange_x = schlange_x - PIXEL_PRO_TICK
    # Wenn Richtung = UNTEN ist, soll Schlange sich nach unten bewegen
    elif RICHTUNG == "UNTEN":
        schlange_y = schlange_y + PIXEL_PRO_TICK

    schlange_pos = [schlange_x, schlange_y]

    # wenn Schlange Apfel isst:
    if schlange_pos == apfel_pos:
        # TODO
        # Schlange wird um 1 größer
        # Apfel teleportiert sich zufällig auf den Bildschirm
        print("HMMMMM LECKER")

    # Bildschirm "reinigen": alle Alte löschen und nur Hintergrundfarbe reinsetzen
    bildschirm.fill(HINTERGRUND_FARBE)

    # Schlange und Apfel in Bildschirm reinsetzen
    bildschirm.blit(schlange_körper, schlange_pos)
    bildschirm.blit(apfel_körper, apfel_pos)

    # Bildschirm anzeigen
    pygame.display.flip()

    # 20 Bilder pro Sekunde einstellen
    uhr.tick(20)
