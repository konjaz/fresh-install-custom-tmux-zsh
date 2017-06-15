"""
author: Konrad Jazownik
mail: konjaz@gmail.com
licence: GPL-3.0

"""
from log.console_logger import LOG as log
from basic_functions import system_handler


def installer():
    dist = system_handler.define_distro()
    log.info("Found distro: %s", dist[0])
    user, path = system_handler.find_user_path()
    log.info("Found username and home dir, where installation proceed\n"
             "current username: {0}\n"
             "path: {1}".format(user, path))


if __name__ == "__main__":
    installer()
