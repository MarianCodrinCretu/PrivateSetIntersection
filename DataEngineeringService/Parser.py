
# Parser abstract class for exposing different strategies
# for parsing: XLS or CSV files

# author mcretu
# cretu.marian.5000@gmail.com

class Parser():

    def parse(self, file):
        pass

    def extractColumnNames(self, file):
        pass