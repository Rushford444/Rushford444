# DONE — PROFIL-VIE (2026-09-14)

Mission : remettre de la vie dans le profil (animations + interactivité) en respectant la contrainte
dure GitHub/self-hosted — **pas de `<script>`, pas d'iframe externe, pas de CDN**. Levier utilisé :
les SVG **commités** avec CSS `<style>` + `@keyframes` inline, que github.com rend **animés**
(le SVG est servi tel quel, l'animation tourne dans le navigateur du visiteur).

## Fichiers créés / modifiés

| Fichier | Quoi |
|---|---|
| `assets/anim/divider-vague.svg` | Séparateur de section : trait d'encre vermillon qui **se dessine en boucle lente** (`pathLength=100` + `stroke-dashoffset` 100→0→−100, cycle 7 s : dessin → pause → effacement). Remplace les `---` markdown (intro et footer). |
| `assets/anim/intro-tapage.svg` | Tagline **« Just a dev who ships. »** frappée lettre par lettre (21 `<tspan>`, un créneau par lettre dans une timeline commune de 5,2 s) + curseur vermillon qui avance en `steps(21)` et clignote ; pause, fondu, boucle. Remplace le `###` statique. |
| `assets/anim/chat-idle.svg` | **Neko samurai** sumi-e inversé (crème sur carte encre `#29201e`, bord vermillon, cohérent avec `assets/cards/`) : 2 frames dessinées à la main (queues du bandeau au repos vs au vent, oreille gauche pliée, queue relevée) alternées en 0,6 s + ombre qui pulse (1,8 s). Héros du jeu à venir, en section Playground. |
| `assets/anim/drop-pulse.svg` | Goutte d'encre vermillon qui **pulse** (scale 1→1,1 + halo qui s'évanouit, 1,8 s) — Playground. |
| `README.md` | Intégration : intro-tapage sous la bannière, divider ×2 (après l'intro, avant le footer ASCII), projets en `<details>` pliables, chat + goutte en Playground. Tout le reste conservé (bannière, bio FR/EN, skill-icons, cartes commitées, snake, footer ASCII). |
| `preuves-profils/` | 8 captures (2 frames × 4 SVG) + `README.md` méthodo + scores AE. |

## Interactivité native

Les 3 projets de « Ce que je construis » sont passés de puces statiques à des **`<details>/<summary>`
pliables** (interactivité native GitHub, zéro JS) : summary = titre FR compact, contenu déplié =
détail FR + ligne *EN*. Une ligne « *click to expand* » guide le visiteur.

## Arbitrages

1. **`prefers-reduced-motion` (best-effort)** : chaque SVG a `@media (prefers-reduced-motion: reduce)
   { * { animation: none !important } }`. Best-effort assumé : ça dépend du navigateur du visiteur,
   mais surtout, **l'état de base CSS = état statique final** (divider dessiné, intro entière, chat en
   frame 1, goutte pleine) — si les animations sont coupées, rien n'est invisible ni cassé.
2. **Intro en SVG vs `###` markdown** : le H3 statique est remplacé par l'img animée. Le texte reste
   accessible via `alt="Just a dev who ships."` + `aria-label` + `<title>` du SVG, et la bio FR/EN
   statique en dessous porte l'info (règle « pas de texte critique en SVG uniquement » respectée pour
   le contenu, la tagline reste décorative).
3. **Pas de katana sur le chat** : le hachimaki vermillon (avec queues animées) suffit à lire
   « samurai » à 300 px ; un katana alourdissait le trait sumi-e.
4. **2 dividers seulement** (intro + footer) : l'animation boucle en continu, en multiplier les
   occurrences aurait fait du bruit visuel.
5. **Chat en « sumi-e inversé »** (crème sur carte encre) plutôt qu'encre sur transparent : sur le fond
   sombre GitHub, l'encre `#29201e` pure aurait été illisible ; la carte reprend exactement le style
   des cartes existantes (fond/bord/rx).
6. **Curseur typewriter calibré pour monospace système** (`ui-monospace, JetBrains Mono, Menlo,
   Consolas`) : avance en `steps(21)` = 21 paliers, synchro parfaite avec les 21 créneaux lettres ;
   à ±quelques px près selon la fonte dispo, sans risque de clipping (viewBox 660, contenu ≈ 554).

## Gates (toutes vertes)

- XML valide (`xmllint --noout`) sur les 4 SVG.
- Aucun `<script>`, `<foreignObject>`, `<iframe>`, `javascript:`, `href`, `url()` ; aucune URL externe
  hors namespace XML (self-hosted strict).
- Largeurs : 850 / 620 / 340 / 64 px — tout ≤ 850, `viewBox` exact, scale-down propre mobile
  (intro ≈ 16 px de font rendue sur un écran 320 px). Aucune table.
- Liens relatifs du README : les 9 `src="assets/…"` existent sur disque.
- **Preuves d'animation** (`preuves-profils/`) : 2 frames par SVG via Chrome headless
  (`animation-play-state: paused` + `animation-delay: -t` = seek déterministe à t=0 et t=moitié),
  diff ImageMagick `AE` > 0 pour les 4 (3270 / 4772 / 6488 / 1681 pixels différents) + vérif visuelle
  des frames (divider vide→dessiné, intro 0 lettre→frappée, chat pose A→pose B, goutte→halo).

## Hors périmètre / notes

- `docs/profil-research.md` vit dans `~/dev/Rushford444/docs/` (repo principal, non commité sur la
  branche) — source lue pour widgets/pièges : largeur ≤ 850, pas de table, mobile-first, contrastes OK.
- Pas de push ni de merge : la lane `lane/profil-vie` contient 3 commits atomiques, prêts pour review.
