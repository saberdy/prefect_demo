import httpx
from prefect import flow


@flow(log_prints=True)
def get_repo_info(repo_id: str = "53809079"):
    """ select a personal repository as default argument in the function
    definition.
    """

    url = f"https://gitlab.com/api/v4/projects/{repo_id}"
    response = httpx.get(url)
    response.raise_for_status()
    repo = response.json()
    print(f"{repo_id} repository statistics 🤓:")
    print(f"Stars 🌠 : {repo['stargazers_count']}")
    print(f"Forks 🍴 : {repo['forks_count']}")


if __name__ == "__main__":
    get_repo_info()
