# Preuves d'animation — assets/anim/

Pour chaque SVG : 2 captures headless (Chrome `--headless=new`, horloge figée par
`animation-play-state: paused` + `animation-delay: -t !important`, SVG inline, fond GitHub sombre `#0d1117`),
à **t=0** et **t = moitié du cycle**. La différence entre les deux frames est vérifiée par
`compare -metric AE` (ImageMagick) : AE > 0 = les frames diffèrent = l'animation tourne.

| SVG | cycle | t0 | t mid | AE (pixels différents) | ce qui bouge |
|---|---|---|---|---|---|
| `divider-vague.svg` | 7 s | `divider-vague-t0.png` | `divider-vague-tmid.png` | 3270 | trait qui se dessine (stroke-dashoffset 100→0) |
| `intro-tapage.svg` | 5,2 s | `intro-tapage-t0.png` | `intro-tapage-tmid.png` | 4772 | frappe lettre par lettre + curseur |
| `neko-samurai.svg` | 3,4 s (alternate) | `neko-samurai-t0.png` | `neko-samurai-tmid.png` | 38382 | respiration (translateY+scale) + ombre en contre-phase |
| `drop-pulse.svg` | 1,8 s | `drop-pulse-t0.png` | `drop-pulse-tmid.png` | 1681 | goutte qui grossit + halo |

- t0 divider : trait absent (début du dessin) / tmid : vague complète.
- t0 intro : seul le curseur / tmid : « Just a dev who ship… » frappé, curseur mi-course.
- t0 neko : au sol, ombre large et claire / tmid : chat monté de 3,5 px, ombre resserrée et densifiée.
  (sprite RÉEL du jeu SUMI en data URI — remplace `chat-idle.svg`, dessiné main, supprimé.)

Note : ces captures figent l'animation à un instant voulu — sur github.com, le SVG animé boucle en continu
(CSS `@keyframes` inline, rendu animé par le navigateur du visiteur, rien ne passe par un CDN).
