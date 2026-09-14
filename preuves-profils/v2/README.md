# Preuves — PROFIL-AWWWARDS-V2 (5 retours Luis)

Captures rendues au navigateur (Chromium via Playwright), en simulant le rendu
réel de GitHub : markup servi par le sanitizer (`<p align="center">`,
`<img width="..." style="max-width:100%">`), fond `#0d1117`, container mesuré
**846 px** en desktop 1280 et **308 px** en mobile 390 (mesuré sur
github.com/Rushford444). Les `src` sont des chemins locaux servis depuis la
racine du repo.

## Cartes stats (retour 3 — fini l'empilement)

| Fichier | Preuve |
|---|---|
| `cartes-avant-desktop.png` | AVANT — container 846 : la paire 425+425 dépasse (850 + espace) → **wrap**, tout empilé |
| `cartes-apres-desktop.png` | APRÈS — diptyque langs+stats, diptyque streak+productive (2×415 = 835 ≤ 846), `profile-details` 780 en fermeture |
| `cartes-apres-mobile.png` | APRÈS — 308 px : chaque carte passe pleine largeur, lisible, l'ordre narratif langs → activité → streak → annexes reste vertical |

## Hero (retours 1 et 5 — bannière + respiration)

| Fichier | Preuve |
|---|---|
| `hero-apres-desktop.png` | bannière Onizuka en 1re image, pause ~64 px (`<p><br><br></p>`), diorama dessous, tagline animée, bio FR/EN |

## Neko transparent (retour 2)

| Fichier | Preuve |
|---|---|
| `neko-avant.png` | AVANT — carte papier `#f4e8dd` opaque (pixel centre : `rgb(244,232,221,255)`) |
| `neko-transparent-t0.png` | APRÈS — keyframe « from » figée : fond transparent, **alpha = 0 aux 4 coins** |
| `neko-transparent-tmid.png` | APRÈS — keyframe « to » figée (translateY −3.5 px, scale 1.012, ombre pleine) |
| `neko-fonds-github.png` | rendu réel sur fonds GitHub dark `#0d1117` et light `#ffffff` — le halo papier détache le chat encre, lisible dans les deux thèmes |

Frames t0/tmid = le `<style>` retiré et les transforms CSS des keyframes
`breathe`/`shadow` figés en attribut SVG ; rendu `omit_background` (Playwright).
Vérifs : alpha coins `[0,0,0,0]` sur les deux frames, différence entre frames
AE moyenne 18.0 (99 458 pixels > 8) → l'animation reste vivante.
