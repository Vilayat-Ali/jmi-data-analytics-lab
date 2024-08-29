import logging
from itertools import combinations, chain

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AssociationRuleMining:
    def __init__(self, rows: list[list[str]], m: int):
        self.rows = rows
        self.candidates = set(chain(*[combinations(row, m) for row in rows]))
        logging.info(f"Initialized with {len(rows)} transactions and {len(self.candidates)} initial candidates")

    def get_frequent_itemsets(self, itemsets, min_support):
        itemset_counts = {itemset: 0 for itemset in itemsets}
        
        for transaction in self.rows:
            transaction_set = set(transaction)
            for itemset in itemsets:
                if set(itemset).issubset(transaction_set):
                    itemset_counts[itemset] += 1

        frequent_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count >= min_support}
        logging.info(f"Generated {len(frequent_itemsets)} frequent itemsets with min_support {min_support}")
        return frequent_itemsets
    
    def apriori(self, min_support):
        items = sorted(set(chain(*self.rows)))
        k = 1
        frequent_itemsets = {}
        current_itemsets = {tuple([item]) for item in items}
        logging.info(f"Starting Apriori with {len(current_itemsets)} single-item itemsets")

        while current_itemsets:
            current_frequent_itemsets = self.get_frequent_itemsets(current_itemsets, min_support)
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
        transaction_count = len(self.rows)
        
        for itemset, support in frequent_itemsets.items():
            for i in range(1, len(itemset)):
                for antecedent in combinations(itemset, i):
                    consequent = tuple(set(itemset) - set(antecedent))
                    
                    antecedent_support = frequent_itemsets.get(antecedent, 0)
                    
                    if antecedent_support > 0:
                        confidence = support / antecedent_support
                        
                        if confidence >= min_confidence:
                            lift = confidence / (frequent_itemsets.get(consequent, 0) / transaction_count)
                            rules.append((antecedent, consequent, confidence, lift))
                            logging.info(f"Generated rule: {antecedent} -> {consequent} (Confidence: {confidence:.2f}, Lift: {lift:.2f})")
        
        return rules
