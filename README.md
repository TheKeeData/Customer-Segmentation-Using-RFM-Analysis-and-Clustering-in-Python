# Customer Segmentation Using RFM Analysis and Clustering in Python
## Overview

This project applies clustering techniques to segment customers based on their purchasing behaviors. In addition, by analyzing customer transaction data, the project identifies distinct customer groups to guide personalized marketing strategies and improve customer engagement.

## Objectives

- Identify actionable customer segments based on Recency, Frequency, and Monetary (RFM) metrics.
- Enable targeted marketing strategies tailored to specific customer behaviors.
- Provide visual and analytical insights for decision-making.

## Dataset

The dataset used for this analysis is found on Kaggle and it includes 1 million retail transactions with the following:

1-Transaction_ID: Unique identifier for each transaction.

2-Customer_Name: Identifier for each customer.

3-Total_Cost: Total amount spent in a transaction.

4-Total_Items: Number of items in a transaction.

5-Customer_Category: Demographic group or background of the customer.

6-Product: Products purchased in the transaction.

7-Discount_Applied: Binary indicator of whether a discount was used.

8-Season: Season of the transaction.

9-Promotion: Type of promotion applied (e.g., "BOGO," "None").

10-City: Location of the purchase.

This dataset is suitable for performing RFM analysis (Recency, Frequency, Monetary value) and clustering customers for segmentation.


## Methodology

1. **Data Preprocessing**:
   
   - Normalized RFM metrics for fair clustering.
     
   - Handled missing values in the dataset.
   
   - Engineered features to represent customer behaviors.

3. **Clustering**:
   
   - Applied the K-Means algorithm to group customers.
     
   - Used the Elbow Method to determine the optimal number of clusters (3 clusters).
     
   - Evaluated clustering quality with a Silhouette Score of **0.863**, indicating well-defined clusters.

5. **Analysis and Recommendations**:

   - Cluster analysis revealed three distinct customer groups:
     
     - **Occasional Shoppers**: Infrequent, low spenders.
       
     - **Regular Customers**: Moderate frequency and spending.
       
     - **High-Value Customers**: High frequency and spending, core revenue contributors.
       
   - Recommendations include targeted promotions, loyalty programs, and personalized experiences.

## Results

### Key Insights

- **Cluster 0: Occasional Shoppers**
  
  - Low frequency and spending.
    
  - Suggested actions: Re-engage with discounts and first-purchase rewards.

- **Cluster 1: Regular Customers**
  
  - Moderate frequency and spending.
    
  - Suggested actions: Maintain loyalty with occasional promotions and upselling.

- **Cluster 2: High-Value Customers**
  
  - High frequency and spending.
    
  - Suggested actions: Retain and reward through VIP perks and tailored recommendations.

### Visualizations
- **Elbow Method**: Used to determine the optimal number of clusters.
   
![Fig_6 elbow methods to calculate clusters](https://github.com/user-attachments/assets/1366d322-411f-4c9e-9909-01af3250a0fa)


- **Customer Segments**: Scatter plot showing distinct clusters based on Frequency and Monetary value.
   
![Fig_7 Customer segments](https://github.com/user-attachments/assets/730eaefe-daf7-4b01-bce3-fae72e212432)

- **Silhouette Score**: Achieved a score of **0.863**, indicating high-quality clustering.  

![figure_8  score for 3 clusters](https://github.com/user-attachments/assets/cb2b969b-a751-4c13-a719-468f2daf70a4)

- Additional visualizations include:
  
  - Distribution of Total Costs:
    
    ![Fig_1_Total Cost Distribution](https://github.com/user-attachments/assets/06558ef5-10d3-4bb2-89ee-7c5804a214e1)

  - Discount Application Analysis:
  
![Fig_2  Discount applied](https://github.com/user-attachments/assets/ab9b13b3-dc73-48a1-8f7b-3bdf177b0385)


