import subprocess
from subprocess import PIPE
from main import init


def run_docker():
    """
    This method will execute docker and
    spin up all container services
    :return: Boolean
    """
    command = ''

    init.logger.debug("Command to be executed ", command)
    session = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=PIPE, stderr=PIPE)

    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error " + str(stderr))

    return True

