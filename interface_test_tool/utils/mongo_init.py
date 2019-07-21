#! python2
#coding: utf-8
import sys
import urllib

from pymongo import MongoClient

# mongo_ip = "10.20.222.63"
# mongo_port = "27017"
# mongo_username = "root"
# mongo_password = "123456"

class Mongo_Init:

    def __init__(self):
        pass

    def init_Mongo(self, ip=None, port=None, user_name=None, password=None,mongo_database_name=None):
        # try: 
            #user_name = urllib.quote_plus(user_name)
        passowrd = urllib.quote_plus(password)

        conn = MongoClient('mongodb://%s:%s@%s:%s/' %(user_name,passowrd,ip,port))
         #这种方式也可以
        #conn = MongoClient(ip, int(port))
        #db_auth = conn.admin
        #db_auth.authenticate(user_name, password)
        database = conn[mongo_database_name]
        return {
                "msg":"success",
                "result":database
        }
        # except Exception as a:
        #     print("mongo init fail")
        #     return {"msg":"fail"}
        '''
           #===================================================================================
           #制定用户名和密码连接制定的数据库 
                  conn = MongoClient('mongodb://dev:%s@172.29.0.6:27017/user_center' %bb)
                  database = conn[mongo_database_name]
         
                 # database.authenticate(user_name, bb)
                  print(database)
                  print(database.passport.find_one({"userName":"pukunwen"}))
         #===================================================================================   
        '''
    def main(self):

        self.init_Mongo(ip=mongo_ip, port=mongo_port, user_name=mongo_username, password=mongo_password,mongo_database_name="user_center")



    def www(self):
        print(888)

if __name__ == '__main__':
    ss = Mongo_Init()
    ss.main()


