# Tiger codes for flash-any.nvim

[简体中文](README.zh-CN.md)

Use Tiger codes to search Chinese text and jump with
[flash-any.nvim](https://github.com/dirichy/flash-any.nvim/tree/main).

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

The default optional selection keys are Space for the first candidate and `;` for
the second. For example, `gch;` matches “羔”; `gch` still matches all candidates.

To change the keys, replace `opts` above with:

```lua
opts = {
  sources = {
    { name = "tiger", selection = { keys = { " ", ";" } } },
  },
}
```

Use `{ name = "tiger", selection = false }` to disable selection keys.
This repository is currently private; GitHub access is required to install it.

## More

- [flash-any configuration](https://github.com/dirichy/flash-any.nvim/blob/main/README.md)
- [Updating the table and recording demos](docs/maintenance.md)

## License

Code: [MIT](LICENSE). Table sources and upstream terms: [THIRD_PARTY.md](THIRD_PARTY.md).
