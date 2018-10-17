import git 

repo = git.Repo()

repo.remotes.origin.fetch()

repo_name = repo.active_branch.name

commits_behind = repo.iter_commits('{0}..origin/{0}'.format(repo_name))
commits_ahead = repo.iter_commits('{0}..origin/{0}'.format(repo_name))

count_commits_ahead = sum(1 for c in commits_ahead)
count_commits_behind = sum(1 for c in commits_behind)
print ('commits ahead of origin {}'.format(count_commits_ahead))
print ('commits behind of origin {}'.format(count_commits_behind))
