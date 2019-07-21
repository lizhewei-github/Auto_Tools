#! python2
#coding: utf-8



class Database_Connect_Data_Read:

    def __init__(self):
        #self.database_name = database_name
        pass
        
    def read_Mongo_Connect_Data(self,enviromment_flag=None, global_data=None,mongo_database_name=None):
        #如果是开发环境，根据环境标识读取mongo的信息
        if enviromment_flag == "1":
            result = {
                    "ip":global_data["mongo_dev"]["mongo_ip"],
                    "port":global_data["mongo_dev"]["mongo_port"],
                    "user_name":global_data["mongo_dev"][mongo_database_name]["mongo_username"],
                    "password":global_data["mongo_dev"][mongo_database_name]["mongo_password"]
            }
            return {
                    "msg":"success",
                    "result":result
                    
            }
        #如果是测试环境，根据环境标识读取mongo的信息
        elif enviromment_flag == "0":
            result = {
                    "ip":global_data["mongo_test"]["mongo_ip"],
                    "port":global_data["mongo_test"]["mongo_port"],
                    "user_name":global_data["mongo_test"][mongo_database_name]["mongo_username"],
                    "password":global_data["mongo_test"][mongo_database_name]["mongo_password"]
            }

            return {
                    "msg":"success",
                    "result": result
            }
        #线上环境不支持
        elif enviromment_flag == "2":
            print("online db cannot modify")
            return {"msg":"fail"}
        else:
            return {
                    "msg":"fail"
            }

    def read_Sql_Connect_Data(self,enviromment_flag=None, global_data=None,sql_database_name=None):
        #如果是开发环境，根据环境标识读取mongo的信息
        if enviromment_flag == "1":
            result = {
                    "ip":global_data["sql_dev"]["sql_ip"],
                    "port":global_data["sql_dev"]["sql_port"],
                    "user_name":global_data["sql_dev"]["sql_username"],
                    "password":global_data["sql_dev"]["sql_password"]
            }
            return {
                    "msg":"success",
                    "result":result
                    
            }
        #如果是测试环境，根据环境标识读取mongo的信息
        elif enviromment_flag == "0":
            result = {
                    "ip":global_data["sql_test"]["sql_ip"],
                    "port":global_data["sql_test"]["sql_port"],
                    "user_name":global_data["sql_test"]["sql_username"],
                    "password":global_data["sql_test"]["sql_password"]
            }

            return {
                    "msg":"success",
                    "result": result
            }
        #线上环境不支持
        elif enviromment_flag == "2":
            print("online db cannot modify")
            return {"msg":"fail"}
        else:
            return {
                    "msg":"fail"
            } 
    def read_Redis_Connect_Data(self,enviromment_flag=None, global_data=None):
        #python链接redis需要什么数据都写在这个地方，根据环境标识读取
        #python 链接sql需要什么数据都写在这个地方，根据环境标识读取
        if enviromment_flag == "1":
            result = {
                    "ip": global_data["redis_dev"]["redis_ip"],
                    "port": global_data["redis_dev"]["redis_port"]
            }
            return {
                    "msg":"success",
                    "result": result
            }

        elif enviromment_flag == "0":
            result = {
                    "ip": global_data["redis_test"]["redis_ip"],
                    "port": global_data["redis_test"]["redis_port"]
            }
            return {
                    "msg":"success",
                    "result": result
            }
        #线上环境不支持
        elif enviromment_flag == "2":
            print("online db cannot modify")
            return {"msg":"fail"}
        else:
            return {
                    "msg":"fail"
            }


    def main(self):
        pass



if __name__ == '__main__':
    ss = Database_Connect_Data_Read()
    ss.main()