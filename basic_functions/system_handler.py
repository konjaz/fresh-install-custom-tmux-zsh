"""
author: Konrad Jazownik
mail: konjaz@gmail.com
licence: GPL-3.0

"""
import os
import platform

from log.console_logger import LOG


def find_user_path():
    user = os.getlogin()
    home_path = "/home/{}".format(user)
    LOG.info("Current username: %s", user)
    LOG.info("User path is: %s", home_path)
    return user, home_path


def define_distro():
    return platform.dist()


def get_submodule_list():
    NotImplementedError
