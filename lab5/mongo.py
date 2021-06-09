import pymongo

class Mongo:

    def __init__(self):

        self.db = pymongo.MongoClient('localhost', 27017).labs

    def get_tables(self):

        return self.db.list_collection_names()

    def execute(self, command):
        try:
            self.db.command(command)
        except Exception as ex:
            return False

        return "OK"

    def get_table_data(self, table_name):

        table = self.db[table_name].find()
        colnames = []
        data = []
        for line in table:
            d = []
            for key in line:
                if key != "_id":
                    if key not in colnames:
                        colnames.append(key)
                    d.append(line[key])
            data.append(d)
        return [colnames, data]


if __name__ == "__main__":

    mongo = Mongo()

    mongo.get_table_data("items")

