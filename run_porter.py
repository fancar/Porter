#!/enforta/env-cfg/bin/python3.6
# -*- coding: utf-8 -*-
from pprint import pprint
from porter import *
import yaml

config_yaml = 'porter/config/config.yaml'


def main():
	# Read YAML file
	with open(config_yaml, 'r') as stream:
		run_app(yaml.load(stream))
    #	pprint(data_loaded)



if __name__ == "__main__":
	main()