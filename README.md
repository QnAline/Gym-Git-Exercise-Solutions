# Gym-Git-Exercise-Solutions
## Bundle 1 Exercise 1
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
 
 ## BUNDLE 1 EXERCISES 2
<!-- CREATING HOME PAGE AND ADDING SOME CHANGES  -->
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git status
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Guessgame.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        home.html

no changes added to commit (use "git add" and/or "git commit -a")
 
<!-- STASHING HOME PAGE CURRENT CHANGES  -->
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git stash -u
Saved working directory and index state WIP on dev: 493b0d8  Changing all file n
ames to start with a capital letter
 
<!--  CREATING ABOUT PAGE AND STASHING CURRENT CHANGES -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git status
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        about.html

nothing added to commit but untracked files present (use "git add" to track)

$ git stash -u
Saved working directory and index state WIP on dev: 493b0d8  Changing all file n
ames to start with a capital letter
 
<!-- CREATING AND STASHING TEAM PAGE CURRENT CHANGES  -->
$ git status
On branch dev
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        team.html

nothing added to commit but untracked files present (use "git add" to track)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git stash -u
Saved working directory and index state WIP on dev: 493b0d8  Changing all file n
ames to start with a capital letter

<!--  STASH LIST-->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git stash list
stash@{0}: WIP on dev: 493b0d8 Changing all file names to start with a capital l
etter
stash@{1}: WIP on dev: 493b0d8 Changing all file names to start with a capital l
etter
stash@{2}: WIP on dev: 493b0d8 Changing all file names to start with a capital l
etter
stash@{3}: WIP on dev: 493b0d8 Changing all file names to start with a capital l
etter



<!-- STASH POP RESTORE TO ABOUT PAGE -->
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Guessgame.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
       about.html

no changes added to commit (use "git add" and/or "git commit -a")
Dropped stash@{1} (8f62a82b12554594040886d50ed1bb51507d057f)
 
<!-- USING STASH POP TO BRING BACK HOME.HTML  -->
 On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Guessgame.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        home.html

no changes added to commit (use "git add" and/or "git commit -a")
Dropped stash@{2}

<!--COMMITTING CURRENT CHANGES AND PUSHINT THEM -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git status
On branch dev
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   Guessgame.py
        new file:   about.html
        new file:   home.html

$ git commit -m "commiting current changes to home and about page"
[dev 361af3b] commiting current changes to home and about page
 3 files changed, 54 insertions(+), 1 deletion(-)
 create mode 100644 about.html
 create mode 100644 home.html

$ git stash -u
Saved working directory and index state WIP on dev: 361af3b commiting current changes to home and about page

$ git push --set-upstream origin dev
Enumerating objects: 22, done.
Counting objects: 100% (22/22), done.
Delta compression using up to 4 threads
Compressing objects: 100% (22/22), done.
Writing objects: 100% (22/22), 33.73 KiB | 1.77
 MiB/s, done.
Total 22 (delta 7), reused 0 (delta 0), pack-re
used 0
remote: Resolving deltas: 100% (7/7), done.
remote: This repository moved. Please use the n
ew location:
remote:   https://github.com/QnAline/Gym-Git-Ex
ercise-Solutions.git
remote:
remote: Create a pull request for 'dev' on GitH
ub by visiting:
remote:      https://github.com/QnAline/Gym-Git
-Exercise-Solutions/pull/new/dev
remote:
To https://github.com/QnAline/GITPR.git
 * [new branch]      dev -> dev
branch 'dev' set up to track 'origin/dev'.

<!-- stash pop restore the changes of the team page index -->
 
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git stash pop stash@{1}
Already up to date.
On branch dev
Your branch is up to date with 'origin/dev'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        team.html

nothing added to commit but untracked files present (use "git add" to track)
Dropped stash@{1} (c8f7738362efee729491ce93b432815a94a05a43)
 
<!-- Reset the current changes using git reset and go back to the changes without the team page -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (dev)
$ git reset --hard
HEAD is now at 361af3b commiting current changes to home and about page
$ git status
On branch dev
Your branch is up to date with 'origin/dev'.

nothing to commit, working tree clean

 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
