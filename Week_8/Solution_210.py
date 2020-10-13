class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # prepare the lists
        fanin = [0] * numCourses
        fanout = [[] for _ in range(numCourses)] 
        order = []

        # loop for prerequisites
        for i, j in prerequisites:
            fanin[i] += 1
            fanout[j].append(i)

        # loop for numCourses
        for i in range(numCourses):
            if fanin[i] == 0:
                order.append(i)
        
        # loop for output
        length = 0
        while length != len(order):
            tmp = order[length]
            length += 1
            for i in fanout[tmp]:
                fanin[i] -= 1
                if fanin[i] == 0:
                    order.append(i)
        
        # return order if there are valid answers
        return order if length == numCourses else []