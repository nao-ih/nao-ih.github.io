# HOSHIORI star data / HOSHIORI の星のデータ

This folder contains the star data used by the iOS app **HOSHIORI**, and the script that produced it.
このフォルダは、iOSアプリ「HOSHIORI」が使う星のデータと、それを作ったスクリプトです。

**The files in this folder are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).**
**このフォルダの中のファイルは、[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ja) で提供しています。**

Only the files in this folder (`stars.json`, `make_stars_json.py`) are covered by this license.
The rest of this website, and the HOSHIORI app itself (its code, artwork, and designs), are **not** covered by it.
このライセンスの対象は、このフォルダの `stars.json` と `make_stars_json.py` だけです。このサイトのほかの部分と、HOSHIORIアプリ本体(コード・絵・デザイン)は、対象では**ありません**。

## Attribution / 出典

Based on the **HYG Database** (version 4.2), created and maintained by astronexus.com:

- https://www.astronexus.com/projects/hyg
- https://codeberg.org/astronexus/hyg

The HYG Database is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License
(https://creativecommons.org/licenses/by-sa/4.0/). It is itself compiled from the Hipparcos, Yale Bright Star,
and Gliese (nearby stars) catalogs.

元になったのは、astronexus.com が作成・公開している **HYG Database**(バージョン4.2)です。
HYG Database は CC BY-SA 4.0 で提供されています。Hipparcos・Yale Bright Star・Gliese の各星表をまとめたものです。

## Changes made / 加工した内容

The original data was modified as follows. 元のデータに、次の加工をしました。

1. Kept only stars with apparent magnitude **5.0 or brighter** (`mag <= 5.0`). 見かけの明るさが5.0等級以下(明るい星)だけを残した。
2. Removed the Sun (HYG `id` 0). 太陽(`id` 0)を除いた。
3. Kept only these columns, and renamed `proper` to `name`. 次の列だけを残し、`proper` を `name` に改名した。
   - `id` (HYG id), `ra` (right ascension, hours), `dec` (declination, degrees), `mag` (magnitude), `name` (proper name, `null` if none)
4. Sorted by brightness (brightest first), and wrote the result as compact JSON. 明るい順に並べ、JSONにした。

The result is `stars.json` (1,637 stars). 結果は `stars.json`(1,637個)です。
To reproduce: `python3 -I make_stars_json.py <hyg_v42.csv> <stars.json>`

## License / ライセンス

`stars.json` and `make_stars_json.py` are distributed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.
Full text: https://creativecommons.org/licenses/by-sa/4.0/legalcode

You may copy, redistribute, and adapt this data, including for commercial purposes, as long as you:
- give appropriate credit (see "Attribution" above), provide a link to the license, and indicate if you made changes; and
- distribute your adapted version under the same license (CC BY-SA 4.0).

This data is provided "as is", without any warranty.
このデータは、現状のまま提供し、いかなる保証もしません。
