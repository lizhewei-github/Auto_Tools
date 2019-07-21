
#! python2
#coding: utf-8
import sys

import redis

#mongo_ip = "10.30.0.234"
#mongo_port = "6379"
# mongo_username = "root"
# mongo_password = "123456"

class Redis_Init:

    def __init__(self):
        pass

    def init_Redis(self, ip=None, port=None):
        try: 
            pool = redis.ConnectionPool(host=ip, port=int(port),decode_responses=True)
            r = redis.Redis(connection_pool=pool)
            return {
                    "msg":"success",
                    "result":r
            }
        except Exception as a:
            print("redis init fail")
            return {"msg":"fail"}
        

    def main(self):

        self.init_Redis(ip=mongo_ip, port=mongo_port)
    def www(self):
        print(99999)

if __name__ == '__main__':
    ss = Redis_Init()
    ss.main()


