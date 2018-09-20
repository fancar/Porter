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


'''
input data example

{'devices': {'s1mr': {'ip': '10.77.77.79',
                      'name': 's1.c6807.mr.msk',
                      'port': 23,
                      'protocol': 'telnet'},
             's6m1': {'ip': '10.77.77.3',
                      'name': 's1.cs.m9.msk_2nd_fl',
                      'port': 23,
                      'protocol': 'telnet'},
             's6m9': {'ip': '10.77.77.90',
                      'name': 's6-new.c6807.m9.msk',
                      'port': 23,
                      'protocol': 'telnet'}},
 'templates': [{'menu_name': 'Прогнать vlan до ЭРТХ (в s1mr[po1,po2] от '
                             'vip.r7(pair))...',
                'switches': [{'device': 's1mr',
                              'to_ports': ['Gi6/10', 'po10', 'po1', 'po2']},
                             {'device': 's6m9',
                              'to_ports': ['Gi6/10', 'po10']}]},
               {'menu_name': 'Прогнать vlan до ЭРТХ (в s1m9[po1,po2] от '
                             'vip.r7(pair))...',
                'switches': [{'device': 's1mr', 'to_ports': ['Gi6/10', 'po10']},
                             {'device': 's6m9',
                              'to_ports': ['Gi6/10', 'po10', 'po1', 'po2']}]},
               {'menu_name': 'Прогнать vlan до Мегафона (от vip.r7 до Gi2/1 на '
                             'S1M9)...',
                'switches': [{'device': 's1mr', 'to_ports': ['Gi6/10', 'po10']},
                             {'device': 's6m9',
                              'to_ports': ['Gi6/10', 'po10', 'po8']},
                             {'device': 's1m9', 'to_ports': ['Gi2/1', 'po3']}]},
               {'menu_name': 'Прогнать vlan до Мегафона (от vip.r7 до Gi2/2 на '
                             'S1M9)...',
                'switches': [{'device': 's1mr', 'to_ports': ['Gi6/10', 'po10']},
                             {'device': 's6m9',
                              'to_ports': ['Gi6/10', 'po10', 'po8']},
                             {'device': 's1m9',
                              'to_ports': ['Gi2/2', 'po3']}]}]}
'''