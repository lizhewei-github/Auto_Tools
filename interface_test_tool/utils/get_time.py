#! python2
#coding: utf-8

import time 
import datetime


class Get_Time:

    #返回字符串类型不包含小数的时间
    def get_Int_Str_Time(self):
        return str(int(time.time()))

    #返回不包含小数的int型的时间
    def get_Int_Time(self):
        return int(time.time())

    #返回正常时间
    def get_Normal_Time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    def main(self):

        print(self.get_Int_Time())
        print(self.get_Int_Str_Time())
        print(self.get_Normal_Time())

if __name__ == '__main__':
    s = Get_Time()
    s.main()