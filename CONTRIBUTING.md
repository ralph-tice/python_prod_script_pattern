# Submitting Issues

The issue tracker is for project changes. Bugfixes, improvements, etc. If you need help, check out
[operatingops.org](operatingops.org) instead of submitting an issue.

1. Write everything you know. Think of all the questions a maintainer might ask and write in the answers.

1. Remember that this is free software! We have day jobs 👷. We might not respond right away.

# Contributing Code

1. [Fork and clone the repo](https://help.github.com/articles/fork-a-repo/).

1. Make sure the tests pass.

   ```shell
   tox
   ```

1. Create a feature branch:

   ```shell
   git checkout -b my_feature
   ```

1. Make your change. Add tests for your change.

1. Make sure the tests pass.

   ```shell
   tox
   ```

1. Push to your fork.

   ```shell
   git push origin my_feature
   ```

1. [Create a Pull Request](https://help.github.com/articles/creating-a-pull-request/).

To increase the chance that your pull request gets accepted:

* Write tests.
* Follow [Simple Style](https://github.com/operatingops/simple_style/blob/v0.1.0/SIMPLE_STYLE.md).
* Write [good commit messages](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).
* Organize your commits. "Fix typo" and "work in progress" commits are hard to follow. If you like to commit often,
  check out git's [rebase](https://help.github.com/articles/about-git-rebase/). You can use it to clean up at the end.
