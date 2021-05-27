import logging
from socket import gethostname


# define filter to add hostname
class HostnameAddingFormatter(logging.Formatter):
    def __init__(self, fnt=None, datefnt=None, style='%'):
        super().__init__(fnt, datefnt, style)
        
    def format(self, record):
      # Try to add a hostname attribute to every log record
      try:
          record.__dict__['hostname'] = gethostname()
      except:
          record.__dict__['hostname'] = 'exception-getting-hostname'
      s = super().format(record)
      return s