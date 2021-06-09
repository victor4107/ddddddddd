import psycopg2
from tabulate import tabulate

class Psql:

    def __init__(self, password, dbname = 'lab2', user ='postgres', host='localhost'):

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
        # self.cursor.close()


    def execute_file(self, file_path):
        with open(file_path, "r", encoding='utf-8') as f:
            hreny = f.read()
            self.cursor.execute(hreny)

    def execute_fetch(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def get_table_contents(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        colnames = [desc[0] for desc in self.cursor.description]
        values = self.cursor.fetchall()
        ret = [{colnames[i]:row[i] for i in range(len(colnames))} for row in values]
        return ret


    def __del__(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    psql = Psql('crosspepes123',
                dbname='lab2',
                user='postgres',
                host='localhost')


