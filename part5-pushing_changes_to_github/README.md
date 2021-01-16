## Pushing your local changes to Github
Now that you've created your own branch and made some changes, its time to push them to Github.

The great thing about Git is all the work you did before makes it simple to push your changes to the internet. 

#### To push your change to Github, enter:
```
git push origin <branch_name>
```
Where `<branch_name>` is the name of the branch you've created. 

But what's going on here? In simple terms:
 - `git push` is the command that tells Git its time to push the commits
 - `origin` tells git which repo to push the commits to. If you type `git remote -v` you'll get a list of remotes and their corresponding names and you'll see that `origin` points to the online version of this repo. This parameter gets more interesting when dealing with [Forked repositories](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks).
 - `<branch_name>` tells git which branch of the repo to push your commits to. You won't have access to directly push to the master branch of this repo, so you'll need to specify your branch every time.

If everything worked successfully, you should be able to see your branch under the branches tab or the branches link.
![](branches-link.png)
