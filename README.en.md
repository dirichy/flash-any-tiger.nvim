# Tiger codes for flash-any.nvim

[简体中文](README.md)

Use Tiger codes to search Chinese text and jump with
[flash-any.nvim](https://github.com/dirichy/flash-any.nvim/tree/main).
This project is primarily intended for Tiger users who type individual characters.
If you type words or phrases, see [flash-any-tigress.nvim](https://github.com/dirichy/flash-any-tigress.nvim/tree/main).

![Search and jump](https://github.com/dirichy/flash-any-tiger.nvim/releases/download/demos/table.gif)

[HD MP4](https://github.com/dirichy/flash-any-tiger.nvim/releases/download/demos/table.mp4)

## Install

Requires Neovim 0.11+, make and a C compiler. Add this to your lazy.nvim configuration:

```lua
{
  "dirichy/flash-any.nvim",
  branch = "main",
  version = false,
  dependencies = { "folke/flash.nvim", "dirichy/flash-any-tiger.nvim" },
  build = "make",
  opts = { sources = { "tiger" } },
  keys = {
    { "s", mode = { "n", "x", "o" }, function() require("flash-any").jump() end },
  },
}
```

## Use

1. Press `s` and enter a character's code.
2. Choose a displayed label to jump there.
3. Keep typing to match a longer phrase, mixing codes and ordinary ASCII text.

- Type `zhh` to find “虎”.
- Type `zhhmnm with flash` to find “虎码 with flash”.
- Type ordinary ASCII directly to search it.

## Configuration

`sources = { "tiger" }` works with the defaults. The main setting is optional
candidate-selection keys:

| Option | Default | Purpose |
| --- | --- | --- |
| `selection` | Enabled | `false` disables selectors; a table customizes keys |
| `selection.keys` | `{ " ", ";" }` | Assign keys to candidates in ranked order |
| `matcher` | `full_code` | Required with selectors; initial/prefix are available when selectors are disabled |

Space selects the first candidate and semicolon the second; there is no default
third-candidate key. All candidates still accept bare codes: `gch` matches every
candidate for that code, while `gch;` matches the second candidate “羔”. Selectors
preserve typing habits and are never mandatory.

To change or extend the keys, replace opts in the installation example with:

```lua
opts = {
  sources = {
    { name = "tiger", selection = { keys = { " ", ";", "'" } } },
  },
}
```

This explicitly adds an apostrophe for the third candidate. The list must be nonempty
and keys distinct. Each key must be a nonempty ASCII string of 1–127 bytes. Candidates without assigned keys retain bare-code matching.
Ranking uses static weights, then original row order, then text; it does not track
an input method's dynamic frequency.

To disable selectors:

```lua
opts = { sources = { { name = "tiger", selection = false } } }
```

Chinese punctuation is already included; type `,`, `.` and similar keys directly.
Punctuation rows omit weights, so they do not participate in ranking or receive selectors.

See [configuration examples](docs/options.en.md) for changing the matching mode
when selectors are disabled.

## More

- [flash-any configuration](https://github.com/dirichy/flash-any.nvim/blob/main/README.md)
- [Updating the table and recording demos](docs/maintenance.md)

## License

Code: [MIT](LICENSE). Table sources and upstream terms: [THIRD_PARTY.md](THIRD_PARTY.md).
