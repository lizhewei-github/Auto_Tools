#! python2
#coding: utf-8
import sys

from utils.config_file_path import Config_File_Path
from utils.data_read import Data_Read
from utils.own_config_file_path import Own_Config_File_Path


class All_Kinds_Of_Data_Read:
    '''
    程序执行顺序，
    所有接口的调用都需要的数据
    1. 全局数据--读取当前环境地址，代理信息性能参数，公共依赖的接口名字和编号，以及返回结果下标
    2. 接口的配置数据--读取请求方法，接口地址，请求方法，请求参数，是否依赖，
    3. 默认参数，用于在没有参数输入的情况下，请求接口
    可选数据：
    1. 测试数据
    2. 性能数据
    3. log文件

    三种调用关系：
        测试接口调用被测接口
            测试接口的名字和被测接口的名字是相同的，exec数据和own读取的数据相同的数据
        被测接口调用依赖接口
            测试接口的名字和依赖接口不一样，测试接口数据已经保存在自己的进程中，依赖接口只要读取全局数据，自己的配合数据，自己的默认数据就可以
        依赖接口调用依赖接口
            依赖接口先被调用，它的数据已经被保存在自己的进程中，被依赖接口读取全局数据，自己的配合数据，自己的默认数据就可以

    这里面即读取了执行路径字典，也读取了本接口路径字典，实际上有一些数据是用不到的，但是为了以后扩容方便，就全部先保留了下来
    '''
    def __init__(self):
        self.default_data_list = ["test_data_test.yml","test_data_dev.yml","test_data_online.yml"]

    def all_Kinds_Of_Data_Read(self,center_name=None, own_interface_name=None):

        default_data_list = self.default_data_list
        # try:
        # exec_path_dict_dict = Config_File_Path().config_File_Path(exec_from=exec_from, interface_name=interface_name)
        # if exec_path_dict_dict["msg"] == "success":
        #     exec_path_dict = exec_path_dict_dict["result"]

        # else:
        #     print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     print("--%s--%s--problem data is exec_path_dict_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     return exec_path_dict_dict
        #==========================================================================
        #确定当前文件对应的数据的路径
        own_path_dict_dict = Own_Config_File_Path().own_Config_File_Path(center_name=center_name, own_interface_name=own_interface_name)
        if own_path_dict_dict["msg"] == "success":
            own_path_dict = own_path_dict_dict["result"]
        else:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("--%s--%s--problem data is own_path_dict_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return own_path_dict_dict
        #==========================================================================
        #读取全局配置文件
        data_config_globle_dict = Data_Read().yaml_Read(own_path_dict['global_config_path'])
        if data_config_globle_dict["msg"] == "success":
            data_config_globle = data_config_globle_dict["result"][0]

        else:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("--%s--%s--problem data is data_config_globle_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return data_config_globle_dict
        #==========================================================================
        interface_config_dict = Data_Read().yaml_Read(own_path_dict["own_interface_config_path"])
        if interface_config_dict["msg"] == "success":
            interface_config = interface_config_dict["result"][0]
            request_method = interface_config["request_method"]
        else:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("--%s--%s--problem data is interface_params_list_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return interface_config_dict
        #==========================================================================
        #读取环境标识
        environment_flag = data_config_globle['environment_flag']
        if environment_flag not in ["0","1","2"]:
            environment_flag = "0"
        #==========================================================================
        #读取测试数据
        func_test_data_dict = Data_Read().yaml_Read(own_path_dict['func_data_path']+default_data_list[int(environment_flag)])
        if func_test_data_dict["msg"] == "success":
            func_test_data = func_test_data_dict["result"][0]
        else:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("--%s--%s--problem data is test_data_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return test_data_dict
        #==========================================================================
        #获取自己对应环境的默认数据
        default_data_dict = Data_Read().yaml_Read("%s%s" % (own_path_dict["own_default_data_path"], \
                                                            default_data_list[int(environment_flag)]))
        if default_data_dict["msg"] == "success":
            default_data = default_data_dict["result"][0]
        else:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("--%s--%s--problem data is default_data_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return default_data_dict
         #==========================================================================
         #先声明两个返回变量，以免返回的时候报错误
        pref_python_get_test_data = None
        pref_python_post_test_data = None
        pref_siege_get_test_data = None
        pref_siege_post_test_data = None
         #如果请求方法是get，读取get的数据
        if request_method == "get":
            pref_python_get_test_data_dict = Data_Read().yaml_Read(own_path_dict['pref_python_data_get_path']+default_data_list[int(environment_flag)])
            if pref_python_get_test_data_dict["msg"] == "success":
                pref_python_get_test_data = pref_python_get_test_data_dict["result"][0]
            else:
                print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                print("--%s--%s--problem data is pref_python_get_test_data_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                return pref_python_get_test_data_dict
            #==================================================================
            pref_siege_get_test_data_dict = Data_Read().yaml_Read(own_path_dict['pref_siege_data_get_path']+default_data_list[int(environment_flag)])
            if pref_siege_get_test_data_dict["msg"] == "success":
                pref_siege_get_test_data = pref_siege_get_test_data_dict["result"][0]
            else:
                print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                print("--%s--%s--problem data is pref_siege_get_test_data_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                return pref_siege_get_test_data_dict
        #==========================================================================
         #如果请求方法是post，读取post的数据
        elif "post" in request_method:
            pref_python_post_test_data_dict = Data_Read().yaml_Read(own_path_dict['pref_python_data_post_path']+default_data_list[int(environment_flag)])
            if pref_python_post_test_data_dict["msg"] == "success":
                pref_python_post_test_data = pref_python_post_test_data_dict["result"][0]
            else:
                print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                print("--%s--%s--problem data is pref_python_post_test_data_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                return pref_python_post_test_data_dict
            #==================================================================
            pref_siege_post_test_data_dict = Data_Read().yaml_Read(own_path_dict['pref_siege_data_post_path']+default_data_list[int(environment_flag)])
            if pref_siege_post_test_data_dict["msg"] == "success":
                pref_siege_post_test_data = pref_siege_post_test_data_dict["result"][0]
            else:
                print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                print("--%s--%s--problem data is pref_siege_post_test_data_dict" % (self.__class__.__name__, sys._getframe().f_code.co_name))
                return pref_siege_post_test_data_dict

        else:
            print("--%s--%s--request_method error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return {"msg":"error"}

        interface_pref_log_path = own_path_dict["interface_pref_log_path"]
        interface_pref_siege_log_path = own_path_dict["data_for_siege_content"]
        #recover_path_deep = own_path_dict["recover_path_deep"]
        #==========================================================================
        #读取接口的配置文件
        interface_log_path = own_path_dict["interface_log_path"]
        return {
                "msg":"success",
                "result":
                        {
                            #全局配置数据
                            "global_config":data_config_globle,
                            #执行接口的功能测试数据
                            "func_test_data":func_test_data,
                            #本接口的默认数据
                            "default_data":default_data,
                            #执行接口的性能数据
                            "pref_python_get_test_data": pref_python_get_test_data,
                            #执行接口的性能数据
                            "pref_python_post_test_data": pref_python_post_test_data,
                            #执行接口siege性能数据
                            "pref_siege_get_test_data": pref_siege_get_test_data,
                            #执行接口siege性能数据
                            "pref_siege_post_test_data": pref_siege_post_test_data,
                            #本接口的配置文件
                            "interface_config":interface_config,
                            #执行接口的测试结果路径
                            "interface_log_path":interface_log_path,
                            #执行接口的性能log路径
                            "interface_pref_log_path":interface_pref_log_path,
                            "data_for_siege_content": interface_pref_siege_log_path,


                        }

                }
        # except Exception as f:
        #     print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     print("python error is: %s" % f)
        #     return {
        #             "msg":"error"
        #     }


    def main(self):
        pass

if __name__ == "__main__":
    ss = All_Kinds_Of_Data_Read()
    ss.main()