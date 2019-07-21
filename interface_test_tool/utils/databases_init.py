#! python2
#coding: utf-8
import sys

from mongo_init import Mongo_Init
from redis_init import Redis_Init
from sql_init import Sql_Init
from database_connect_data_read import Database_Connect_Data_Read
import interfaces_recover_and_check


class Databases_Init:

    def __init__(self):
        pass

    def init(self,database_instance_dict=None,global_data=None):
        mongo_database_name = global_data["mongo_database_name"]
        sql_database_name = global_data["sql_database_name"]
        environment_flag = global_data["environment_flag"]
        lib_name = global_data["lib_name"]
        log_level = global_data["log_level"]
        ##############################
        # print(lib_name)
        # print("$################################")
        #####################################
        for lib in lib_name:
                #根据数据库的类型选择要执行的函数
            if lib == "mongo":
                #获取mongo的参数
                mongo_connect_data_dict = Database_Connect_Data_Read().read_Mongo_Connect_Data(enviromment_flag=environment_flag, \
                                                                                               global_data=global_data,\
                                                                                               mongo_database_name=mongo_database_name)
                if mongo_connect_data_dict["msg"] == "success":
                    mongo_connect_data = mongo_connect_data_dict["result"]
                    mongo_instance_dict = Mongo_Init().init_Mongo(ip=mongo_connect_data['ip'], \
                                                            port=mongo_connect_data['port'], \
                                                            user_name=mongo_connect_data['user_name'], \
                                                            password=mongo_connect_data['password'],\
                                                            mongo_database_name=mongo_database_name)
                    if mongo_instance_dict["msg"] == "success":
                        mongo_instance = mongo_instance_dict["result"]
                        database_instance_dict["mongo_instance"] = mongo_instance
                        if log_level == "DEBUG" or log_level == "DETAIL":
                            print("mongo init success")

                    else:
                        return mongo_instance_dict
                else:
                    return mongo_connect_data_dict
#***************************************************************************************************************************************
#***************************************************************************************************************************************
            elif lib == "redis":
                redis_connect_data_dict = Database_Connect_Data_Read().read_Redis_Connect_Data(enviromment_flag=environment_flag, \
                                                                                               global_data=global_data)
                if redis_connect_data_dict["msg"] == "success":
                    redis_connect_data = redis_connect_data_dict["result"]
                    redis_instance_dict = Redis_Init().init_Redis(ip=redis_connect_data['ip'], \
                                                            port=redis_connect_data['port'])



                    if redis_instance_dict["msg"] == "success":
                        redis_instance = redis_instance_dict["result"]
                        database_instance_dict["redis_instance"] = redis_instance
                        if log_level == "DEBUG" or log_level == "DETAIL":
                            print("redis init success")
                    else:
                        return redis_instance_dict

                else:
                    return redis_connect_data_dict
#***************************************************************************************************************************************
#***************************************************************************************************************************************
            elif lib == "mysql":
                sql_connect_data_dict = Database_Connect_Data_Read().read_Sql_Connect_Data(enviromment_flag=environment_flag, \
                                                                                           global_data=global_data,\
                                                                                           sql_database_name=sql_database_name)
                if sql_connect_data_dict["msg"] == "success":
                    sql_connect_data = sql_connect_data_dict["result"]
                    sql_instance_dict = Sql_Init().init_Sql(ip=sql_connect_data['ip'], \
                                                      port=sql_connect_data['port'],\
                                                      user_name=sql_connect_data["user_name"],\
                                                      password=sql_connect_data["password"],\
                                                      sql_database_name=sql_database_name)
                    if sql_instance_dict["msg"] == "success":
                        sql_instance = sql_instance_dict["result"]
                        database_instance_dict["sql_instance"] = sql_instance
                        if log_level == "DEBUG" or log_level == "DETAIL":
                            print("sql init success")
                    else:
                        return sql_instance_dict
                else:
                    return sql_connect_data_dict
            else:
                pass

        return {
                "msg":"success",
                "result":database_instance_dict
        }

    def init_Databases(self,center_init_flag=None, test_init_flag=None,script_init_flag=None,database_instance_dict=None,global_data=None):
        #如果实例字典有东西，代表已经有上级初始化过了，直接返回
        environment_flag = global_data["environment_flag"]
        if environment_flag == "2":
            print("online enviromment --quit database init")
            return{
                    "msg":"success",
                    "result":{}
            } 
        if database_instance_dict:
            return{
                    "msg":"success",
                    "result":database_instance_dict
            }
        #实例字典时空，中心标识是真，则依据全局数据执行中心初始化
        elif center_init_flag == True:
            center_result_dict = self.init(database_instance_dict=database_instance_dict,global_data=global_data)
            if center_result_dict["msg"] == "success":
                database_instance_dict = center_result_dict["result"]
                return {
                        "msg":"success",
                        "result":database_instance_dict
                }
            else:
                return center_result_dict
        #实例字典是空，测试标识是真，则依据全局数据执行测试初始化
        elif test_init_flag == True:
            test_result_dict = self.init(database_instance_dict=database_instance_dict,global_data=global_data)
            if test_result_dict["msg"] == "success":
                database_instance_dict = test_result_dict["result"]
                return {
                        "msg":"success",
                        "result":database_instance_dict
                }
            else:
                return test_result_dict
        #实例字典是空，脚本标识是真，则依据全局数据执行脚本初始化，
        elif script_init_flag == True:
            script_result_dict = self.init(database_instance_dict=database_instance_dict,global_data=global_data)
            if script_result_dict["msg"] == "success":
                database_instance_dict = script_result_dict["result"]
                return {
                        "msg":"success",
                        "result":database_instance_dict
                }
            else:
                return script_result_dict

        else:
            print("all database init flag is false")
            return {
                    "msg":"success",
                    "result":database_instance_dict
            }
            

if __name__ == '__main__':
    ss = Databases_init()
    ss.init_Databases()