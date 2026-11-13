# flash-any.nvim 虎码

[English](README.en.md)

配合 [flash-any.nvim](https://github.com/dirichy/flash-any.nvim/tree/main)，
在 Neovim 中输入虎码搜索中文并跳转。
本项目主要为虎码打单用户提供，打词用户可以看 [flash-any-tigress.nvim](https://github.com/dirichy/flash-any-tigress.nvim/tree/main)，

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

## 配置

通常直接使用 `sources = { "tiger" }` 即可，主要配置是可省略的选键：

| 选项 | 默认值 | 用途 |
| --- | --- | --- |
| `selection` | 启用 | `false` 关闭选键，表可定制 keys |
| `selection.keys` | `{ " ", ";" }` | 按权重依次给首选、次选等候选分配按键 |
| `matcher` | `full_code` | 启用选键时必须是 full_code；关闭选键后可改用 initial/prefix |

默认首选空格、次选分号，没有默认三选键。所有候选仍支持裸码，例如 `gch` 仍可
匹配同码的所有字，`gch;` 可匹配二选“羔”。选键用于保留输入手感，不强制输入。

修改或追加选键时，将安装示例的 opts 换成：

```lua
opts = {
  sources = {
    { name = "tiger", selection = { keys = { " ", ";", "'" } } },
  },
}
```

这里单引号是主动追加的三选键。列表必须非空、各键不能重复，每个键为 1–127 字节的非空 ASCII 字符串。未分配按键的候选保留裸码匹配。
候选按静态权重排序，同权按码表原始顺序，再按文字排序，不跟随输入法的动态词频。

关闭选键：

```lua
opts = { sources = { { name = "tiger", selection = false } } }
```

中文标点已在码表中，直接输入 `,`、`.` 等即可，不需要额外配置。标点条目
不提供权重，因此不参与候选排名、不分配选键。

关闭选键后选择其他匹配方式的示例，见[配置示例](docs/options.md)。

## 更多

- [flash-any 配置说明](https://github.com/dirichy/flash-any.nvim/blob/main/README.zh-CN.md)
- [更新码表与录制演示](docs/maintenance.md)

## 许可

项目代码采用 [MIT](LICENSE)，码表来源与上游条款见 [THIRD_PARTY.md](THIRD_PARTY.md)。
