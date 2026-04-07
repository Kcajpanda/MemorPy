from classes.Text import Text
from classes.Parser import Parser

class MemorPy:

    def __init__(self):
        self.parse = Parser()
        self.texts = []
        self.current_txt = None

    def loop(self, filename):
        self.add(filename)
        self.current_txt = self.texts[-1]
        print(f"first print: {self.current_txt.out_txt()}")
        while(True):
            self.interpret()

    def add(self, filename):
        parsed_txt = self.parse.parse(filename)
        self.texts.append(Text(parsed_txt))
    
    def set_curr(self, index):
        self.current_txt = self.texts[index]

    def interpret(self) -> None:
        user_in = input("What's Next? (Harder = m or ENTER, Easier = b):")
        if user_in == "m" or user_in == "M" or user_in == "":
            self.current_txt.inc_level()
            print(f"Text: {self.current_txt.out_txt()}")
            print(f"Level: {self.current_txt.level}")
        elif user_in == "b" or user_in == "B":
            self.current_txt.dec_level()
            print(f"Text: {self.current_txt.out_txt()}")
            print(f"Level: {self.current_txt.level}")
        elif user_in == "exit":
            exit()
        else:
            print(f"Input not recognized: {user_in}, try again:")