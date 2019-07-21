#! python2
#coding: utf-8
import sys 
import re

from data_read import Data_Read

class Choose_Server:

    def __init__(self):


        self.proxy = None


    def choos_Server(self, data_config_global=None, environment_flag=None):

        try:
            if environment_flag == "0": 

                if re.search(r"(\d{1,3}\.){3}\d{1,3}", data_config_global['http_test']):
                    self.proxy = {"http": data_config_global['http_test']}
                return {
                        "msg": "success",
                        "result":
                            {
                            "server": data_config_global['server_address_test'],
                            "proxy": self.proxy,

                            }
                        }

            elif environment_flag == "1":
                if re.search(r"(\d{1,3}\.){3}\d{1,3}", data_config_global['http_dev']):
                    self.proxy = {"http": data_config_global['http_dev']}
                return {
                        "msg": "success", 
                        "result":
                            {
                            "server": data_config_global['server_address_dev'],
                            "proxy": self.proxy,
                            }
                        }

            elif environment_flag == "2":
                if re.search(r"(\d{1,3}\.){3}\d{1,3}", data_config_global['http_online']):
                    self.proxy = {"http": data_config_global['http_online']}
                return {
                        "msg": "success",    
                        "result":
                            {
                            "server": data_config_global['server_address_online'],
                            "proxy": self.proxy,

                            }
                        }
            elif environment_flag == "3":
                if re.search(r"(\d{1,3}\.){3}\d{1,3}", data_config_global['http_online']):
                    self.proxy = {"http": data_config_global['http_online']}
                return {
                        "msg": "success",    
                        "result":
                            {
                            "server": data_config_global['server_address_aliyun'],
                            "proxy": self.proxy
                            }
                        }
        except Exception as f:
            print("--%s--%s--tool run error"% (self.__class__.__name__, sys._getframe().f_code.co_name))
            return {"msg":"error"}

    def main(self):

        print(self.choos_Server("2"))

if __name__ == "__main__":
    ss = Choose_Server()
    ss.main()


