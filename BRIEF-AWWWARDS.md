# BRIEF — PROFIL AWWWARDS (lane profil-awwwards)

> Mission Luis, 14/09 soir : « fusionner le design ET le fonctionnel —
> awwward github profil. » Le profil actuel = cartes empilées proprement
> mais sans âme. On veut que quelqu'un qui scrolle s'arrête et dise « waouh ».

## Matière première (TOUT est dans assets/, commité)

- `assets/banner.jpeg` — bannière GTO sumi-e (NE PAS toucher)
- `assets/diorama/ciel.png` — couche ciel + soleil vermillon, **OPAQUE** (fond)
- `assets/diorama/montagnes.png` — crêtes encre (transparent)
- `assets/diorama/erables.png` — érables vermillon (transparent)
- `assets/diorama/torii.png` — torii + lanternes (transparent)
- `assets/diorama/brume.png` — voile brume très léger (transparent)
- `assets/diorama/neko-idle.png` — **LE chat samurai du jeu SUMI** (transparent, 1254²)
- `assets/anim/*.svg` — les 4 SVG animés existants (divider, tapage, chat-idle, drop)
- `assets/cards/*.svg` — les cartes stats commitées (générées par Action nocturne)

## Les 6 chantiers, par ordre d'impact

### 1. HERO diorama parallax (le remplace-aux-cartes-collées)
Compose les 5 couches en **UNE seule image hero** (Python PIL disponible, ou
compose les couches en CSS via un HTML→screenshot). Ciel opaque en fond,
par-dessus : montagnes → érables → torii → **le chat en bas au tiers droit**
(net, PAS dessiné à la main — le vrai sprite) → brume par-dessus tout.
Export : `assets/hero-diorama.png` (≤ 500 Ko, 1600×900 → affiché ~850px large).
Le README s'ouvre SUR cette image, pleine largeur, sans marges GitHub visibles
(si possible via `<img>` + width 100%). Pas d'animation CSS obligatoire ici :
la scène doit claquer en statique ; si tu animes, reduced-motion = statique.

### 2. FUSION design/fonctionnel — les cartes actuelles sont moches
Les `assets/cards/*.svg` générées par l'Action ont des couleurs par défaut
qui jurent. **Re-stylise la génération** : lis `.github/workflows/profile-cards.yml`,
applique le thème exact (bg #1a1412, titre/vermillon #e16c37, texte #f4e8dd,
traits #ddbba2) dans les PARAMÈTRES du générateur (github-profile-summary-cards
et streak-stats acceptent des params de couleur — c'est ça qu'il faut câbler,
pas retoucher les SVG à la main). Re-run le workflow si possible sinon note-le
dans DONE (il tourne à 3h).

### 3. Le snake — le rendre digne
Actuel : le SVG de base de Platane. Améliore : couleurs du serpent en vermillon
`#e16c37` sur fond encre `#1a1412` (le plugin supporte des palettes custom),
et si possible le variant **gel-slots** : les cases mangées prennent la teinte
sable `#ddbba2`. Regénère un run (`gh workflow run snake.yml`) et vérifie le SVG
résultat dans la branche `output`.

### 4. Playground — remplacer le chat SVG dessiné par le VRAI chat
`assets/anim/chat-idle.svg` (dessiné par la lane précédente, « moche » — verdict
Luis) est remplacé par le **vrai sprite** `neko-idle.png` dans la section
Playground. Animation acceptable : un léger `transform` CSS via le SVG wrapper
ou APNG généré depuis les frames du jeu ; à défaut, statique mais NET et fidèle.
Supprime `chat-idle.svg` et toute référence.

### 5. Le texte chelou de fin de README
Le footer ASCII + le bloc texte actuel ne passent pas. Réécris la fin :
une ligne de signature sobre et stylée (EN/FR au choix), éventuellement le
sceau hanko ASCII ou un divider animé existant — PAS de bloc de texte bavard.
« Moins mais mieux ».

### 6. Les assets GitHub de base encore visibles
Le repos pinned/les couleurs par défaut trahissent le profil. Corrige ce qui
est accessible depuis le repo : description + topics du repo profil
(`gh repo edit Rushford444/Rushford444 --description "..." --add-topic ...`),
vérifie qu'aucune image par défaut ne traîne dans le README. La partie
contribution graph native n'est PAS contrôlable — note-le comme limite dans DONE.

## GATES

- Hero ≤ 500 Ko, 1600×900, aucune couche écrasée (le chat doit rester NET)
- XML valide sur tout SVG modifié, aucune URL externe ajoutée (self-hosted !)
- README : aucune table 2-col, largeurs ≤ 850, tous liens relatifs existants
- `xmllint` ou python XML ok, liens relatifs testés par fs.stat
- A11y : alt text sur chaque img, reduced-motion respecté

## DONE

`DONE-PROFIL-AWWWARDS.md` : fichiers, avant/après décrits, arbitrages, limites
GitHub rencontrées. Commits atomiques `type(scope)`.
