import httpx
from prefect import flow
from prefect.runner.storage import GitRepository, BlockStorageAdapter


@flow(log_prints=True)
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
def get_repo_info(repo_name: str = "saberdy/prefect_demo"):
    url = f"https://gitlab.com/api/v4/projects/{repo_name}"
    # url = f"https://api.github.com/repos/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


# git_storage_block_flow = flow.from_source(
#     source=GitRepository(
#         url=BlockStorageAdapter.url
#     )
# )

if __name__ == "__main__":
    get_repo_info.from_source(
        source="https://gitlab.com/saberdy/prefect_demo.git",
        entrypoint="managed_prefect_cloud_deployment.py:get_repo_info"
    ).deploy(
        name="my-first-deployment",
        work_pool_name="my-managed-pool",
    )
