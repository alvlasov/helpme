import logging


class LoggerMixin:

    @property
    def _logger(self):
        return logging.getLogger(type(self).__name__)

