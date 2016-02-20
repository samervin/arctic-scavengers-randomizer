from pymongo import MongoClient
import arctic_cards


def insert_unique_document(collection, document):
    if collection.find_one({"name": document['name']}) is None:
        return collection.insert_one(document)
    else:
        return None

client = MongoClient()
db = client.arcticscavengers

mercs_json = arctic_cards.Mercenaries.ALL_MERCENARIES
for mercenary in mercs_json:
    result = insert_unique_document(db.mercenaries, mercenary)
    if result is None:
        print('{} already exists in {} collection!'.format(mercenary['name'], db.mercenaries.name))
    else:
        print('Inserted {} into {} collection'.format(mercenary['name'], db.mercenaries.name))