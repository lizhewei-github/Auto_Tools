#! python2
#coding: utf-8

import sys
import os
#=========================================================
#无论哪个文件执行，只要执行，就把当前路径切换到脚本的根目录
#目前执行，只有两地，enter和脚本，如果后续还有其他的执行地可以在这个地方扩展
if __name__ == '__main__':
    if "interfaces" in os.getcwd():
        os.chdir("../../../..")
        sys.path.append(".")
    else:
        os.chdir("..")
        sys.path.append(".")
#=========================================================
import json
import requests
import time
import random 

from utils.data_read import Data_Read
from utils.gen_signature import Gen_Signature
from utils.dynamic_read_and_gen_param import Dynamic_Read_And_Gen_Param
from utils.all_kinds_of_data_read import All_Kinds_Of_Data_Read
from utils.gen_url import Gen_Url
from utils.choose_server_according_environment_flag import Choose_Server


class Father_Siege_Test:

    def __init__(self):

        pass
#========================================================================
#========================================================================
#读取所有参数
    def gen_All_Data(self,center_name=None,own_interface_name=None):

        all_data_dict = All_Kinds_Of_Data_Read().all_Kinds_Of_Data_Read(center_name=center_name, \
                                                                        own_interface_name=own_interface_name)
        if all_data_dict["msg"] == "success":
            all_data = all_data_dict["result"]
            #读取全局数据
            self.global_config = all_data["global_config"]
            self.default_data = all_data["default_data"]
            #读取接口配置数据
            self.interface_config = all_data["interface_config"]
            #================================================================
            #================================================================
            #根据接口配置数据读取请求方法
            self.request_method = self.interface_config["request_method"]
            #根据请求方法读取，get post方法对应的pref数据
            if self.request_method == "get":
                self.pref_siege_test_data = all_data["pref_siege_get_test_data"]
            elif self.request_method == "post":
                self.pref_siege_test_data = all_data["pref_siege_post_test_data"]
            #读取log标识
            self.log_level = self.global_config["log_level"]
            #读取环境标识，用于确认请求地址和代理
            self.environment_flag = self.global_config['environment_flag']
            if self.environment_flag not in ["0","1","2"]:
                self.environment_flag = "0" 
            #读取请求方法
            self.request_method = self.interface_config["request_method"]
            #读取请求url
            self.interface_url = self.interface_config["interface_url"]
            #读取性能测试结果路径
            self.interface_pref_log_path = all_data["interface_pref_log_path"]
            #读取siege性能测试结果中转路径
            self.interface_pref_siege_log_path = all_data["data_for_siege_content"]
            #在性能测试的数据中随机选区一组数据

            self.kwargs = random.choice(self.pref_siege_test_data)
 
        else:
            print("--%s--%s--gen all data fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return all_data_dict
#========================================================================
#========================================================================
#读取服务器信息
#Choose_Server().choos_Server这个里面的代理方法是可以自定义的，也就是以后服务器和代理发生变化的花
#只需要调整，这个类里面输入参数对应的值就就可以了， 其他的代码都不需要修改
        server_data_dict = Choose_Server().choos_Server(data_config_global=self.global_config, \
                                                        environment_flag=self.environment_flag)
        if server_data_dict['msg'] == "success":
            server_data = server_data_dict['result']
            #确定请求地址，和方法
            self.server = server_data["server"]
            self.proxy = server_data["proxy"]
            return {"msg":"success"}
        else:
            print("--%s--%s--choos_Server fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return server_data_dict
#========================================================================
#========================================================================


    def pref_test(self):
        PASS = 0
        TOTAL = 0
        #外部读取进来的数据kwargs
        dynamic_param_dict = Dynamic_Read_And_Gen_Param().dynamic_Read_And_Gen_Param(kwargs=self.kwargs, \
                                                                                     interface_config=self.interface_config, \
                                                                                     default_data=self.default_data, \
                                                                                     data_config_global=self.global_config)
        if dynamic_param_dict["msg"] == "success":
            param_current = dynamic_param_dict["result"]


        else:
            print("--%s--%s--gen dynamic_param_dict fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return dynamic_param_dict
        # else:
        #     print("--%s--%s--gen all data fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     return gen_all_data_dict

#========================================================================
#========================================================================

        url_dict = Gen_Url().gen_Url(request_method=self.request_method, \
                                     param_current=param_current, \
                                     server=self.server, \
                                     interface_url=self.interface_url)
        if url_dict["msg"] == "success":
            url = url_dict["result"]
        else:
            print("--%s--%s--gen_Url error,success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return url_dict
#========================================================================
#========================================================================
        data_for_siege_content = open(self.interface_pref_siege_log_path, "w")
        #请求方法，请求参数，请求url
        data_for_siege_content.write("request_method:---%s" % self.request_method+'\n')
        data_for_siege_content.write("params:---%s" % param_current+'\n')
        data_for_siege_content.write("url:---%s" % url+'\n')
        data_for_siege_content.close()
        print("request_method:---%s" % self.request_method)
        print("params:---%s" % param_current)
        print("url:---%s" % url)
#========================================================================
#先生成全部参数，参数生成成功了之后，调用pref_test方法   
    def main(self):
        gen_all_data_dict = self.gen_All_Data(center_name=self.center_name, own_interface_name=self.own_interface_name)
        if gen_all_data_dict["msg"] == "success": 
            self.pref_test()
        else:
            return {"msg":"error"}
#========================================================================
#========================================================================
# if __name__ == "__main__":

#     ss = Get_Access_Token_Siege_Test()

#     ss.main()
