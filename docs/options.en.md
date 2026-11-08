# All Tiger options

[简体中文](options.md) · [README](../README.en.md)

Put settings inside `{ name = "tiger", ... }` in opts.sources. The
[README](../README.en.md#configuration) covers defaults, a third key and disabling selectors.

## Selectors and matching

| Option | Default | Accepted values |
| --- | --- | --- |
| `name` | Shorthand `"tiger"` | Use name="tiger" in an options table |
| `selection` | Default selectors enabled | false disables; a table configures keys |
| `selection.keys` | `{ " ", ";" }` | Nonempty list of distinct single ASCII punctuation characters; only the first may be Space |
| `matcher` | `"full_code"` | Only full_code with selectors; initial/prefix also work with selection=false |
| `scope` | `"chinese"` | all/ascii/chinese/unicode/private_use or character/range declarations |
| `fallback` | `false` | Participate only when earlier ordinary sources did not recognize the grapheme |
| `groups` | None | Core spelling-group map; a code cannot combine group references and selectors, so normally disable selection first |

Keys 1, 2, 3… correspond to ranked candidates; unassigned candidates retain bare
codes. Ranking is descending weight, ascending order, then text. Missing weight is
0; missing order uses input order. Only codes containing ASCII letters receive
selectors; punctuation and other codes without letters do not. Ranking is static
and does not follow an input method's dynamic frequency. All selectors are optional.

Unsupported: scheme, selection_keys, force, punctuation, selection.force,
selection.first_omit_before, and append_space_below (even with selection=false).

## Dictionary overrides

| Option | Default | Accepted values |
| --- | --- | --- |
| `file` | Bundled tiger.tsv | External dictionary; supply weights/order for ranked selectors |
| `data` | No override | Small grapheme-to-code map; requires selection=false |
| `lua` | No override | Lua dictionary file; requires selection=false |
| `tsv` | None | Complete companion to lua; use file for a standalone TSV |

Overrides replace the entire table, including punctuation. file excludes data, lua
and tsv. The bundled TSV uses text/code/weight/order columns. External files use
format defaults, file metadata or explicit columns. Without weights, candidates
are ranked by input order. Change scope for non-Chinese entries.

```lua
{
  name = "tiger",
  file = "/path/to/tiger.dict.yaml",
  selection = { keys = { " ", ";" } },
}
```

A converter requires both file and selection=false:

```lua
{
  name = "tiger",
  file = "/path/to/custom.tsv",
  selection = false,
  converter = "/path/to/converter.lua",
}
```

## External file options

These settings apply only to `file`:

| Option | Default | Accepted values |
| --- | --- | --- |
| `format` | `"auto"` | auto, rime, tsv/tab, csv, space, fcitx, ibus |
| `columns` | File metadata or format defaults | Column-name array containing text and code; optional weight/order; other columns ignored |
| `encoding` | UTF-8 | Encodings supported by Neovim, such as gb18030 or utf-16le |
| `header` | `false` | Skip the first CSV record as a heading; does not apply to TSV |
| `converter` | None | Path to a Lua code-list conversion function; nil/empty output removes an entry |

Headerless TSV uses text/code order; set `columns = { "code", "text" }` for the
reverse order. Each row has one code; repeat rows for alternatives. Commas are
literal code characters. Rime imports use relative paths. File sources filter
multi-grapheme entries; direct data/Lua tables require one complete grapheme per key.
Converters run at build time, never as runtime matchers.

See the [core reference](https://github.com/dirichy/flash-any.nvim/blob/main/docs/sources.md)
for file formats, scope declarations and spelling-group semantics.
