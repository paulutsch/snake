import pygame
from logik import (
    events_prüfen,
    schlange_bewegen,
    wandcrash_prüfen,
    selbstcrash_prüfen,
    apfel_essen_prüfen,
    apfel_teleportieren,
    bildschirm_rendern,
)

pygame.init()

uhr = pygame.time.Clock()

spiel_läuft = True
score = 0

# Hauptteil des Spielsa: Spiel wird immer wieder aktualisiert
while spiel_läuft:
    spiel_läuft = events_prüfen()
    schlange_bewegen()

    wand_gecrasht = wandcrash_prüfen()
    selbst_gecrasht = selbstcrash_prüfen()
    if wand_gecrasht or selbst_gecrasht:
        spiel_läuft = False
        break

    apfel_gegessen = apfel_essen_prüfen()
    if apfel_gegessen:
        apfel_teleportieren()
        score += 10
        print("SCORE:✭", score)

    bildschirm_rendern()

    # 20 Bilder pro Sekunde einstellen
    uhr.tick(20)

print("Spiel wird beendet.")
pygame.quit()
quit()
