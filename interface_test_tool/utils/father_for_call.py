#! python2
#coding: utf-8
import sys
import os
# #=========================================================
# #无论哪个文件执行，只要执行，就把当前路径切换到脚本的根目录
# #目前执行，只有两地，enter和脚本，如果后续还有其他的执行地可以在这个地方扩展
if __name__ == '__main__':
    if "interfaces" in os.getcwd():
        os.chdir("../../../..")
        sys.path.append(".")
    else:
        os.chdir("..")
        sys.path.append(".")
#=========================================================
import requests
import json
import copy
import importlib

from utils.gen_signature import Gen_Signature
from utils.get_time import Get_Time
from utils.data_read import Data_Read
from utils.choose_server_according_environment_flag import Choose_Server
from utils.gen_url import Gen_Url
from utils.request_url import Request_Url
from utils.result_judge import Result_Judge
from utils.dynamic_read_and_gen_param import Dynamic_Read_And_Gen_Param
from utils.all_kinds_of_data_read import All_Kinds_Of_Data_Read
from utils.for_call_log_output import For_Call_Log_Output
from utils.databases_init import Databases_Init
from utils.databases_operation import Databases_Operation

class Father_For_Call:

    def __init__(self):

       	pass
    def gen_All_Data(self,center_name=None, own_interface_name=None):
        #生成所有数据
        # try:
        all_data_dict = All_Kinds_Of_Data_Read().all_Kinds_Of_Data_Read(center_name=center_name, \
                                                                        # interface_name=self.interface_name, \
                                                                        own_interface_name=own_interface_name)

        if all_data_dict["msg"] == "success":
            all_data = all_data_dict["result"]
            self.global_config = all_data["global_config"]
            self.log_level = self.global_config["log_level"]
            self.environment_flag = self.global_config['environment_flag']
            if self.environment_flag not in ["0","1","2"]:
                self.environment_flag = "0" 
            self.default_data = all_data["default_data"]
            self.success_str = self.default_data["success_str"]
            self.interface_config = all_data["interface_config"]
            self.request_method = self.interface_config["request_method"]
            self.interface_url = self.interface_config["interface_url"]
            self.script_init_flag = self.default_data["script_init_flag"]
#=================================================================================

#===================================================================

        else:
            print("--%s--%s--gen all data fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return all_data_dict

        server_data_dict = Choose_Server().choos_Server(data_config_global=self.global_config, \
                                                        environment_flag=self.environment_flag)
        if server_data_dict['msg'] == "success":
            server_data = server_data_dict['result']
            self.server = server_data["server"]
            self.proxy = server_data["proxy"]
            self.dobbu_server = server_data.get("dobbu_server", None)
            self.dobbu_port = server_data.get("dobbu_port", None)
            #=========================================================
             #=========================================================
            return {"msg":"success"}
        else:
            print("--%s--%s--choos_Server fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return server_data_dict

        # except Exception as f:
        #     print("--%s--%s--gen data error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     print("--%s--%s--python error is: %s" % (self.__class__.__name__, sys._getframe().f_code.co_name,f))
        #     return {
        #             "msg":"error"
        #     }

    def default_test(self,**kwargs):
        '''
        本接口用来生成请求参数
        gen
        '''
        # try:
        gen_all_data_dict = self.gen_All_Data(center_name=self.center_name, own_interface_name=self.own_interface_name)
        if gen_all_data_dict["msg"] == "success":
            dynamic_param_dict = Dynamic_Read_And_Gen_Param().dynamic_Read_And_Gen_Param(kwargs=kwargs, \
                                                                                         interface_config=self.interface_config, \
                                                                                         default_data=self.default_data, \
                                                                                         # exec_from=self.exec_from,\
                                                                                         # interface_name=self.interface_name,\
                                                                                         data_config_global=self.global_config)
            if dynamic_param_dict["msg"] == "success":
                param_current = dynamic_param_dict["result"]
                files = dynamic_param_dict["files"]
            else:
                print("--%s--%s--gen dynamic_param_dict fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                return dynamic_param_dict
        else:
            print("--%s--%s--gen all data fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return gen_all_data_dict
        # except Exception as a:
        #     print("--%s--%s--Dynamic error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     print("--%s--%s--python error is: %s" % (self.__class__.__name__, sys._getframe().f_code.co_name,a))
        #     return {
        #             "msg":"error"
        #     }

#========================================================================
#生成url
        try:
        
            url_dict = Gen_Url().gen_Url(request_method=self.request_method, \
                                         param_current=param_current, \
                                         server=self.server, \
                                         interface_url=self.interface_url)
            if url_dict["msg"] == "success":
                url = url_dict["result"]
            else:
                print("--%s--%s--gen_Url error,success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                return url_dict
        except Exception as b:
            print("--%s--%s--gen url error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("--%s--%s--python error is: %s" % (self.__class__.__name__, sys._getframe().f_code.co_name,b))
            return {
                    "msg":"error"
            }
        
#========================================================================
#========================================================================
# 根据参数确定请求次数
# 被当作依赖调用的时候，默认数据的执行次数，一定要为1，否则会出问题
        if kwargs.get("times", False):
        	self.times = int(kwargs["times"])
        elif self.default_data.get("times", False):
       		self.times = int(self.default_data["times"])
       	else:
       		self.times = 1
#========================================================================
#========================================================================
#访问url
        for i in range(self.times):
            try:
                res_dict = Request_Url().request_Url(request_method=self.request_method, \
                                                     proxy=self.proxy, \
                                                     param_current=param_current,\
                                                     url=url, \
                                                     interface_config=self.interface_config,\
                                                     files=files,\
                                                     log_level=self.log_level,\
                                                     dobbu_port=self.dobbu_port,\
                                                     dobbu_server=self.dobbu_server)
                if res_dict["msg"] == "success":
                    res = res_dict["result"]
                else:
                    print("--%s--%s--request_Url error,success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                    return res_dict 
            except Exception as c:
                print("--%s--%s--request url error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                print("--%s--%s--python error is: %s" % (self.__class__.__name__, sys._getframe().f_code.co_name,c))
                return {
                        "msg":"error"
                }
    #========================================================================
    #========================================================================
    #判断结果, 
    #如果成功了，返回字典，由上一层调用者获取结果
    #如果失败了，也返回字典，错误结果由上一层返回
            # try:
            judge_dict = Result_Judge().result_Judge(success_str=self.success_str, \
                                                     res=res,\
                                                     class_name=self.__class__.__name__, \
                                                     method_name=sys._getframe().f_code.co_name,\
                                                     log_level=self.log_level,\
                                                     url=url,\
                                                     param_current=param_current)
    #========================================================================

            database_instance_dict_dict = Databases_Init().init_Databases(script_init_flag=self.script_init_flag,\
                                                                              database_instance_dict=self.database_instance_dict,\
                                                                              global_data=self.global_config)
            if database_instance_dict_dict["msg"] == "success":
                self.database_instance_dict = database_instance_dict_dict["result"]

                    #print(self.database_instance_dict)
            else:
                return database_instance_dict_dict

        #========================================================================
            #数据库操作
            Databases_Operation().operation_Database(global_data=self.global_config,\
                                                    database_instance_dict=self.database_instance_dict,\
                                                    kwargs=kwargs,\
                                                    default_data=self.default_data,\
                                                    log_level=self.log_level)


        return judge_dict


# if __name__ == '__main__':
#     ss = Get_Access_Token()
#     asd = ss.default_test()

