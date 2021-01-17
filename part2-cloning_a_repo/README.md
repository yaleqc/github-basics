## Cloning a repository locally

The first step in contributing to a project is cloning the GitHub repository. Saying that we are "cloning" is just another way of saying that we are copying that repository from the internet onto our local machines. 

One important distinction between just copying and cloning, however, is that a remote is automatically set up between your local copy and the copy of the repository on GitHub. This remote tracks the changes that you make locally and allows you to see where your copy the and GitHub copy differ, check if your local copy needs to be updated, and push any local changes you make to GitHub. You can think of a remote as a link between your local copy of the repo and the GitHub copy. 

Cloning a repository is simple. Navigate to the desired directory in your computer and enter:
```
git clone <repo_link>
```

But where do we get this `<repo_link>`? 

At the top of every repository, there is a green button (depicted below) that expands to provide you the link to the repo! 

![](code-button.png)
![](https-url-clone.png)

###### Source: [GitHub Docs: Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

For the purposes of this tutorial, we will only worry about cloning using HTTPS. All you have to do is copy the given link and paste it in!

## Challenge 1:

Clone this repo!

[Next: Creating a new branch for your local changes](../part3-make_a_new_branch)