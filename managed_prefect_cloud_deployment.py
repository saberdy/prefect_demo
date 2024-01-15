import httpx
from prefect import flow

from prefect_gitlab.repositories import GitLabRepository

gitlab_repository_block = GitLabRepository.load("prefect-gitlab-block")


@flow(log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
def get_repo_info(repo_name: str = "saberdy/prefect_demo"):
    """ select a personal repository as default argument in the function
    definition.
    """

    url = f"https://gitlab.com/api/v4/projects/{repo_name}"
    # url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


# from prefect.runner.storage import GitRepository, BlockStorageAdapter
# git_storage_block_flow = flow.from_source(
#     source=GitRepository(
#         url=BlockStorageAdapter.url
#     )
# )

if __name__ == "__main__":
    get_repo_info.from_source(
        # source="git@gitlab.com:saberdy/prefect_demo.git",
        source=gitlab_repository_block,
        entrypoint="managed_prefect_cloud_deployment.py:get_repo_info"
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-managed-pool",
    )
