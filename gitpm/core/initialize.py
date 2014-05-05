# -*- coding: utf-8 -*-
import sys, os
from git import Repo, Git
from git.errors import InvalidGitRepositoryError, GitCommandError

DIRECTORIES = ["issues", "pull_requests", "users", "wiki"]

def initialize(path, branch):
    try:
        repo = Repo(path)
        git = Git(path)
    except InvalidGitRepositoryError as err:
        print "Not a valid Git repo: %s" % err
        sys.exit("Run `git init %s` first" % err)

    output = ['Initializing in %s [%s]' % (path, branch)]
    current_branch = repo.active_branch

    if branch in [b.name for b in repo.branches]:
        output.append("error: A branch named '%s' already exists in this repo!"
                % branch)
        return output

    output.append("--> Stashing current branch contents [%s]" % current_branch)
    try:
        cmd = git.stash(u=True)
        for line in cmd.splitlines():
            output.append(" %s" % line)
    except GitCommandError as err:
        output.append("error: %s" % err)
        return output

    output.append("--> Switching to branch '%s'" % branch)
    try:
        git.checkout(B=branch)
    except GitCommandError as err:
        output.append("error: %s" % err)
        return output

    output.append("--> Clearing current files and committing")
    try:
        files = os.listdir(path)
        files.remove('.git')
        for entry in files:
            git.rm(entry, r=True, f=True)

        cmd = git.commit(m="Clearing files in preparation for git-pm")
        for line in cmd.splitlines():
            output.append(" %s" % line)
    except GitCommandError as err:
        output.append("error: %s" % err)
        return output

    output.append("--> Creating git-pm file structure and committing")
    try:
        for directory in DIRECTORIES:
            dir_path = os.path.join(path, directory)
            gitkeep = os.path.join(dir_path, '.gitkeep')
            os.mkdir(dir_path)
            with open(gitkeep, 'a'):
                os.utime(gitkeep, None)

        cmd = git.commit(m="Created git-pm file structure")
        for line in cmd.splitlines():
            output.append(" %s" % line)
    except GitCommandError as err:
        output.append("error: %s" % err)
        return output

    output.append("--> Returning to previous branch and popping stash")
    try:
        git.checkout(current_branch)
        git.stash("pop")
    except GitCommandError as err:
        output.append("error: %s" % err)
        return output

    return output

