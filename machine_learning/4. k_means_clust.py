'''
k-평균 알고리즘 (k-means clustering)
자율 학습(unsupervised learning)의 일종이다. 주어진 데이터를 k개의 클러스터로 묶는 알고리즘으로, 
각 클러스터와 거리 차이의 분산을 최소화하는 방식으로 동작한다. 

동작 방식:
  1. 'k'값 정의, 'X'는 feature arraydefine, 'hetrogeneity'는 빈 배열
  
  2. 각 그룹의 중심(centroid) 초기화
  
        initial_centroids = get_initial_centroids(
            X, 
            k, 
            seed=0 # 초기화를 위한 시드, None은 랜덤 생성 (default=None)
            )

  3. 각 그룹의 중심을 찾고 k-means 함수를 이용해 그룹화(cluster)
  
        centroids, cluster_assignment = kmeans(
            X, 
            k, 
            initial_centroids, 
            maxiter=400,
            record_heterogeneity=heterogeneity, 
            verbose=True # whether to print logs in console or not.(default=False)
            )
  
  
  4. 비용 함수와 그룹간 비유사도를 매 반복마다 출력
        plot_heterogeneity(
            heterogeneity, 
            k
        )
'''

from __future__ import print_function
from sklearn.metrics import pairwise_distances
import numpy as np

TAG = 'K-MEANS-CLUST/ '

def get_initial_centroids(data, k, seed=None):
    '''k개의 데이터를 랜덤으로 뽑아서 그룹의 중심으로 초기화'''
    if seed is not None: # 일정한 결과를 출력하게 해줌
        np.random.seed(seed)
    n = data.shape[0] # 데이터의 개수
        
    # K번째 원소를 봅음 [0, N).
    rand_indices = np.random.randint(0, n, k)
    
    centroids = data[rand_indices,:]
    
    return centroids

def centroid_pairwise_dist(X,centroids):
    return pairwise_distances(X,centroids,metric='euclidean')

def assign_clusters(data, centroids):
    
    # 각 데이터와 그룹의 중심간의 거리를 계산:
    distances_from_centroids = centroid_pairwise_dist(data,centroids)
    
    # 각 데이터들의 그룹을 계산:
    cluster_assignment = np.argmin(distances_from_centroids,axis=1)
    
    return cluster_assignment

def revise_centroids(data, k, cluster_assignment):
    new_centroids = []
    for i in range(k):
        # i번째 그룹에 속하는 데이터를 모두 고름:
        member_data_points = data[cluster_assignment==i]
        # 데이터들의 중간값을 계산:
        centroid = member_data_points.mean(axis=0)
        new_centroids.append(centroid)
    new_centroids = np.array(new_centroids)
    
    return new_centroids

def compute_heterogeneity(data, k, centroids, cluster_assignment):
    
    heterogeneity = 0.0
    for i in range(k):
        
        member_data_points = data[cluster_assignment==i, :]
        
        if member_data_points.shape[0] > 0: # i번째 그룹이 비었는지 확인
            distances = pairwise_distances(member_data_points, [centroids[i]], metric='euclidean')
            squared_distances = distances**2
            heterogeneity += np.sum(squared_distances)
        
    return heterogeneity

from matplotlib import pyplot as plt
def plot_heterogeneity(heterogeneity, k):
    plt.figure(figsize=(7,4))
    plt.plot(heterogeneity, linewidth=4)
    plt.xlabel('# Iterations')
    plt.ylabel('Heterogeneity')
    plt.title('Heterogeneity of clustering over time, K={0:d}'.format(k))
    plt.rcParams.update({'font.size': 16})
    plt.show()

def kmeans(data, k, initial_centroids, maxiter=500, record_heterogeneity=None, verbose=False):
    '''This function runs k-means on given data and initial set of centroids.
       maxiter: maximum number of iterations to run.(default=500)
       record_heterogeneity: (optional) a list, to store the history of heterogeneity as function of iterations
                             if None, do not store the history.
       verbose: if True, print how many data points changed their cluster labels in each iteration'''
    centroids = initial_centroids[:]
    prev_cluster_assignment = None
    
    for itr in range(maxiter):        
        if verbose:
            print(itr, end='')
        
        # 1. 가장 가까운 그룹의 중심으로 그룹화를 지음
        cluster_assignment = assign_clusters(data,centroids)
            
        # 2. k 그룹을 바탕으로 새로운 그룹의 중심을 계산
        centroids = revise_centroids(data,k, cluster_assignment)
            
        # 그룹이 바꼈는지 확인: none이면 바꼈거나 중단
        if prev_cluster_assignment is not None and \
          (prev_cluster_assignment==cluster_assignment).all():
            break
        
        # 새로운 그룹을 출력
        if prev_cluster_assignment is not None:
            num_changed = np.sum(prev_cluster_assignment!=cluster_assignment)
            if verbose:
                print('    {0:5d} elements changed their cluster assignment.'.format(num_changed))   
        
        # 그룹간 비유사도를 측정
        if record_heterogeneity is not None:
            # YOUR CODE HERE
            score = compute_heterogeneity(data,k,centroids,cluster_assignment)
            record_heterogeneity.append(score)
        
        prev_cluster_assignment = cluster_assignment[:]
        
    return centroids, cluster_assignment

# 테스트
if False: # true로 바꿔 run
    import sklearn.datasets as ds
    dataset = ds.load_iris()
    k = 3
    heterogeneity = []
    initial_centroids = get_initial_centroids(dataset['data'], k, seed=0)
    centroids, cluster_assignment = kmeans(dataset['data'], k, initial_centroids, maxiter=400,
                                        record_heterogeneity=heterogeneity, verbose=True)
    plot_heterogeneity(heterogeneity, k)
