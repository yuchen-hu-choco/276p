
import numpy as np
import tensorflow as tf

'''Dummy Data'''
# each row represents a user's rating for the different jobs
users_jobs = tf.constant([
                [4,  6,  8,  0, 0, 0],
                [0,  0, 10,  0, 8, 3],
                [0,  6,  0,  0, 3, 7],
                [10, 9,  0,  5, 0, 2]],dtype=tf.float32)

# features of each jobs
# e.g. columns could represent ['Enrey_Level', 'high_salary', 'Degree_required', 'full_time', 'big_company']
jobs_features = tf.constant([
                [1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 0, 1]],dtype=tf.float32)

users = ['Caleb', 'Yaxuan',  'Yukan', 'Yuchen']
jobs = ['Software Engineer - Amazon', 'Software Developer - abc technology',
          'applied scientist - Google', 'manager - taco bell', 'register nurse - uci', 'Analyst - Goldman Sachs']
features = ['Enrey_Level', 'high_salary', 'Degree_required', 'full_time', 'big_company']

num_users = len(users)
num_jobs = len(jobs)
num_features = len(features)
num_recommendations = 2

# product then standardize
users_features = tf.matmul(users_jobs, jobs_features)

users_features = users_features/tf.reduce_sum(users_features,axis=1,keepdims=True)

# ranking top features
top_users_features = tf.nn.top_k(users_features, num_features)[1]

for i in range(num_users):
    feature_names = [features[int(index)] for index in top_users_features[i]]
    print('{}: {}'.format(users[i], feature_names))


# calculate top ratings
users_ratings = tf.matmul(users_features, tf.transpose(jobs_features))

print(users_ratings);

users_ratings_new = tf.where(tf.equal(users_jobs, tf.zeros_like(users_jobs)),
                                  users_ratings,
                                  tf.zeros_like(tf.cast(users_jobs, tf.float32)))

top_jobs = tf.nn.top_k(users_ratings_new, num_recommendations)[1]

for i in range(num_users):
    job_names = [jobs[index] for index in top_jobs[i]]
    print('{}: {}'.format(users[i], job_names))
