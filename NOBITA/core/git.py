import asyncio
import shlex
from typing import Tuple
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
import config
from ..logging import LOGGER

loop = asyncio.get_event_loop_policy().get_event_loop()


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return loop.run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO  # Ensure this is set correctly in your config

    # Use the GitHub token for authentication if available
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        # Explicitly specify the repo path in Heroku app, assuming /app/NOBITA_VIP is the repo path
        repo = Repo('/app/NOBITA_VIP')  # Replace with the correct path if needed
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except (GitCommandError, InvalidGitRepositoryError):
        # Initialize the repo in the specified directory if it doesn't exist
        repo = Repo.init('/app/NOBITA_VIP')  # Initialize repo in /app/NOBITA_VIP
        if "origin" in repo.remotes:
            origin = repo.remote("origin")
        else:
            origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()

        # Check if the upstream branch exists, if not, create it from the origin
        if config.UPSTREAM_BRANCH not in repo.branches:
            try:
                # Try to create the branch from the origin if it exists
                repo.create_head(
                    config.UPSTREAM_BRANCH,
                    origin.refs[config.UPSTREAM_BRANCH],
                )
            except Exception as e:
                LOGGER(__name__).error(f"Could not create branch: {e}")
                return  # Early return on error

        # Set tracking branch for the new or existing branch
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)

    # Fetch the latest changes from the remote origin
    nrs = repo.remote("origin")
    nrs.fetch(config.UPSTREAM_BRANCH)

    # Try pulling the latest changes
    try:
        nrs.pull(config.UPSTREAM_BRANCH)
    except GitCommandError:
        # If there is a merge conflict or other issue, reset the repository to the fetched state
        repo.git.reset("--hard", "FETCH_HEAD")

    # Install requirements after pulling the updates
    install_req("pip3 install --no-cache-dir -r requirements.txt")
    LOGGER(__name__).info(f"Fetched Updates from: {REPO_LINK}")
