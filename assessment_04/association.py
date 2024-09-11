import logging
from itertools import combinations, chain

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AssociationRuleMining:
    def __init__(self, rows: list[list[str]], m: int):
        self.rows = rows
        self.candidates = set(chain(*[combinations(row, m) for row in rows]))
        logging.info(f"Initialized with {len(rows)} transactions and {len(self.candidates)} initial candidates")

    def get_frequent_itemsets(self, itemsets, min_support: int, max_support: int):
        itemset_counts = {itemset: 0 for itemset in itemsets}
        
        for transaction in self.rows:
            transaction_set = set(transaction)
            for itemset in itemsets:
                if set(itemset).issubset(transaction_set):
                    itemset_counts[itemset] += 1

        frequent_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count >= min_support and count < max_support}
        logging.info(f"Generated {len(frequent_itemsets)} frequent itemsets with min_support {min_support}")
        return frequent_itemsets
    
    def apriori(self, min_support: int, max_support: int):
        items = sorted(set(chain(*self.rows)))
        k = 1
        frequent_itemsets = {}
        current_itemsets = {tuple([item]) for item in items}
        logging.info(f"Starting Apriori with {len(current_itemsets)} single-item itemsets")

        while current_itemsets:
            current_frequent_itemsets = self.get_frequent_itemsets(current_itemsets, min_support, max_support)
            frequent_itemsets.update(current_frequent_itemsets)
            
            k += 1
            current_itemsets = self.get_itemsets(k)
            current_itemsets = {itemset for itemset in current_itemsets if all(subset in frequent_itemsets for subset in combinations(itemset, k-1))}
            logging.info(f"Generated {len(current_itemsets)} itemsets of length {k}")

        return frequent_itemsets

    def get_itemsets(self, k):
        return set(chain(*[combinations(row, k) for row in self.rows]))

    def generate_association_rules(self, frequent_itemsets, min_confidence):
        rules = []
        
        # he first item or itemset is the antecedent, and the second is the consequent
        
        for itemset, support in frequent_itemsets.items():
            for i in range(1, len(itemset)):
                for curr_itemset in combinations(itemset, i):
                    consequent = tuple(set(itemset) - set(curr_itemset))
                    
                    curr_itemset_support = frequent_itemsets.get(curr_itemset, 0)
                    
                    if curr_itemset_support > 0:
                        confidence = support / curr_itemset_support
                        
                        if confidence >= min_confidence:
                            rules.append((curr_itemset, consequent, confidence))
                            logging.info(f"Generated rule: {curr_itemset} -> {consequent} (Confidence: {confidence:.2f})")
        
        return rules
