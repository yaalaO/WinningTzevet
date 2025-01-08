from sklearn.cluster import KMeans
from main import *
import os.path


########################
#     data             #
########################

original_table = load_file(
    "input/with_id/With ID/Target bank data/Ashdod_with_ID.csv")
tables = separate_by_ids(original_table)



########################
#        funcs         #
########################

def extract_max_z_with_time(table):
    dat = (table[["time", 'z']]).copy()
    dat.sort_values(by='time', inplace=True)
    start = dat['time'][0]
    dat.sort_values(by='z', inplace=True)
    end = dat['time']
    max_z = dat['z']

    time_to_max = end - start
    return max_z, time_to_max


print(tables[0]['z'])






########################
#     algorithm        #
########################
if False:
    kmeans = KMeans(init="random", n_clusters=4, n_init=10, max_iter=300, random_state=42 )
    kmeans.fit(tables) #Replace your training dataset instead of x_train
    # The lowest SSE value
    print(kmeans.inertia_)
    # Final locations of the centroid
    print(kmeans.cluster_centers_)
    # The number of iterations required to converge
    print(kmeans.n_iter_)
    # first five predicted labels
    print(kmeans.labels_[:5])


# init controls the initialization technique. The standard version of the k-means algorithm is implemented by setting init to "random". Setting this to "k-means++" employs an advanced trick to speed up convergence, which you’ll use later.

# n_clusters sets k for the clustering step. This is the most important parameter for k-means.

# n_init sets the number of initializations to perform. This is important because two runs can converge on different cluster assignments. The default behavior for the scikit-learn algorithm is to perform ten k-means runs and return the results of the one with the lowest SSE.

# max_iter sets the number of maximum iterations for each initialization of the k-means algorithm.