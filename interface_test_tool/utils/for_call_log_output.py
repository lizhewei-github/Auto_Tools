#! python2
#coding: utf-8
import json

class For_Call_Log_Output:

    def __init__(self):

        pass

    def main(self, res=None, judge_dict=None, request_method=None, proxy=None):
        print("--->"+res.content)
        print("===>proxy is:%s" % proxy)
        print("===>url is: %s" % judge_dict["url"])
        print("===>param is:%s" % json.dumps(judge_dict["param_current"], encoding='UTF-8', ensure_ascii=False))
        print("===>request_method is: %s" % request_method)

if __name__ == '__main__':
    ss = For_Call_Log_Output()
    ss.main()

