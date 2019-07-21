#! python2
#coding: utf-8

import paramiko

# ip="10.30.10.32"
# port="22"
# user_name="root"
# password="yunzhisheng"

class Paramiko:

	def __init_(self):
		self.client = None

	def get_Instance(self):

		self.client = paramiko.SSHClient()
		return self.client

	def connectting(self,instance=None, ip=None,port=None,user_name=None,password=None):
		instance.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		instance.connect(ip, port, user_name, password)
		

	def excute_Input(self, instance, command):
		stdin,stdout,stderr=instance.exec_command(command)
		return stdout.read()

	def oauth_Get_Code(self, global_data=None):
		environment_flag = global_data["environment_flag"]
		# try: 
		if environment_flag == "1":
			ip = global_data["linux_host_dev"]["ip"]
			port = global_data["linux_host_dev"]["port"]
			user_name = global_data["linux_host_dev"]["user_name"]
			password = global_data["linux_host_dev"]["password"]
			paramiko_instance = self.get_Instance()
			self.connectting(instance=paramiko_instance,ip=ip,port=port, user_name=user_name, password=password)
			#result = self.excute_Input(paramiko_instance, "cd /opt/tomcat8/logs && tail -n 4 catalina.out |grep code |awk -F '>' '{printf $2}'")
			result = self.excute_Input(paramiko_instance, "cd /opt/tomcat8/logs && tail -n 6 catalina.out | grep code | awk -F '>' '{printf $2}' ")
			print(result)
			return {
					"msg":"success",
					"result":result
			}
		elif environment_flag == "0" or environment_flag == "2" or environment_flag == "3":
			ip = global_data["linux_host_test"]["ip"]
			port = global_data["linux_host_test"]["port"]
			user_name = global_data["linux_host_test"]["user_name"]
			password = global_data["linux_host_test"]["password"]
			paramiko_instance = self.get_Instance()
			self.connectting(instance=paramiko_instance,ip=ip,port=port, user_name=user_name, password=password)
			result = self.excute_Input(paramiko_instance, "cd /home/wenpukun && tail -n 12 nohup.out |grep code |awk -F ',' '{printf $2}'|awk -F '=' {printf $2}")
			return {
					"msg":"success",
					"result":result
			}
		# except Exception as a:
		# 	print("paramiko error")
		# 	return {"msg":"error"}

if __name__ == '__main__':
	client = Paramiko()
	client.oauth_Get_Code()
	# paramiko_instance = client.get_instance()
	# client.connectting(paramiko_instance,"172.29.2.31",48022, "root", "yunzhishengtest@999")
	# client.excute_input(paramiko_instance, "ls -l")