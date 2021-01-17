## Keeping up with the repository

If you've successfully gotten your PR out, congrats! You're almost there!

Now things get a bit more interesting. What happens when other people update the master branch? 

If you've completed all the challenges one sitting, there's a pretty good chance that no updates to the master branch of this repo have been made and you don't need to worry about what we call **merge conflicts**. Merge conflicts happen when two branches differ outside of the changes that were committed. For example, let's take the main characters from the quantum world, Alice and Bob, and assume that they're both collaborating on a project. Now assume the following happens:

  1. Alice and Bob both clone the repo on Monday.
  2. Alice and Bob both create their dev branches and get to work on their code.
  3. Alice finishes her code on Tuesday and submits a pull request to merge her dev branch to master. Master has not changed, so the branch is merged seamlessly.
  4. Bob finishes his code on Wednesday and tries to merge his dev branch to master. Master from Bob's perspective is now different than master from Alice's perspective, and so a conflict occurs, since Git isn't sure which master is the correct one.

So how do we resolve this conflict? The easiest way to resolve merge conflicts is by preventing them in the first place by keeping both your local master and dev branch up to date with the master branch on GitHub. An easy way to do this is, before you ever push any changes to your dev branch, pull the changes from the online master branch to your local master and dev branch.

#### To pull changes to a branch:
```
git checkout <branch_name>
git fetch origin
git pull origin master
```

Where `<branch_name>` is the name of the branch you want to update. You can update both master and your dev branch by checking them out and running fetch/pull on each.

And with that, you've learned exactly what's needed to contribute to a large majority of open-source projects on GitHub, and now have a basic toolkit of Git commands under your belt. If there are any issues in any of the READMEs, or you feel that there's something valuable to add to this tutorial, you're now equipped to submit a pull request and fix it! (And I highly encourage you to do so!)

If you want to learn more about the ins and outs of Git and GitHub, check out the following links:
- [GitHub Docs](https://docs.github.com/en)
- [Git Documentation](https://git-scm.com/doc)