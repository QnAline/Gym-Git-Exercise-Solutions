# Gym-Git-Exercise-Solutions
## Bundle Exercise 1
<!-- RENAMING MASTER TO MAIN BRANCH -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 ~
$ git config --global init.default branch main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /c/Users/pproject/PROJECT (main)
$ git branch
* main
* 
<!--Adding files , renaming and editing them as well as committing them  -->

<!-- Adding files -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git add --all
<!-- Renaming files -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git mv activate.css Activate.css

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git mv logo.jpeg Logo.jpeg

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git mv setting.webp Setting.webp

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git commit -m " Changing all file names to start with a capital letter"
[main 493b0d8]  Changing all file names to start with a capital letter
 3 files changed, 0 insertions(+), 0 deletions(-)
 rename activate.css => Activate.css (100%)
 rename logo.jpeg => Logo.jpeg (100%)
 rename setting.webp => Setting.webp (100%)
 
<!-- Editing files  -->
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
 $ git status
 On branch main
 Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git restore <file>..." to discard changes in working directory)
         modified:   Guessgame.py
 
 no changes added to commit (use "git add" and/or "git commit -a")
 
<!-- PUSHING CHANGES TO GITHUB CREATED  -->
   LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git remote add origin https://github.com/QnAline/GITPR.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch -M main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git push -u origin main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 4 threads
Compressing objects: 100% (17/17), done.
Writing objects: 100% (17/17), 32.75 KiB | 1.64 MiB/s, done.
Total 17 (delta 5), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (5/5), done.
To https://github.com/QnAline/GITPR.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

<!--creating branch dev and in dev creating another branch test and then deleting it from dev branch-->
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch dev

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch
  dev
* main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git switch dev
Switched to branch 'dev'
M       Guessgame.py

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git branch test

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git branch
* dev
  main
  test

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git branch -d test
Deleted branch test (was 493b0d8).

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git branch
* dev
  main

 
 
 
 
 
