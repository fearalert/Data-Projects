import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Read the dataset into a pandas DataFrame
data = pd.read_csv('Market_Basket_DataSet.csv')

# Print the column names to verify
print("Columns in the dataset:", data.columns)

# Correct the attributes list based on actual column names
attributes = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

# Check if the attributes exist in the dataset
missing_columns = [col for col in attributes if col not in data.columns]
if missing_columns:
    print(f"Missing columns: {missing_columns}")
else:
    # Select the attributes for clustering
    X = data[attributes]

    # Determine the optimal number of clusters using the elbow method
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    # Plot the elbow curve to visualize the optimal number of clusters
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.show()

    # Based on the elbow curve, select the optimal number of clusters
    n_clusters = 5

    # Perform K-means clustering with the selected number of clusters
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
    kmeans.fit(X)

    # Add the cluster labels to the original dataset
    data['Cluster'] = kmeans.labels_

    # Print the cluster centers
    cluster_centers = kmeans.cluster_centers_
    print("Cluster Centers:")
    print(cluster_centers)

    # Visualize the clusters in a scatter plot
    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=kmeans.labels_, cmap='viridis')
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='X', color='red', s=100)
    plt.title('K-means Clustering')
    plt.xlabel('Age')
    plt.ylabel('Annual Income (k$)')
    plt.show()
