#! python2
#coding: utf-8

import sys 

from data_read import Data_Read

class Own_Config_File_Path:
    '''此接口只是根据执行地点，和执行脚本本身的名字，来返回跟本身相关的数据
        注意，无论从哪里执行，读取的都是interface_for_call下接口名字对应的数据
        主要包括：
            1. 本接口默认数据路径 不包括文件名字
            2. 本接口测试数据路径 不包括文件名字
            3. 本接口性能测试数据路径 不包括文件名字
                性能数据包含get和post的数据
            4. 本接口配置文件路径 包括文件名
            5. 全局配置文件路径 包括文件名
        接口只管返回，但是调用者是否使用，就不管了
        own没有log路径
    '''
    def __init__(self):
        pass

    def own_Config_File_Path(self,center_name=None, own_interface_name=None):

        # try:
            #如果是None代表是当前路径
        if center_name == None:
            print("--Config_File_Path--config_File_Path--need two params，but 0 given")
            return {
                    "msg": "error"
                     }

        #如果是测试脚本
        else:

            return {
                        "msg":"success",
                        "result":
                            {
                            "global_config_path":"%s/config/global_config/global_config.yml" % center_name,
                            "func_data_path": "%s/test_data/%s/func/" % (center_name, own_interface_name),
                            "own_default_data_path": "%s/test_data/%s/default/" % (center_name, own_interface_name),
                            "pref_python_data_get_path": "%s/test_data/%s/pref/get/" % (center_name, own_interface_name),
                            "pref_python_data_post_path": "%s/test_data/%s/pref/post/" % (center_name, own_interface_name),
                            "pref_siege_data_get_path": "%s/test_data/%s/siege/get/" % (center_name, own_interface_name),
                            "pref_siege_data_post_path": "%s/test_data/%s/siege/post/" % (center_name, own_interface_name),
                            "own_interface_config_path": "%s/config/%s/interface_config.yml" % (center_name, own_interface_name),
                            "interface_log_path": "%s/result/%s/%s_result.txt" % (center_name,own_interface_name,own_interface_name),
                            "interface_pref_log_path": "%s/result/pref_test_result.txt"% center_name,
                            "error_log_path": "%s/result/error_log.log" % center_name,
                            "data_for_siege_content": "%s/siege/siege_data.txt" % center_name,
                            }
                        }
        # except Exception as f:
        #     print("--%s--%s--run error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     print("python error is :%s" % f)
        #     return {
        #             "msg":"error"
        #         }


    def main(self):
        #本地调试请打开上面本地调用，关闭入口调用
        print(self.config_File_Path())

if __name__ == "__main__":
    ss = Config_File_Path()
    ss.main()