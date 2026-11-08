#!/usr/bin/env python3
"""Build sorted Tiger text/code/weight/original-order TSV from a Rime dictionary."""
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
        rows[text] = {code: (0, 0) for code in codes}
    with args.output.open("w", encoding="utf-8") as output:
        for text in sorted(rows, key=lambda value: value.encode("utf-8")):
            for code, (weight, order) in sorted(rows[text].items()):
                output.write(f"{text}\t{code}\t{weight}\t{order}\n")
    print(f"wrote {len(rows)} characters")


if __name__ == "__main__":
    main()
