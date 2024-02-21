# GitLab to GitHub Contribution History Transfer Script

This script transfers the commit history from a GitLab repository to Github. It performs the following tasks:

1. Clones the GitLab repository locally.
2. Removes files from the Git history with specified extensions such as Images and gifs to speed up the process.
3. Adds a remote pointing to the GitHub repository.
4. Pushes the filtered commit history to a new branch on the GitHub repository.
5. Merges the new branch into the existing GitHub repository.

## Usage

### Prerequisites

- Python installed.
- Both GitLab and GitHub repositories accessible with the appropriate permissions.

### Running the Script

1. Clone this repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the directory containing the script:

    ```bash
    cd <repository-directory>
    ```

3. Run the script `gl2gh.py` with the following command, provide the URLs of the GitLab and GitHub repositories as arguments:

    ```bash
    python gl2gh.py <gitlab_repo_url> <github_repo_url>
    ```

    Replace `<gitlab_repo_url>` with the URL of the GitLab repository and `<github_repo_url>` with the URL of the GitHub repository.



### Note

- Ensure that you have the necessary permissions to clone, push, and merge branches in both the GitLab and GitHub repositories.
- Review the `SKIP_EXTENSIONS` list in the script to verify that it matches the file extensions you want to exclude from the transfer.


## Your History after!
![after](https://github.com/joeloftusdev/get-gitlab-commits/assets/152509645/23c05bb4-0efd-46a6-8139-63bc7466e94b)



## License

This script is licensed under the [MIT License](LICENSE).
