from utils import setup_nginx, setup_env


def execute():
    setup_env.delete_dot_env("./assets/.env")
    setup_nginx.delete_default_conf()
    setup_nginx.delete_docker_compose()

