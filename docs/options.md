# 虎码完整选项

[English](options.en.md) · [返回主页](../README.md)

选项放在 `opts.sources` 中的 `{ name = "tiger", ... }` 内。
[主页](../README.md#配置)说明默认选键、增加三选键和关闭选键。

## 选键和匹配

| 选项 | 默认值 | 支持内容 |
| --- | --- | --- |
| `name` | 名称简写为 `"tiger"` | 配置表写 name="tiger" |
| `selection` | 启用默认选键 | false 关闭，表可配置 keys |
| `selection.keys` | `{ " ", ";" }` | 非空数组；各项为一个 ASCII 标点，仅第一项可为空格，各键不同 |
| `matcher` | `"full_code"` | 开启选键只允许 full_code；selection=false 时也支持 initial、prefix |
| `scope` | `"chinese"` | all/ascii/chinese/unicode/private_use，或字符/区间声明表 |
| `fallback` | `false` | 仅在此前普通 source 未识别该字素时参与 |
| `groups` | 无 | 核心的编码组映射；同一编码不能既引用组又附加选键，通常先关闭 selection |

keys 第 1、2、3…项对应按权重排列的候选；数量不足的候选仍只有裸码。
候选按 weight 降序、order 升序、文字排序。缺失 weight 用 0，缺失 order 用读取顺序。
编码必须包含 ASCII 字母才参与选键，标点等不含字母的编码不附加选键。
排名来自静态码表，不同步输入法的动态词频。所有选键都可省略。

不支持 scheme、selection_keys、force、punctuation、selection.force、
selection.first_omit_before，也不支持 append_space_below（即使 selection=false）。

## 覆盖码表

| 选项 | 默认值 | 支持内容 |
| --- | --- | --- |
| `file` | 内置 tiger.tsv | 外部词典；若保留选键，需要正确的候选权重和顺序 |
| `data` | 无覆盖 | 少量字素到编码字符串/数组，必须 selection=false |
| `lua` | 无覆盖 | Lua 码表文件，必须 selection=false |
| `tsv` | 无 | 仅与 lua 一起使用的完整 TSV 伴随表；独立 TSV 用 file |

覆盖是替换，不是追加；包括标点也由覆盖表提供。file 不能同时配 data、lua、tsv。
内置 TSV 默认按 text/code/weight/order 四列读取；外部 file 使用自动识别/文件声明的列，
或由 columns 指定。启用选键时应提供权重列，否则候选按读取顺序排列。
非中文条目应同时调整 scope。

```lua
{
  name = "tiger",
  file = "/path/to/tiger.dict.yaml",
  selection = { keys = { " ", ";" } },
}
```

使用 converter 时，必须同时指定 file 并关闭选键：

```lua
{
  name = "tiger",
  file = "/path/to/custom.tsv",
  selection = false,
  converter = "/path/to/converter.lua",
}
```

## 外部文件读取选项

以下选项只用于 `file`：

| 选项 | 默认值 | 支持内容 |
| --- | --- | --- |
| `format` | `"auto"` | auto、rime、tsv/tab、csv、space、fcitx、ibus |
| `columns` | 文件声明或格式默认列序 | 列名数组，必须含 text、code；可含 weight、order，其他列忽略 |
| `encoding` | UTF-8 | Neovim 支持的文件编码，例如 gb18030、utf-16le |
| `header` | `false` | CSV 首条记录是否为标题；不用于 TSV |
| `converter` | 无 | 返回编码数组转换函数的 Lua 文件路径；返回 nil/空数组可移除条目 |

无头 TSV 默认文字在前、编码在后；反向列序设置 `columns = { "code", "text" }`。
每行一个编码，多编码重复写行，逗号是编码本身的一部分。Rime 可读取相对路径的导入表。
文件中的多字素条目会被过滤；直接 data/Lua 表要求每个键恰好一个完整字素。
converter 只在构建时运行，不是运行时 matcher。

完整格式规则、scope 声明与编码组语义见[核心参考](https://github.com/dirichy/flash-any.nvim/blob/main/docs/sources.md)。
