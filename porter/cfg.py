import os
import sys
import logging
from logging import handlers

the_name = os.environ['MY_NAME']
__version__ = os.environ['MY_VERSION']

def show_version():
	return '{} {}'.format(the_name,__version__)

#commands for cisco()
make_vlan = '''
vlan {vlan}
name {case}
exit
'''
add_vlan_to_if = '''
interface {interface}
switchport trunk allowed vlan add {vlan}
exit
'''

log_folder = '/config/logs/'

fullpath = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(fullpath+log_folder):
	os.makedirs(fullpath+log_folder)

logfile = fullpath+log_folder+the_name+'.log'

logger = logging.getLogger(the_name)
formatter = logging.Formatter('%(asctime)s | %(name)s |  %(levelname)s | %(message)s\r')
stream_formatter = logging.Formatter('\n%(levelname)s: %(message)s')
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)
stream_handler.setFormatter(stream_formatter)

file_handler = logging.handlers.TimedRotatingFileHandler(filename = logfile, when = 'W6', interval=1, backupCount = 8)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)