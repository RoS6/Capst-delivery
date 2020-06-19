import atool
import copy
class requestQ():
    def __init__(self,item):
        self.item = item
        self.requestamount = 0
        self.shopamount = 0
        # self.waitList = [] #?? wait to be sent?
        # self.addList = []
        self.shopList = []
        self.userCount = 0
        self.userList = []
        self.edge = []
        self.graph = []
        self.matchedResult = []

    def addR(self,request,item,amount):
        tempUserList = []
        tempAmount = self.requestamount + amount
        tempshop = self.shopamount
        tempshopList = []
        shopIndexList = []
        tempShopAmount = 0
        userIndex = 0
        # if request.user not in self.userList:
        if not atool.In(request.user,self.userList):
            # indx = self.userList.index(request.user)
            # indshop = self.shopList.index(shop)
            # self.edge +=
            # graph[indx+1][indshop+1+self.userCount] += amount

            userIndex = self.userCount + 1
            tempUserList.append(request.user)
        else:
            userIndex = self.userList.index(request.user)

        # if request.matchPharm == []:
        #     raise TypeError
        for shop,dis in request.matchPharm:
            # shop = index.get("shop")
            if shop not in self.shopList:
                tempShopAmount += 1
                tempshop += shop.checkStock(item)
                tempshopList.append(shop)
                shopIndexList.append(len(self.shopList)+tempShopAmount-1)
            else:
                shopIndexList.append(self.shopList.index(shop))

        if tempAmount > tempshop:
            print("rejected :"+str(request))
            print(tempAmount)
            print(tempshop)
            # self.shopList.pop(-1)
            pass

        else:
            self.shopList = self.shopList + tempshopList
            # self. userList = self.userList.append()
            self.requestamount += tempAmount
            self.shopamount += tempshop
            self.userCount = self.userCount +len(tempUserList)
            # addList = [request,userIndex, shopIndexList]
            self.createEdge(request,userIndex,shopIndexList)
            # self.edge.append([request,userIndex, shopIndexList])  # userCount mean the index of user,request give the flow
            print(str(self.item.name)+str(self.edge) + str(self.edge[0][0].medicine[1]))
            # self.addList.append([request, item, amount])
        #build edges
    #every 5min run once or every 50 inputs
    def runRankCost(self):
        graph = []
        edgeLength = len(self.shopList)+self.userCount+2
        for i in range(edgeLength):
            row = []
            for j in range(edgeLength):
                row.append(0)
            graph.append(row)

        for i in self.edge:
            graph[0][i[1]] = i[0].medicine[1]
            for j in i[2]:
                # shop = self.shopList[j]
                graph[i[1]][1+self.userCount+j] = 100+i[0].matchPharm[j][1]

        for s in range(len(self.shopList)):
            shop = self.shopList[s]
            graph[1 + self.userCount + s][edgeLength - 1] = shop.getStock()
            # print(shop.getStock())

        # print(graph)
        self.graph = copy.deepcopy(graph)


        self.FFAMatch(graph,edgeLength)

    def FFAMatch(self,graph,edgelength):
        source = 0
        sink = edgelength-1
        parent = [-1] * (edgelength)
        max_flow = 0

        while self.BFS(source, sink, parent,edgelength,graph):

            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while (v != source):
                u = parent[v]
                graph[u][v] = graph[u][v] - path_flow
                graph[v][u] = graph[v][u] + path_flow
                v = parent[v]
        print(graph)

        self.matchedResult = graph

        self.match(edgelength)

    def BFS(self,s,t,parent,edgeLength,graph):
        visited = [False] * (edgeLength)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)
            # if u>0 and u < self.userCount+1:
            for ind, val in list(sorted(enumerate(graph[u]),key = lambda x:x[1])):
                # if len(val) == 2:
                #     val = val[1]
                if visited[ind] == False and val > 0:#index 链接之后的点
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def createEdge(self,request,userIndex, shopIndexList):  #[request,userIndex, shopIndexList]  = list
        if self.edge == []:
            self.edge = [[request,userIndex,shopIndexList]]
        else:
            for i in self.edge: #check same user
                if i[0].user == request.user:
                    if i[0].cost>=request.cost:
                        i[0].medicine[1] += request.medicine[1]

                    else:
                        i[0].cost = request.cost
                    self.userCount = self.userCount - 1
                    return

            self.edge.append([request,userIndex,shopIndexList])
            return

    def match(self,edgeLength):
        for i in range (1,self.userCount+1):
            for j in range(1,edgeLength-1):
                v = self.graph[i][j] - self.matchedResult[i][j]
                if v>0 :
                    print(self.shopList[j-self.userCount-1])
                        # addRequest(
                    print(self.edge[i-1][0],v)
                    self.shopList[j-1-self.userCount].addRequest(self.edge[i-1][0],v)


