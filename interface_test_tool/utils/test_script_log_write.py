#! python2
#coding: utf-8

import sys


class Test_Script_Log_Write:
    def __init__(self):
        pass

    def test_Case_Write(self, **kwargs):
        try:
            kwargs["content"].write("====================================================================================\n")
            kwargs["content"].write("No.%d-------fail\n" % kwargs["count"])
            #kwargs["content"].write("66666666666666666666666666666666666666666666666")
            #print(kwargs)
            kwargs["content"].write("===>url is: %s \n" % kwargs["result_dict"]["url"])
            kwargs["content"].write("===>param is:%s \n" % kwargs["result_dict"]["param_current"])
            kwargs["content"].write("===>request_method is: %s \n" % kwargs["method"])
            kwargs["content"].write("---read data is:\n")
            kwargs["content"].write("-------------------------------------------------------------\n")
            kwargs["content"].write(str(kwargs["data"]))
            kwargs["content"].write("\n")
            kwargs["content"].write("-------------------------------------------------------------\n")
            kwargs["content"].write("---return data is:\n")
            kwargs["content"].write(str(kwargs["result_dict"]["result"]))
            kwargs["content"].write("\n")
            kwargs["content"].write("-------------------------------------------------------------\n")
            kwargs["content"].write("please check the error log,if the error log is empty, case fail,else deal with the error log first\n")
            kwargs["content"].write("====================================================================================\n")
            return {"msg":"success"}

        except Exception as a:
            print("--%s--%s-- tool error " % (self.__class__.__name__,sys._getframe().f_code.co_name))
            return {"msg":"error"}

    def test_Main_Write(self, **kwargs):
        try:
            kwargs["content"].write("moudle name is: %s\n" % kwargs["interface_name"]) 
            kwargs["content"].write("all cases num is: %d\n" % kwargs["count"]) 
            kwargs["content"].write("PASS cases num is: %d\n" % kwargs["PASS"])
            kwargs["content"].write("FAIL cases num is: %d\n" % kwargs["FAIL"])
            kwargs["content"].write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            kwargs["content"].write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            return {"msg":"success"}
        except Exception as a:
            print("--%s--%s-- tool error " % (self.__class__.__name__,sys._getframe().f_code.co_name))
            return {"msg":"error"}

    def main(self):
        pass

if __name__ == "__main__":
    ss = Test_Script_Log_Write()
    ss.main()