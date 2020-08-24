############################################################
# Node.py
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2020
###########################################################


class Node:
  #Remove pass
  #DEFINE your data structure here
  ##YOU CAN add whatever you want
  def __init__(self, item):
    self._item = item # name of the node
    self._fanins = [] # list of list, [[node1, weight1], [node1, weight2], ... ]
    self._fanouts = [] # list of list, [[node1, weight1], [node1, weight2], ... ]
  
  def _add_fanin(self, node, weight=0):
    self._fanins.append([node, weight])

  def _add_fanout(self, node, weight=0):
    self._fanouts.append([node, weight])