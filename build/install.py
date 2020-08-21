"""
#/*****************************************************************************
# *  Filename:  install.py
# *
# *  FILE HISTORY
# *=========================================================================
# * DATE         Author               Details
# *=========================================================================
# * 21/07/2020   Tanmay Prakash       Initial Draft
# *
# *  Copyright (c) tanmayp1192@gmail.com.
# ****************************************************************************/
"""

import argparse
from main import init, executor
from utils import user_input

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interactive', action="store_true", default=False,
                        help="Interactive installation, helps user to override configuration file")
    parser.add_argument('-f', '--file', action="store", help="Path of configuration file for deployment",
                        default=None)
    args = parser.parse_args()

    if args.interactive is False and args.file is None:
        print("Argument required !!!")
        parser.print_help()
        exit(-1)

    # Read configuration file and save in global context
    init.read_config_file(args.file)
    # Override configuration file parameters
    if args.interactive is True:
        user_input.get_update_conf(user_input.get_options())

    # Execute all deployment tasks
    executor.run()





