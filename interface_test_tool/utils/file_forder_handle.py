#! python2
#coding: utf-8
import os 
import shutil
import sys 


class File_Folder_Handle:
	def __init__(self):
		pass

	def create_Full_Dir(self, reference_center_name=None,new_center_name=None):
		'''接受新中心的名字，创建完整目录结构，只是第一级'''
		#os.chdir("../..")
		os.chdir("..")
		print(os.getcwd())
		shutil.copytree(reference_center_name, new_center_name)
		os.chdir("./%s" % new_center_name)

		for dir_name in ["./config", "./interfaces", "./result", "./test_data"]:
			document_list = os.listdir(dir_name)
			for node in document_list:
				if os.path.isdir("%s/%s" % (dir_name,node)):
					shutil.rmtree("%s/%s" %(dir_name,node))
				else:
					pass

	def copy_Folder(self, source_folder_path=None, target_forder_path=None):
		'''接受原路径，目标路径，把所有文件都拷贝过去'''
		try:
			shutil.copytree(source_folder_path, target_forder_path)
			return {"msg":"success"}
		except Exception as a:
			print("--%s--%s-- yaml copy_Folder error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			return {
		 			"msg": "error"
		  			}

	def copy_Content(self, source_file_path=None, target_file_path=None):
		'''接受原文件名字，目标文件名字，把源文件的内容写入到目标文件中去'''
		try:
			source_content = open(source_file_path, "r")
			source_data = source_content.read()
			target_content = open(target_file_path, "w")
			target_content.write(source_data)
			source_content.close()
			target_content.close()
			return {"msg":"success"}
		except Exception as a:
			print("--%s--%s-- yaml copy_Content error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			return {
		 			"msg": "error"
		  			}

	def create_Folder(self, new_folder_name=None):
		'''接受文件夹路径名字创建文件夹'''
		try:
			os.makedirs(new_folder_name)
			return {"msg":"success"}
		except Exception as a:
			print("--%s--%s-- yaml create_Folder error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			return {
		 			"msg": "error"
		  			}

	def create_File(self, new_file_name=None):
		'''接受文件名字，创建文件'''
		try:
			os.mknod(new_file_name)
			return {"msg":"success"}
		except Exception as a:
			print("--%s--%s-- yaml create_File error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
			return {
		 			"msg": "error"
		  			}

	def main(self):
		self.create_Full_Dir(reference_center_name="user_center_all",new_center_name="new")


if __name__ == '__main__':
	ss = File_Folder_Handle()
	ss.main()