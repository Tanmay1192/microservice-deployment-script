import os
from main import init


def create_dot_env(path):
    """
     This method is reponsible for
     creating deployment setup
     specific .env file

    :param path:
    :return:
    """
    if path is None:
        print("Please provide path of environment file")
        return

    data = list()
    # data.append("API_URL=http://{addr}{port}\n".format(addr=config_reader.config['APP']['ADDRESS'],
    #             port='' if config_reader.config['APP']['PORT'] is None
    #             else ":"+config_reader.config['APP']['PORT']))

    data.append("API_URL={}\n".format(init.config['NGINX']['API_URL']))
    file = open(path, "a")
    file.write("".join(data))
    file.close


def delete_dot_env(path):
    """
      This method is responsible for deleting .env file
      at the end of deployment task
    :param path:
    :return:
    """
    if path is None:
        init.logger.error("Please provide path of environment file")
        return

    os.remove(path)
    init.logger.debug("Environment file cleanup .... done")
