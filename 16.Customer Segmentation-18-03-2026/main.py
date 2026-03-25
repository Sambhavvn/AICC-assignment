import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("customer.csv")

print(df.head())
print(df.info())
print(df.describe())

X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []
K_range = range(1, 11)

for k in K_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_scaled)
    wcss.append(model.inertia_)

plt.figure()
plt.plot(K_range, wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid()
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

df['Cluster'] = clusters

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.figure()
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=clusters)
plt.scatter(centroids[:,0], centroids[:,1], s=300, marker='X')
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()

cluster_summary = df.groupby('Cluster').mean(numeric_only=True)
print("\nCluster Summary:\n", cluster_summary)

for i in range(5):
    print(f"\nCluster {i} Customers:\n")
    print(df[df['Cluster'] == i])

def describe_cluster(row):
    income = row['Annual Income (k$)']
    score = row['Spending Score (1-100)']
    
    if income > 20 and score > 70:
        return "High Income - High Spending"
    elif income > 20 and score < 40:
        return "High Income - Low Spending"
    elif income < 20 and score > 70:
        return "Low Income - High Spending"
    elif income < 20 and score < 40:
        return "Low Income - Low Spending"
    else:
        return "Average"

df['Segment_Type'] = df.apply(describe_cluster, axis=1)

print("\nFinal Segmented Data:\n")
print(df[['CustomerID','Annual Income (k$)','Spending Score (1-100)','Cluster','Segment_Type']])