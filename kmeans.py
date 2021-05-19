import math
#extracting the dataset
x = [2,2,8,5,7,6,1,4]
y = [10,5,4,8,5,4,2,9]
#dataset = open('dataset.txt')
#for i in dataset:
#    x[i]= i.split()[0]
#    y[i]= i.split()[1]

#cluster data into k groups

#select points for center of centeroid

#take the x and y at each point and calculate ecludian distance
#to each centroid


#choose which custer the point belongs to

#repeat the last two for every point

#find the center[average] of each custer

#then repeat from take x and y of each point and deciding whether it belongs to a cluster

#stop when the centroid averages don't change

#number of cluster
k = 3

#the cluster centroid point no.
cluster1 = 0
cluster2 = 3
cluster3 = 6

#the cluster lists contains points in that cluster
cluster1_list = []
cluster2_list = []
cluster3_list = []

#eculdian distance for each centroid
e_distance_cluster1 = 0.0
e_distance_cluster2 = 0.0
e_distance_cluster3 = 0.0
a = 0
#finding cluster groupings
while (a < 3):
    a+=1
    for c in range(0,8):
        print(c)
        e_distance_cluster1 = math.sqrt(((x[cluster1]-x[c])**2) +((y[cluster1]-y[c])**2))
        e_distance_cluster2 = math.sqrt(((x[cluster2]-x[c])**2) +((y[cluster2]-y[c])**2))
        e_distance_cluster3 = math.sqrt(((x[cluster3]-x[c])**2) +((y[cluster3]-y[c])**2))

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



print(x)
print(y)
