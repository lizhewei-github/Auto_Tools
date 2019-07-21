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

from utils.data_read import Data_Read
from utils.get_now_time import Get_Time
#from user_center.interfaces.get_access_token.interface_for_call.get_access_token import Get_Access_Token
from utils.config_file_path import Config_File_Path
from utils.data_read_result_judge import Data_Read_Result_Judge
from utils.test_script_log_write import Test_Script_Log_Write
from utils.class_name_upper import Class_Name_Upper
from utils.all_kinds_of_data_read1 import All_Kinds_Of_Data_Read
from utils.func_test_log_output import Func_Test_Log_Output
from utils.databases_init import Databases_Init


class Father_Func:
    def __init__(self):

        pass
    def gen_All_Data(self,center_name=None,own_interface_name=None):

        all_data_dict = All_Kinds_Of_Data_Read().all_Kinds_Of_Data_Read(center_name=self.center_name, \
                                                                        own_interface_name=self.own_interface_name)

        if all_data_dict["msg"] == "success":
            all_data = all_data_dict["result"]
            self.global_config = all_data["global_config"]
            self.environment_flag = self.global_config['environment_flag']
            if self.environment_flag == "0":
                self.proxy = self.global_config['http_test']
            elif self.environment_flag == "1":
                self.proxy = self.global_config['http_dev']
            elif self.environment_flag == "2":
                self.proxy = self.global_config['http_online']
            else:
                pass
            self.func_test_data = all_data["func_test_data"]["test_data"]
            self.func_test_times = all_data["func_test_data"]["times"]
            self.interface_config = all_data["interface_config"]
            self.test_init_flag = self.interface_config['test_init_flag']
            self.interface_log_content = open(all_data["interface_log_path"], "w")
            self.interface_log_content.write(Get_Time().get_Normal_Time()+"\n")
            self.log_level = self.global_config["log_level"]
            self.request_method = self.interface_config["request_method"]
            return {"msg":"success"}   
        else:
            print("--%s--%s--gen all data fail , success not in the return result" % (self.__class__.__name__, sys._getframe().f_code.co_name))

            return all_data_dict



    def func_Test(self):
        # try:
        
        database_instance_dict_dict = Databases_Init().init_Databases(test_init_flag=self.test_init_flag,\
                                                                      database_instance_dict=self.database_instance_dict,\
                                                                      global_data=self.global_config)
        if database_instance_dict_dict["msg"] == "success":
            database_instance_dict = database_instance_dict_dict["result"]
            #print(database_instance_dict)
        else:
            return database_instance_dict_dict


        for i in range(int(self.func_test_times)):
            for data in self.func_test_data:
                self.count += 1
                self.description = data["description"]

                interface_class_name_dict = Class_Name_Upper().upper(self.interface_config["interface_name"])
                if interface_class_name_dict["msg"] == "success":
                    interface_class_name = interface_class_name_dict["result"]

                exec("from %s.interfaces.%s.interface_for_call.%s import %s" \
                    %(self.center_name, self.interface_config["interface_name"],\
                        self.interface_config["interface_name"],interface_class_name))


                result_dict = eval("%s(database_instance_dict=%s).default_test(%s)" % (interface_class_name, \
                                                                                    'database_instance_dict',\
                                                                                    '**data'))
                #如果返回得结果中包含了success或者fail那说明接口返回成功了。没有报错误，报了错误返回error
                if result_dict["msg"] == "success" or result_dict["msg"] == "fail":
                    result = result_dict["result"]
                    if data["success_str"] in str(result):
                        self.PASS += 1
                        Func_Test_Log_Output().func_Success_Output(result=result, \
                                                                   count=self.count, \
                                                                   description=self.description,\
                                                                   proxy=self.proxy,\
                                                                   result_dict=result_dict,\
                                                                   request_method=self.request_method,\
                                                                   log_level=self.log_level)
                    else:
                        self.FAIL += 1
                        if self.interface_log_content:
                            Test_Script_Log_Write().test_Case_Write(content=self.interface_log_content,\
                                                                    count=self.count,\
                                                                    data=data,\
                                                                    result_dict=result_dict,\
                                                                    module_name=self.__class__.__name__,\
                                                                    method=self.request_method,\
                                                                    proxy=self.proxy)
                        Func_Test_Log_Output().func_Fail_Output(center_name=self.center_name,\
                                                                data=data,\
                                                                result=result,\
                                                                count=self.count,\
                                                                description=self.description,\
                                                                proxy=self.proxy,\
                                                                result_dict=result_dict,\
                                                                request_method=self.request_method)
                        
                else:
                    print("--%s--%s--interface test fail, multi_Test error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                    return result_dict

        return {"msg":"success"}

        # except Exception as a:
        #     print("--%s--%s-- multi_Test error  please contact administrator" % (self.__class__.__name__,sys._getframe().f_code.co_name))
        #     print("python error is:%s" % a)
        #     return {
        #             "msg":"error"
        #             }
 

    def main(self):

        gen_all_data_res = self.gen_All_Data(center_name=None, own_interface_name=None)
        if gen_all_data_res["msg"] == "success":
            pass
        else:
            return gen_all_data_res

        multi_test_res = self.func_Test()
        if multi_test_res["msg"] == "success":

            if self.test_log_global:
                write_result_dict = Test_Script_Log_Write().test_Main_Write(content=self.test_log_global,\
                                                                            count=self.count,\
                                                                            PASS=self.PASS,\
                                                                            FAIL=self.FAIL,\
                                                                            interface_name=self.__class__.__name__)
                if write_result_dict["msg"] == "success":
                    return {
                        "msg": "success",
                        "result": ["%s" % self.__class__.__name__,self.count, self.PASS, self.FAIL]
                    }
                else:
                    print("--%s--%s-- test_Main_Write error " % (self.__class__.__name__,sys._getframe().f_code.co_name))
                    return write_result_dict

            else:
                return {
                            "msg": "success",
                            "result": ["%s" % self.__class__.__name__,self.count, self.PASS, self.FAIL]
                        }
        else:
            print("--%s--%s-- multi_Test return error " % (self.__class__.__name__,sys._getframe().f_code.co_name))
            return multi_test_res
                

# if __name__ == "__main__":
#     ss = Get_Access_Token_Func_Test()
#     ss.main()