import os
from main import  init


def update_default_conf(path):
    """
    This method is responsible for updating
    nginx -> default_sample.conf
    :return:
    """
    file = open(path, "r")
    lines = "".join(file.readlines())
    lines = lines.replace("%%ADDRESS%%", init.config['APP']['ADDRESS'])\
        .replace("%%PORT%%", init.config['APP']['PORT'])

    f = open("./assets/default.conf", "w+")
    f.writelines(lines)


def delete_default_conf():
    """
    Delete nginx->default file present inside assets folder
    :return:
    """

    os.remove("./assets/default.conf")
    init.logger.debug("Default conf cleanup .... done")


def create_docker_compose(path):
    """
    This method will update docker-compose file
    :param path:
    :return:
    """

    file = open(path, "r")
    lines = "".join(file.readlines())
    lines = lines.replace("%%REACT_APP_NAME%%", init.config['NGINX']['REACT_APP']) \
        .replace("%%IMAGE%%", init.config['NGINX']['IMAGE'])\
        .replace("%%API_URL%%", init.config['NGINX']['API_URL'])

    f = open("docker-compose.yml", "w+")
    f.writelines(lines)


def delete_docker_compose():
    """
    Delete setup specific docker-compose.yml file
    :param path:
    :return:
    """

    os.remove("docker-compose.yml")
    init.logger.debug("docker-compose cleanup... done")

