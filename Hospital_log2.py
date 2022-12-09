#çekilen verileri istenilen sütunları alma

import pm4py
log = pm4py.read_xes('C:/Users/90531/Desktop/Hospital_log (1).xes')
print(log['concept:name'] +"   "+ log['org:group'] +"    "+ str(log['time:timestamp']))
