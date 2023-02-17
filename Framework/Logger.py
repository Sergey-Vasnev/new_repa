import logging


class Logg:
    def __init__(self,name):
        self.logger = logging.getLogger(name)

    def make_DEBUG(self, text):
        self.logger.debug(msg=text)

    def make_INFO(self, text):
        self.logger.info(msg=text)

    def make_WARNING(self, text):
        self.logger.warning(msg=text)

    def make_CRITICAL(self, text):
        self.logger.critical(msg=text)
