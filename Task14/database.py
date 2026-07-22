from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self, connection_string , timeout_seconds):
        self.__connection_string = connection_string
        self.__timeout_seconds = timeout_seconds

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    def display_all_details(self, test_query):
        print(f"Connecting to Endpoint: {self.__connection_string}")
        print(f"Timeout Configuration : {self.__timeout_seconds}s")
        self.connect()
        self.query(test_query)

class MySQLDatabase(Database):

    def connect(self):
        print("MySQL Engine   : Establishing secure TCP/IP handshake with MySQL Server.")

    def query(self, sql):
        print(f"MySQL Execution: Parsing relational syntax -> Executing row-based SQL: [{sql}]")

class MongoDatabase(Database):

    def connect(self):
        print("MongoDB Engine : Initializing persistent cluster connection pool.")

    def query(self, sql):
        print("MongoDB Engine : [!] Notice: MongoDB uses Document structures instead of standard SQL tables.")
        print(f"Mongo Execution: Compiling query into BSON filter criteria expressions -> [{sql}]")

mysql = MySQLDatabase("mysql_connection_str", 30)
mongo = MongoDatabase("mongo_connection_str", 70)


mysql.display_all_details("SELECT * FROM students;")
mongo.display_all_details("db.students.find()")
