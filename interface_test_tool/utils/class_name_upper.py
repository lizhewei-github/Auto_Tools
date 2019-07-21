#! python2
#coding: utf-8


class Class_Name_Upper:
	def __init__(self):
		pass

	def upper(self, data):
		try:
			str_list = data.split("_")
			result_list = []
			for i in str_list:
				result_list.append(i.capitalize())
			result_str = "_".join(result_list)
			return {
					"msg":"success",
					"result":result_str
					}
		except Exception as a:
			print("--%s--%s--tools error,maybe the input data is wrong type"% (self.__class__.__name__, sys._getframe().f_code.co_name))
			print("--%s--%s--request a str" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			print("--%s--%s--input data is:" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			print("-->"+str(data))
			print("python error is :%s" % a)
			return {
					"msg":"error"
					}   

if __name__ == "__main__":
	ss = Class_Name_Upper()
	print(ss.upper("script_data"))