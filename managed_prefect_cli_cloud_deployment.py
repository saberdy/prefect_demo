import httpx
from prefect import flow


@flow(log_prints=True)
def get_repo_info(repo_name: str = "saberdy/prefect_demo"):
    """ select a personal repository as default argument in the function
    definition.
    """

    url = f"https://gitlab.com/api/v4/projects/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_name} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


if __name__ == "__main__":
    get_repo_info()
