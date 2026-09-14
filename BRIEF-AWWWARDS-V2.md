# BRIEF — PROFIL-AWWWARDS-V2 (retours Luis, 21h19)

> Le hero diorama : GARDÉ (il plaît). Cinq retours précis à traiter.
> Périmètre : repo Rushford444 (README, assets, workflows). Rien d'autre.

## Retour 1 — BANNIÈRE ONIZUKA EN HAUT (le plus important)
Luis voulait la bannière GTO/Onizuka VISIBLE. Elle est sortie du README par la
lane v1 (arbitrage « moins mais mieux ») — Luis la redemande. Ordre final voulu :
1. `assets/banner.jpeg` (bannière Onizuka, pleine largeur) EN PREMIER
2. le diorama juste en dessous (il plaît, on le garde)
Composition : bannière → diorama → tagline → bio FR/EN → sections.

## Retour 2 — CHAT FIN DE README : FOND TRANSPARENT
Le playground `assets/anim/neko-samurai.svg` est posé sur une carte papier
`#f4e8dd` (rect rx=6 fill f4e8dd). Luis le veut SUR FOND TRANSPARENT.
- Supprime le rect de fond papier du wrapper SVG.
- Attention (l'arbitrage v1 reste valable) : le chat est noir → il n'est PAS
  lisible sur le fond encre sombre de GitHub. Solution : garde le chat noir
  MAIS ajoute un halo/glow doux CLAIR derrière lui (radial gradient blanc-cassé
  → transparent, subtil) OU inverse : silhouette du chat en PAPIER #f4e8dd
  (négatif sumi-e : le chat devient la lumière). Choisis la plus élégante des
  deux, montre les 2 frames de preuve.
- L'animation (respiration + ombre) reste.

## Retour 3 — CARTES : RECHERCHE DANS LE POSITIONNEMENT
Les 6 cartes stats sont toujours EMPILÉES (une par ligne). Luis veut une vraie
composition : cherche, compare, propose ET applique (pas de proposition sans
application — il teste ce soir).
- Contraintes dures : max-width 850px total, SANS <table> (pète sur mobile),
  mobile-first = ça doit rester lisible en ~360px de large.
- Pistes à tester en réel : paires côte à côte en <p> flex-wrap, une carte
  pleine largeur forte (activity) + 2×2 compact, espacements rythmés,
  alternance de largeurs. Vérifie le rendu au HTML final (curl + parse),
  pas juste dans le markdown source.
- Ordre narratif voulu : ce que je code (langs) → activité (activity) →
  constance (streak) → annexes (commit/PR/etc).

## Retour 4 — ICONES STACK
La row skill-icons existe déjà mais Luis veut des icônes PAR CATÉGORIE de
stack, pas une seule row plate. Réorganise par groupes avec un titre bref
chaque : Langages / Front / Back & Data / Outils & Infra. Groupes séparés par
des lignes distinctes, icônes ≤ 10 par ligne (mobile), garde skillicons.dev
(seul CDN toléré). Les icônes DOIVENT refléter la vraie stack : TS, React,
Next.js, Node, Rails, Postgres, Docker, Tailwind, Phaser (le jeu !), Git, gh.

## Retour 5 — NETTOYAGE GÉNÉRAL
Relis le README entier œil neuf : tout ce qui reste « empilé par défaut »,
redondant, ou sans intention → recompose. La signature finale (goutte +
« l'encre sèche, le code reste. ») reste. Bannière Onizuka + diorama doivent
respirer : pas deux images pleine largeur COLLÉES, garde un espace/pause
entre elles (hauteur maîtrisée).

## GATES
- README final : bannière 1re image, diorama 2e, aucun rect papier dans
  neko-samurai.svg, aucune <table>, 0 référence morte (tous les src existent),
  groupes d'icônes présents, largeur totale ≤ 850.
- XML des SVG modifiés valide (python xml.dom.minidom).
- 2 frames de preuve du neko transparent (AE > 0, fond transparent vérifié :
  alpha=0 aux coins).
- curl du README servi + vérif que les chemins relatifs répondent 200 sur
  raw.githubusercontent.
- Preuves captures avant/après dans preuves-profils/v2/.

## DONE
DONE-PROFIL-V2.md : ce qui a changé, captures, arbitrages. Commits type(scope).
NE POUSSE PAS master — livre ta branche lane/profil-awwwards-v2, le merge est
révisé par Jarvis.
