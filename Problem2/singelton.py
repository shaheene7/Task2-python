import json
import os

class Config:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            print("Loading config…")
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        try:
            config_path = os.path.join(os.path.dirname(__file__), "config.json")
            with open(config_path, 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {}
        except json.JSONDecodeError:
            self.config = {}


"""I use singelton because i need a shared file that all module use it to read 
    and i want to load the file once """





