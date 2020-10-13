class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prepare the dictionary
        route = {}
        rec = {}
        
        # loop for numCourses
        for i in range(numCourses):
            route[i] = []

        # loop for prerequisites
        for i in prerequisites:
            if len(i) == 0:
                continue # []
            a, b = i
            route[a].append(b)
        
        # function for output
        def check(nodes, i, past=""):
            if i in rec:
                return rec[i]
            if len(nodes[i]) == 0:
                rec[i] = True
                return True
            for j in nodes[i]:
                if str(j) in past.split(","):
                    return False
                else:
                    tmp = check(nodes, j, past+"%s,"%j)
                    if tmp == False:
                        rec[i] = False
                        return False
            rec[i] = True
            return True

        nodes = list(route.values())
        for i in range(len(nodes)):
            if not check(nodes, i, "%i,"%i):
                return False

        return True