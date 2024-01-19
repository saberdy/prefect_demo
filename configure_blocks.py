from prefect_gitlab import GitLabRepository
from prefect_gitlab import GitLabCredentials
from prefect.blocks.system import Secret


pat = Secret.load("gl-personal-access-token").get(),
gl_credentials = GitLabCredentials(
    name="gl-credentials",
    # personal_access_token or access_token only?
    access_token=pat,
    url="https://gitlab.com/saberdy/prefect_demo",  # Adjust if you use a self-hosted GitLab instance
)
gl_credentials.save("gl-credentials", overwrite=True)

gl_repository = GitLabRepository(
    name="gl-repository",
    # <your_gitlab_url>
    # repository=f'https://:{Secret.load("gl-personal-access-token").get()}@gitlab.com/saberdy/prefect_demo.git',
    repository="https://gitlab.com/saberdy/prefect_demo.git",
    # <your_branch_name>
    reference="gl-api-pat",
    credentials=gl_credentials
)
gl_repository.save("gl-repository", overwrite=True)
