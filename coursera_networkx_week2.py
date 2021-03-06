
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 2 - Network Connectivity
# 
# In this assignment you will go through the process of importing and analyzing an internal email communication network between employees of a mid-sized manufacturing company. 
# Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

# In[2]:

import networkx as nx

# This line must be commented out when submitting to the autograder
#!head email_network.txt


# ### Question 1
# 
# Using networkx, load up the directed multigraph from `email_network.txt`. Make sure the node names are strings.
# 
# *This function should return a directed multigraph networkx graph.*

# In[3]:

def answer_one():
    #read txt file ,and get print(nx.info(G))
    G = nx.read_edgelist('email_network.txt', delimiter='\t', data=[('time', int)], create_using=nx.MultiDiGraph())
    return G


# In[18]:

answer_one()


# ### Question 2
# 
# How many employees and emails are represented in the graph from Question 1?
# 
# *This function should return a tuple (#employees, #emails).*

# In[27]:

def answer_two():
    g = answer_one()
    #count number of nodes and edges 
    return len(g.nodes()), len(g.edges())


# In[28]:

answer_two()


# ### Question 3
# 
# * Part 1. Assume that information in this company can only be exchanged through email.
# 
#     When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# *This function should return a tuple of bools (part1, part2).*

# In[37]:

def answer_three():
    g1 = answer_one()
    # part 1 check for strongly connected 
    # part 2 check for weekly connected(convert directional graph to uni directional ) 
    return nx.is_strongly_connected(g1),nx.is_connected(g1.to_undirected())
answer_three()


# ### Question 4
# 
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# 
# *This function should return an int.*

# In[ ]:

def answer_four():
    G = answer_one()  
    #weekly_conn = (nx.weakly_connected_components(G))
    largest_cc = max(nx.weakly_connected_components(G), key=len)
    return largest_cc


# In[ ]:

def answer_four():
    G = answer_one()
    wccs = nx.weakly_connected_components(G)
    print(wcss)
    return len(max(wccs, key=len))
answer_four()


# ### Question 5
# 
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# 
# *This function should return an int*

# In[20]:

def answer_five():
    G = answer_one()
    sccs = nx.strongly_connected_components(G)
    return len(max(sccs, key=len))


# ### Question 6
# 
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. 
# Call this graph G_sc.
# 
# *This function should return a networkx MultiDiGraph named G_sc.*

# In[22]:

def answer_six():
    G = answer_one()
    scc = nx.strongly_connected_component_subgraphs(G)
    G_sc = max(scc,key=len)
    return G_sc
answer_six()


# ### Question 7
# 
# What is the average distance between nodes in G_sc?
# 
# *This function should return a float.*

# In[23]:

def answer_seven():    
    g = answer_six()
    avd_dist = nx.average_shortest_path_length(g)
    return avd_dist


# ### Question 8
# 
# What is the largest possible distance between two employees in G_sc?
# 
# *This function should return an int.*

# In[25]:

def answer_eight():   
    g = answer_six() 
    return (nx.diameter(g))


# ### Question 9
# 
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# 
# *This function should return a set of the node(s).*

# In[27]:

def answer_nine():   
    g = answer_six()
    a = (nx.periphery(g))
    
    return set(a)
#answer_nine()


# ### Question 10
# 
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# 
# *This function should return a set of the node(s).*

# In[28]:

def answer_ten():
        
    g = answer_six()
    
    return set(nx.center(g))
#answer_ten()


# ### Question 11
# 
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# 
# How many nodes are connected to this node?
# 
# 
# *This function should return a tuple (name of node, number of satisfied connected nodes).*

# In[ ]:

def answer_eleven():
        
    # Your Code Here
    
    return # Your Answer Here


# ### Question 12
# 
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)? 
# 
# *This function should return an integer.*

# In[ ]:

def answer_twelve():
        
    # Your Code Here
    
    return # Your Answer Here


# ### Question 13
# 
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# 
# *This function should return a networkx Graph.*

# In[31]:

def answer_thirteen():
        
    g = answer_six()
    g_undirected = g.to_undirected()
    g_un = nx.Graph(g_undirected)
    
    return g_un
#answer_thirteen()


# ### Question 14
# 
# What is the transitivity and average clustering coefficient of graph G_un?
# 
# *This function should return a tuple (transitivity, avg clustering).*

# In[33]:

def answer_fourteen():
        
    g13 = answer_thirteen()
    return nx.transitivity(g13),nx.average_clustering(g13)
#answer_fourteen()

