import einstellungen
import pygame
import random

# Position der Schlange

# Auf "links-rechts"-Achse vom Bildschirm soll die Schlange genau auf der Hälfte sein
schlange_x = einstellungen.BILDSCHIRM_BREITE // 2
# Auf "unten-oben"-Achse vom Bildschirm soll die Schlange auch genau auf der Hälfte sein
schlange_y = einstellungen.BILDSCHIRM_HÖHE // 2

# Schlangen-Position ist Kombi aus schlange_x und schlange_y
schlangen_kopf = [schlange_x, schlange_y]
schlangen_körper_liste = [
    schlangen_kopf
]  # Schlangenkopf wird in Schlanegekörperliste gespeichert

apfel_x = einstellungen.BILDSCHIRM_BREITE - 10 * einstellungen.PIXEL_PRO_TICK
apfel_y = einstellungen.BILDSCHIRM_HÖHE - 10 * einstellungen.PIXEL_PRO_TICK
apfel_pos_liste = [apfel_x, apfel_y]

# Bildschirm mit Maßen erstellen
bildschirm = pygame.display.set_mode(
    (einstellungen.BILDSCHIRM_BREITE, einstellungen.BILDSCHIRM_HÖHE)
)

schlangen_oberfläche = pygame.Surface(
    (einstellungen.PUNKT_DURCHMESSER, einstellungen.PUNKT_DURCHMESSER)
)
schlangen_oberfläche.fill(einstellungen.SCHLANGEN_FARBE)

apfel_oberfläche = pygame.Surface(
    (einstellungen.PUNKT_DURCHMESSER, einstellungen.PUNKT_DURCHMESSER)
)
apfel_oberfläche.fill(einstellungen.APFEL_FARBE)


RICHTUNG = "RECHTS"


def wandcrash_prüfen():
    global schlange_x
    global schlange_y

    if (
        (schlange_x >= einstellungen.BILDSCHIRM_BREITE)
        or (schlange_x <= 0)
        or (schlange_y <= 0)
        or (schlange_y >= einstellungen.BILDSCHIRM_HÖHE)
    ):
        game_over()
        return True

    return False


def selbstcrash_prüfen():
    global schlangen_kopf
    global schlangen_körper_liste

    anzahl_körperteile = len(schlangen_körper_liste)
    for i in range(anzahl_körperteile):
        körperteil = schlangen_körper_liste[i]

        # wenn letztes Körperteil, also Kopfteil, dann überspringe
        if i == anzahl_körperteile - 1:
            pass
        elif schlangen_kopf == körperteil:
            game_over()
            return True

        return False


def apfel_essen_prüfen():
    global schlangen_kopf
    global apfel_pos_liste

    if schlangen_kopf == apfel_pos_liste:
        return True

    return False


def game_over():
    global bildschirm

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


def schlange_bewegen():
    global schlange_x
    global schlange_y
    global schlangen_kopf
    global schlangen_körper_liste

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

    schlangen_kopf = [schlange_x, schlange_y]
    schlangen_körper_liste.append(schlangen_kopf)
    if schlangen_kopf != apfel_pos_liste:
        del schlangen_körper_liste[0]


def events_prüfen():
    global RICHTUNG

    # Events durchschauen, ob ein Event namens "Beenden" dabei ist. Wenn ja, dann beenden!
    for event in pygame.event.get():
        # Ist das Event das Beenden-Event? Wenn ja, dann beende das Programm.
        if event.type == pygame.QUIT:
            return False

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

    return True


def bildschirm_rendern():
    global bildschirm
    global schlangen_körper_liste
    global apfel_pos_liste
    global schlangen_oberfläche
    global apfel_oberfläche

    # Bildschirm "reinigen": alle Alte löschen und nur Hintergrundfarbe reinsetzen
    bildschirm.fill(einstellungen.HINTERGRUND_FARBE)

    # Schlange und Apfel in Bildschirm reinsetzen
    # schlangen_körper_liste = [ [körperteil_x, körperteil_y], [körperteil_x, körperteil_y], [körperteil_x, körperteil_y] ]
    for körperteil_pos_liste in schlangen_körper_liste:
        bildschirm.blit(schlangen_oberfläche, körperteil_pos_liste)
    bildschirm.blit(apfel_oberfläche, apfel_pos_liste)

    # Bildschirm anzeigen
    pygame.display.flip()


def apfel_teleportieren():
    global apfel_pos_liste

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

    apfel_pos_liste = [apfel_x, apfel_y]
