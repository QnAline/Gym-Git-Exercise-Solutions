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
 
 ##BUNDLE 1 EXERCISES 1
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
 
 ## BUNDLE 2 EXERCICES 2
<!-- TO CHECKOUT MAIN  AND PULL LAST CHANGES  -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git pull origin main
From https://github.com/QnAline/Gym-Git-Exercise-Solutions
 * branch            main       -> FETCH_HEAD
   493b0d8..28c047b  main       -> origin/main
Updating 493b0d8..28c047b
Fast-forward
 Guessgame.py  |   2 +-
 README.md     | 299 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 about.html    |  18 ++++
 home.html     |  39 ++++++++
 services.html |  18 ++++
 5 files changed, 375 insertions(+), 1 deletion(-)
 create mode 100644 README.md
 create mode 100644 about.html
 create mode 100644 home.html
 create mode 100644 services.html

<!-- NEW BRANCH ft/service-redesign  -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch ft/service-redesign

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch
  dev
  ft/bundle-2
  ft/service-redesign
* main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git switch ft/service-redesign
Switched to branch 'ft/service-redesign'

<!-- NEW CHANGES TO services.html  -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git switch ft/service-redesign
Switched to branch 'ft/service-redesign'

$ git status
On branch ft/service-redesign
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   services.html

no changes added to commit (use "git add" and/or "git commit -a")
 
<!-- COMMITTING AND PUSHING THEM  -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git add --all

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git commit -m " committing changes to services.html"
[ft/service-redesign 39b274d]  committing changes to services.html
 1 file changed, 8 insertions(+)


LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git push --set-upstream origin ft/service-redesign
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 317 bytes | 63.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'ft/service-redesign' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/ft/service-redesign
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      ft/service-redesign -> ft/service-redesign
branch 'ft/service-redesign' set up to track 'origin/ft/service-redesign'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git push -u origin ft/service-redesign
Everything up-to-date
branch 'ft/service-redesign' set up to track 'origin/ft/service-redesign'.


LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git status
On branch ft/service-redesign
Your branch is up to date with 'origin/ft/service-redesign'.

nothing to commit, working tree clean
 
<!-- NEW CHANGES TO service.html IN MAIN BRANCH -->

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   services.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git add --all

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git commit -m " Changing againservice to html in this main branch"
[main 5917e4b]  Changing againservice to html in this main branch
 1 file changed, 1 insertion(+), 1 deletion(-)

<!-- COMMITTING AND PUSHING AGAIN THOSE CHANGES IN MAIN  -->

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git remote set-url https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
usage: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    --push                manipulate push URLs
    --add                 add URL
    --delete              delete URLs


LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git push -u --set-upstream origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 323 bytes | 323.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
   28c047b..5917e4b  main -> main
branch 'main' set up to track 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

<!--CHECKOUT ft/service-redesign branch  -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git diff ft/service-redesign..main
diff --git a/services.html b/services.html
index 8ecade9..2cd434c 100644
--- a/services.html
+++ b/services.html
@@ -7,13 +7,12 @@
     </head>
     <body>
         <p>
             changing dolor sit amet consectetur adipisicing elit.<br>
          
-            NEW CHANGES ipsum dolor sit amet consectetur adipisicing elit.<br>
   
+            changing dolor sit amet consectetur adipisicing elit.<br>
              Nesciunt beatae recusandae esse voluptatem repellat labore assumenda,<br>
               possimus corrupti nostrum. Cum nihil similique magnam soluta,<br>
                ad aut vero consequatur veniam iste sunt autem tempore illum dolor<br>
                 est officiis voluptas commodi quam nulla, id amet dolorem distinctio fugiat. <br>
                 Itaque provident natus odit.
         </p>
-
     </body>
 </html>
\ No newline at end of file


<!-- merge the main branch with ft/service-redesign branch and commit and push CHANGES AGAIN  -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git merge main
Auto-merging services.html
CONFLICT (content): Merge conflict in services.html
Automatic merge failed; fix conflicts and then commit the result.

$ git status
On branch ft/service-redesign
Your branch is ahead of 'origin/ft/service-redesign' by 1 commit.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   services.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign|MERGING)
$ git status
On branch ft/service-redesign
Your branch is ahead of 'origin/ft/service-redesign' by 1 commit.
  (use "git push" to publish your local commits)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   services.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .services.html.swp
        .services_BASE_2118.html.swp
        .services_LOCAL_2118.html.swp
        .services_REMOTE_2118.html.swp
        services_BACKUP_2118.html
        services_BASE_2118.html
        services_LOCAL_2118.html
        services_REMOTE_2118.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign|MERGING)
$ git reset
Unstaged changes after reset:
M       services.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git add -p
diff --git a/services.html b/services.html
index 8ecade9..4150f5a 100644
--- a/services.html
+++ b/services.html
@@ -7,7 +7,11 @@
     </head>
     <body>
         <p>
+<<<<<<< HEAD
             NEW CHANGES ipsum dolor sit amet consectetur adipisicing elit.<br>
+=======
+            changing dolor sit amet consectetur adipisicing elit.<br>
+>>>>>>> main
              Nesciunt beatae recusandae esse voluptatem repellat labore assumenda,<b
r>
               possimus corrupti nostrum. Cum nihil similique magnam soluta,<br>
                ad aut vero consequatur veniam iste sunt autem tempore illum dolor<br
>
(1/1) Stage this hunk [y,n,q,a,d,s,e,?]?

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/service-redesign)
$ git merge main
Auto-merging services.html
CONFLICT (content): Merge conflict in services.html
Automatic merge failed; fix conflicts and then commit the result.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/service-redesign|MERGING)
$ git commit -a -m "Updated services.html"
[ft/service-redesign 66b70b1] Updated services.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/service-redesign)
$ git push --set-upstream origin ft/service-redesign
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 4 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 980 bytes | 980.00 KiB/s, done.
Total 10 (delta 7), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (7/7), completed with 2 local objects.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
   39b274d..66b70b1  ft/service-redesign -> ft/service-redesign
branch 'ft/service-redesign' set up to track 'origin/ft/service-redesign'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/service-redesign)
$ git status
On branch ft/service-redesign
Your branch is up to date with 'origin/ft/service-redesign'.

nothing to commit, working tree clean






 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
