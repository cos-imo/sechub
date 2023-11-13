import argparse

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(usage='python3 main.py [OPTIONS]', add_help=False, description='Python cybersecurity toolbox')
        self.parse_arguments()

    def parse_arguments(self):

        self.parser.add_argument('-h','--help', action='help', help="Affiche ce message d'aide")

        self.args = self.parser.parse_args()


