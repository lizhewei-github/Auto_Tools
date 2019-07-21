#! python2
#coding: utf-8
import sys
import json

import requests



class Request_Url:

    def __init__(self):
        pass

    def request_Url(self,request_method=None,proxy=None,param_current=None,\
                    url=None,interface_config=None, log_level=None, files=None,\
                    dobbu_server=None,dobbu_port=None):


        interface_name = interface_config["interface_name"]

        try:
            #===================================================================================
            if request_method == "post":

                #===================================================================================
                for key,value in param_current.items():
                    if value == "input":
                        param_current[key]=raw_input("please input %s:"% key)
                        continue
                if log_level == "DETAIL":
                    print("========= Detail log info ==========")
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ===>request_method：%s" %request_method)
                    #可以把字典中的中文正常的输出
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))

                res = requests.post(url, data=param_current, proxies=proxy)
                if int(res.status_code) == 200:
                    return {
                            "msg":"success",
                            "result":res
                            }
                else:
                    print("--%s--%s--the return code is: %s " %(self.__class__.__name__, sys._getframe().f_code.co_name,str(res.status_code)))
                    print("request_method is %s" % request_method)
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ---> %s" % res.content)
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))
                    return {
                            "msg":"fail",
                            "result":res
                            }
            #===================================================================================
            elif request_method == "post_with_image_file":
                if log_level == "DETAIL":
                    print("========= Detail log info ==========")
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ===>request_method: %s" %request_method)
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))
                    print("    ===>files:%s" % files)
                res = requests.post(url, data=param_current, proxies=proxy, files=files)
                if int(res.status_code) == 200:
                    return {
                            "msg":"success",
                            "result":res
                            }
                else:
                    print("--%s--%s--the return code is: %s " %(self.__class__.__name__, sys._getframe().f_code.co_name,str(res.status_code)))
                    print("request_method is %s" % request_method)
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ---> %s" % res.content)
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))
                    return {
                            "msg":"fail",
                            "result":res
                            }
            #===================================================================================
            elif request_method == "get":
                if log_level == "DETAIL":
                    print("========= Detail log info ==========")
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ===>request_method: %s" %request_method)
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))
                res = requests.get(url,proxies=proxy)   
                if int(res.status_code) == 200:
                    return {
                            "msg":"success",
                            "result":res
                            }
                else:
                    print("--%s--%s--the return code is: %s " %(self.__class__.__name__, sys._getframe().f_code.co_name,str(res.status_code)))
                    print("request_method is %s" % request_method)
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ---> %s" % res.content)
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))
                    return {
                            "msg":"fail",
                            "result":res
                            }
            elif request_method == "post_with_json":

                if log_level == "DETAIL":
                    print("========= Detail log info ==========")
                    print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
                    print("    ===>request_Url:%s" % url)
                    print("    ===>request_method：%s" %request_method)
                    #可以把字典中的中文正常的输出
                    print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))

                res = requests.post(url, json=param_current["json_data"], proxies=proxy)
                if int(res.status_code) == 200:
                    return {
                            "msg":"success",
                            "result":res
                            }
                else:
                    print("--%s--%s--the return code is: %s " %(self.__class__.__name__, sys._getframe().f_code.co_name,str(res.status_code)))
                    print("request_method is %s" % request_method)
                    print("    ---> %s" % res.content)
                    return {
                            "msg":"fail",
                            "result":res
                            }
            # elif request_method == "post_dobbu":
            #     dobbu_interface = interface_config["dobbu_interface"]
            #     dobbu_method = interface_config["dobbu_method"]
            #     dobbu_param_list =  interface_config["dobbu_param"]
            #     if log_level == "DETAIL":
            #         print("========= Detail log info ==========")
            #         print("    ===>interface_name: |-->>>>  %s  <<<<--|" % interface_name)
            #         print("    ===>dobbu_server_port:%s:%s" % (dobbu_server,dobbu_port))
            #         print("    ===>request_method：%s" %request_method)
            #         #可以把字典中的中文正常的输出
            #         print("    ===>request_param:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))

            #     conn = dubbo_telnet.connect(dobbu_server, int(dobbu_port))
            #     # 设置telnet连接超时时间
            #     conn.set_connect_timeout(10)
            #     # 设置dubbo服务返回响应的编码
            #     conn.set_encoding('gbk')
            #     # list_middle = []
            #     # for key in dobbu_param_list:
            #     #     list_middle.append(param_current.pop(key))

            #     param = '"2", "uc_py_test_2","172.29.2.24","zhenzhen", "96e79218965eb72c92a549dd5a330112"'
            #     command = 'invoke %s.%s(%s)' % (dobbu_interface, dobbu_method, param)

            #     res = conn.do(command)
            #     print(res)
            #     return {
            #                 "msg":"success",
            #                 "result":res
            #             }

            #===================================================================================
            else:
                print("--%s--%s-- request_method not in post get post_with_image_file "%(self.__class__.__name__, sys._getframe().f_code.co_name))
                print("request_method is %s" % request_method)
        except Exception as e:
            print("===>url is: %s" % url)
            print("===>proxy is:%s" % proxy)
            print("===>param is:%s" % json.dumps(param_current, encoding='UTF-8', ensure_ascii=False))
            print("===>request_method is: %s" % request_method)
            print("--%s--%s-- tool error "%(self.__class__.__name__, sys._getframe().f_code.co_name))
            print("python error is %s" % e)
            return {"msg":"error"}

    def main(self):
        self.request_Url()
if __name__ == "__main__":
    ss = Request_Url()
    ss.main()