# Market Basket Clustering Analysis

## Overview

This project implements K-means clustering on a market basket dataset to identify distinct customer segments based on their age, annual income, and spending score. The goal is to understand customer behavior and facilitate targeted marketing strategies.

## Dataset

The dataset used for this analysis is `Market_Basket_DataSet.csv`, which contains the following columns:

- **Age**: The age of the customer.
- **Annual Income (k$)**: The annual income of the customer in thousands of dollars.
- **Spending Score (1-100)**: A score assigned by the retailer based on the customer's purchasing behavior.

## Requirements

To run this project, you will need the following Python libraries:

- pandas
- scikit-learn
- matplotlib

You can install the required libraries using pip:

```bash
pip install pandas scikit-learn matplotlib
```
## Usage

1. **Load the Dataset**: The dataset is loaded into a pandas DataFrame.

2. **Verify Columns**: The script prints the column names to ensure that the necessary attributes are present.

3. **Select Attributes**: The relevant attributes for clustering are selected.

4. **Elbow Method**: The optimal number of clusters is determined using the elbow method. The Within-Cluster Sum of Squares (WCSS) is calculated for different cluster counts, and the results are plotted.

5. **K-means Clustering**: Based on the elbow curve, the optimal number of clusters (set to 5) is used to perform K-means clustering.

6. **Cluster Labels**: The cluster labels are added to the original dataset.

7. **Visualize Clusters**: A scatter plot visualizes the clusters and their centers.

## Run the script in your Python environment:

```bash
python3 clustering_analysis.py
```
Make sure the Market_Basket_DataSet.csv file is in the same directory as the script.

## Conclusion
This analysis provides insights into customer segmentation, which can be leveraged for personalized marketing efforts. Future work may include exploring additional features and applying different clustering techniques.
