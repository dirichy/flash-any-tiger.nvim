# flash-any.nvim 虎码

[English](README.en.md)

配合 [flash-any.nvim](https://github.com/dirichy/flash-any.nvim/tree/main)，
在 Neovim 中输入虎码搜索中文并跳转。

![搜索跳转](https://github.com/dirichy/flash-any-tiger.nvim/releases/download/demos/table.gif)

[高清 MP4](https://github.com/dirichy/flash-any-tiger.nvim/releases/download/demos/table.mp4)

## 安装

需要 Neovim 0.11+、make 和 C 编译器。在 lazy.nvim 配置中添加：

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

## 使用

1. 按 `s`，输入要找的字的编码。
2. 按屏幕上显示的标签跳转。
3. 继续输入可以匹配更长的文本，编码与普通 ASCII 可以混输。

- 输入 `zhh`，找到“虎”。
- 输入 `zhhmnm with flash`，找到“虎码 with flash”。
- 搜索 ASCII 时直接输入原文。

默认首选键为空格、次选键为分号，均可省略。例如 `gch;` 可匹配“羔”，
`gch` 仍可匹配所有候选。

若想修改选键，将上面的 `opts` 换成：

```lua
opts = {
  sources = {
    { name = "tiger", selection = { keys = { " ", ";" } } },
  },
}
```

使用 `{ name = "tiger", selection = false }` 可以关闭选键。
本仓库目前为私有仓库，安装前需要具备 GitHub 访问权限。

## 更多

- [flash-any 配置说明](https://github.com/dirichy/flash-any.nvim/blob/main/README.zh-CN.md)
- [更新码表与录制演示](docs/maintenance.md)

## 许可

项目代码采用 [MIT](LICENSE)，码表来源与上游条款见 [THIRD_PARTY.md](THIRD_PARTY.md)。
