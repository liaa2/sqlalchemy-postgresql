import sqlalchemy as db


class Database():
    engine = db.create_engine('postgresql://postgres@localhost/sqlalchemydb')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQuery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)
