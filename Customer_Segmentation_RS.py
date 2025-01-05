import pandas as pd

# Load the dataset
data = pd.read_csv(r'C:\Users\abdoh\Downloads\Customer Segmentation Project\Retail_Transactions_Dataset.csv')

# Display the first few rows of the dataset
print(data.head())


import pandas as pd


data = pd.read_csv(r'C:\Users\abdoh\Downloads\Customer Segmentation Project\Retail_Transactions_Dataset.csv')

# Display basic information about the dataset
print("Dataset Info:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Visualize the distribution of numerical columns
import matplotlib.pyplot as plt

# Histogram for Total_Cost
plt.hist(data['Total_Cost'], bins=20, edgecolor='k')
plt.title('Total Cost Distribution')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')
plt.show()

# Bar chart for Discount_Applied
data['Discount_Applied'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Discount Applied (True/False)')
plt.xlabel('Discount Applied')
plt.ylabel('Count')
plt.show()


from sklearn.preprocessing import MinMaxScaler

# Reload the dataset
data = pd.read_csv(r'C:\Users\abdoh\Downloads\Customer Segmentation Project\Retail_Transactions_Dataset.csv')

# Handle missing values in the 'Promotion' column
# Replace missing values with 'None'
data['Promotion'].fillna('None', inplace=True)

# Feature Engineering: Creating RFM Features
# Recency: Placeholder as we don't have the last purchase date, set all as a constant for now.
data['Recency'] = 365  # Assuming uniform value for demonstration 

# Frequency: Count the number of transactions per customer
frequency = data.groupby('Customer_Name')['Transaction_ID'].count()
data = data.merge(frequency, on='Customer_Name', suffixes=('', '_Frequency'))

# Monetary: Total spending per customer
monetary = data.groupby('Customer_Name')['Total_Cost'].sum()
data = data.merge(monetary, on='Customer_Name', suffixes=('', '_Monetary'))

# Drop duplicates to keep unique customers for clustering
data_unique = data.drop_duplicates(subset='Customer_Name')

# Normalize the RFM Features (Recency, Frequency, and Monetary)
scaler = MinMaxScaler()
data_unique[['Recency', 'Transaction_ID_Frequency', 'Total_Cost_Monetary']] = scaler.fit_transform(
    data_unique[['Recency', 'Transaction_ID_Frequency', 'Total_Cost_Monetary']]
)

# Display the transformed data
print("Transformed Data (Top 5 Rows):")
print(data_unique[['Customer_Name', 'Recency', 'Transaction_ID_Frequency', 'Total_Cost_Monetary']].head())

# Save the processed dataset for clustering
data_unique.to_csv(r'C:\Users\abdoh\Downloads\Customer_Segmentation_Processed.csv', index=False)



from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Select RFM features for clustering
rfm_features = data_unique[['Recency', 'Transaction_ID_Frequency', 'Total_Cost_Monetary']]

# Determine the optimal number of clusters using the Elbow Method
distortions = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_features)
    distortions.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.plot(K, distortions, 'bx-')
plt.xlabel('Number of Clusters')
plt.ylabel('Distortion')
plt.title('Elbow Method to Determine Optimal Clusters')
plt.show()

# Apply K-Means with optimal clusters (assuming k=3 for demonstration)
optimal_clusters = 3  
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data_unique['Cluster'] = kmeans.fit_predict(rfm_features)

# Evaluate clustering using Silhouette Score
silhouette_avg = silhouette_score(rfm_features, data_unique['Cluster'])
print(f'Silhouette Score for {optimal_clusters} clusters: {silhouette_avg}')

# Visualize the clusters in 2D (using first two RFM features)
plt.scatter(data_unique['Transaction_ID_Frequency'], data_unique['Total_Cost_Monetary'], 
            c=data_unique['Cluster'], cmap='viridis')
plt.xlabel('Frequency')
plt.ylabel('Monetary')
plt.title('Customer Segments')
plt.colorbar(label='Cluster')
plt.show()



# Apply K-Means with the chosen number of clusters (3)
optimal_clusters = 3  
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
data_unique['Cluster'] = kmeans.fit_predict(rfm_features)

# Evaluate clustering using Silhouette Score
silhouette_avg = silhouette_score(rfm_features, data_unique['Cluster'])
print(f'Silhouette Score for {optimal_clusters} clusters: {silhouette_avg}')

# Visualize the clusters
plt.scatter(data_unique['Transaction_ID_Frequency'], data_unique['Total_Cost_Monetary'], 
            c=data_unique['Cluster'], cmap='viridis')
plt.xlabel('Frequency')
plt.ylabel('Monetary')
plt.title(f'Customer Segments with {optimal_clusters} Clusters')
plt.colorbar(label='Cluster')
plt.show()

#Analyze the charachteristics of each cluster

cluster_summary = data_unique.groupby('Cluster')[['Transaction_ID_Frequency', 'Total_Cost_Monetary']].mean()
print(cluster_summary)


