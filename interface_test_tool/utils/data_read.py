#! python2
#coding: utf-8

#读取yaml 返回片列表
#读取txt  返回readlines列表
#读取json 返回json
import sys #这里只是一个对sys的引用，只能reload才能进行重新加载
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr 
reload(sys) #通过import引用进来时,setdefaultencoding函数在被系统调用后被删除了，所以必须reload一次
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde 
sys.setdefaultencoding('utf-8')
import yaml
import json


class Data_Read:

	def __init__(self):
		pass

	def yaml_Read(self, path=None):
		# try: 
		content = open(path, "r")
		data = yaml.load_all(content)
		return {
				"msg":"success",
				"result":list(data)
				}
		# except Exception as a:
		#  	print("--%s--%s-- yaml read file error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
		#  	return {
		#  			"msg": "error"
		#  			}

	def txt_Read(self, path=None):
		try:
			content = open(path, "r")
			data = content.readlines()
			content.close()
			return {
					"msg":"success",
					"result":data
					}
		except Exception as a:
			print("--%s--%s-- txt read file error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			return {
					"msg": "error",
					}	

	def json_Read(self, path=None):
		try:
			content = open(path,"r")
			data = json.load(content)
			content.close()
			return {
					"msg":"success",
					"result":data
					}
		except Exception as a:
			print("--%s--%s-- json read file error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			return {
					"msg": "error",
					}	


	def main(self):
		
		
		#self.txt_Read("../config/qwe.txt")
		path = "../dcs/test_data/get_weather_info/pref/get/test_data_online.yml"
		x = self.yaml_Read(path)
		print(x["result"][0])

if __name__ == '__main__':
	ss = Data_Read()
	ss.main()