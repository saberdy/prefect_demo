from prefect_gitlab.repositories import GitLabRepository


def create_gitlab_sb():
    private_gitlab_block = GitLabRepository(
        name="prefect_demo gitlab repository block",
        repository="https://gitlab.com/saberdy/prefect_demo.git",
        access_token="glpat-oquVHZssxayWJwF4A-hJ"
    )
    private_gitlab_block.save("prefect-gitlab-block")


if __name__ == "__main__":
    create_gitlab_sb()
