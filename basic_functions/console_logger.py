"""
author: Konrad Jazownik
mail: konjaz@gmail.com
licence: GPL-3.0

"""

import logging

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
CONFIG = logging.basicConfig(format=FORMAT,
                             level=logging.INFO)
LOG = logging.getLogger(__name__)
