
from abc import ABC, abstractmethod

class Template(ABC):

    def process(self, data):
        loaded = self.load(data)
        parsed = self.parse(loaded)
        transformed = self.transform(parsed)
        exported = self.export(transformed)
        return exported
    
    def load(self, data):
        print("[LOAD]")
        if not self.validate(data):
            raise ValueError("Invalid data format")
        return data

    @abstractmethod
    def validate(self, data):
        pass

    @abstractmethod
    def parse(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def export(self, data):
        pass


class CSVParser(Template):

    def parse(self, data):
        print("[PARSE]")
        return f"Parsed {data} as CSV"
    
    def validate(self, data):
        print("[VALIDATE]")
        if isinstance(data, str) and data.endswith('.csv'):
            return True
        return False
    
    def transform(self, data):
        print("[TRANSFORM CSV]")
        return f"Transformed {data} to CSV format"
    
    def export(self, data):
        print("[EXPORT]")
        return f"Exported {data} as CSV file"
    

class XMLParser(Template):

    def parse(self, data):
        print("[PARSE]")
        return f"Parsed {data} as XML"
    
    def validate(self, data):
        print("[VALIDATE]")
        if isinstance(data, str) and data.endswith('.xml'):
            return True
        return False
    
    def transform(self, data):
        print("[TRANSFORM XML]")
        return f"Transformed {data} to XML format"
    
    def export(self, data):
        print("[EXPORT]")
        return f"Exported {data} as XML file"


    


def main():
    parsers = [CSVParser(), XMLParser()]
    files = ["data.csv", "data.xml"]

    for parser, file in zip(parsers, files):
        print(parser.process(file))

main()

""" it defines the overall algorithm structure in a base class
 allowing subclasses to override specific steps without changing the algorithm's sequence"""
