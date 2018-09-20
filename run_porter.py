#!/enforta/env-cfg/bin/python3.6
# -*- coding: utf-8 -*-
from pprint import pprint
from porter import *
import sys
import yaml

try:
  config_yaml = sys.argv[1]
except IndexError:
  print('Error! Config not specified. Run it this way: ./run_porter.py /path/to/config.yaml')
  sys.exit()


#config_yaml = 'porter/config/config.yaml'


def main():
	# Read YAML file
	with open(config_yaml, 'r') as stream:
		run_app(yaml.load(stream))
    #	pprint(data_loaded)



if __name__ == "__main__":
	main()