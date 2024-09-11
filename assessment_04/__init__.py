from .db import Database, setup_database, fetch_data
from .association import AssociationRuleMining

def main():
    db = Database("WALMART.db")
    setup_database(db)
    rows = fetch_data(db)
    print(rows)
    print()
    # using association rule mining
    configs = {
        'itemset_size': 3,
        'min_support': 2,
        'max_support': 4,
        'min_confidence': 0.5
    }
    arm = AssociationRuleMining(rows, configs['itemset_size'])
    freq_itemset = arm.apriori(configs['min_support'], configs['max_support'])
    rules = arm.generate_association_rules(freq_itemset, configs['min_confidence'])