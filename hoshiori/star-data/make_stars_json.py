#!/usr/bin/env python3
"""HYG Database v4.2 の CSV から、明るい星だけを抜き出して JSON にする。

使い方:
    python3 -I scripts/make_stars_json.py <hyg_v42.csv> <出力するstars.json>

- mag <= 5.0 の星だけを残す
- 太陽(id 0)は除外する
- 必要な列だけを残す: id / ra(時) / dec(度) / mag / proper(固有名)
- 明るい順に並べる

元データ: HYG Database v4.2 (CC BY-SA 4.0)  https://codeberg.org/astronexus/hyg
"""
import csv
import json
import sys

MAG_LIMIT = 5.0


def extract_stars(rows):
    """CSV の行(辞書)の並びから、条件に合う星のリストを作る。"""
    stars = []
    for row in rows:
        star_id = int(row["id"])
        if star_id == 0:  # 太陽は除外
            continue
        mag = float(row["mag"])
        if mag > MAG_LIMIT:
            continue
        stars.append({
            "id": star_id,
            "ra": float(row["ra"]),    # 赤経(時)
            "dec": float(row["dec"]),  # 赤緯(度)
            "mag": mag,
            "name": row["proper"] or None,  # 固有名。無い星は null
        })
    stars.sort(key=lambda s: s["mag"])
    return stars


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, newline="", encoding="utf-8") as f:
        stars = extract_stars(csv.DictReader(f))
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(stars, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(stars)} 個の星を書き出しました: {dst}")


if __name__ == "__main__":
    main()
