#! python2
#coding: utf-8

import hashlib
import urllib2
import base64


class Gen_Signature:

    def __init__(self):
        pass

    def gen_Signature_Default(self):
        pass

    def gen_Signature_User_Device_Center(self,param_dict):    
        try:
            data_list = param_dict.values()
            data_list = [str(i) for i in data_list]
            data_list.sort()
            data_str = "".join(data_list)
            signature = hashlib.sha1(data_str.encode("utf-8")).hexdigest().upper()
            return {
                    "msg":"success",
                    "result":signature
                    }
        except Exception as f:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("python error is %s" % f)
            return {
                    "msg": "fail"
                     }
    def gen_Signature_Product_Auth(self,param_dict):
        try:
            st = ''
            for t_kv in sorted(param_dict.iteritems(), key=lambda d:d[0], reverse=False):
                if not t_kv[1]:
                    continue
                k = urllib2.quote(str(t_kv[0]))
                v = urllib2.quote(str(t_kv[1]))
                st += '%s=%s&' % (k, v)
            st = st.strip('&')
            m = hashlib.md5()
            m.update(base64.b64encode(st))
            signature = m.hexdigest()
            return {
                    "msg":"success",
                    "result":signature
                    }

        except Exception as f:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("python error is %s" % f)
            return {
                    "msg": "fail"
                     }
                     
    def gen_Signature_Product_Auth_Image(self,param_dict):
        try:
            #产测的签名是“建=值”这种形式，然后在进行签名，不是只有值
            param_list = param_dict.items()
            for key,value in param_list:
                data_str = key+"="+value
            print(data_str)
            m = hashlib.md5()
            
            m.update(base64.b64encode(data_str))
            signature = m.hexdigest()
            return {
                    "msg": "success",
                    "result":signature
                     }
        except Exception as f:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("python error is %s" % f)
            return {
                    "msg": "fail"
                     }

    def gen_Signature_User_Center_Oauth(self,param_dict,appsecret=None):
        try:
            param_list = param_dict.values()
            param_list.append(appsecret)
            param_list.sort()
            data_str = "".join([i.strip() for i in param_list])
            #print(param_list)
            signature = hashlib.sha1(data_str.encode("utf-8")).hexdigest().upper()
            return {
                    "msg": "success",
                    "result":signature
                     }

        except Exception as f:
            print("--%s--%s--tool error" % (self.__class__.__name__, sys._getframe().f_code.co_name))
            print("python error is %s" % f)
            return {
                    "msg": "fail"
                     }

    def main(self):
        self.gen_Signature_Product_Test(a="a",b="b")

if __name__ == '__main__':
    ss = Gen_Signature()
    ss.main()