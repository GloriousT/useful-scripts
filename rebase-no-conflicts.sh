#!/bin/sh
function rebase_with_temporary_commit {
	echo "Changes detected, commiting to temporary commit"
	git commit -a -m "temporary commit"
	rebase_on_latest_master
	git reset --soft HEAD~1
}

function rebase_on_latest_master {
	echo "No changes detected, rebasing"
	git checkout master
	git -c core.quotepath=false fetch origin --progress --prune
	git -c core.quotepath=false rebase origin/master
	git checkout -
	git rebase master
}

PROJECT_PATH=
set -o history
# set -o verbose
cd ${PROJECT_PATH}

output="$(git status -uno)"
echo $output
if [[ $output != *"nothing to commit"* ]]; then
	rebase_with_temporary_commit
else
	rebase_on_latest_master
fi
echo "THE END"
