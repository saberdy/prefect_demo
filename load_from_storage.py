from datetime import datetime
from prefect import flow


@flow(retries=3, retry_delay_seconds=5, log_prints=True)
def dummy_flow(date: datetime = datetime.now()):
    print(f"It was {date.strftime('%A')} on {date.isoformat()}")


if __name__ == "__main__":
    # dummy_flow()
    flow.from_source(
        source="https://github.com/saberdy/prefect_demo.git",
        entrypoint="load_from_storage.py:dummy_flow"
    ).deploy(name='dummy_flow_deploy', work_pool_name='my-managed-pool')
