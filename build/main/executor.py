from utils import setup_env, setup_nginx, cleanup
from progress.bar import IncrementalBar
import time
from functools import partial


def run():
    tasks = {
        1: partial(setup_env.create_dot_env, "./assets/.env"),
        2: partial(setup_nginx.update_default_conf, "./nginx/default_sample.conf"),
        3: partial(setup_nginx.create_docker_compose, "./nginx/docker-compose.yml"),
        4: partial(cleanup.execute) # It should be the last method to execute
    }

    bar = IncrementalBar("Installing", max=len(tasks))
    for task in tasks:
        tasks[task]()
        bar.next()
        time.sleep(1)

    bar.finish()
