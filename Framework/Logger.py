import logging


class Logg:
    def __init__(self,name):
        self.logger = logging.getLogger(name)

    def make_log(self, text):
        self.logger.debug(msg=text)
