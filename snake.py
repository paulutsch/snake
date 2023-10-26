import pygame
import random

import einstellungen

# starte Pygame
pygame.init()

# Bildschirm mit Maßen erstellen
bildschirm = pygame.display.set_mode(
    (einstellungen.BILDSCHIRM_BREITE, einstellungen.BILDSCHIRM_HÖHE)
)

schlangen_körperteil = pygame.Surface(
    (einstellungen.PUNKT_DURCHMESSER, einstellungen.PUNKT_DURCHMESSER)
)
schlangen_körperteil.fill(einstellungen.SCHLANGEN_FARBE)

apfel_körper = pygame.Surface(
    (einstellungen.PUNKT_DURCHMESSER, einstellungen.PUNKT_DURCHMESSER)
)
apfel_körper.fill(einstellungen.APFEL_FARBE)

# Position der Schlange
# Auf "links-rechts"-Achse vom Bildschirm soll die Schlange genau auf der Hälfte sein
schlange_x = einstellungen.BILDSCHIRM_BREITE // 2
# Auf "unten-oben"-Achse vom Bildschirm soll die Schlange auch genau auf der Hälfte sein
schlange_y = einstellungen.BILDSCHIRM_HÖHE // 2
# Schlangen-Position ist Kombi aus schlange_x und schlange_y
schlangen_kopf = [schlange_x, schlange_y]
schlangen_körper = [schlangen_kopf]

apfel_x = einstellungen.BILDSCHIRM_BREITE - 10 * einstellungen.PIXEL_PRO_TICK
apfel_y = einstellungen.BILDSCHIRM_HÖHE - 10 * einstellungen.PIXEL_PRO_TICK
apfel_pos = [apfel_x, apfel_y]

RICHTUNG = "RECHTS"

score = 0

# Schlange bewegen
uhr = pygame.time.Clock()

spiel_läuft = True

# Hauptteil des Spiels: Spiel wird immer wieder aktualisiert
while spiel_läuft:
    # Events durchschauen, ob ein Event namens "Beenden" dabei ist. Wenn ja, dann beenden!
    for event in pygame.event.get():
        # Ist das Event das Beenden-Event? Wenn ja, dann beende das Programm.
        if event.type == pygame.QUIT:
            spiel_läuft = False

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

    # Schlange bewegt sich in RICHTUNG
    # Wenn Richtung = OBEN ist, soll Schlange sich nach oben bewegen
    if RICHTUNG == "OBEN":
        schlange_y = schlange_y - einstellungen.PIXEL_PRO_TICK
    # Wenn Richtung = RECHTS ist, soll Schlange sich nach rechts bewegen
    elif RICHTUNG == "RECHTS":
        schlange_x = schlange_x + einstellungen.PIXEL_PRO_TICK
    # Wenn Richtung = LINKS ist, soll Schlange sich nach links bewegen
    elif RICHTUNG == "LINKS":
        schlange_x = schlange_x - einstellungen.PIXEL_PRO_TICK
    # Wenn Richtung = UNTEN ist, soll Schlange sich nach unten bewegen
    elif RICHTUNG == "UNTEN":
        schlange_y = schlange_y + einstellungen.PIXEL_PRO_TICK

    if (
        (schlange_x >= einstellungen.BILDSCHIRM_BREITE)
        or (schlange_x <= 0)
        or (schlange_y <= 0)
        or (schlange_y >= einstellungen.BILDSCHIRM_HÖHE)
    ):
        schrift = pygame.font.SysFont("Arial", 50)
        game_over = schrift.render("GAME OVER", True, (255, 0, 0))
        bildschirm.blit(
            game_over,
            [
                einstellungen.BILDSCHIRM_BREITE // 2,
                einstellungen.BILDSCHIRM_HÖHE // 2,
            ],
        )
        pygame.display.flip()
        pygame.time.wait(5000)
        break

    schlangen_kopf = [schlange_x, schlange_y]
    schlangen_körper.append(schlangen_kopf)

    # wenn Schlange Apfel isst:
    if schlangen_kopf == apfel_pos:
        # Punktestand um 15 erhöhen
        score = score + 15
        print("SCORE:", score)

        # Apfel teleportiert sich zufällig an neue Position auf dem Bildschirm
        apfel_x = (
            random.randint(
                0,
                (einstellungen.BILDSCHIRM_BREITE // 10) - 1,
            )
            * einstellungen.PUNKT_DURCHMESSER
        )

        apfel_y = (
            random.randint(
                0,
                (einstellungen.BILDSCHIRM_HÖHE // 10) - 1,
            )
            * einstellungen.PUNKT_DURCHMESSER
        )

        apfel_pos = [apfel_x, apfel_y]

        # Schlange wird um 1 größer
        print("HMMMMM LECKER")
    else:
        del schlangen_körper[0]

    # Bildschirm "reinigen": alle Alte löschen und nur Hintergrundfarbe reinsetzen
    bildschirm.fill(einstellungen.HINTERGRUND_FARBE)

    # Schlange und Apfel in Bildschirm reinsetzen
    for körperteil in schlangen_körper:
        bildschirm.blit(schlangen_körperteil, körperteil)
    bildschirm.blit(apfel_körper, apfel_pos)

    # Bildschirm anzeigen
    pygame.display.flip()

    # 20 Bilder pro Sekunde einstellen
    uhr.tick(15)

print("Spiel wird beendet.")
pygame.quit()
quit()
