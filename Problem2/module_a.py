from singelton import Config

def run_a():
    config = Config()
    print("Running A with config:", config.config["mode"])
