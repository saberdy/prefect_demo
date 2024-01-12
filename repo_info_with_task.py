import httpx
from prefect import flow, task
# from prefect import tags


@task(name="get_url", description="tutorial task for getting url and returning json",
      tags=["tutorial"])
def get_url(url: str, params: dict = None):
    response = httpx.get(url, params=params)
    response.raise_for_status()
    return response.json()


@flow(retries=3, retry_delay_seconds=5, log_prints=True,
      name="get_repo_info",
      description="tutorial example flow for getting repo info")
def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
    url = f"https://api.github.com/repos/{repo_name}"
    repo_stats = get_url(url)
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo_stats['stargazers_count']}")
    print(f"Forks 🍴 : {repo_stats['forks_count']}")


if __name__ == "__main__":
    get_repo_info()
