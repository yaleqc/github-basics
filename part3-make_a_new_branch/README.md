## Making a new branch to start editing code

The next step you need to take before actually contributing is creating a new branch for your change. Understanding how to use branches is required to contribute to the [Quantum Programming API](https://github.com/yaleqc/quantum-programming-api).

### Why do we need branches? 

Branches allow you to create a local copy of the repository at its current state, which you can later merge into the `master` branch. But why would we want to do this?

##### Stability
Put simply, using separate branches as workspaces allows for the `master` branch to be the point of reference for all contributors in the project. The `master` branch should be a stable and functioning version of the project at all times. Creating separate branches for separate features allows you to make changes, test them, and push them to Github without ruining the stable version of the product.

##### Organization
Using branches also allows for implementations features to be organized well and later merged to the `master` branch piece by piece rather than in one large chunk of code. For example, if you have working code for a basic game of Pong and want to add more features, contributors might create a branch to implement different ball colors, one for different background colors, and one for different fonts. If the contributor working on the background colors gets done first, they can merge those changes into the `master` branch without having to wait for the people working on the other features to finish. This becomes especially important as the number of project contributors grows. 

##### Code Reviews
Branches are also needed for creating [Pull Requests](../part6-pull_requests), which we'll discuss in depth later. The importance of branches in PRs have to do with making changes. When you submit a PR (pull request) for you branch to be merged to the `master`, normally the owner(s) of the repository will check the code to make sure that the code is written well and does what it's supposed to. If you submit your branch in a PR and changes are requested, all you need to do is push the changes to your branch **and the changes will automatically show up in the PR**. Again, we'll talk more about it later, but this is an important part of branches. 

### Now that we know why branches are important, how do we create and manage them? 

#### To checkout a new branch, enter:
```
git checkout -b <branch_name>
```
where `<branch_name>` is up do you.

#### To view all local branches, enter:
```
git branch
```

in your shell. The branch you are currently on will be highlighted.

#### To switch to an existing branch, enter:
```
git checkout <branch_name>
```
where `<branch_name>` is the name of the desired branch.

When starting a fresh feature, first [make sure your master branch is up to date](https://github.com/yaleqc/github-basics), then create your new branch! To learn how to actually change the code and add the changes to your branch, see the next section.

## Challenge 2:

Create a branch with your last name titled `lastname-first-branch` and go into it. Use `git branch` to check. 

[Next: Make changes to the code locally](../part4-changing_the_code)