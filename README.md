
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
 
 
 
## BUNDLE 2 EXECICES 1
 
<!--creating branch ft/bundle-2 -->
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch ft/bundle-2 

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git switch ft/bundle-2
Switched to branch 'ft/bundle-2'

 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git status
On branch ft/bundle-2
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   Guessgame.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        services.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git status
On branch ft/bundle-2
Your branch is up to date with 'origin/ft/bundle-2'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   services.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git add --all

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git commit -m " Changing againservice to html in thisft/bundle-2 branch"
[main 5917e4b]  Changing againservice to html in this ft/bundle-2 branch
 1 file changed, 1 insertion(+), 1 deletion(-)

<!-- COMMITTING AND PUSHING AGAIN THOSE CHANGES IN ft/bundle-2  -->

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git remote set-url https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
usage: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    --push                manipulate push URLs
    --add                 add URL
    --delete              delete URLs


LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git push -u --set-upstream origin ft/bundle-2
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 323 bytes | 323.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
   28c047b..5917e4b  ft/bundle-2 -> main
branch 'ft/bundle-2' set up to track 'origin/ft/bundle-2'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/bundle-2)
$ git status
On branch ft/bundle-2
Your branch is up to date with 'origin/ft/bundle-2'.

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
          
          

## BUNDLE 3 EXERCICES 1

          
<!--CREATING NEW BRANCH ft/team-page,team.html committing  -->
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git branch ft/team-page

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git branch
  dev
  ft/bundle-2
* ft/service-redesign
  ft/team-page
  main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/service-redesign)
$ git switch ft/team-page
Switched to branch 'ft/team-page'

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git status
On branch ft/team-page
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        team.html

nothing added to commit but untracked files present (use "git add" to track)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git commit -m " new changes to team.html"
[ft/team-page 50c839b]  new changes to team.html
 1 file changed, 12 insertions(+)
 create mode 100644 team.html
         
<!--   PUSHING AND CREATING AN PR         -->
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git push --set-upstream origin ft/team-page
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 419 bytes | 104.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'ft/team-page' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/ft/team-page
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      ft/team-page -> ft/team-page
branch 'ft/team-page' set up to track 'origin/ft/team-page'.
          
<!--  CHECKOUT MAIN BRANCH          -->
          
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git checkout main
Already on 'main'
Your branch is up to date with 'origin/main'.

<!--    CREATING ft/contact-page BRANCH         -->
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch ft/contact-page

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git branch
  dev
  ft/bundle-2
  ft/contact-page
  ft/service-redesign
  ft/team-page
* main        
 
<!--    IN ft/team-page TAKING LAST COMMIT        -->

$ git switch ft/team-page
Switched to branch 'ft/team-page'
Your branch is up to date with 'origin/ft/team-page'.


LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git log --oneline
50c839b (HEAD -> ft/team-page, origin/ft/team-page)  new changes to team.html
66b70b1 (origin/ft/service-redesign, ft/service-redesign) Updated services.html
d78f73c updated text on service
d84ffac Difficult
5917e4b (origin/main, main, ft/contact-page)  Changing againservice to html in this main branch
ebcda22 Commiting inorder to reach to main
39b274d  committing changes to services.html
28c047b Merge pull request #1 from QnAline/ft/bundle-2
be5675c Merge branch 'main' into ft/bundle-2
05ea163  Making pull request on our services page
361af3b (origin/dev, dev) commiting current changes to home and about page
52d9979 Update README.md
8f4ed68 Update README.md
945a54e Add files via upload
493b0d8  Changing all file names to start with a capital letter
d82d70b updated text for systemactivate.html
4725558 guessgame changed to Guessgame.py
4c2dcd6  Commiting all my files by adding, renaming or editing
386ce90 Create README.md

50c839b          
          
<!--      Checkout ft/contact-page, GIT CHERRY-PICK TO GET LAST COMMIT OF ft/team-page     -->
       
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/team-page)
$ git switch ft/contact-page
Switched to branch 'ft/contact-page'

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git cherry-pick 50c839b
[ft/contact-page 5e56022]  new changes to team.html
 Date: Thu May 18 22:43:02 2023 -0700
 1 file changed, 12 insertions(+)
 create mode 100644 team.html

<!--   ADDING NEW CHANGES TO contact page and commit, push AND CREATING PR     -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git status
On branch ft/contact-page
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        contact.html

nothing added to commit but untracked files present (use "git add" to track)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git add contact.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git commit -m "NEW CHANGES TO THE CONTACT PAGE"
[ft/contact-page 770a629] NEW CHANGES TO THE CONTACT PAGE
 1 file changed, 14 insertions(+)
 create mode 100644 contact.html
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git push --set-upstream origin ft/contact-page
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 885 bytes | 11.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
remote:
remote: Create a pull request for 'ft/contact-page' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/ft
/contact-page
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      ft/contact-page -> ft/contact-page
branch 'ft/contact-page' set up to track 'origin/ft/contact-page'.

  
<!--  IN ft/contact-page CREATING ft/faq-page ,faq.html page ADD CHANGES ,COMMIT AND PUSH THEM     -->
          
 LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git branch ft/faq-page

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/contact-page)
$ git switch ft/faq-page
Switched to branch 'ft/faq-page'

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/faq-page)
$ git status
On branch ft/faq-page
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        faq.html

nothing added to commit but untracked files present (use "git add" to track)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/faq-page)
$ git add faq.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/faq-page)
$ git commit -m " CHANGES TO THE FAQ PAGE"
[ft/faq-page f96d22a]  CHANGES TO THE FAQ PAGE
 1 file changed, 12 insertions(+)
 create mode 100644 faq.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (ft/faq-page)
$ git push --set-upstream origin ft/faq-page
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 473 bytes | 236.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'ft/faq-page' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/ft
/faq-page
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      ft/faq-page -> ft/faq-page
branch 'ft/faq-page' set up to track 'origin/ft/faq-page'.

          
<!--   REVERT LAST CHANGES OF ft/team-page,PUSH AND CREATING AN PR         -->
 
Revert " new changes to team.html"

This reverts commit 50c839b5035cb796b6e64625c420539a56e55d78.

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch ft/faq-page
# Your branch is up to date with 'origin/ft/faq-page'.
#
# Changes to be committed:
#       deleted:    team.html
#
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
.git/COMMIT_EDITMSG [unix] (00:14 19/05/2023)                          1,1 All
"/d/pproject/PROJECT/.git/COMMIT_EDITMSG" [unix] 13L, 370Bm
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git log --oneline
2f86d7a (HEAD -> ft/faq-page) Revert " new changes to team.html"
f96d22a (origin/ft/faq-page)  CHANGES TO THE FAQ PAGE
770a629 (origin/ft/contact-page, ft/contact-page) NEW CHANGES TO THE CONTACT PAG
E
5e56022  new changes to team.html
5917e4b (origin/main, main)  Changing againservice to html in this main branch
28c047b Merge pull request #1 from QnAline/ft/bundle-2
be5675c Merge branch 'main' into ft/bundle-2
05ea163  Making pull request on our services page
361af3b (origin/dev, dev) commiting current changes to home and about page
52d9979 Update README.md
8f4ed68 Update README.md
945a54e Add files via upload
493b0d8  Changing all file names to start with a capital letter
d82d70b updated text for systemactivate.html
4725558 guessgame changed to Guessgame.py
4c2dcd6  Commiting all my files by adding, renaming or editing
386ce90 Create README.md

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git push --set-upstream origin ft/faq-page
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 276 bytes | 276.00 KiB/s, done.
Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
   f96d22a..2f86d7a  ft/faq-page -> ft/faq-page
branch 'ft/faq-page' set up to track 'origin/ft/faq-page'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git push --set-upstream origin ft/faq-page
Everything up-to-date
branch 'ft/faq-page' set up to track 'origin/ft/faq-page'.
          
          
          

## BUNDLE 3 EXERCISES 2 
          
          
          
<!--  IN ft/faq-page CREATING ft/home-page-redesign, IN MAIN I MADE CHANGES, COMMITTED AND PUSHED THEM  -->
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git branch ft/home-page-redesign

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git branch
  dev
  ft/bundle-2
  ft/contact-page
* ft/faq-page
  ft/home-page-redesign
  ft/service-redesign
  ft/team-page
  main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/faq-page)
$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   home.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git add home.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git commit -m " RECHANGING IN HOME.TML "
[main 2992530]  RECHANGING IN HOME.TML
 1 file changed, 1 insertion(+)
          
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/QnAline/Gym-Git-Exercise-Solutions
.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git fetch origin main
remote: Enumerating objects: 23, done.
remote: Counting objects: 100% (23/23), done.
remote: Compressing objects: 100% (21/21), done.
remote: Total 21 (delta 13), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (21/21), 9.61 KiB | 11.00 KiB/s, done.
From https://github.com/QnAline/Gym-Git-Exercise-Solutions
 * branch            main       -> FETCH_HEAD
   5917e4b..9caccbb  main       -> origin/main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git merge origin main
merge: origin - not something we can merge

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git fetch origin main:tmp
From https://github.com/QnAline/Gym-Git-Exercise-Solutions
 * [new branch]      main       -> tmp

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git rebase tmp
Successfully rebased and updated refs/heads/main.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git push origin HEAD:main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 329 bytes | 109.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/master
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      HEAD -> main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git branch -D tmp
Deleted branch tmp (was 9caccbb).
                     <!--    OR        -->
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 303 bytes | 303.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
   da5edc0..11892f5  main -> main


          
          
<!--     IN ft/home-page-redesign TO REBASE main ,change home.html,commit,push and CREATE AN PR       -->
 
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git switch ft/home-page-redesign
Switched to branch 'ft/home-page-redesign'

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git rebase main
Successfully rebased and updated refs/heads/ft/home-page-redesign.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git status
On branch ft/home-page-redesign
nothing to commit, working tree clean

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git status
On branch ft/home-page-redesign
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   home.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git add home.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ GIT commit -m " RECHANGING AGAIN HOME IN HOME-PAGE-REDESIGN"
[ft/home-page-redesign 34e1bb5]  RECHANGING AGAIN HOME IN HOME-PAGE-REDESIGN
 1 file changed, 1 insertion(+), 1 deletion(-)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git push
Enumerating objects: 16, done.
Counting objects: 100% (16/16), done.
Delta compression using up to 4 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (14/14), 1.80 KiB | 141.00 KiB/s, done.
Total 14 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 2 local objects.
remote:
remote: Create a pull request for 'ft/home-page-redesign' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/ft/home-page-
redesign
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      ft/home-page-redesign -> ft/home-page-redesign
branch 'ft/home-page-redesign' set up to track 'origin/ft/home-page-redesign'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git remote -v
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/home-page-redesign)
$ git push
Everything up-to-date
          


## BUNDLE 4 EXERCISE 1
          
          
<!--    CHECKOUT main         -->
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git checkout
Your branch is up to date with 'origin/main'.   
          
<!--     ADDING MY REPOSITORY TO ANOTHER REMOTE       -->
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git remote add git-copy https://github.com/QnAline/GITPROJECTS.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git remote
git-copy
origin
          
<!--     MAKING CHANGES TO home ,COMMIT AND PUSHING THEM TO ORIGIN AND GIT-COPY REMOTES     -->
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   home.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git add home.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git commit -m "Making changes to html in both remote"
[main 62a3b0c] Making changes to html in both remote
 1 file changed, 1 insertion(+)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git push origin
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 4 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 817 bytes | 817.00 KiB/s, done.
Total 7 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git/
   e7669e2..f36596c  main -> main

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/PROJECT (main)
$ git push git-copy
Enumerating objects: 92, done.
Counting objects: 100% (92/92), done.
Delta compression using up to 4 threads
Compressing objects: 100% (90/90), done.
Writing objects: 100% (90/90), 52.08 KiB | 4.73 MiB/s, done.
Total 90 (delta 50), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (50/50), done.
To https://github.com/QnAline/GITPROJECTS.git
   6e252c0..4a5dee7  main -> main

        

## BUNDLE 4 EXERCISE 2
          
<!--   CHECKOUT ft/footer, CHANGES AND ANOTHER CHANGES BOTH COMMITTED          -->
          
          
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/bundle-2)
$ git checkout ft/footer
Switched to branch 'ft/footer'
Your branch is up to date with 'origin/ft/footer'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git status
On branch ft/footer
Your branch is up to date with 'origin/ft/footer'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        footer.html

nothing added to commit but untracked files present (use "git add" to track)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git add footer.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git commit -m " editing footer"
[ft/footer 08e1340]  editing footer
 1 file changed, 11 insertions(+)
 create mode 100644 footer.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git status
On branch ft/footer
Your branch is ahead of 'origin/ft/footer' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   footer.html

no changes added to commit (use "git add" and/or "git commit -a")

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git add footer.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git commit -m " editing footer again"
[ft/footer bd6fd68]  editing footer again
 1 file changed, 1 insertion(+)          
    

<!--  CREATING A PR -->
        
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git remote -v
git-copy        https://github.com/QnAline/GITPROJECTS.git (fetch)
git-copy        https://github.com/QnAline/GITPROJECTS.git (push)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/footer)
$ git push --set-upstream origin ft/footer
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 623 bytes | 124.00 KiB/s, done.
Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
   ea759b3..bd6fd68  ft/footer -> ft/footer
branch 'ft/footer' set up to track 'origin/ft/footer'.
 
 
<!-- CHECKOUT main AND CREATING ft/squashing ,SQUASHING CHANGES TO ft/footer AND COMMIT  -->
 
 $ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git merge ft/footer
Merge made by the 'ort' strategy.
 footer.html | 12 ++++++++++++
 1 file changed, 12 insertions(+)
 create mode 100644 footer.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (main)
$ git checkout ft/squashing
Switched to branch 'ft/squashing'

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/squashing)
$ git merge --squash ft/footer
Updating 4a5dee7..bd6fd68
Fast-forward
Squash commit -- not updating HEAD
 README.md   | 66 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 footer.html | 12 +++++++++++
 home.html   |  2 ++
 3 files changed, 80 insertions(+)
 create mode 100644 footer.html

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/squashing)
$ git commit -m "footer changes squashing"
[ft/squashing 30a3630] footer changes squashing
 3 files changed, 80 insertions(+)
 create mode 100644 footer.html
 
 
<!--  ANOTHER PR FOR ft/squashing-->
 
LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/squashing)
$ git remote set-url origin https://github.com/QnAline/Gym-Git-Exercise-Solutions.git

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/squashing)
$ git remote -v
git-copy        https://github.com/QnAline/GITPROJECTS.git (fetch)
git-copy        https://github.com/QnAline/GITPROJECTS.git (push)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (fetch)
origin  https://github.com/QnAline/Gym-Git-Exercise-Solutions.git (push)

LENOVO@DESKTOP-UBP6ER8 MINGW64 /d/pproject/project (ft/squashing)
          
$ git push --set-upstream origin ft/squashing
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.07 KiB | 548.00 KiB/s, done.
Total 5 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote:
remote: Create a pull request for 'ft/squashing' on GitHub by visiting:
remote:      https://github.com/QnAline/Gym-Git-Exercise-Solutions/pull/new/ft/squashing
remote:
To https://github.com/QnAline/Gym-Git-Exercise-Solutions.git
 * [new branch]      ft/squashing -> ft/squashing
branch 'ft/squashing' set up to track 'origin/ft/squashing'.
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 

# GITPROJECT
 6e252c057fc506f789bdd79768134e3578f5d33a
