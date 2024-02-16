import subprocess
import os
import sys

def transfer_commit_history(gitlab_repo, github_repo):
    SKIP_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".mov"]

    try:
        subprocess.run(['git', 'clone', gitlab_repo, 'gitlab_repo'])
        os.chdir('gitlab_repo')

        for ext in SKIP_EXTENSIONS:
            subprocess.run(['git', 'filter-branch', '--force', '--index-filter', f'git rm --cached --ignore-unmatch *{ext}', '--prune-empty', '--tag-name-filter', 'cat', '--', '--all'])


        subprocess.run(['git', 'remote', 'add', 'github', github_repo])
        subprocess.run(['git', 'fetch', 'github'])
        subprocess.run(['git', 'checkout', '-b', 'new_branch'])
        subprocess.run(['git', 'push', 'github', 'new_branch'])

        merge_process = subprocess.Popen(['git', 'merge', 'github/new_branch', '--allow-unrelated-histories'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        merge_output, merge_error = merge_process.communicate()

        if merge_process.returncode != 0:
            if b'CONFLICT' in merge_error:
                print("Merge conflict detected. Please resolve conflicts manually and then run the script again.")
            else:
                print("An error occurred while merging branches:", merge_error.decode())
            return

        subprocess.run(['git', 'push', 'github', 'master'])

        print("Commit history successfully transferred from GitLab to GitHub.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <gitlab_repo_url> <github_repo_url>")
        sys.exit(1)

    gitlab_repo_url = sys.argv[1]
    github_repo_url = sys.argv[2]

    transfer_commit_history(gitlab_repo_url, github_repo_url)
