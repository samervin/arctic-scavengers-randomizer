from pymongo import MongoClient
import arctic_cards


def insert_unique_document(collection, document):
    if collection.find_one({"name": document['name']}) is None:
        return collection.insert_one(document)
    else:
        return None


def insert_array(collection, documents):
    for document in documents:
        result = insert_unique_document(collection, document)
        if result is None:
            print('{} already exists in {} collection!'.format(document['name'], collection.name))
        else:
            print('Inserted {} into {} collection'.format(document['name'], collection.name))

client = MongoClient()
db = client.arcticscavengers

insert_array(db.mercenaries, arctic_cards.Mercenaries.ALL_MERCENARIES)
insert_array(db.items, arctic_cards.Items.ALL_ITEMS)
insert_array(db.gangs, arctic_cards.Gangs.ALL_GANGS)
insert_array(db.buildings, arctic_cards.Buildings.ALL_BUILDINGS)
insert_array(db.leaders, arctic_cards.Leaders.ALL_LEADERS)
