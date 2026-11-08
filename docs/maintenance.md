# Maintaining a code-table package / 维护码表包

This document is for contributors; installing and using the package does not require
editing its dictionary or recording a demo.
本文面向维护者；普通用户无需修改码表或安装录制工具。

## Dictionary / 码表

Tiger TSV columns are grapheme, code, weight and original order, separated by Tabs.
Repeat rows for multiple codes; commas in codes are literal. Other formats, column order, converters,
and optional weights are documented in [source configuration](https://github.com/dirichy/flash-any.nvim/blob/main/docs/sources.md).
虎码 TSV 四列为字素、编码、权重、原始顺序，以 Tab 分隔；多编码重复写行，逗号原样保留。
其他文件格式、列顺序、编码转换及可选权重见上述 source 文档。

Record the upstream source and license in THIRD_PARTY.md when updating the dictionary.
更新时在 THIRD_PARTY.md 中记录上游来源与许可。

To regenerate the table / 重新生成码表：

```sh
python scripts/build.py tiger.dict.yaml lua/flash-any/tables/tiger.tsv
```

Python is needed only for this maintenance command, not installation.
Python 仅用于上述维护命令，不是安装依赖。

Selection suffixes use static weights and original order. Punctuation entries do not
receive selection keys. See the source configuration above for matching semantics.
选键按静态权重和原始顺序分配，标点条目不附加选键；详细匹配规则见上述 source 文档。

## Demo / 演示

Copy flash-any's [workflow template](https://github.com/dirichy/flash-any.nvim/blob/main/demos/templates/table-demo.yml)
to .github/workflows/demo.yml and its commented [Lua config](https://github.com/dirichy/flash-any.nvim/blob/main/demos/templates/table-demo.lua)
to demo.lua. Set the dictionary path and familiar target text, edit both narration
comments, and use `config: demo.lua` in the workflow. Optional `sample` loads your own
short sample file. Codes come from the table automatically.
复制上述工作流模板和带注释的 Lua 配置，填写码表路径、熟悉的目标文字、两段旁白；
工作流用 `config: demo.lua` 指向配置。可用 `sample` 指定简短样本文件，编码自动从码表推导。

Pin the workflow reference and flash-any-ref to the same tested core commit.
Run the workflow manually, inspect the uploaded GIF/MP4 and verification report,
then copy the chosen GIF to docs/table.gif. The reusable workflow uploads artifacts;
it does not publish a release or change this repository.
将工作流引用和 flash-any-ref 固定到同一已测试核心提交。手动录制后检查画面与验证报告，
将选用的 GIF 放到 docs/table.gif；可复用工作流只上传 artifact，不自动发布或修改仓库。

For local commands, dependencies, font coverage and playback checks, see the
[recording guide](https://github.com/dirichy/flash-any.nvim/blob/main/demos/README.md).
本地命令、录制依赖、字体覆盖与回放验证见上述录制说明。

The currently published recording is [this Actions run](https://github.com/dirichy/flash-any-tiger.nvim/actions/runs/42483049458).
Download its [HD MP4](https://github.com/dirichy/flash-any-tiger.nvim/releases/download/demos/table.mp4).
The Lua-config workflow described above requires a core revision containing that interface;
the previously published workflow still uses the earlier recording configuration.
当前已发布演示和高清 MP4 见上述链接。本文的 Lua 配置流程需要包含该接口的核心版本；
此前已发布的工作流仍使用旧录制配置，尚未随本地文档更新。
