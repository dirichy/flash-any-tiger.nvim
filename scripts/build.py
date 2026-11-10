#!/usr/bin/env python3
"""Build Tiger text/code/weight TSV preserving Rime dictionary row order."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
PUNCTUATION = {
    '￥': ['$'],
    '·': ['`'],
    '—': ['_'],
    '…': ['^'],
    '〕': [']'],
    '〔': ['['],
    '』': ['}'],
    '『': ['{'],
    '」': [']'],
    '「': ['['],
    '〉': ['>'],
    '〈': ['<'],
    '》': ['>'],
    '《': ['<'],
    '】': [']'],
    '【': ['['],
    '）': [')'],
    '（': ['('],
    '’': ["'"],
    '‘': ["'"],
    '”': ['"'],
    '“': ['"'],
    '！': ['!'],
    '？': ['?'],
    '：': [':'],
    '；': [';'],
    '、': ['/', '\\'],
    '。': ['.'],
    '，': [','],
}


ROW = re.compile(r"^([^\t]+)\t([^\t]+)\t(-?\d+)(?:\t.*)?$")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--codes-from", type=Path)
    args = parser.parse_args()
    keep = None
    if args.codes_from:
        keep = {tuple(line.split("\t")[:2]) for line in args.codes_from.read_text(encoding="utf-8").splitlines()}
    rows = {}
    for order, line in enumerate(args.source.read_text(encoding="utf-8").splitlines(), 1):
        match = ROW.match(line)
        if not match:
            continue
        text, code, weight = match.groups()
        if len(text) != 1 or (keep is not None and (text, code) not in keep):
            continue
        candidates = rows.setdefault(text, {})
        weight = int(weight)
        if code not in candidates or weight > candidates[code][0]:
            candidates[code] = (weight, order)
    for text, codes in PUNCTUATION.items():
        rows[text] = {code: (None, None) for code in codes}
    entries = [(order, text, code, weight) for text, codes in rows.items()
               for code, (weight, order) in codes.items() if weight is not None]
    entries.sort(key=lambda row: row[0])
    with args.output.open("w", encoding="utf-8") as output:
        for _, text, code, weight in entries:
            output.write(f"{text}\t{code}\t{weight}\n")
        for text, codes in PUNCTUATION.items():
            for code in codes:
                output.write(f"{text}\t{code}\n")
    print(f"wrote {len(rows)} characters")


if __name__ == "__main__":
    main()
