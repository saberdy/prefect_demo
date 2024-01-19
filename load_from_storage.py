from datetime import datetime
from prefect import flow
# from prefect.runner.storage import GitRepository
# from prefect.runner.storage import GitLabRepository

@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dummy_flow(date: datetime = datetime.now()):
    print(f"It was {date.strftime('%A')} on {date.isoformat()}")


my_flow = dummy_flow.from_source(
    source="https://github.com/saberdy/prefect_demo"
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
