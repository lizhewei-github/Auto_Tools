#! python2
#coding: utf-8
import sys
import copy

from utils.class_name_upper import Class_Name_Upper
from utils.get_now_time import Get_Time
from utils.gen_signature import Gen_Signature



class Dynamic_Read_And_Gen_Param:

    def __init__(self):
        self.param_current = {}
        #最终返回的参数
        self.center_name = None
        self.dependency_interface_dict = {}
        #字典结构
        #建  当前参数的名字
        #值  [依赖接口名字,结果列表下标]
        self.dependency_param_dict = {}
        #字典结构
        #建  当前参数的名字
        #值  [依赖参数的名字,结果列表下标]
        self.common_dependency_interface_dict = {}
        #字典结构
        #建  当前参数的名字
        #值  [公共依赖接口名字(只有签名的名字有意义，其他名字只是个说明),公共依赖的编号]
        self.mid_result_dict = {}
        #字典结构
        #建  当前参数的名字
        #值  请求接口之后，返回的完整结果

    def dynamic_Read_And_Gen_Param(self, kwargs=None,\
                                   default_data=None,\
                                   interface_config=None,\
                                   data_config_global=None):
        '''
        #kwargs=None,default_data=None,interface_config=None
        #根据上面三个参数来确定，目前接口中传了那些参数，没传哪些参数，传了就用，没传就用默认
        '''
        self.center_name = data_config_global["center_name"]
        log_level = data_config_global["log_level"]
        if kwargs:
            sync_data_flag = kwargs.get("sync_data_flag",False)
        else:
            sync_data_flag = default_data.get("sync_data_flag",False)
        # try:

        for interface_params in interface_config["params"]:
            for param_name,dependency_interface_name in interface_params.items():
                if param_name.startswith("call"):
                    self.dependency_interface_dict[param_name] = dependency_interface_name.split("-")[1:]
                    continue
                elif kwargs.has_key(param_name):
                    self.param_current[param_name] = kwargs[param_name]
                    if dependency_interface_name.startswith("yes_interface"):
                        self.dependency_interface_dict[param_name] = dependency_interface_name.split("-")[1:]
                    elif dependency_interface_name.startswith("comm"):
                        self.common_dependency_interface_dict[param_name] = dependency_interface_name.split("-")[1:]
                    elif dependency_interface_name.startswith("yes_param"):
                        self.dependency_param_dict[param_name] = dependency_interface_name.split("-")[1:]
                    else:
                        pass

                else:
                    self.param_current[param_name] = default_data[param_name]
                    if dependency_interface_name.startswith("yes_interface"):
                        self.dependency_interface_dict[param_name] = dependency_interface_name.split("-")[1:]
                    elif dependency_interface_name.startswith("comm"):
                        self.common_dependency_interface_dict[param_name] = dependency_interface_name.split("-")[1:]
                    elif dependency_interface_name.startswith("yes_param"):
                        self.dependency_param_dict[param_name] = dependency_interface_name.split("-")[1:]
                    else:
                        pass

        # print(self.dependency_interface_dict)
        # print(self.common_dependency_interface_dict)

        #处理字典，把签名放到最后
        dependency_list = self.dependency_interface_dict.items()
        for i in dependency_list:
            if i[0] == "signature":
                dependency_list.append(dependency_list.pop(i))

        for key_name, class_name in dependency_list:
            #获取类名字的大写以及结果的下标
            class_name_upper = Class_Name_Upper().upper(class_name[1])
            if class_name_upper["msg"] == "success":
                class_name_upper = class_name_upper["result"]
            dependency_result_index = int(class_name[2])


            if sync_data_flag == True and kwargs:
                self.dyncmic_Call_Func_inner(class_name=class_name,\
                                            kwargs=kwargs,\
                                            key_name=key_name,\
                                            class_name_upper=class_name_upper,\
                                            # exec_from=exec_from,\
                                            # interface_name=interface_name,\
                                            default_data=default_data,\
                                            dependency_result_index=dependency_result_index,\
                                            func_data='**kwargs')

            elif sync_data_flag == True and default_data:
                self.dyncmic_Call_Func_inner(class_name=class_name,\
                                            kwargs=kwargs,\
                                            key_name=key_name,\
                                            class_name_upper=class_name_upper,\
                                            # exec_from=exec_from,\
                                            # interface_name=interface_name,\
                                            default_data=default_data,\
                                            dependency_result_index=dependency_result_index,\
                                            func_data='**default_data')
            elif sync_data_flag == False:
                self.dyncmic_Call_Func_inner(class_name=class_name,\
                                            kwargs=kwargs,\
                                            key_name=key_name,\
                                            class_name_upper=class_name_upper,\
                                            # exec_from=exec_from,\
                                            # interface_name=interface_name,\
                                            default_data=default_data,\
                                            dependency_result_index=dependency_result_index,\
                                            func_data='**empty_dict')

        # print(self.mid_result_dict)
        # print("=======")
        #根据配置文件中的参数依赖关系，读取接口保存的数据
        if self.dependency_param_dict:
            for nname, vvalue in self.dependency_param_dict.items():
                self.param_current[nname] = self.mid_result_dict[vvalue[0]][int(vvalue[1])]

        for com_keyname,com_index in self.common_dependency_interface_dict.items():

            if com_index[1] == "100" and self.param_current[com_keyname] == "normal":
                from utils.paramiko_operation import Paramiko
                code_dict = Paramiko().oauth_Get_Code(global_data=data_config_global)

                if code_dict["msg"] == "success":
                    code = code_dict["result"]
                    self.param_current[com_keyname] = code
                else:
                    return code_dict 

            elif com_index[1] == "101" and self.param_current[com_keyname] == "normal":
                self.param_current[com_keyname] = Get_Time().get_Int_Str_Time()


            #用户中心和设备中心签名
            elif com_index[1] == "202" and self.param_current[com_keyname] == "normal":
                sig_dict = copy.deepcopy(self.param_current)
                sig_dict.pop(com_keyname)
                signature_dict = Gen_Signature().gen_Signature_User_Device_Center(sig_dict)
                if signature_dict["msg"] == "success":
                    self.param_current[com_keyname] = signature_dict["result"]
                else:
                    print("--%s--%s--dynamic 10 gen_signature result error"% (self.__class__.__name__, sys._getframe().f_code.co_name))
                    return {
                            signature_dict
                    }
            #产测签名
            elif com_index[1] == "203" and self.param_current[com_keyname] == "normal":
                sig_dict = copy.deepcopy(self.param_current)
                sig_dict.pop(com_keyname)
                signature_dict = Gen_Signature().gen_Signature_Product_Auth(sig_dict)
                if signature_dict["msg"] == "success":
                    self.param_current[com_keyname] = signature_dict["result"]
                else:
                    print("--%s--%s--dynamic 11 gen_signature result error"% (self.__class__.__name__, sys._getframe().f_code.co_name))
                    return {
                            signature_dict
                    }
            #产测图片接口签名
            elif com_index[1] == "204" and self.param_current[com_keyname] == "normal":
                sig_dict = copy.deepcopy(self.param_current)
                sig_dict.pop(com_keyname)
                signature_dict = Gen_Signature().gen_Signature_Product_Auth_Image(sig_dict)
                if signature_dict["msg"] == "success":
                    self.param_current[com_keyname] = signature_dict["result"]
                else:
                    print("--%s--%s--dynamic 11 gen_signature result error"% (self.__class__.__name__, sys._getframe().f_code.co_name))
                    return {
                            signature_dict
                    }

            #用户中心oauth签名
            elif com_index[1] == "205" and self.param_current[com_keyname] == "normal":
                sig_dict = copy.deepcopy(self.param_current)
                sig_dict.pop(com_keyname)
                if kwargs:
                    signature_dict = Gen_Signature().gen_Signature_User_Center_Oauth(sig_dict,appsecret=kwargs["appSecret"])
                elif default_data:
                    signature_dict = Gen_Signature().gen_Signature_User_Center_Oauth(sig_dict,appsecret=default_data["appSecret"])
                else:
                    pass
                if signature_dict["msg"] == "success":
                    self.param_current[com_keyname] = signature_dict["result"]
                else:
                    print("--%s--%s--dynamic 11 gen_signature result error"% (self.__class__.__name__, sys._getframe().f_code.co_name))
                    return {
                            signature_dict
                    }

            else:
                pass

        if interface_config["is_upload_file"] == True:
            if kwargs:
                if kwargs["image_file"].values()[0] == "empty":
                    files = {kwargs["image_file"].keys()[0]: None}
                else:
                    files = {kwargs["image_file"].keys()[0]: (open(kwargs["image_file"].values()[0], "rb"))}
            elif default_data:
                if default_data["image_file"].values()[0] == "empty":
                    files = {default_data["image_file"].keys()[0]: None}
                else:
                    files = {default_data["image_file"].keys()[0]: (open(default_data["image_file"].values()[0], "rb"))}

        else:
            files = None

            
        return {
                "msg":"success",
                "result":self.param_current,
                "files": files
                }   

    def dyncmic_Call_Func_inner(self,class_name=None, \
                                kwargs=None,\
                                key_name=None,\
                                class_name_upper=None,\
                                empty_dict = {},\
                                default_data=None,\
                                dependency_result_index=None,\
                                func_data=None):
        if self.dependency_interface_dict:          
            for key, value in self.dependency_interface_dict.items():
                class_name_upper_name_dict = Class_Name_Upper().upper(value[1])
                if class_name_upper_name_dict["msg"] == "success":
                    class_name_upper_name = class_name_upper_name_dict["result"]
                else:
                    return class_name_upper_name_dict

                #=====================================================================================================
                exec("from %s.interfaces.%s.interface_for_call.%s import %s" %(value[0], value[1],value[1],class_name_upper_name))

        if key_name.startswith("call"):
            result = eval("%s().%s(%s)" % (class_name_upper, \
                                         "default_test",\
                                         func_data))
            if result["msg"] == "success":
                pass
            else:
                print("--%s--%s--dynamic %s class result error"% (self.__class__.__name__, sys._getframe().f_code.co_name,class_name))

                return result
        elif self.param_current[key_name] == "normal":
            result = eval("%s().%s(%s)" % (class_name_upper, \
                                       "default_test",\
                                       func_data))
            
            if result["msg"] == "success":
                self.param_current[key_name] = result["result"].split('"')[int(dependency_result_index)]
                self.mid_result_dict[key_name] = result["result"].split('"')
            else:
                print("--%s--%s--dynamic class result error"% (self.__class__.__name__, sys._getframe().f_code.co_name))
                print(result)
                return result  

if __name__ == "__main__":
    ss = Dynamic_read_and_gen_param()
    ss.main()


