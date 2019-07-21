#! python2
#coding: utf-8

import re
from sys import argv
import time

Log = argv[1]
Tps_Log = argv[2]
loop_count = argv[3]

TPS = 0.0
Reps = 0.0
Counter = 0
Float_Pattern = re.compile(r"\d{1,}\.\d{1,}")

with open(Log) as inputs:
    for ln in inputs:
        if ln.strip():
            find_floats = Float_Pattern.findall(ln.strip())
            if find_floats:
                Counter += 1
                TPS += float(find_floats[0])
                Reps += float(find_floats[1])

with open(Tps_Log, 'a') as Tps_Log:
    Tps_Log.write('-' *10 + 'The ' + loop_count + ' round' + '-'*10 + '\n')
    Tps_Log.write("       CC: %d" % Counter + '\n')
    Tps_Log.write("      TPS: %.2f" % TPS + '\n')
    Tps_Log.write("Reps_Time: %.4f(s)" % (Reps/Counter) + '\n')
    Tps_Log.write("Current_Time:" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\n')
#print '-' * 30
print('-' *10 + 'The ' + loop_count + ' round' + '-'*10)
print("       CC: %d" % Counter)
print("      TPS: %.2f" % TPS)
print("Reps_Time: %.4f(s)" % (Reps/Counter))
print("Current_Time:" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

x= open(Log, "w")
x.close()