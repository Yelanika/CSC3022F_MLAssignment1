#importing math for the sqrt function
import math

#the dataset
x = [2,2,8,5,7,6,1,4]
y = [10,5,4,8,5,4,2,9]

#number of cluster
k = 3

#eculdian distance initialsation for each centroid
e_distance_cluster1 = 0.0
e_distance_cluster2 = 0.0
e_distance_cluster3 = 0.0

#convergence checking variables initialsation
converge = False

converge_prev_value_1_x = x[0]
converge_prev_value_1_y = y[0]

converge_prev_value_2_x = x[3]
converge_prev_value_2_y = y[3]

converge_prev_value_3_x = x[6]
converge_prev_value_3_y = y[6]

#iteration counter
iteration = 1

#Clusters lists which holds the dataset points in a cluster
cluster1_list = [0]
cluster2_list = [3]
cluster3_list = [6]

#printing initial interation before any computation occurs
print("Iteration 0")

print("Cluster 1: 1")
print("Centroid: (", round(x[0],2), ", ", round(y[0],2) , ")")

print("Cluster 2: 4")
print("Centroid: (", round(x[3],2) , ", ", round(y[3],2) , ")")

print("Cluster 3: 7")
print("Centroid: (", round(x[6],2), ", ", round(y[6],2), ")")

#finding cluster groupings
while (converge == False):

    #comparing each point to centroids
    for c in range(0,8):
            e_distance_cluster1 = math.sqrt(((converge_prev_value_1_x-x[c])**2) + ((converge_prev_value_1_y-y[c])**2))
            e_distance_cluster2 = math.sqrt(((converge_prev_value_2_x-x[c])**2) + ((converge_prev_value_2_y-y[c])**2))
            e_distance_cluster3 = math.sqrt(((converge_prev_value_3_x-x[c])**2) + ((converge_prev_value_3_y-y[c])**2))

            list_max = [e_distance_cluster1,e_distance_cluster2,e_distance_cluster3]

            
            if (min(list_max) == e_distance_cluster1):                
                if c not in cluster1_list:
                    cluster1_list.append(c) 
            elif(min(list_max) == e_distance_cluster2):
                if c not in cluster2_list:
                    cluster2_list.append(c)
            elif(min(list_max) == e_distance_cluster3):
                if c not in cluster3_list:
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

    #checking whether convergence occurs in iteration, to exit the while loop and end program
    if (converge_prev_value_1_x == converge_current_value_1_x) and (converge_prev_value_1_y == converge_current_value_1_y) and (converge_prev_value_2_x == converge_current_value_2_x) and (converge_prev_value_2_y == converge_current_value_2_y) and (converge_prev_value_3_x == converge_current_value_3_x) and (converge_prev_value_3_y == converge_current_value_3_y):
        converge = True

    #updating dataset points accordingly in the cluster lists
    for k in range(0,len(cluster1_list)):
        cluster1_list[k] +=1

    for k in range(0,len(cluster2_list)):
        cluster2_list[k] +=1

    for k in range(0,len(cluster3_list)):
        cluster3_list[k] +=1

    #printing iteration information
    print("Iteration ", iteration)

    print("Cluster 1: ", *iter(cluster1_list), sep=' ')
    print("Centroid: (", round(converge_current_value_1_x, 2), ", ", round(converge_current_value_1_y,2) , ")")

    print("Cluster 2: ", *iter(cluster2_list), sep=' ')
    print("Centroid: (", round(converge_current_value_2_x,2) , ", ", round(converge_current_value_2_y,2) , ")")

    print("Cluster 3: ", *iter(cluster3_list), sep=' ')
    print("Centroid: (", round(converge_current_value_3_x,2), ", ", round(converge_current_value_3_y,2), ")")

    #incrementing the iteration counter
    iteration += 1

    #assigning the current centroid values to previous centroid values
    converge_prev_value_1_x = converge_current_value_1_x
    converge_prev_value_1_y = converge_current_value_1_y

    converge_prev_value_2_x = converge_current_value_2_x
    converge_prev_value_2_y = converge_current_value_2_y

    converge_prev_value_3_x = converge_current_value_3_x
    converge_prev_value_3_y = converge_current_value_3_y

    #deleting the old custer information, in order to assign new cluster information
    cluster1_list = []
    cluster2_list = []
    cluster3_list = []


