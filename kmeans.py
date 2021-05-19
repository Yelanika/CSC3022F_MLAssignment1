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

#the cluster centroid point no.
cluster1_x = x[0]
cluster1_y = y[0]

cluster2_x = x[3]
cluster2_y = y[3]

cluster3_x = x[6]
cluster3_y = y[6]

#the cluster lists contains points in that cluster
cluster1_list = []
cluster2_list = []
cluster3_list = []

#eculdian distance for each centroid
e_distance_cluster1 = 0.0
e_distance_cluster2 = 0.0
e_distance_cluster3 = 0.0

#convergence check variables
converge = False
converge_prev_value = 0.0
converge_current_value = 0.0

#finding cluster groupings
while (converge == False):

    #comparing each point to centroids
    for c in range(0,8):
        print(c)
        e_distance_cluster1 = math.sqrt(((cluster1_x-x[c])**2) + ((cluster1_y-y[c])**2))
        e_distance_cluster2 = math.sqrt(((cluster2_x-x[c])**2) + ((cluster2_y-y[c])**2))
        e_distance_cluster3 = math.sqrt(((cluster3_x-x[c])**2) + ((cluster3_y-y[c])**2))

        list_max = [e_distance_cluster1,e_distance_cluster2,e_distance_cluster3]

        if (max(list_max) == e_distance_cluster1):
            #add to list of cluster 1
            cluster1_list.append(c)
        elif(max(list_max) == e_distance_cluster2):
            cluster2_list.append(c)
            #add to list of cluster 2
        elif(max(list_max) == e_distance_cluster3):
            #add to list of cluster 3
            cluster3_list.append(c)
    
    #calculate new centroids
    

        



print(x)
print(y)
