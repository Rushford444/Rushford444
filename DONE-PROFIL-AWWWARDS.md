# DONE — PROFIL-AWWWARDS (2026-09-14)

Mission Luis : « fusionner le design ET le fonctionnel — awwward github profil ». Le profil était
des cartes empilées proprement mais sans âme ; la matière première (5 couches diorama sumi-e + le
VRAI sprite du chat samurai du jeu SUMI) était commitée dans `assets/`. Les 6 chantiers du brief
sont livrés, gates verts.

## Fichiers créés / modifiés

| Fichier | Quoi |
|---|---|
| `assets/hero-diorama.png` | **Le hero** : les 5 couches composées en une seule scène 1600×900, **479 Ko** (gate ≤ 500). Ciel opaque (soleil vermillon) → montagnes → érables → torii + lanternes → **le chat samurai NET au tiers droit, pieds sur la ligne d'encre** → brume par-dessus tout. Le soleil se lève pile derrière sa tête : halo naturel, pas un seul pixel forcé. |
| `tools/compose_hero.py` | Pipeline reproductible de composition (PIL + numpy, quantisation ImageMagick FS256 si dispo). `diff` byte-identique au PNG commité. |
| `assets/anim/neko-samurai.svg` | **Playground** : le sprite RÉEL du jeu (plus le chat dessiné main) en **data URI** dans un wrapper SVG — carte papier `#f4e8dd` au trait sable, ombre d'encre qui respire en contre-phase de la respiration du chat (translateY −3,5 px + scale 1,012, cycle 3,4 s). `prefers-reduced-motion` = statique. 176 Ko. |
| `assets/anim/chat-idle.svg` | **Supprimé** (dessin main, verdict Luis : moche) + toutes références (README, `preuves-profils/`). |
| `README.md` | Le profil **s'ouvre sur le hero pleine largeur** (`width="100%"`) — la bannière-carte est sortie du README (asset conservé). Playground avec le vrai neko. **Footer** : l'ASCII bavard remplacé par la goutte vermillon + une ligne — *« l'encre sèche, le code reste. — the ink dries, the code remains. »* |
| `.github/workflows/profile-cards.yml` | **Fusion design/fonctionnel** : la génération des cartes est re-stylée dans les PARAMS, pas à la main. Streak : `background=1a1412` + `border/stroke=e16c37` + `currTotalNum=f4e8dd` câblés (fini le `#E4E2E2` par défaut sur la flamme). Summary cards : `bg_color=1a1412`, `border_color=ddbba2` (traits), titre/vermillon `e16c37`, texte `f4e8dd`. |
| `.github/workflows/snake.yml` | Case vide = **encre `#1a1412`** (fini le `#1b1f23` dark GitHub), rampe chaude `#2b2320 → #e16c37` jusqu'au serpent. |
| `assets/cards/*.svg` | **6 cartes régénérées par le workflow réel** (run sur cette branche) — toutes en palette : encre `1a1412` / vermillon `e16c37` / sable `ddbba2` / texte `f4e8dd` / dates `8a7a70`. Vérifié couleur par couleur. |
| `preuves-profils/` | 2 frames `neko-samurai` (t0/tmid, **AE 38382** — l'anim tourne) ; lignes `chat-idle` retirées du registre. |
| Repo (hors code) | `gh repo edit` : description « Diorama sumi-e — produits web complets & systèmes d'agents IA qui livrent · full-stack that ships · encre & vermillon » + topics `github-profile`, `profile-readme`, `sumie`, `creative-coding`. |

## Avant / après (l'essentiel)

- **Ouverture** : bannière GTO 850 px + textes → **diorama plein cadre** avec le héros du jeu dedans.
  Quelqu'un qui scrolle voit une scène, pas des cartes empilées.
- **Cartes** : fond `29201e` + rampes par défaut qui juraient (`701516` rouge sombre, `586e75`
  gris-bleu, flamme `E4E2E2`, fond snake `1b1f23`) → palette unique `1a1412/e16c37/ddbba2/f4e8dd`,
  régénérée par les workflows (zéro retouche manuelle des SVG commités).
- **Playground** : chat SVG dessiné à la main → **le vrai sprite**, net, animé, avec preuves AE.
- **Footer** : 8 lignes d'ASCII bavard → une goutte + une ligne de signature.

## Arbitrages

1. **Bannière GTO sortie du README** : le hero LA remplace (l'asset reste dans `assets/`, intact).
   Deux images pleines largeur d'affilée aurait tué le hero — « moins mais mieux ».
2. **Chat du playground sur carte papier, pas sur encre** : le chat est noir ; sur la carte encre
   `#1a1412` il disparaissait. Le papier `#f4e8dd` le fait émerger et rappelle le support sumi-e.
3. **Data URI plutôt qu'un PNG séparé** : un wrapper SVG référence un PNG `src` relatif — GitHub
   ne résout pas les ressources relatives *dans* un SVG servi en image. Data URI = autonome.
   Sprite nettoyé (alpha < 18 coupé), cropé sur la bbox, quantisé : 65 Ko → wrapper 176 Ko.
4. **Chat NET préservé dans le hero** : le fond (peinture) passe au médian 5×5 (tue le grain papier
   qui gonflait le PNG de 40 %), puis le chat — seul — est recomposé net par-dessus, brume comprise.
5. **Signature en texte, pas de hanko SVG** : le sceau hanko en SVG `<text>` dépend des fonts CJK du
   visiteur (tofu possible) ; en chemins vectoriels je fabrique le glyphe. Texte sobre retenu.

## Limites GitHub / API rencontrées

1. **Rampe des camemberts langages non câblable** : l'API github-profile-summary-cards code en dur
   la rampe `github_dark` pour `repos-per-language` / `most-commit-language` (`chart_color` ne la
   couvre pas, testé : rampe multi-valeurs refusée). Normalisation automatique dans le workflow :
   `#586e75→#b35a2e`, `#701516→#7a4429`. C'est la seule retouche post-fetch, scriptée, pas manuelle.
2. **Pas de variant « gel-slots »** chez Platane/snk (doc vérifiée 14/09) : les cases mangées
   reprennent la case vide — pas de paramètre sable `#ddbba2` possible sans fork le projet, qui
   n'accepte pas de PR. Noté tel quel.
3. **Ombre d'anim du snake** : snk code en dur `--cb:#1b1f230a` (ombre de la cellule animée, alpha
   4 %) — invisible sur l'encre, laissée telle quelle.
4. **Graphe de contributions natif** : non contrôlable (couleurs GitHub), comme prévu au brief.
5. **`skillicons.dev`** reste la seule URL externe du README (pré-existante, non ajoutée — gate
   « aucune nouvelle URL externe » vert) ; la passer en self-hosted est un chantier séparé.

## Gates (tous verts)

- Hero : 1600×900, **479 Ko ≤ 500 Ko**, aucune couche écrasée (chat recomposé net, zoom vérifié).
- XML valide sur les 10 SVG du repo (python `minidom`).
- README : aucune table 2-col, largeurs fixes ≤ 850 (hero en 100 %), 10 img relatives toutes
  vérifiées par `fs.stat`, `alt` sur chaque img, aucune nouvelle URL externe vs master.
- A11y : `prefers-reduced-motion` présent dans les 4 SVG animés (état de base = état statique final).
- Workflows : `snake` et `profile-cards` re-run **avec succès** sur cette branche
  (runs 34882831657 / 34882835248) ; SVG résultats vérifiés (branche `output` pour le snake).

## Commits (atomiques)

1. `assets(hero)` — diorama composé + `tools/compose_hero.py`.
2. `ci(cards,snake)` — palette exacte dans les workflows.
3. `profil(playground)` — vrai neko samurai, chat-idle supprimé.
4. `profil(readme)` — hero en ouverture, signature sobre.
5. `preuves(playground)` — 2 frames AE 38382.
6. `docs(done)` — ce fichier.
