def dis(a,b):
    x1,y1 = a.position[0],a.position[1]
    x2,y2 = b.position[0],b.position[1]
    return (x1-x2)**2 + (y1-y2)**2


# class Graph:
#
#     def __init__(self, graph):
#         self.graph = graph
#         self. ROW = len(graph)
#
#
#     # Using BFS as a searching algorithm
#     def searching_algo_BFS(self, s, t, parent):
#
#         visited = [False] * (self.ROW)
#         queue = []
#
#         queue.append(s)
#         visited[s] = True
#
#         while queue:
#
#             u = queue.pop(0)
#             tempList = []
#             for ind, val in enumerate(self.graph[u]):
#                 if visited[ind] == False and val > 0:
#                     tempList.append(ind)
#
#
#
#                     queue.append(ind)
#                     visited[ind] = True
#                     parent[ind] = u
#
#         return True if visited[t] else False
#
#     # Applying fordfulkerson algorithm
#     def ford_fulkerson(self, source, sink):
#         parent = [-1] * (self.ROW)
#         max_flow = 0
#
#         while self.searching_algo_BFS(source, sink, parent):
#
#             path_flow = float("Inf")
#             s = sink
#             while(s != source):
#                 path_flow = min(path_flow, self.graph[parent[s]][s])
#                 s = parent[s]
#
#             # Adding the path flows
#             max_flow += path_flow
#
#             # Updating the residual values of edges
#             v = sink
#             while(v != source):
#                 u = parent[v]
#                 self.graph[u][v] -= path_flow
#                 self.graph[v][u] += path_flow
#                 v = parent[v]
#         print(self.graph)
#         return max_flow
#
# # graph = [[0, 1, 1, 0, 0, 0],
# #          [0, 0, 0, 1, 1, 0],
# #          [0, 0, 0, 1, 1, 0],
# #          [0, 0, 0, 0, 0, 1],
# #          [0, 0, 0, 0, 0, 1],
# #          [0, 0, 0, 0, 0, 0]]
# #
# # g = Graph(graph)
# #
# # source = 0
# # sink = 5
# #
# # print("Max Flow: %d " % g.ford_fulkerson(source, sink))

def In(A,B):
        for i in B:
            if A == B:
                return True
        return False