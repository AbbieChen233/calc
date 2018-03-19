#!/usr/bin/env python3

import csv
import sys

class Config:
	def __init__(self,configfile):
		self._config = {}
		with open(configfile) as fopen:
			for row in fopen:
				row = row.strip()
				data = row.split(' = ')
				self._config[data[0]] = data[1]
				

	def get_config(self,str):
		return self._config[str]

#file = Config("test.cfg")
#print(file.get_config('JiShuL'))

class UserData:
	def __init__(self,userdatafile):
		self._userdata = {}
		with open(userdatafile,'r') as fopen:
			for row in fopen:
				row = row.strip()
				data = row.split(',')
				self._userdata[data[0]] = data[1]
			print(self._userdata)

	def calculator(self,employee_id,configfile):
		config = Config(configfile)
		self.employee_id = employee_id
		salary = float(config.get_config(self.employee_id))
		self.shebao_rate = float(config.get_config('YangLao')) + float(config.get_config('YiLiao')) + float(config.get_config('ShiYe')) + float(config.get_config('GongShang')) + float(config.get_config('ShengYu')) + float(config.get_config('GongJiJin'))


		try:
			if isinstance(salary,float) == False:
				raise ValueError()
			else:
				if salary >= float(config.get_config('JiShuL')) and salary <= float(config.get_config('JiShuH')):
					self.salary = salary * (1-self.shebao_rate)
					self.shebao = salary * self.shebao_rate

				elif salary < float(config.get_config('JiShuL')):
					self.salary = float(config.get_config('JiShuL')) * (1-self.shebao_rate)
					self.shebao = float(config.get_config('JiShuL')) * self.shebao_rate

				elif salary > float(config.get_config('JiShuH')):
					self.salary = float(config.get_config('JiShuH')) * (1-self.shebao_rate)
					self.shebao = float(config.get_config('JiShuH')) * self.shebao_rate

				self.salary = self.salary - 3500
				if self.salary <= 0:
					self.tax = 0
				elif self.salary > 0 and self.salary <= 1500:
					self.tax = self.salary * 0.03

				elif self.salary > 1500 and self.salary <= 4500:
					self.tax = self.salary * 0.1 - 105

				elif self.salary > 4500 and self.salary <= 9000:
					self.tax = self.salary * 0.2 - 555

				elif self.salary > 9000 and self.salary <= 35000:
					self.tax = self.salary * 0.25 - 1005

				elif self.salary > 35000 and self.salary <= 55000:
					self.tax = self.salary * 0.3 - 2755

				elif self.salary > 55000 and self.salary <= 80000:
					self.tax = self.salary * 0.35 - 5505

				elif self.salary > 80000:
					self.tax = self.salary * 0.45 - 13505

			salary_list = []
			salary_list.append(self.employee_id)
			salary_list.append(salary)
			salary_list.append(self.shebao)
			salary_list.append(self.salary)
			salary_list.append(self.tax)
			return salary_list
			
	def dumptofile(self,salary_list,outputfile):
		if isinstance(salary_list,list):
			with open(outputfile,'a') as fopen:
				csv_reader = csv.reader(fopen)
				csv_reader.writerow(salary_list)
			
if __name__ == '__main__':
	if len(sys.argv) < 2:
		raise ValueError()
	else:
		argvs = sys.argv[1:]
		index = sys.argv
			
	
	
	
	
	
	
	
	
	
	
	
	
	

