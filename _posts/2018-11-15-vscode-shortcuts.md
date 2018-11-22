---
title: "Shortcuts for VSCode"
date: 2018-10-19T
header:
    overlay_image: https://code.visualstudio.com/assets/docs/editor/multi-root-workspaces/hero.png
    teaser: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Visual_Studio_Code_1.18_icon.svg/1200px-Visual_Studio_Code_1.18_icon.svg.png
    og_image: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Visual_Studio_Code_1.18_icon.svg/1200px-Visual_Studio_Code_1.18_icon.svg.png
    overlay_filter: 0.8
    caption: "Image credit: [**VSCode**](https://code.visualstudio.com)"
    actions:
        - label: "Learn More"
          url: "https://code.visualstudio.com/"
excerpt: "Shortcuts Overview when working with VSCode."
categories:
    - Programming
tags:
    - VSCode
    - Shortcuts
---


**Notice!** This page is still in progress!
{: .notice--primary}


This overview is intended to give a short overview on the most important shortcuts for working with [Visual Studio Code](https://code.visualstudio.com/) (*VSCode*).
I won't include all of the shortcuts but the most important ones, well at least in my opinion.

I will start with the basic *VSCode* shortcuts and then give some shortcuts examples when working with specific file formats like *HTML* or *Markdown*.

## Basic Shortcuts

In every text and code editor there are certain tasks which are basically the same for everyone of them.
This includes file managament, navigation, display options or editor management.

### General

| Windows            | MacOS     | Linux              | Description                  |
| ------------------ | --------- | ------------------ | ---------------------------- |
| `Ctrl+Shift+P, F1` | `⇧⌘P, F1` | `Ctrl+Shift+P, F1` | Show command palette         |
| `Ctrl+P`           | `⌘P`      | `Ctrl+P`           | Quick open                   |
| `Ctrl+Shift+N`     | `⇧⌘N`     | `Ctrl+Shift+N`     | New window/instance          |
| `Ctrl+Shift+W`     | `⌘W`      | `Ctrl+Shift+W`     | Close window/instance        |
| `Ctrl+,`           | `⌘`       | `Ctrl+,`           | Open user settings           |
| `Ctrl+K Ctrl+S`    | `⌘K ⌘S`   | `Ctrl+K Ctrl+S`    | Open user keyboard shortcuts |

### Editing

| Windows            | MacOS         | Linux              | Description                     |
| ------------------ | ------------- | ------------------ | ------------------------------- |
| `Ctrl+X`           | `⌘X`          | `Ctrl+T`           | Cut                             |
| `Ctrl+C`           | `⌘C`          | `Ctrl+T`           | Copy                            |
| `Ctrl+A`           | `⌘A`          | `Ctrl+A`           | Select all                      |
| `Alt+`             | `⌥▲/⌥▼`       | `Alt+`             | Move line up/down               |
| `Shift+Alt+`       | `⇧⌥▲/⇧⌥▼`     | `Shift+Alt+`       | Copy line up/down               |
| `Ctrl+Shift+K`     | `⇧⌘K`         | `Ctrl+Shift+K`     | Delete line                     |
| `Ctrl+Enter`       | `⌘Enter`      | `Ctrl+Enter`       | Insert line below               |
| `Ctrl+Shift+Enter` | `⇧⌘Enter`     | `Ctrl+Shift+Enter` | Insert line above               |
| `Home/End`         | `⌘◀︎/⌘▶︎`     | `Home/End`         | Go to beginning/end of the line |
| `Ctrl+Home/End`    | `⌘▲/⌘▼`       | `Ctrl+Home/End`    | Go to beginning/end of the file |
| `Ctrl+`            | `^PgUp/^PgDn` | `Ctrl+`            | Scroll line up/down             |
| `Ctrl+PgUp/PgDn`   | `⌘PgUp/⌘PgDn` | `Ctrl+PgUp/PgDn`   | Scroll page up/down             |
| `Ctrl+K Ctrl+C`    | `⌘K ⌘C`       | `Ctrl+K Ctrl+C`    | Add line comment                |
| `Ctrl+K Ctrl+U`    | `⌘K ⌘U`       | `Ctrl+K Ctrl+U`    | Remove line comment             |
| `Shift+Alt+A`      | `⇧⌥A`         | `Shift+Alt+A`      | Toggle block comment            |
| `Alt+Z`            | `⌥Z`          | `Alt+Z`            | Toggle word wrap                |

### File Management

| Windows          | MacOS   | Linux            | Description                             |
| ---------------- | ------- | ---------------- | --------------------------------------- |
| `Ctrl+O`         | `⌘O`    | `Ctrl+O`         | Open file                               |
| `Ctrl+N`         | `⌘N`    | `Ctrl+N`         | New file                                |
| `Ctrl+S`         | `⌘S`    | `Ctrl+S`         | Save file                               |
| `Ctrl+Shift+S`   | `⇧⌘S`   | `Ctrl+Shift+S`   | Save file as                            |
| `Ctrl+K S`       | `⌥⌘S`   | `Ctrl+K S`       | Save all                                |
| `Ctrl+F4`        | `⌘W`    | `Ctrl+F4`        | Close                                   |
| `Ctrl+K Ctrl+W`  | `⌘K ⌘W` | `Ctrl+K Ctrl+W`  | Close all                               |
| `Ctrl+Shift+T`   | `⇧⌘T`   | `Ctrl+Shift+T`   | Reopen closed editor                    |
| `Ctrl+Tab`       | `^Tab`  | `Ctrl+Tab`       | Open next file                          |
| `Ctrl+Shift+Tab` | `⇧Tab`  | `Ctrl+Shift+Tab` | Open previouse file                     |
| `Ctrl+K P`       | `⌘K P`  | `Ctrl+K P`       | Copy path of active file                |
| `Ctrl+K R`       | `⌘K R`  | `Ctrl+K R`       | Reveal open file in Explorer            |
| `Ctrl+K O`       | `⌘K O`  | `Ctrl+K O`       | Show active file in new window/instance |

### Rich Language Support

| Windows            | MacOS     | Linux              | Description                 |
| ------------------ | --------- | ------------------ | --------------------------- |
| `Ctrl+Space`       | `^Space`  | `Ctrl+Space`       | Trigger suggestion          |
| `Ctrl+Shift+Space` | `⇧⌘Space` | `Ctrl+Shift+Space` | Trigger parameter hints     |
| `F12`              | `F12`     | `F12`              | Go to definition            |
| `Alt+F12`          | `⌥F12`    | `Ctrl+Shift+F10`   | Peek definition             |
| `Ctrl+K F12`       | `⌘K F12`  | `Ctrl+K F12`       | Open definition on the side |
| `Shift+F12`        | `⇧F12`    | `Shift+F12`        | Open definition on the side |
|                    | `^⌘Space` |                    | Insert emojis & symbols     |

### Navigation

| Windows        | MacOS                       | Linux          | Description                        |
| -------------- | --------------------------- | -------------- | ---------------------------------- |
| `Ctrl+T`       | `⌘T`                        | `Ctrl+T`       | Show all symbols                   |
| `Ctrl+G`       | `^G`                        | `Ctrl+G`       | Go to line                         |
| `Ctrl+P`       | `⌘P`                        | `Ctrl+P`       | Go to file                         |
| `Ctrl+Shift+O` | `⇧⌘O`                       | `Ctrl+Shift+O` | Go to symbol                       |
| `Ctrl+Shift+M` | `^⇧M`                       | `Ctrl+Shift+M` | Show problem panel                 |
| `F8/Shift+F8`  | `F8/⇧F8`                    | `F8/Shift+F8`  | Go to next/previouse error warning |
| `Alt+←/Alt+→`  | `⌥◀/⌥▶︎`                    |                | Go backward/forward                |
| `⌘▲/⌘▼`        | Scroll up/Scroll down       |
| `⌘◀︎/⌘▶︎`      | Go to start/end of the line |


### Editor Management

### Display

| Windows        | MacOS  | Linux          | Description             |
| -------------- | ------ | -------------- | ----------------------- |
| `F11`          | `^⌘F`  | `F11`          | Toggle fullscreen       |
| `Ctrl+Shift+G` | `^⇧G`  | `Ctrl+Shift+G` | Open Git/source control |
| `Ctrl+Sift+E`  | `⇧⌘E`  | `Ctrl+Sift+E`  | Show explorer           |
| `Ctrl+Shift+H` | `⇧⌘H`  | `Ctrl+Shift+H` | Show search & replace   |
| `Ctrl+Shift+D` | `⇧⌘D`  | `Ctrl+Shift+D` | Show debug              |
| `Ctrl+Shift+X` | `⇧⌘X`  | `Ctrl+Shift+X` | Show extensions         |
| `Ctrl+Shift+U` | `⇧⌘U`  | `Ctrl+Shift+U` | Open ouput panel        |
| `Ctrl+K Z`     | `⌘K Z` | `Ctrl+K Z`     | Toggle Zen mode         |



### Integrated Terminal

| Shortcut | Description         |
| -------- | ------------------- |
| `^⇧´`    | Create new terminal |

## Markdown

This section refers to working with *Markdown* and the awesome [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) extension.

| Windows        | MacOS  | Linux          | Description                                    |
| -------------- | ------ | -------------- | ---------------------------------------------- |
| `Ctrl+Shift+F` | `⇧⌘V`  | `Ctrl+Shift+F` | Open Markdown preview                          |
| `Ctrl+K V`     | `⌘K V` | `Ctrl+K V`     | Open Markdown preview on the side              |
| `Ctrl+B`       | `⌘B`   | `Ctrl+B`       | Toggle `**bolt**` => **bolt**                  |
| `Ctrl+I`       | `⌘I`   | `Ctrl+I`       | Toggle `*italic*` => *italic*                  |
| `Ctrl+M`       | `⌘I`   | `Ctrl+M`       | Toggle math environment `$E=mc^2$` => $E=mc^2$ |
| `Alt+S`        | `⌘I`   | `Alt+S`        | Toggle strikethrough `~~word~~` => ~~word~~    |
| `Alt+Shift+F`  | `⇧⌥F`  | `Alt+Shift+F`  | Table formatter                                |

### List editing

![](https://github.com/neilsustc/vscode-markdown/raw/master/images/gifs/on-enter-key1.gif)

![](https://github.com/neilsustc/vscode-markdown/raw/master/images/gifs/on-enter-key2.gif)

![](https://github.com/neilsustc/vscode-markdown/raw/master/images/gifs/on-tab-key.gif)

![](https://github.com/neilsustc/vscode-markdown/raw/master/images/gifs/on-backspace-key.gif)

![](https://github.com/neilsustc/vscode-markdown/raw/master/images/gifs/marker-fixing.gif)

There are also some useful command like for example automatically create a table of contents. 
Just press `Ctrl+Shift+P` respectifely `⇧⌘P` and by start typing `Markdown` the following entries should pop up:

* *Markdown: Create Table of Contents*
* *Markdown: Update Table of Contents*
* *Markdown: Toggle code span*
* *Markdown: Print current document to HTML*
* *Markdown: Toggle math environment*
* *Markdown: Toggle unordered list*

**Tip!** Adam Pritchard has created a nice [Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#emphasis) regarding common Markdown tasks.
{: .notice--primary}

## References

* [VS Shortcuts for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
* [VS Shortcuts for MacOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
* [VS Shortcuts for Linux](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)