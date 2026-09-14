#!/usr/bin/env python3
"""Compose le hero diorama sumi-e depuis les couches de assets/diorama/.

Pipeline :
  1. neko-idle.png : l'alpha est nettoyé (voile de scan < 18 coupé, rampe
     douce jusqu'à 70) — le sprite reste NET, le fond devient transparent.
  2. fond = ciel (opaque) + montagnes + érables + torii, médian 5×5 :
     tue le grain papier (coûteux en PNG) sans toucher aux coups de pinceau.
  3. le chat est recomposé NET par-dessus (tiers droit, pieds sur la ligne
     d'encre), puis la brume médian-é couvre l'ensemble.
  4. quantisation : ImageMagick (FloydSteinberg, 256 couleurs) si dispo,
     sinon PIL. Objectif ≤ 500 Ko en 1600×900.

Usage : .venv-sumi/bin/python tools/compose_hero.py  (depuis la racine repo)
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIO = os.path.join(ROOT, "assets", "diorama")
OUT = os.path.join(ROOT, "assets", "hero-diorama.png")

NEKO_H = 470          # hauteur du chat dans le canvas 1600×900
NEKO_CX = 1100        # centre X — tiers droit, entre érables et lanternes
NEKO_FEET_Y = 880     # ligne de sol encre


def load(name: str) -> Image.Image:
    return Image.open(os.path.join(DIO, name)).convert("RGBA")


def main() -> int:
    # 1. alpha du sprite : <18 → 0, rampe linéaire 18→70, ≥70 conservé
    neko = load("neko-idle.png")
    arr = np.asarray(neko, dtype=np.float32).copy()
    al = arr[:, :, 3]
    arr[:, :, 3] = np.where(al < 18, 0.0, np.where(al <= 70, (al - 18) / (70 - 18) * 255.0, al))
    neko_clean = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

    # 2. fond médian
    bg = load("ciel.png")
    for layer in ("montagnes.png", "erables.png", "torii.png"):
        bg.alpha_composite(load(layer))
    canvas = bg.convert("RGB").filter(ImageFilter.MedianFilter(5)).convert("RGBA")

    # 3. chat net + brume médian par-dessus tout
    w = int(round(neko_clean.width * NEKO_H / neko_clean.height))
    sprite = neko_clean.resize((w, NEKO_H), Image.LANCZOS)
    canvas.alpha_composite(sprite, (NEKO_CX - w // 2, NEKO_FEET_Y - NEKO_H))

    mist_arr = np.asarray(load("brume.png"), dtype=np.float32).copy()
    mist_arr[:, :, 3] = np.where(mist_arr[:, :, 3] < 6, 0.0, mist_arr[:, :, 3])
    mist = Image.fromarray(np.clip(mist_arr, 0, 255).astype(np.uint8))
    mist = mist.filter(ImageFilter.MedianFilter(5))
    canvas.alpha_composite(mist)

    src = canvas.convert("RGB")

    # 4. quantisation ≤ 500 Ko
    if subprocess.run(["which", "magick"], capture_output=True).returncode == 0:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            tmp = f.name
        src.save(tmp)
        subprocess.run(
            ["magick", tmp, "-strip", "-dither", "FloydSteinberg", "-colors", "256",
             "-define", "png:compression-level=9", f"PNG8:{OUT}"],
            check=True,
        )
        os.unlink(tmp)
    else:  # repli PIL — plus lourd, gate 500 Ko non garanti
        q = src.quantize(256, dither=Image.Dither.FLOYDSTEINBERG)
        q.save(OUT, optimize=True)

    ko = os.path.getsize(OUT) / 1024
    print(f"{OUT} — {Image.open(OUT).size} — {ko:.0f} Ko")
    return 0 if ko <= 500 else 1


if __name__ == "__main__":
    sys.exit(main())
