import math
#the dataset
x = [2,2,8,5,7,6,1,4]
y = [10,5,4,8,5,4,2,9]

#choose which custer the point belongs to

#repeat the last two for every point

#find the center[average] of each custer

#then repeat from take x and y of each point and deciding whether it belongs to a cluster

#stop when the centroid averages don't change

#number of cluster
k = 3

#eculdian distance for each centroid
e_distance_cluster1 = 0.0
e_distance_cluster2 = 0.0
e_distance_cluster3 = 0.0

#convergence check variables
converge = False

converge_prev_value_1_x = x[0]
converge_prev_value_1_y = y[0]

converge_prev_value_2_x = x[3]
converge_prev_value_2_y = y[3]

converge_prev_value_3_x = x[6]
converge_prev_value_3_y = y[6]

#iteration counter
iteration = 1

cluster1_list = [0]
cluster2_list = [3]
cluster3_list = [6]

#finding cluster groupings
while (converge == False):

    #the cluster lists contains points in that cluster
    

    #comparing each point to centroids
    for c in range(0,8):
        e_distance_cluster1 = math.sqrt(((converge_prev_value_1_x-x[c])**2) + ((converge_prev_value_1_y-y[c])**2))
        e_distance_cluster2 = math.sqrt(((converge_prev_value_2_x-x[c])**2) + ((converge_prev_value_2_y-y[c])**2))
        e_distance_cluster3 = math.sqrt(((converge_prev_value_3_x-x[c])**2) + ((converge_prev_value_3_y-y[c])**2))

        list_max = [e_distance_cluster1,e_distance_cluster2,e_distance_cluster3]

        if (min(list_max) == e_distance_cluster1):
            cluster1_list.append(c)
        elif(min(list_max) == e_distance_cluster2):
            cluster2_list.append(c)
        elif(min(list_max) == e_distance_cluster3):
            cluster3_list.append(c)
    
    converge_current_value_1_x = 0.0
    converge_current_value_1_y = 0.0

    converge_current_value_2_x = 0.0
    converge_current_value_2_y = 0.0

    converge_current_value_3_x = 0.0
    converge_current_value_3_y = 0.0

    #calculate new centroids
    if (len(cluster1_list) != 0):
        for c1 in cluster1_list:
            converge_current_value_1_x += x[c1]
            converge_current_value_1_y += y[c1]
        converge_current_value_1_x = converge_current_value_1_x/len(cluster1_list)
        converge_current_value_1_y = converge_current_value_1_y/len(cluster1_list)    

    if (len(cluster2_list) != 0):
        for c2 in cluster2_list:
            converge_current_value_2_x += x[c2]
            converge_current_value_2_y += y[c2]
        converge_current_value_2_x = converge_current_value_2_x/len(cluster2_list)
        converge_current_value_2_y = converge_current_value_2_y/len(cluster2_list) 

    if (len(cluster3_list) != 0):
        for c3 in cluster3_list:
            converge_current_value_3_x += x[c3]
            converge_current_value_3_y += y[c3]
        converge_current_value_3_x = converge_current_value_3_x/len(cluster3_list)
        converge_current_value_3_y = converge_current_value_3_y/len(cluster3_list)     

    if (converge_prev_value_1_x == converge_current_value_1_x) and (converge_prev_value_1_y == converge_current_value_1_y) and (converge_prev_value_2_x == converge_current_value_2_x) and (converge_prev_value_2_y == converge_current_value_2_y) and (converge_prev_value_3_x == converge_current_value_3_x) and (converge_prev_value_3_y == converge_current_value_3_y):
        converge = True

    print("Iteration ", iteration)

    print("Cluster 1: ", *iter(cluster1_list), sep=' ')
    print("Centroid: (", converge_current_value_1_x, ", ", converge_current_value_1_y, ")")

    print("Cluster 2: ", *iter(cluster2_list), sep=' ')
    print("Centroid: (", converge_current_value_2_x, ", ", converge_current_value_2_y, ")")

    print("Cluster 3: ", *iter(cluster3_list), sep=' ')
    print("Centroid: (", converge_current_value_3_x, ", ", converge_current_value_3_y, ")")

    iteration += 1

    converge_prev_value_1_x = converge_current_value_1_x
    converge_prev_value_1_y = converge_current_value_1_y

    converge_prev_value_2_x = converge_current_value_2_x
    converge_prev_value_2_y = converge_current_value_2_y

    converge_prev_value_3_x = converge_current_value_3_x
    converge_prev_value_3_y = converge_current_value_3_y

    cluster1_list = []
    cluster2_list = []
    cluster3_list = []


