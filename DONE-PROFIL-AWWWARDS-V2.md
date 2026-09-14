# DONE — PROFIL-AWWWARDS-V2 (lane profil-awwwards-v2, agent NOUVEAU)

Les 5 retours de Luis (BRIEF-AWWWARDS-V2.md) traités le 2026-09-14 sur
`lane/profil-awwwards-v2`. Le hero diorama est conservé (retour Luis).
Preuves : `preuves-profils/v2/`. Merge révisé par Jarvis — master non poussé.

NB : `DONE-PROFIL-V2.md` existait déjà (trace d'une autre lane, `lane/profil-v2`
cartes self-hosted) — ce rapport prend un nom non collisant.

## Retour 1 — Bannière Onizuka en tête ✅

`assets/banner.jpeg` (1536×904) est la **première image** du README, en 850
(GitHub clampe à 846, ratio préservé). Ordre final : bannière → diorama →
tagline (`intro-tapage`) → bio FR/EN → sections. Preuve :
`preuves-profils/v2/hero-apres-desktop.png`.

## Retour 2 — Neko sur fond transparent ✅

`assets/anim/neko-samurai.svg` : le rect papier `#f4e8dd rx6` est **supprimé**.
Arbitrage entre les deux options du brief : **halo clair** retenu (radial
gradient `#f4e8dd` 0.9 → 0, ellipse 130×150 derrière le chat), pas le chat
papier — un chat `#f4e8dd` serait invisible sur le thème light de GitHub,
alors que chat noir + halo est lisible sur les deux thèmes (preuve
`neko-fonds-github.png`). Effet lune/lanterne sumi-e, cohérent avec le diorama.
Animation conservée (respiration + ombre, `prefers-reduced-motion` intact).

Gates : 0 `<rect` avant le sprite ; frames t0/tmid avec alpha = 0 aux 4 coins ;
AE entre frames 18.0 (99 458 px modifiés) → animation vivante prouvée.

## Retour 3 — Vraie composition des cartes ✅

Cause racine de l'empilement mesurée : le container GitHub fait **846 px** ;
l'ancienne paire 425+425 + espace inline = 854 > 846 → wrap systématique.
Nouvelle compo (sans table, mobile-first, ordre narratif demandé) :

1. diptyque `most-commit-language` + `stats` — 415 chacun (835 ≤ 846) : *ce que je code → l'activité*
2. diptyque `streak` + `productive-time` — 415 chacun : *la constance → le rythme*
3. `profile-details` — 780, la carte large de fermeture

À 308 px (mobile 390) chaque carte repasse pleine largeur : lisible
(`cartes-apres-mobile.png`).

Arbitrage : `repos-per-language` reste **non affichée** — l'API renvoie
actuellement « There are no repos to show » (0 repo indexé), une carte vide
casserait la compo. À ajouter au diptyque langs le jour où l'API l'alimente.

## Retour 4 — Stack par catégories ✅

4 groupes, labels discrets en `<sub><strong>`, ≤ 10 icônes/ligne (2-4 réels),
skillicons.dev (seul CDN, theme=dark) :

- **Langages** : TypeScript, Ruby
- **Front** : React, Next.js, Tailwind, **Phaser**
- **Back & Data** : Node.js, Rails, PostgreSQL
- **Outils & Infra** : Docker, Git, GitHub

Arbitrage notable : **l'API skillicons est cassée sur `i=phaser`** — elle
renvoie HTTP 200 avec littéralement `undefined` à la place de l'icône (vérifié
dans le SVG servi et dans leur repo : 402 icônes, zéro Phaser ; absent aussi de
simple-icons). Le brief exige Phaser dans les icônes et un seul CDN : la tuile
`assets/icons/phaser.svg` est donc **locale, style skillicons** (rect
`#242938 rx60`, monogramme « P » pixel-art bleu `#42ADF5`, 48 px, taille
identique aux tuiles du lot). Documentée dans le fichier.

## Retour 5 — Nettoyage général ✅

- Pause maîtrisée entre bannière et diorama : `<p align="center"><br><br></p>`
  (~64 px) — nécessaire car dans un bloc HTML GitHub les `<img>` hors `<p>` sont
  collées (~4 px d'espace inline) : c'était exactement le défaut signalé.
- 0 `<table>`, 0 référence morte (13 src locaux existent, distants vérifiés 200),
  toutes les largeurs ≤ 850 (le `100%` du diorama clampe à 846).
- Signature (goutte + « l'encre sèche, le code reste. ») intacte, dividers
  inchangés, sections `details` inchangées, snake inchangé.
- Aucune carte orpheline inutile : 5 des 6 SVG de `assets/cards/` affichés, la
  6e (`repos-per-language`) gardée pour plus tard (cf. retour 3).

## Gates du brief — toutes vertes

- ✅ Bannière 1re image, diorama 2e (vérifié par parse du README)
- ✅ Aucun rect papier dans `neko-samurai.svg` ; halo + animations présents
- ✅ Aucune `<table>` ; largeurs ≤ 850
- ✅ Groupes d'icônes présents (4, ≤ 10/ligne) ; tuile Phaser locale
- ✅ XML valide (`xml.dom.minidom`) : `neko-samurai.svg`, `phaser.svg`
- ✅ 2 frames neko : coins alpha 0, AE > 0
- ✅ curl raw sur `refs/heads/lane/profil-awwwards-v2` : README → 200, et les
      13 src relatifs → 200 ; snake (ref `output`) → 200 ; les 4 rows
      skillicons → 200 avec un user-agent navigateur (urllib reçoit un 403
      anti-bot du CDN, mais le rendu réel navigateur est prouvé en captures)
- ✅ Captures avant/après dans `preuves-profils/v2/`

## Fichiers modifiés / créés

| Fichier | Action |
|---|---|
| `README.md` | bannière en tête + pause, stack 4 catégories, compo cartes, tuile phaser référencée |
| `assets/anim/neko-samurai.svg` | rect papier supprimé, halo radial ajouté, anims intactes |
| `assets/icons/phaser.svg` | **créé** — tuile pixel-art locale (skillicons cassé sur phaser) |
| `preuves-profils/v2/` | **créé** — 10 captures avant/après + README de méthode |
| `DONE-PROFIL-AWWWARDS-V2.md` | **créé** (ce fichier) |

Intouchés : workflows (`profile-cards.yml`, `snake.yml`), diorama, cartes SVG
committées, signature, sections projets.
