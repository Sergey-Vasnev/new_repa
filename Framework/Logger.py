import logging


class Logg:
    def __init__(self,name):
        self.logger = logging.getLogger(name)

    def make_debug(self, text):
        self.logger.debug(msg=text)

    def make_info(self, text):
        self.logger.info(msg=text)

    def make_warning(self, text):
        self.logger.warning(msg=text)

    def make_critical(self, text):
        self.logger.critical(msg=text)
