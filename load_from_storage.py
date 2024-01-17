from prefect import flow
from prefect.runner.storage import GitRepository
from prefect.blocks.system import Secret

my_flow = flow.from_source(
    source=GitRepository(
        url="https://gitlab.com/saberdy/prefect_demo.git",
        branch="gl-api-pat",
        credentials={
            "access_token": Secret.load("prefect-demo-pat").get()
            }
       ),
    entrypoint="repo_info.py:get_repo_info"
   )

if __name__ == "__main__":
    my_flow()
