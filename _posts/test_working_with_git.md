---
title: "Working with Git"
date: 2019-04-03T
header:
    overlay_image: https://code.visualstudio.com/assets/docs/editor/multi-root-workspaces/hero.png
    teaser: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Visual_Studio_Code_1.18_icon.svg/1200px-Visual_Studio_Code_1.18_icon.svg.png
    og_image: https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Visual_Studio_Code_1.18_icon.svg/1200px-Visual_Studio_Code_1.18_icon.svg.png
    overlay_filter: 0.8
    caption: "Image credit: [**VSCode**](https://code.visualstudio.com)"
    actions:
        - label: "Learn More"
          url: "https://code.visualstudio.com/"
excerpt: "A short overview of the most important git commands as well as coomon workflow operations."
categories:
    - Programming
tags:
    - Git
---

**Notice!** This page is still in progress!
{: .notice--primary}

## Overview on commands

| Command                                      | Meaning                                                      |
| -------------------------------------------- | ------------------------------------------------------------ |
| `git init`                                   | Initialize empty repository                                  |
| `git add filename`                           | Add file to staging area                                     |
| `git add .`                                  | Add all files to staging area                                |
| `git add -p`                                 | Add files to staging area + view changes                     |
| `git commit -m message`                      | Commit change and add a message regarding the change         |
| `git reset`                                  | Unstage changes                                              |
| `git reset -p`                               | Unstage changes + view which files are being unstaged        |
| `git reset --hard number`                    | Hard reset to last commit *number*                           |
| `git push -u origin`                         | Push branch to origin                                        |
| `git pull`                                   | Clone and merge current branch with master branch            |
| `git clone repository_url`                   | Clone repository to currently selected path                  |
| `git status`                                 | Check status                                                 |
| `git checkout -b branchname`                 | Create new branch named *branchname*                         |
| `git checkout master`                        | Go to master branch                                          |
| `git merge branchname`                       | Merge *branchname* with master                               |
| `git merge --abort`                          | Abort merge attempt                                          |
| `git log --oneline --decorate --all --graph` | Show some informations regarding current branch and statuses |