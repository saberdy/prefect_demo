from datetime import datetime
from prefect import flow
# from prefect.runner.storage import GitRepository
# from prefect.runner.storage import GitLabRepository
from prefect_gitlab import GitLabRepository
from prefect_gitlab.credentials import GitLabCredentials
from prefect.blocks.system import Secret

# gitlab_credentials_block = GitLabCredentials.load("gl-prefect-block")
# gitlab_repository_block = GitLabRepository.load("my-private-gitlab-block")


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dummy_flow(date: datetime = datetime.now()):
    print(f"It was {date.strftime('%A')} on {date.isoformat()}")


gitlab_credentials = GitLabCredentials(
    personal_access_token=Secret.load("gl-personal-access-token").get(),
    api_url="https://gitlab.com",  # Adjust if you use a self-hosted GitLab instance
)

gitlab_repository_block = GitLabRepository(
    # <your_gitlab_url>
    url="https://gitlab.com/saberdy/prefect_demo",
    # <your_branch_name>
    branch="gl-api-pat",
    credentials=gitlab_credentials
)

my_flow = dummy_flow.from_source(
    source=gitlab_repository_block,
    entrypoint="load_from_storage.py:dummy_flow"
)
# my_flow = flow.from_source(
#     source=gitlab_repository_block,
#     # GitRepository(
#     # url="https://gitlab.com/saberdy/prefect_demo.git",
#     # url=gitlab_credentials_block,
#     # url="https://gitlab.com/api/v4/projects/53809079",
#     # branch="master",
#     # credentials={"username": "saberdy",
#     #             "access_token": gitlab_credentials_block},
#     # credentials={
#     #     "username": "saberdy",
#     #     "access_token": Secret.load("prefect-demo").get(),
#     #     # "branch": "master"
#     entrypoint="repo_info.py:get_repo_info"
#    )

if __name__ == "__main__":
    # dummy_flow()
    my_flow()
