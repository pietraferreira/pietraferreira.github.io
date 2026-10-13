---
title: "Retroma Callouts Cheatsheet"
tags:
  - cheatsheet
  - obsidian
created: 2026-08-25
type: cheatsheet
---
# Retroma Callouts Cheatsheet

> [!nav]
> [[cheatsheets-hub|Cheatsheets]]

Every callout the **Retroma** theme (v3.1.1) defines, read straight from `.obsidian/themes/Retroma/theme.css`. **79 retro types** plus the 27 standard Obsidian ones.

> [!warning] These only render while Retroma is the active theme
> They are theme-provided, not vault-provided. Switch to Things or Minimal and every one of these falls back to a plain callout. The text is never lost.

## Syntax

```markdown
> [!polaroid-1] Title goes here
> Body text.
```

**Sizes** — every retro callout takes `-s`, `-m` or `-l`. No suffix uses the theme default.

```markdown
> [!cassette-1-s] Small
> [!cassette-1-m] Medium
> [!cassette-1-l] Large
```

**Folding** — standard Obsidian modifiers work throughout. `+` starts expanded, `-` starts collapsed.

```markdown
> [!blueprint]- Collapsed by default
> Hidden until clicked.
```

**No title** — omit the title and the header bar disappears.

```markdown
> [!polaroid-2]
> Just the frame, no caption.
```

---

## Live examples

Switch this note to Reading view to see these render.

> [!polaroid-1] Summer 1987
> A polaroid frame with a caption strip.

> [!cassette-1-m] Mixtape Vol. 1
> Side A. Medium size.

> [!terminal] boot.log
> `> SYSTEM READY`

> [!stickynote-yellow] Don't forget
> Sticky notes come in seven colours.

> [!blueprint-l] Assembly drawing
> Large blueprint, for diagrams and schematics.

> [!receipt-1] TOTAL — 12.40
> Receipt styling, right down to the perforation.

---

## Photo & film

*8 types — all accept `-s` / `-m` / `-l`.*

|  |  |  |  |
|---|---|---|---|
| `film` | `filmstrip` | `negative` | `photoalbum` |
| `photomount` | `photoslide` | `polaroid-1` | `polaroid-2` |

## Media & hardware

*21 types — all accept `-s` / `-m` / `-l`.*

|  |  |  |  |
|---|---|---|---|
| `arcademarquee` | `calculator` | `cassette-1` | `cassette-2` |
| `eurorack` | `floppy` | `highscore` | `marquee` |
| `matrixstream` | `pager-1` | `pager-2` | `pagerunit` |
| `pcbboard` | `punchedtape` | `radio` | `reeltoreel` |
| `tamagotchi` | `terminal` | `transistor` | `vinyl` |
| `walkietalkie` |  |  |  |

## Office & stationery

*28 types — all accept `-s` / `-m` / `-l`.*

|  |  |  |  |
|---|---|---|---|
| `artpostcard` | `clipboard` | `dailycalendar` | `duedate` |
| `filingtab` | `graphmemo` | `gridnotebook` | `indexcard` |
| `indextab` | `kraftpaper` | `krafttag` | `legalpad` |
| `library` | `luggagetag` | `mailbox` | `matchbook` |
| `museumtag` | `news` | `notepad` | `postcard-1` |
| `postcard-2` | `receipt-1` | `receipt-2` | `scrapbook` |
| `ticketstub` | `toploader` | `touristcard` | `visastamp` |

## Sticky notes

*7 types — all accept `-s` / `-m` / `-l`.*

|  |  |  |  |
|---|---|---|---|
| `stickynote-blue` | `stickynote-green` | `stickynote-indigo` | `stickynote-orange` |
| `stickynote-red` | `stickynote-violet` | `stickynote-yellow` |  |

## Academics & journaling

*10 types — all accept `-s` / `-m` / `-l`.*

|  |  |  |  |
|---|---|---|---|
| `blueprint` | `chalkboard` | `compbook` | `fieldnote` |
| `flashcard` | `inspection` | `labnotebook` | `librarycard` |
| `ruler` | `typewriter` |  |  |

## Vintage & tactile paper

*4 types — all accept `-s` / `-m` / `-l`.*

|  |  |  |  |
|---|---|---|---|
| `cardboard-cutout-shape` | `passport-stamp` | `typewriter-page` | `vintage-ticket` |

---

## Standard Obsidian callouts

Retroma restyles these too, and they keep working under any theme:

| | | | |
|---|---|---|---|
| `note` | `abstract` | `summary` | `tldr` |
| `info` | `todo` | `tip` | `hint` |
| `important` | `success` | `check` | `done` |
| `question` | `help` | `faq` | `warning` |
| `caution` | `attention` | `failure` | `fail` |
| `missing` | `danger` | `error` | `bug` |
| `example` | `quote` | `cite` | |

## Vault-specific

`nav` is **ours**, not Retroma's — defined in `.obsidian/snippets/nav-buttons.css`. It renders its links as a row of pill buttons and is what every note's footer uses.

```markdown
> [!nav]
> [[cs-hub|Computer Science]]
```

> [!info] One thing to know
> `readability.css` restyles callouts, but only the 27 standard types listed above — explicitly, by name. That is deliberate: a blanket rule would flatten all 79 retro designs, since snippets load after the theme and win on equal specificity.

## Source

- Theme: [emarpiee/Retroma](https://github.com/emarpiee/Retroma)
- Upstream examples: [retroma-retro-callouts.md](https://github.com/emarpiee/Retroma/blob/main/assets/examples/retroma-retro-callouts.md)

> [!nav]
> [[cheatsheets-hub|Cheatsheets]]
