#! python2
#coding: utf-8
import json
import os
#以utf-8打开文件   codecs.open()  但是不能写入二进制文件
#之所以用这个是因为图片验证码接口用例失败了以后会写入二进制文件到文件中
#导致其他中文不能正常显示
#所以用这个接口代替一下，阻止二进制文件写入，出现异常直接捕获了
import codecs
import time 

class Func_Test_Log_Output:

    def __init__(self):

        pass

    def func_Success_Output(self, result=None,count=None,description=None, proxy=None,\
                            result_dict=None,request_method=None,log_level=None):
        print("-pass-No.%d--%s" % (count, description))
        print("    --->" + result)
        print("")
        if log_level == "DEBUG":
            print("     ===>proxy is: %s" % proxy)
            print("     ===>url is: %s" % result_dict["url"])
            print("     ===>param is:%s" % json.dumps(result_dict["param_current"], encoding='UTF-8', ensure_ascii=False))
            print("     ===>request_method is: %s" % request_method)
            print("     ---------------------------------------------------------")

    def func_Fail_Output(self, data=None, result=None,count=None,center_name=None,\
                        description=None, proxy=None,result_dict=None,request_method=None):
        
        print("-fail-No.%d--%s" % (count, description))
        print("     ===>proxy is: %s" % proxy)
        print("     ===>url is: %s" % result_dict["url"])
        print("     ===>param is:%s" % json.dumps(result_dict["param_current"], encoding='UTF-8', ensure_ascii=False))
        print("     ===>request_method is: %s" % request_method)
        print("     --------------------------------------------------------------")
        print("     ---read data is:")
        print("     "+json.dumps(data, encoding='UTF-8', ensure_ascii=False))
        print("     --------------------------------------------------------------")
        print("     ---return data is:")
        print("     "+str(result))
        print("     --------------------------------------------------------------")
        print("")
        #=====================================================================================

        try:
            content = codecs.open("%s/result/error_log.txt" % center_name, "a+", "utf-8")
            content.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            content.write("++++++++++++++++++++++++++++++++++++%s++++++++++++++++++++++++++++++++++++\n"\
             % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            content.write("-fail-No.%d--%s--\n" % (count, description))
            content.write("     ===>proxy is: %s \n" % proxy)
            content.write("     ===>url is: %s \n" % result_dict["url"])
            content.write("     ===>param is:%s \n" % json.dumps(result_dict["param_current"], encoding='UTF-8', ensure_ascii=False))
            content.write("     ===>request_method is: %s \n" % request_method)
            content.write("     -------------------------------------------------------------- \n")
            content.write("     ---read data is: \n")
            content.write("     "+json.dumps(data, encoding='UTF-8', ensure_ascii=False)+" \n")
            content.write("     -------------------------------------------------------------- \n")
            content.write("     ---return data is: \n")
            content.write("     "+str(result)+" \n")
            content.write("     -------------------------------------------------------------- \n")
            content.write(" \n")
            content.close()
            #=====================================================================================
        except Exception:
            pass

    def main(self):
        pass

if __name__ == '__main__':
    ss = Func_Test_Log_Output()
    ss.main()

