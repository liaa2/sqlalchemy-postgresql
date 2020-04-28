import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column


class Database():
    engine = db.create_engine('postgresql://postgres@localhost/sqlalchemydb')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQuery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)

    def saveData(self, customer):
        self.connection.execute(f"""INSERT INTO customer(name, age, email, address, zip_code) VALUES('{customer.name}', '{customer.age}', '{customer.email}', '{customer.address}', '{customer.zip_code}')""")

    def fetchUserByName(self):
        meta = MetaData()
        customer = Table('customer', meta, Column('name'), Column('age'), Column('email'), Column('address'), Column('zip_code'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)


class Customer():
    def __init__(self, name, age, email, address, zip_code):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code


