#! python2
#coding: utf-8


class Databases_Operation:

    def __init__(self):
        pass

    def operation_Database(self, global_data=None,database_instance_dict={},kwargs=None,default_data=None,log_level=None):
        #如果传入的db实例为空的话
        
        if not database_instance_dict:
            return {
                    "msg":"fail"
            }
        else:
            if kwargs:
                for name, instance in database_instance_dict.items():
                   self.operation_Database_Method(name=name,instance=instance,data=kwargs,log_level=log_level) 

            elif default_data:
                for name, instance in database_instance_dict.items():
                    self.operation_Database_Method(name=name,instance=instance,data=default_data,log_level=log_level)

    def operation_Database_Method(self,name=None, instance=None,data=None,log_level=None):
        if name == "mongo_instance":
            mongo_command = data["mongo_command"]
            if not isinstance(mongo_command,list):
                pass
            else:
                print("---mongo output---")
                for command in mongo_command:
                    if log_level == "DEBUG" or log_level == "DETAIL":
                        print("    ~~~>command: "+str(command))
                        print("    ~~~>result: "+str(eval(command)))
                        print("    ------------------------------------------------------------------------------")
                    else:
                        eval(command)

        elif name == "redis_instance":
            redis_command = data["redis_command"]
            if not isinstance(redis_command,list):
                pass
            else:
                print("---redis output---")
                for command in redis_command:
                    if log_level == "DEBUG" or log_level == "DETAIL":
                        
                        print("    ~~~>command: "+str(command))
                        print("    ~~~>result: "+str(eval(command)))
                        print("    ------------------------------------------------------------------------------")
                    else:
                        eval(command)

        elif name == "sql_instance":
            sql_command = data["sql_command"]
            cur = instance["cur"]
            conn = instance["conn"]
            if not isinstance(sql_command,list):
                pass
            else:
                print("---sql output---")
                for command in sql_command:
                    if log_level == "DEBUG" or log_level == "DETAIL":
                        
                        print("    ~~~>command: "+str(command))
                        print("    ~~~>result: "+str(eval(command)))
                        print("    ------------------------------------------------------------------------------")
                    else:
                        eval(command)

        else:
            pass
 
         
if __name__ == '__main__':
    ss = Databases_Operation()
    ss.operation_Database()