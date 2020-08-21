from configparser import ConfigParser, ExtendedInterpolation
import logging


logging.basicConfig(filename="./log/install.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
config = ConfigParser(interpolation=ExtendedInterpolation())


def read_config_file(path):
    """
    Method is responsible to read deployment specific configuration
    file as provided as commandline argument
    :param path:
    :return:
    """
    try:
        config.read(path)
        logger.setLevel(logging.DEBUG)
    except:
        print("Error in reading configuration file [{}]".format(path))
