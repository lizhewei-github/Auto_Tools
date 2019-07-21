#! python2
#coding: utf-8
import sys

import pymysql


class Sql_Init:

    def __init__(self):
        pass

    def init_Sql(self, ip=None, port=None, user_name=None, password=None,sql_database_name=None):
        try: 
            conn = pymysql.connect(host=ip, user=user_name, passwd=password, db=sql_database_name)
            cur = conn.cursor()

            return {
                    "msg":"success",
                    "result":{
                            "cur":cur,
                            "conn":conn
                    }
            }
        except Exception as a:
            print("Sql init fail")
            return {"msg":"fail"}
        

    def main(self):

        self.init_Sql(ip=ip, port=port, user_name=username, password=password,sql_database_name=sql_database_name)


if __name__ == '__main__':
    ss = Sql_Init()
    ss.main()


