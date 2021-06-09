import psycopg2
from tabulate import tabulate

class Psql:

    def __init__(self, password, dbname = 'postgres', user ='postgres', host='localhost'):

        self.conn = psycopg2.connect(dbname = dbname,
                                user = user, 
                                password = password,
                                host = host)

        self.cursor = self.conn.cursor()

        print('Connect Successed')

    def get_data_command(self):
        text = input("Input SQL command -->")
        self.cursor.execute(text)
        data = self.cursor.fetchall()
        print(tabulate(data, tablefmt='orgtbl'))

    def get_data_file(self):
        file_name = input("Paste absolute SQL file location -->")
        with open(file_name, "r") as f:
            for line in f.readlines(): 
                self.cursor.execute(line)
                data = self.cursor.fetchall()
                print(tabulate(data, tablefmt='orgtbl'))

    def execute(self, command):
        try:
            self.cursor.execute(command)
            data = self.cursor.fetchall()
        except psycopg2.ProgrammingError:
            return False

        return data

    def get_table_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name} ORDER BY id;")
        colnames = [desc[0] for desc in self.cursor.description]
        data = self.cursor.fetchall()
        print([colnames, data])
        return [colnames, data]

    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    psql = Psql('crosspepes123',
                dbname='lab2',
                user='postgres',
                host='localhost')

    psql.get_table_data("items")
