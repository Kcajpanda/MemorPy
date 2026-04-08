from classes.Text import Text
from classes.Parser import Parser

class MemorPy:

    def __init__(self):
        self.parse = Parser()
        self.texts = []
        self.level_hist = [0]
        self.prev_level = 0
        self.current_txt = None

    def loop(self, filename):
        self.add(filename)
        self.current_txt = self.texts[-1]
        print(f"first print: {self.current_txt.out_txt(self.prev_level)}")
        while(True):
            self.interpret()

    def add(self, filename):
        parsed_txt = self.parse.parse(filename)
        self.texts.append(Text(parsed_txt))
    
    def set_curr(self, index):
        self.current_txt = self.texts[index]

    def in_tokenizer(self, user_in:str) -> list:
        tokens = user_in.split()
        return tokens
    
    def save_level(self) -> None:
        self.prev_level = self.current_txt.get_level()
        self.level_hist.append(self.prev_level)

    def interpret(self) -> None:
        raw_user_in = input("What's Next? (Harder = m or ENTER, Easier = b):")
        user_in = self.in_tokenizer(raw_user_in)

        # Command logic
        if len(user_in) == 1: 
            if user_in[0] == "m" or user_in[0] == "M" or user_in[0] == "1":
                self.c_inc_level()
            elif user_in[0] == "b" or user_in[0] == "B" or user_in[0] == "2":
                self.c_dec_level()
            elif user_in[0] == "exit" or user_in[0] == "0":
                self.memorpy_exit()
            else:
                print(f"Input not recognized: {user_in}, try again:")
        elif len(user_in) == 2:
            if user_in[0] == "set":
                try:
                    val = int(user_in[1])
                except ValueError:
                    raise InvalidCommandArg(user_in[1])
                self.c_set_level(val)
            elif user_in[0] == "upload":
                pass
                # take third arg in as text save to file of name provided in second arg
            else:
                print(f"Input not recognized: {user_in}, try again:")
        else:
                print(f"Input not recognized: {user_in}, try again:")

    def c_inc_level(self):
        self.current_txt.inc_level()
        # print(f"Text: {self.current_txt.out_txt(self.prev_level)}")
        return self.current_txt.out_txt(self.prev_level)

    def c_dec_level(self):
        self.current_txt.dec_level()
        # print(f"Text: {self.current_txt.out_txt(self.prev_level)}")
        return self.current_txt.out_txt(self.prev_level)

    def c_set_level(self, user_in):
        self.current_txt.set_level(user_in)
        # print(f"Text: {self.current_txt.out_txt(self.prev_level)}")
        return self.current_txt.out_txt(self.prev_level)

    def memorpy_exit(self):
        exit()

class InvalidCommandArg (Exception):
    """
    Exception for a command is arg is of the wrong type

    EX:

    """
    def __init__(self, input, message="Error expected arg of type int for second arg, GIVEN="):
        super().__init__(f"{message}{input}")