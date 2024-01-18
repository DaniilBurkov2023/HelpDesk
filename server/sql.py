import psycopg2

class Db():
    def __init__(self) -> None:
        self.connection = psycopg2.connect(dbname='server', user='server', 
                                            password='test', host='db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Tasks (
            id SERIAL PRIMARY KEY,
            cab varchar(50) NOT NULL,
            fio varchar(50) NOT NULL,
            description varchar(500) NOT NULL
            )'''
                       )
        self.connection.commit()

    def get(self, order="id"):
        self.cursor.execute('SELECT id, cab, fio, description FROM Tasks ORDER BY '+order)
        results = self.cursor.fetchall()
        return results
    
    def write(self, data):
        sql = """INSERT INTO Tasks (cab, fio, description) VALUES (%s, %s, %s)"""
        self.cursor.execute(sql,data)
        self.connection.commit()

    def __del__(self):
        self.connection.close()
    