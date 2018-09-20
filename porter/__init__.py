#enforta. Work hard, earn less!
# Mamaev Alexandr 2018. First balls, made out of shit.
# fancarster@gmail.com

from .functions import *
from .cisco import *
from .cfg import *

#from pprint import pprint



def send_commands(settings,cmdlist):
	''' sends cmdlist to cisco  '''
	ip = settings['ip']
	name = settings['name']
	try:
		sw = cisco(ip,cisco_user,cisco_password)
#		sw.showclock()	
		result = sw.sendconfigcmd(cmdlist)		
		logger.info("{} : ({}) | Commands has been sent".format(name,ip))
		return True
	except Exception as e:
		logger.error("{} : ({}) | Commands has NOT been sent!!!\nERROR: {}".format(name,ip,e))
		return False

def send_vlan_to_switch(dic):
	''' for multiprocessing make config and send commands'''
	commands = make_vlan.format(**dic)
	for interface in dic['interfaces']:
		dic['interface'] = interface
		commands += add_vlan_to_if.format(**dic)
#	logger.debug("{} : Команды: {}".format(dic['name'],commands))
	cmdlist = []
	for c in commands.split('\n'):
		if c: cmdlist.append(c)
	return send_commands(dic,cmdlist)



def	append_vlans(input_li):
	''' append vlans to all ports of all devices from list of dictionaries'''
	global vlan_name
	
	vlan = setvlanid()
	vlan_name = setname(' имя влана ',3,20)
	params = []
	for device in input_li:
		name = device['device']
		print('свич {}\t({})\tпорты : {}'.format(my_devices[name]['name'],my_devices[name]['ip'],','.join(device['to_ports'])))
		dic = {
		'name' : my_devices[name]['name'],
		'ip' : my_devices[name]['ip'],
		'protocol' : my_devices[name]['protocol'],
		'port' : my_devices[name]['port'],
		'interfaces' : device['to_ports'],
		'vlan' : vlan,
		'case' : vlan_name			
		}
		logger.info("Adding VLAN{} ({}) to switch {} ({}) ports:{}...".format(vlan,vlan_name,my_devices[name]['name'],my_devices[name]['ip'],','.join(device['to_ports'])))
		params.append(dic)

	if confirm('добавить влан в порты на эти свичи?'):
		return DoinParallel(send_vlan_to_switch,params)
	else:
		print('Bye!')
		sys.exit()


def run_app(config_li):
	global my_devices
	my_devices = config_li['devices']
	templates_li = config_li['templates']
	chosen_template = choose_an_item(templates_li,'menu_item')
	sw_li = chosen_template['switches']

	chosen_switches_li = [d['device'] for d in sw_li]

	if all(devices in my_devices for devices in chosen_switches_li):
		logger.info(chosen_template["menu_item"])
		results = append_vlans(sw_li)
		if all(r for r in results):
			print('Команды залиты на все свичи')
		else:
			print('Команды не залиты далеко не везде. Смотри лог')
		print('The END')
	else:
		logger.error('Ошибка! Какой-то из свичей из шаблона не найден в devices!')


