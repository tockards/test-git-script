# test-git-script
this is used to test git script

# clone test repo
`git clone https://github.com/tockards/test-git-script`
# cd into git repo
`cd test-git-script`
# install packages
`pip install -r requirements.txt`
# create blank file
`touch blank`
# add file
`git add blank`
# commit file
`git commit -m 'added blank'`
# execute the script
`python git-test-script.py`

# the output should display

```
commits ahead of origin 1
commits behind of origin 0
```
