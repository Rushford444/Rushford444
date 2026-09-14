# DONE — PROFIL-V2 (lane profil, agent NOUVEAU)

Refonte complète self-hosted du README de profil `Rushford444/Rushford444`, exécutée le 2026-09-14 sur la branche `lane/profil-v2`. Source de vérité : `docs/profil-research.md` (459 lignes, §5 « recommandation concrète » fait foi), mission lane du 14/09.

## Fichiers modifiés / créés

| Fichier | Action | Contenu |
|---|---|---|
| `README.md` | **réécrit** | bannière contrôlée, intro statique, section « Ce que je construis » conservée, row skillicons, cartes stats self-hostées, snake `<img>` simple, footer ASCII |
| `assets/cards/profile-details.svg` | **créé** | carte profil — palette custom, généré depuis l'API officielle github-profile-summary-cards |
| `assets/cards/most-commit-language.svg` | **créé** | carte langages commités |
| `assets/cards/stats.svg` | **créé** | carte stats |
| `assets/cards/repos-per-language.svg` | **créé** | commité, non affiché (dispo si besoin) |
| `assets/cards/productive-time.svg` | **créé** | commité, non affiché (dispo si besoin) |
| `assets/cards/streak.svg` | **créé** | streak-stats, généré depuis l'API officielle demolab |
| `.github/workflows/profile-cards.yml` | **créé** | régénération nocturne `0 3 * * *` + `workflow_dispatch`, `permissions: contents:write`, GITHUB_TOKEN interne uniquement, commit & push si diff |
| `.github/workflows/snake.yml` | **intouché** | gardé tel quel (sortie branche `output`) |
| `assets/banner.jpeg` | **intouché** | bannière GTO sumi-e conservée (mission prime) |

## Contenu du README, section par section

1. **Bannière** — `assets/banner.jpeg` en `<img width="850">` (source 1536×904, GitHub clampe à 100 % du container → « pleine largeur, max-width contrôlé », fini le `width="100%"` qui déformait).
2. **Tagline** — statique `### Just a dev who ships.`, puis bio FR/EN (textes conservés de la v1, jugés bons par la research §⑤).
3. **Ce que je construis** — conservé tel quel (reco §③) : Agora décrite (concile de LLM, recherche multi-agents, veille contradictoire), studio 3D temps réel et atelier de couture restés floutés.
4. **Stack** — une ligne skillicons : `i=ts,react,nextjs,nodejs,rails,postgres,docker` (IDs vérifiés dans le readme officiel `tandpfun/skill-icons`), `theme=dark`.
5. **Stats** — `profile-details` en 850, paire `most-commit-language` + `stats` en 425 (dans un `<p align>`, **pas de table**), `streak` en 495. Tous pointent vers des fichiers commités `assets/cards/*.svg` — chemins relatifs, zéro CDN.
6. **Snake** — `<img>` simple vers `raw.githubusercontent.com/.../output/github-contribution-grid-snake.svg` (le `<picture>` mort-né de la v1 est supprimé).
7. **Playground** — conservé (reco §⑧).
8. **Footer ASCII** — petit serpent discret en `<pre>` avec la palette.

## Arbitrages (reco research vs mission)

1. **Tagline statique, pas de typing-svg** — la mission demandait d'arbitrer ; la research §② recommande explicitement l'intro statique (« plus fiable, plus pro », le typsvg ne respecte pas `prefers-reduced-motion`). mobile-first → statique.
2. **Summary cards via l'API officielle du projet, pas via son Action** — l'Action officielle `vn7n24fzkq/github-profile-summary-cards@release` **ne supporte pas les couleurs custom** (vérifié dans son `action.yml` le 14/09 : inputs limités à USERNAME/BRANCH_NAME/UTC_OFFSET/EXCLUDE/EXCLUDE_REPOS/AUTO_PUSH/THEME/ANIMATION/DURATION/NAME). La mission impose `bg #29201e / accent #e16c37` → fetch de l'API officielle du projet (params custom colors documentés : `title_color, text_color, bg_color, border_color, icon_color, chart_color`) puis commit, exactement le même pattern fetch→commit que l'Action streak. `theme=github_dark` en base (garde les couleurs sémantiques des langages) + overrides palette + `utcOffset=1` (Paris).
3. **Streak via l'Action officielle** `DenverCoder1/github-readme-streak-stats@main` (inputs `options`/`path`/`token`), `token: ${{ secrets.GITHUB_TOKEN }}` — pas de PAT. `locale=fr` conservé (déjà en v1, supporté §2.5). `disable_animations=true` : SVG committé = figé, et cohérent avec reduced-motion.
4. **Streak affiché en 495 px** (largeur native) au lieu du `850` de la reco §⑤ — upscaler 495→850 rend le texte chunky ; la table §3.1 de la research valide `card_width=495`.
5. **Bannière conservée** (`banner.jpeg`, GTO sumi-e) alors que la reco §① proposait un remplacement PNG 2048×460 — la mission dit « NE PAS remplacer ». Le drift de palette signalé ne concerne que les widgets, corrigé.
6. **5 cartes générées, 3 affichées (+ streak)** — `repos-per-language` et `productive-time` sont commités et prêts, non affichés pour rester fidèle au layout §④.
7. **Concurrence** — `concurrency: profile-cards` ajoutée (schedule + dispatch ne se marchent pas dessus) ; `snake.yml` garde son trigger `push: [master]`.

## Gates passés

- ✅ YAML des 2 workflows validé (`python3 -c yaml.safe_load`) — jobs + cron `0 3 * * *` + `workflow_dispatch`.
- ✅ Largeurs README : 850 ×3, 425 ×2 (paire = 850 max), 495 — tout ≤850, aucun tableau HTML.
- ✅ Liens relatifs testés : `assets/banner.jpeg` + 4 SVG référencés existent.
- ✅ Aucune URL vercel.app / demolab dans le README (seuls restes externes : `skillicons.dev` officiel et le raw du snake sur GitHub).
- ✅ XML des 6 SVG validé ; palette vérifiée dans les fichiers (`#29201e`, `#e16c37`, `#f4e8dd`, `#ddbba2`, `#8a7a70`).

## Post-merge

- Premier run : `workflow_dispatch` sur `Rushford444/Rushford444` → onglet Actions → `profile-cards` (ou attendre 3 h UTC).
- Aucun secret à créer : tout tourne au GITHUB_TOKEN interne.
- Note de fiabilité : demolab a renvoyé des 503 intermittents pendant la génération locale (retry passé) — c'est précisément la fragilité que le commit des SVG neutralise : si un fetch échoue la nuit, l'ancien SVG reste servi.
