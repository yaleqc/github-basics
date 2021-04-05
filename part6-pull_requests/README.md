## Opening pull requests

The final step in making sure that your changes make it into the project is opening up a **pull request**. Pull requests compare your branch to the another branch of the repository, allow for your code to be reviewed and any necessary changes to be made, and handle branch merging automatically. The normal process of submitting code to the master branch via pull requests looks like this:
 1. You push your contributions to your personal branch
 2. You open up a pull request between your branch and the master branch
 3. You add reviewers to your code to check it before merging. Some projects, like the [Quantum Programming API](https://github.com/yaleqc/quantum-programming-api/) do this automatially.
 4. Reviewers either approve or request changes to your code.
 5. Once the code is approved, you merge your changes into the master branch!

#### To open up a pull request:

1. Open up the branch menu on the repository's home page and select your branch.
<img src="branch-dropdown.png" width="50%"/>

2. From the bar on top of the branch contents, click the Pull request button.
<img src="pull-request-start-review-button.png" width="50%"/>

3. Looking at the dropdown menu, set the *base* branch to `master` and the *compare* branch to the branch that you made your changes in.
<img src="choose-base-and-compare-branches.png" width="50%"/>

4. Add a title and description for your PR.
<img src="pullrequest-description.png" width="50%"/>

5. Select **Create Pull Request** (or draft if needed) and you're good to go!
<img src="pullrequest-send.png" width="50%"/>

###### Source: [GitHub Docs: Creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)

Now, let's say that your need to make some changes to your code you submit the PR. As mentioned in a prior part, all you'll have to make the changes locally and push to your branch, and the updates will automatically be reflected in PR. This is how you make changes brought up in **Code Reviews**. If you want to learn more about code reviews, see the [GitHub Docs: About pull request reviews](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-reviews).

If you don't need to make any changes, the reviewer will approve the PR, and the changes will either be automatically merged in, the reviewer can do it, or you can do it yourself!

**Note:** If your branch has gotten out of sync with the master branch, you may get a **merge conflict**. To avoid this, make sure your personal branch up to date with master by runing:
```
git checkout <your_branch>
git fetch origin
git pull origin master
```
This is explained further in the next part.

To learn more about merge conflicts, check out the [GitHub Docs: About merge conflicts](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-merge-conflicts).
## Challenge 5:

Take the changes you pushed to GitHub in the last part and open up a pull request! **Hint: if you followed the tutorial, you cloned a forked repository. [This might be helpful](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork)** If everything checks out, your work in Challenge 3 will be merged into the master branch!

[Next: Keeping up with the repository](../part7-keeping_up_with_repo)