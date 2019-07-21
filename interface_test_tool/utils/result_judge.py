#! python2
#coding: utf-8
import sys 


class Result_Judge:

    def __init__(self):
        pass
        
    def result_Judge(self,success_str=None, res=None, class_name=None,method_name=None,log_level=None,url=None, param_current=None):
        try:
            if log_level == "DETAIL":
                print("    ---------result---------")
                print("    ===>return_result:%s" % str(res.content))
                print("")
            if success_str in res.content:
                if log_level == "DEBUG":
                    # print("--%s--%s--return success" % (class_name, method_name))
                    # print("--%s--%s--return result is:%s" % (class_name, method_name ,res.content))
                    pass
                else:
                    pass
                    #print("--->"+res.content)
                return {
                        "msg": "success",
                        "result": res.content,
                        "url": url,
                        "param_current": param_current
                       }
            else:
                if log_level == "DEBUG":
                    #print("--%s--%s--return error"% (class_name, method_name))
                    #print("--%s--%s--your default result not in the return result or the return result is None" % (class_name, method_name))
                    #print("--%s--%s--return result is:%s" % (class_name, method_name ,res.content))
                    pass
                else:
                    pass
                    #print("--->"+res.content)
                return {
                        "msg": "fail",
                        "result": res.content,
                        "url": url,
                        "param_current": param_current
                       }
        except Exception as f:
            print("--%s--%s-- tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("python error is : %s" % f)
            return {
                    "msg":"error",
            }

    def main(self):
        pass

if __name__ == "__main__":
    ss = Result_Judge()
    ss.main()