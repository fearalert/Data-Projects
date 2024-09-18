import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Load the dataset
data = pd.read_csv('Market_Basket_Dataset.csv', header=None)
transactions = data[0].str.split(',')

# Convert transactions into a list of lists
transactions_list = transactions.to_list()

# Perform one-hot encoding
te = TransactionEncoder()
te_data = te.fit_transform(transactions_list)
df = pd.DataFrame(te_data, columns=te.columns_)

# Perform association rules mining using Apriori algorithm
min_support = 0.05
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Prune the frequent itemsets based on support threshold
support_threshold = 0.02
pruned_itemsets = frequent_itemsets[frequent_itemsets['support'] <= support_threshold]

# Check if pruned_itemsets is empty
if pruned_itemsets.empty:
    # Display the frequent itemsets and association rules
    print("Frequent Itemsets:")
    print(frequent_itemsets)

    print("\nAssociation Rules from Frequent Itemsets:")
    print(rules)
    
    print("\nNo pruned itemsets found with the given support threshold.")

else:
    # Generate association rules from the pruned itemsets
    pruned_rules = association_rules(pruned_itemsets, metric='lift', min_threshold=1)

    # Display the pruned frequent itemsets and association rules
    print("Pruned Frequent Itemsets:")
    print(pruned_itemsets)

    print("\nAssociation Rules from Pruned Itemsets:")
    print(pruned_rules)
