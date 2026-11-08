# 虎码配置示例

[English](options.en.md) · [返回主页](../README.md)

通常只需启用 tiger；选键配置与匹配方式如下。

| 选项 | 默认值 | 用途 |
| --- | --- | --- |
| `selection` | 启用 | false 关闭选键，表可设置 keys |
| `selection.keys` | `{ " ", ";" }` | 依次分配给首选、次选等候选，始终可省略 |
| `matcher` | full_code | 启用选键时保持 full_code；关闭选键后也可使用 initial、prefix |

## 默认配置

```lua
opts = { sources = { "tiger" } }
```

首选键为空格、次选键为分号，没有默认三选键。裸码仍匹配所有同码候选。
例如 gch 匹配同码候选，gch; 可匹配二选“羔”。

## 增加三选键

```lua
opts = {
  sources = {
    { name = "tiger", selection = { keys = { " ", ";", "'" } } },
  },
}
```

列表依次对应候选排名。每项须为一个 ASCII 标点，只有首项可以是空格；
列表不能为空，按键不能重复。未分配选键的候选仍支持裸码。
顺序由随包码表的静态权重决定，不随输入法动态词频变化。

## 关闭选键

```lua
opts = { sources = { { name = "tiger", selection = false } } }
```

## 允许前缀推进

```lua
opts = {
  sources = {
    { name = "tiger", selection = false, matcher = "prefix" },
  },
}
```

默认 full_code 需要完整编码才能继续匹配下一字；关闭选键后可改为 prefix，
允许任意非空编码前缀推进，也可设 initial，只用首字母或完整码推进。
