#!/enforta/env-cfg/bin/python3.6
# -*- coding: utf-8 -*-
# enforta. Work hard, earn less!
# Mamaev Alexandr 2018. First balls, made out of shit.
# fancarster@gmail.com
from dotenv import load_dotenv
load_dotenv()
from porter import *
import sys
import yaml
import argparse


# input variables
parser = argparse.ArgumentParser(description='The Porter\nMultiply \
	adding vlan to a number of switches according to template')
required = parser.add_argument_group('required arguments')
required.add_argument('-c', '--config', help='path to config file', required=True)
parser.add_argument('-v','--version', help='show version', action='version', version=show_version())
parser.add_argument('-u', '--username', help='default username',)
parser.add_argument('-p', '--password', help='default password')
args = parser.parse_args()

if args.config:
	config_yaml = args.config
	if not os.path.exists(config_yaml):
		print('File not found:',config_yaml)
		sys.exit()

if args.username: os.environ['DEFAULT_USERNAME'] = args.username
if args.password: os.environ['DEFAULT_PASSWORD'] = args.password


def main():
	# Read YAML config file
	with open(config_yaml, 'r') as stream:
		run_app(yaml.load(stream))
    #	pprint(data_loaded)

if __name__ == "__main__":
	main()