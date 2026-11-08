# Tiger configuration examples

[简体中文](options.md) · [README](../README.en.md)

The default tiger configuration works on its own. User settings are selectors and
matching behavior:

| Option | Default | Purpose |
| --- | --- | --- |
| `selection` | Enabled | false disables selectors; a table configures keys |
| `selection.keys` | `{ " ", ";" }` | Assigned in candidate order; always optional |
| `matcher` | full_code | Keep full_code with selectors; initial/prefix are available when selectors are disabled |

## Defaults

```lua
opts = { sources = { "tiger" } }
```

Space is the first selector, semicolon the second; no third selector is assigned.
Bare codes still match all candidates. For example, gch matches every candidate for
that code, while gch; matches the second candidate “羔”.

## Add a third selector

```lua
opts = {
  sources = {
    { name = "tiger", selection = { keys = { " ", ";", "'" } } },
  },
}
```

The list follows candidate ranking. Each item must be one ASCII punctuation character;
only the first may be Space. The list must be nonempty and keys distinct. Candidates
without assigned keys retain bare codes. Ranking uses the bundled dictionary's
static weights and does not follow an input method's dynamic frequency.

## Disable selectors

```lua
opts = { sources = { { name = "tiger", selection = false } } }
```

## Allow prefix matching

```lua
opts = {
  sources = {
    { name = "tiger", selection = false, matcher = "prefix" },
  },
}
```

The default full_code mode requires a complete code to advance to the next character.
With selectors disabled, prefix allows any nonempty prefix to advance; initial
allows the first letter or the complete code.
