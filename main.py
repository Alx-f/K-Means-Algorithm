import random

def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the initial users, to be used as centroids.
    initial_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)

    # This creates a new list of just the features for the centroids, not the initial ids. It stores the index too, which will be used as the label.
    centroids = [[user_feature_map[x], idx] for idx, x in enumerate(initial_centroid_users)]


    # This is the main loop. "Repeat at least 10 times"
    for _ in range(10):
        user_closest_centroids = {}
        # step 1,2 - groups users to the centroids
        for user in user_feature_map:
            user_closest_centroids[user] = centroid_distances(user_feature_map[user], centroids)

        # Step 3
        for centroid in centroids:
            centroid[0] = new_centroid_average(centroid, user_closest_centroids, user_feature_map)


    return_list = []

    for cent in centroids:
        return_list.append(cent[0])

    return return_list


# Return list of the distances from each centroid
def centroid_distances(user, centroids):
    distances = []
    
    for centroid in centroids:
        centroid_features = centroid[0]
        centroid_id = centroid[1]

        # 4 feature manhattan distance
        
        distance = sum([abs(val1-val2) for val1, val2 in zip(user,centroid_features)])

        distances.append([distance, centroid_id])

    # Returns the centroid ID for the closest one.

    return sorted(distances, key=lambda x: x[0])[0][1]

def new_centroid_average(centroid, user_closest_centroids, user_feature_map):
    centroid_features = centroid[0]
    centroid_id = centroid[1]
    
    # List of users if their closest centroid is the same id as currently looked at centroid
    
    corresponding_users_features = [user_feature_map[x] for x in user_closest_centroids if user_closest_centroids[x] == centroid_id]

    # Get average of all user features
    feature_1_average = 0
    feature_2_average = 0
    feature_3_average = 0
    feature_4_average = 0

    for user in corresponding_users_features:
        feature_1_average += user[0]
        feature_2_average += user[1]
        feature_3_average += user[2]
        feature_4_average += user[3]

    length_users = len(corresponding_users_features)

    return [feature_1_average/length_users, feature_2_average/length_users, feature_3_average/length_users, feature_4_average/length_users]
