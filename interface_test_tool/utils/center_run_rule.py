#! python2
#coding: utf-8
import os 

class Center_Run_Rule:

    def __init__(self):
        pass

    def center_Run_Rule(self, center_name=None, interfaces=None):
        if interfaces[0] == "all":
            os.chdir("%s/interfaces" %center_name)
            interfaces = []
            for file in os.listdir("."):
                if os.path.isdir(file):
                    interfaces.append(file)
            os.chdir("../..")
            return interfaces
        #判断第一个字段是否以==>开头，开头则只运行以这个开头的一类接口,以逗号分割，可以指定多个特定的
        elif interfaces[0].startswith("==>"):
            os.chdir("%s/interfaces" %center_name)
            matchs = interfaces[0].split(">")[1].split(",")
            interfaces = []
            files = os.listdir(".")
            for match in matchs:
                for file in files:
                    if os.path.isdir(file) and file.startswith(match):
                        interfaces.append(file)
            os.chdir("../..")
            return interfaces
        else:
            return interfaces

if __name__ == "__main__":

    ss = Center_Run_Rule()
    ss.main()