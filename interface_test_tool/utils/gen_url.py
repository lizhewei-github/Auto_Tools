#! python2
#coding: utf-8
import sys


class Gen_Url:

    def __init__(self):
        pass    
        
    def gen_Url(self, request_method=None, param_current=None, server=None, interface_url=None):
        # try:
        if "get" in request_method:
            str_param = ''
            str_list = []
            for i,j in param_current.items():
                str_list.append(i)
                str_list.append("=")
                str_list.append(str(j))
                str_list.append("&")
            str_param = "".join(str_list)
            str_param = str_param[:-1]
            url = "%s%s%s" %(server, interface_url,str_param)
            return {
                    "msg":"success",
                    "result":url
                    }

        elif "post" in request_method:
            url = "%s%s" % (server, interface_url)
            return {
                    "msg":"success",
                    "result":url
                    }
        else:
            print("--%s--%s-- tool fail,not satisfied with any option" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            return {
                    "msg":"fail",
                    "detail":"--%s--%s-- tool fail,not satisfied with any option" % (self.__class__.__name__, sys._getframe().f_code.co_name)
                    }
        # except Exception as a:
        #     print("--%s--%s-- tool error,may be the input param type wrong" % (self.__class__.__name__, sys._getframe().f_code.co_name))
        #     print(a)
        #     return{
        #             "msg":"error",
        #             "detail":"--%s--%s-- tool error,may be the input param type wrong" % (self.__class__.__name__, sys._getframe().f_code.co_name)
        #         }
    def main(self):
        pass

if __name__ =="__main__":

    ss = Gen_Url()
    ss.main()