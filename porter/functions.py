import sys
import re
from multiprocessing.dummy import Pool as ThreadPool

exit_commands = ('q','exit','quit') 

def DoinParallel(function,iplist, threads=5):
    pool = ThreadPool(threads)
    results = pool.map(function, iplist)
    pool.close()
    pool.join()
    return results


def choose_an_item(input_li,menu_item):
	''' simple_menu inpit: list of dicts, with menu_item for show in menu'''
	modtext = "Введите номер из меню (q - выход): "
	while True:
		for i in range(len(input_li)):
#			print (idx,item)
			print("\t",i+1,"\t", input_li[i][menu_item])
		a = input(modtext)
		if a:
			if a.lower() in exit_commands:
				print('Bye!')
				sys.exit()
			try:
				a = int(a) - 1
				if a in range(len(input_li)):
					# for i in range(len(input_li)):
					# 	if int(a) == i:
					result = input_li[a]
	#				print(result[menu_item]," был выбран ")
					return result
				else:
					print(" используйте номер из меню!\n ")
			except ValueError:	
					print('используйте цифры!')
		else:
			continue

def setvlanid():
	'''returns vlanid if it correct'''
	while True:
		a = input('Задайте vlan id("q"-выход): ')
		if a.lower() in exit_commands:
			print('Bye!')
			sys.exit()
		try:
			a = int(a)
			if a in range(4097):
				return a
			else:
				print("vlan id должен быть диапазоне 0-4094")	
		except ValueError:
			print("Введите целочисленный номер (0-4094")

def setname(output,minl = 9,maxl = 40):
	while True:
		name = input(" введите " + output + '("q"-выход): ').replace(" ","")
		if name.lower() in exit_commands:
			print('Bye!')
			sys.exit()
		if len(name) > minl and len(name) < maxl:
			r = re.compile('^[a-zA-Z0-9-_]+$')
			#r = re.compile('\w+')
			if r.match(name):
				return name
			else:	
				print('\n Неверный формат имени!\nРазрешены только латинские буквы, знаки "-", "_" и цифры!\n')
				continue
		print(' Ошибка! Количество знаков должно быть от {} до {} '.format(minl+1,maxl))			


def confirm(s):
	print(str(s))
	yes = ('y','yes')
	no = ('n','no')
	while True:
		try:
			q = input('(y-да/n-нет):')
			if q.lower() in yes:
				return True
			elif q.lower() in no:
				return False
			else:
				print(' Введите "y" или "n"')
				continue
		except:
			continue
