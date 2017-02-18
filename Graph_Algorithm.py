from __future__ import division
import heapq
from random import choice
import random
import networkx as nx
import matplotlib.pyplot as plt
from itertools import *
from random import randrange
import datetime
import itertools
colors = ['Red', 'Blue', 'Green', 'Yellow',  'Black', 'Pink', 'Orange', 'White', 'Gray', 'Purple', 'Brown', 'Navy']
all_possible_optimal_color_combinations=[]
v=[]
n=[]
q=[]
v1=[]
n1=[]
q1=[]
list1=[]
edges=[]
zipped=[]
jl=[]
il=[]
colors_of_nodes={}
non_optimal_color_of_nodes={}
count=0
all_non_optimal_colrings=[]
class MultiGraph():
        
        def __init__(self):
                   
            self.graph ={}
            self.index= 0
            self.num = 0
            self.e = 0
            self.matrix={}

        def new(self):
            self.graph={}
            return self.graph
        def vertices(self):
            self.num=len(self.graph.keys())
            return self.num

        def edges(self):
            return self.e

        def addvertex(self,u):
            if u not in self.graph.keys():
                self.graph[u]={}
                

        def addedge(self,u,v,w):
            if u not in self.graph.keys():
                self.graph[u]={}
            if v not in self.graph.keys():
                self.graph[v]={}
            if v not in self.graph[u].keys():
                self.graph[u][v]=[w]
                self.e=self.e+1
                self.num=self.num+1
            else:
                self.graph[u][v].append(w)
                self.e=self.e+1

        def removeedge(self,u,v,w):
                if u in self.graph.keys():
                    if v in self.graph[u].keys():
                        if w in self.graph[u][v]:
                            self.graph[u][v].pop()
        def removevertex(self,u):
            
            
            if u in self.graph.keys():
               del self.graph[u]
            for i in self.graph.keys():
                if u in self.graph[i].keys():
                        del self.graph[i][u]
            
        def getedge(u,v):
                if u in graph.keys():
                    if v in graph[u].keys():
                        return graph[u][v]
        def setedge(self,u,v,w):
                if u in self.graph.keys():
                    if v in self.graph[u].keys():
                        if len(self.graph[u][v])>=1:
                            self.graph[u][v].append(w)
                        else:
                            self.graph[u][v]=w
        def out_neighbors(self,u):
            if u in self.graph.keys():
                return self.graph[u].keys()
       
       
        def in_neighbors(self,u):
                list1=[]
        
                l=0
                l=self.graph.keys()
                for i in range(len(l)):
                        j=l[i]
                        if u in self.graph[j].keys():
                                list1.append(j)
                return list1
                        
        
        def free(self):
                self.graph.clear()
        def edgelist(self):
            return self.graph

        def is_empty(self,any_structure):
    
            if any_structure:
        
                return False
            else:
        
                return True


        def bfs(self,g,s):

                q=[]

                q.append(s)
        
                global v

                for i in q:

                        if graph.is_empty(graph.out_neighbors(i)) is True and i in v:
                                break
                        else:
                                print type(q)
                                print ("q before adding" , q)

                                q=q+graph.out_neighbors(i)
                                print ("v before v +q" , v)
                                print q
                                v=v +([x for x in q if x not in v])
                
                
                                
                                print "Traversal Path of BFS is ",v
                                q=q.pop()

                        if graph.is_empty(q) is True:
                                return "Traversal is done"
                        else:
                                return graph.bfs(g,q)
                return "Traversal is done"

        def dfs(self,g,s):
                global q1,v1,n1
                if graph4.is_empty(q1) is True:
                        q1.append(s)
                print type(q1)
                p1=[]
                p1.append(s)            
                for i1 in q1:
                     print "i value is :",i1               
                     n1=graph4.out_neighbors(i1)
                     print "Neighbors is :",n1
                     q1.pop(0)
                     v1.append(i1)
                     print "Traversal Path is:",v1
                     q1=q1+([x for x in n1 if x not in v1])
                     q1.reverse()
                     if graph4.is_empty(q1) is True:
                           return "Traversal is done"
                     else:
                           b=len(q1)
                           return graph4.dfs(g,q1[b-1])
                           print type(q1)
                return "Traversal is done"
        def out_degree(self,g,u):
            if u in self.graph.keys():
               a=len(graph.out_neighbors(u))
               return a
            else:
               return 'Is not a node in the graph'
        def in_degree(self,g,u):

            return int(len(graph.in_neighbors(u)))
            """
            if u in self.graph.keys():
               a=len(graph.in_neighbors(u))
               return a
            else:
               return 'Is not a node in the graph'
            """
        def complete_graph_degree(self,g):
            total_degree=0
            total_in_degree=0
            total_out_degree=0
            for i in g.keys():
                total_in_degree+=graph.in_degree(g,i)
                total_out_degree+=graph.out_degree(g,i)
                total_degree=total_in_degree+total_out_degree
            return total_degree

        def BA_add_vertex(self,g,u,m):
                 p={}
                 for i in g.keys():
                 #pn=round((graph.in_degree(g,i)+graph.out_degree(g,i))/graph.complete_graph_degree(g),i)
                         pn=round(graph.out_degree(g,i)/graph.complete_graph_degree(g),i)
                         p[i]=[]
                         p[i].append(pn)
        
                 t=sorted(p, key=p.__getitem__,reverse=True)
        
         
                 top_list=[]
                 for k in range(m):
                         top_list.append(t[k])
                 c=choice(range(100))
                 w=choice(range(100))
                # print top_list
                 if c>20:
                         for l in top_list:
                                 #print c,l
                                 graph.addedge(u,l,w)
                 

                 else:
                        for k in range(m):
                                #print k
                                l=[]
                                l.append(choice(g.keys()))
                                for i in l:
       
                                          graph.addedge(u,i,w)
                                         
                               
                 
                 return g

        def BA_Graph(self,g,n,m):
                ne=max(g.keys())
                #print ne
                n=range(ne+1,ne+n+1)
                #print "n",n
                for i in n:
                        #print i
                        graph.BA_add_vertex(g,i,m)
                return g
                        
        def ER_Graph(self,n,e,p):
                new_graph=MultiGraph()
                new_graph1=new_graph.new()
                total_num_edges=(n*(n-1))/2
                num_edges=round(total_num_edges*p)
                print range(n)
                
                for i in range(n):
                        new_graph.addvertex(i)
                for k in range(int(num_edges)):
                                print k
                                l=[]
                                k=[]
                                l.append(choice(new_graph1.keys()))
                                for i in l:
                                        k.append(choice(new_graph1.keys()))
                                        for j in k:
                                                if i!=j:
                                                      w=choice(range(100))
                                                      new_graph.addedge(i,j,w)
                return new_graph1

        
        def all_neighbor(self,g,u):
                all_neighbors=[]
                neigbors=[]
                all_neighbors.extend(graph.in_neighbors(u))
                for i in graph.out_neighbors(u):
                        #print "i",i,all_neighbors
                        if i not in all_neighbors:
                                all_neighbors.append(i)
 #               all_neighbors.extend(graph.out_neighbors(u))
                        #neigbors.append([x for x in all_neighbors if not (x in seen or seen_add(x))])
                #set_all_neigbors=set(all_neighbors)
                return all_neighbors#,graph.remove_duplicates(all_neighbors)
                        
        def find_neighbor(self,g,u):
                for l in  self.graph.keys():
                        print "Neigbors of l is",graph.in_neighbors(l),graph.in_degree(g,l)
        def get_edges(self,g):
                for i in BA_Graph.keys():
                        
                        i1=[]
                        
                        il=[i]
                        
                        for j in range(len(BA_Graph[i].keys())):
                 #              il=[]
                                il=il+[i]
                                jl=BA_Graph[i].keys()
                                
                                for k in izip(il,jl):
                                     
                                     

                                     zipped.append(k)
                                i1=[]
                out_tup = [i for i in zipped if i[0] != i[1] ]

                seen = set(out_tup)
 #               out_tup_1 = [i for i in out_tup if i= i[1 ]
                return seen
                
        def coloring(self,g,n,c):
           for neighbor in graph.all_neighbor(g,n):
               color_of_neighbor = colors_of_nodes.get(neighbor, None)
               if color_of_neighbor == c:
                  return False

           return True
        def get_color_for_node(self,g,n):
            for color in colors:
               if graph.coloring(g,n, color):
                  return color
        def visualize(self,g):
                a = datetime.datetime.now()
                for node in g.keys():
                        colors_of_nodes[node] = graph.get_color_for_node(g,node)

                print colors_of_nodes
                
                G=nx.MultiGraph()
                G.add_nodes_from(g.keys())
                G.add_edges_from(graph.get_edges(g))
                values = [colors_of_nodes.get(n) for n in G.nodes()]
                pos=nx.spring_layout(G)       
                nx.draw(G,pos=pos,with_labels=True,cmap=plt.get_cmap('jet'), node_color=values)
                b = datetime.datetime.now()
                c = b - a
                print "time:", divmod(c.days * 86400 + c.seconds, 60)
     
                fig1 = plt.gcf()
                plt.show()
                plt.draw()
                fig1.savefig('tessstttyyy.png', dpi=100)


                
        def optimal_coloring(self,g):
                a = datetime.datetime.now()
                list_of_degrees=[]
                sorted_degrees=[]
                list_of_degrees_1=[]
                for i in g.keys():
                        list_of_neighbors=set(graph.all_neighbor(g,i))
                        print i,set(graph.all_neighbor(g,i))
                        list_of_degrees.append(len(list_of_neighbors))
                        k=(i,len(list_of_neighbors))
                        list_of_degrees_1.append(k)
                print list_of_degrees_1
                min_degree=min(list_of_degrees)
                max_degree=max(list_of_degrees)
                sorted_degrees=sorted(list_of_degrees)
                '''
                median_index=int(len(sorted_degrees)/2)
                if (len(sorted_degrees)%2)==0:
                        first_element_index=median_index
                        second_element_index=median_index+1
                        median=int((sorted_degrees[first_element_index]+sorted_degrees[second_element_index])/2)
                else:
                        median=sorted_degrees[median_index+1]
                print sorted_degrees,median
 #               colors_required=colors[0:median]
                '''
                all_nodes=g.keys()
                all_node_permuations=[x for x in itertools.permutations(all_nodes)]
                all_color_combinations={}
                #for m in range(1,len(g)):
                for m in range(1,4):

                        colors_required=colors[0:m]
                        #print colors_required
                        #for i in g.keys():
                        for i in range(len(all_node_permuations)):
                                non_optimal_coloring={}
                                keys=all_node_permuations[i]
                                for j in keys:
                                        #print "colors_required",colors_required
                                        non_optimal_coloring[j]=colors_required.pop(0)
                                        colors_used=non_optimal_coloring[j]
                                        colors_required.append(non_optimal_coloring[j])
                                        #print  "colors_used",colors_used
                                        #print "colors_required_1",colors_required
                                        #break
                                
                                isvalid=True
                                for k in g.keys():
     
                                        color_of_base_node=non_optimal_coloring[k]

                                        for neighbor in graph.all_neighbor(g,k):
                                             #print "neghbor for ",k,"are",neighbor
                                             color_of_neighbor = non_optimal_coloring[neighbor]
                                             if color_of_neighbor == color_of_base_node:
                                                  isvalid=False
                                                  break
                                                  #print "Coloring is not optimal and valid"
                                             #`print len (non_optimal_coloring)
                                        s = set( val for dic in non_optimal_coloring for val in non_optimal_coloring.values())
                                if isvalid==True and len(s) not in all_color_combinations.keys():
                                        print non_optimal_coloring
#                                        s = set( val for dic in non_optimal_coloring for val in non_optimal_coloring.values())
#                                        if len(s) not in all_color_combinations.keys():
                                        all_color_combinations[len(s)]=non_optimal_coloring
                                        print all_color_combinations
                                        minimum_key=min(all_color_combinations)
                                        #print minimum_key
                                        optimal_coloring=all_color_combinations[minimum_key]
                                        print optimal_coloring
                                        print g
                                        
                                        G=nx.MultiGraph()
                                        G.add_nodes_from(g.keys())
                                        G.add_edges_from(graph.get_edges(g))
                                        values = [non_optimal_coloring.get(n) for n in G.nodes()]
                                        pos=nx.spring_layout(G)       
                                        nx.draw(G,pos=pos,with_labels=True,cmap=plt.get_cmap('jet'), node_color=values)
                                        b = datetime.datetime.now()
                                        c = b - a
                                        print "time:", divmod(c.days * 86400 + c.seconds, 60)
                                         
                                        fig1 = plt.gcf()
                                        plt.show()
                                        plt.draw()
                                        fig1.savefig('solution_1_1.png', dpi=100)
    
                                        
                        #if isvalid==True:
                                
                                        
                              

                        
                                
'''
        def non_optimal_coloring(self,g):
                list_of_degrees=[]
                for i in g.keys():
                        list_of_degrees.append(len(g[i]))
                max_degree=max(list_of_degrees)
                print "Max_degree",max_degree
 #               shuffled_colors=convert_list(random.shuffle(colors))
#                print type(shuffled_colors)

                #print len(colors_required)

                for l in reversed(range(max_degree,len(g)+1)):
                        #print "l value",l
                        if l == len(g):
                                colors_required=colors[0:l]
                                permutations_of_all_colors=[x for x in itertools.permutations(colors_required)]
                                rang=len(permutations_of_all_colors)
                                for r in range(rang):
                                        colors_required=list(permutations_of_all_colors.pop())
                                        for i in g.keys():

                                                non_optimal_color_of_nodes[i]=colors_required.pop()
                          

                                        #print "Minimal optimal coloring of the graph",non_optimal_color_of_nodes
     
                                G=nx.MultiGraph()
                                G.add_nodes_from(g.keys())
                                G.add_edges_from(graph.get_edges(g))
                                values = [non_optimal_color_of_nodes.get(n) for n in G.nodes()]
                                pos=nx.spring_layout(G)       
                                nx.draw(G,pos=pos,with_labels=True,cmap=plt.get_cmap('jet'), node_color=values)
                                plt.show()
                                
                        else:
                                print "l value",l
                                colors_required=colors[0:l]
                                #print colors_required
                                permutations_of_all_colors=[x for x in itertools.permutations(colors_required)]
                                rang=len(permutations_of_all_colors)
                                
                                for r in range(rang):
                                        colors_required=list(permutations_of_all_colors.pop())
                                        for i in g.keys():
 
                                                if len(colors_required) !=0:
 #
                                                         non_optimal_color_of_nodes[i]=colors_required.pop()
                                                         colors_used=non_optimal_color_of_nodes[i]
                                                else:
                                                        non_optimal_color_of_nodes[i]=colors_used
                                                color_of_base_node=non_optimal_color_of_nodes[i]
                                               # print color_of_base_node,non_optimal_color_of_nodes

 #                                                non_optimal_color_of_nodes[i]
                                                for k in g.keys():
                                                        color_of_base_node=non_optimal_color_of_nodes[k]
                                                        isvalid=True
                                                        for neighbor in graph.all_neighbor(g,k):
                                                               color_of_neighbor = non_optimal_color_of_nodes[neighbor]
                                                               if color_of_neighbor == color_of_base_node:
                                                                  isvalid=False
                

                                                        if isvalid:
                                                                 all_possible_optimal_color_combinations.append(non_optimal_color_of_nodes)
                                                                       
                return len(all_possible_optimal_color_combinations)
                
                                              
                                      
                       
                        G=nx.MultiGraph()
                        G.add_nodes_from(g.keys())
                        G.add_edges_from(graph.get_edges(g))
                        values = [non_optimal_color_of_nodes.get(n) for n in G.nodes()]
                        pos=nx.spring_layout(G)       
                        nx.draw(G,pos=pos,with_labels=True,cmap=plt.get_cmap('jet'), node_color=values)
                        plt.show()
'''
        
        
graph=MultiGraph()

graph1=graph.new()

graph.addvertex(1)

graph.addedge(1,2,60)

graph.addedge(1,3,90)

graph.addedge(1,4,60)

graph.addedge(2,3,40)
graph.addedge(2,1,40)

graph.addedge(3,4,50)
graph.addedge(3,1,50)
graph.addedge(5,1,28)
graph.addedge(5,2,56)

BA_Graph=graph.BA_Graph(graph1,5,2)


'''

{1: {2: [60], 3: [90], 4: [60]}, 2: {1: [40], 3: [40]}, 3: {1: [50], 4: [50]}, 4: {}, 5: {1: [28], 3: [28]}, 6: {1: [85], 5: [85]}, 7: {1: [12], 3: [12]},
8: {5: [18], 7: [18]}, 9: {1: [18], 2: [18]}, 10: {1: [47], 2: [47]}, 11: {1: [18], 3: [18]}}

'''

#BA_Graph={1: {2: [60], 3: [90], 4: [60]}, 2: {1: [40], 3: [40]}, 3: {1: [50], 4: [50]}, 4: {}, 5: {1:[28],2:[56]}}


#print graph.optimal_coloring(BA_Graph)



print graph.visualize(BA_Graph)

#print BA_Graph

#print graph.get_edges(BA_Graph)







                 


