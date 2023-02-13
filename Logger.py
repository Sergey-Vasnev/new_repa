import logging

class Logg():
    def __init__(self):
        self.logger = logging.getLogger()
        #logging.basicConfig(level=logging.WARNING, filename=f'log_for_test.log',
         #                   filemode="a", format="%(name)s %(asctime)s %(levelname)s %(message)s")

    def makeLog(self,text):
        self.logger.warning(msg=text)
