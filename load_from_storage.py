from prefect import flow
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret

my_flow = flow.from_source(
    source=GitRepository(
        # url="https://gitlab.com/saberdy/prefect_demo",
        url="https://gitlab.com/api/v4/projects/53809079",
        # branch="master",
        credentials={
            # "username": "saberdy",
            "access_token": Secret.load("prefect-demo").get(),
            # "branch": "master"
            }
       ),
    entrypoint="repo_info.py:get_repo_info"
   )

if __name__ == "__main__":
    my_flow()
