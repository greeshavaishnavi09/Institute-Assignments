from abc import ABC, abstractmethod

class Filehandler(ABC):
            
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass
        
    def display_all_details(self):
        self.read()
        self.write()

class TextFileHandler(Filehandler): 
    def read(self):
        print("read : read the data file in form of text")
        
    def write(self):
        print("write : writes the data file in form of text")

class CsvFileHandler(Filehandler):
    def read(self):
        print("read :read the data file in form of Csv ")
        
    def write(self):
        print("write : write the data file in form of Csv")

Text = TextFileHandler()
csv = CsvFileHandler()
Text.display_all_details()
csv.display_all_details()