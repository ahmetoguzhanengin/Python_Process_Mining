#görselleştirme
import os
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.visualization.petri_net import visualizer as pn_visualizer
import graphviz as gviz

log = xes_importer.apply(os.path.join("tests", "input_data", "C:/Users/90531/Desktop/Hospital_log (1).xes"))

dfg, start_activities, end_activities = alpha_miner.apply(log)
gviz = pn_visualizer.apply(dfg, start_activities, end_activities)
pn_visualizer.view(gviz)
