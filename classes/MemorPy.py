from classes.Text import Text
from classes.Parser import Parser

class MemorPy:

    def __init__(self):
        self.parse = Parser()
        self.st_texts = List_Stored_Texts()
        self.current_txt = None

        # for depreceated state behavior
        self.level_hist = [0]
        self.prev_level = 0

    def get_curr_text(self) -> Text:
        return self.current_txt

    def add(self, filename):
        parsed_txt = self.parse.parse(filename)
        self.st_texts.add(filename, Text(parsed_txt))
        # self.texts.append(Text(parsed_txt))
    
    def set_curr_txt(self, index):
        self.st_texts.chng_curr_text(index)
        self.current_txt = self.st_texts.get_curr_text()

    def c_inc_level(self):
        self.current_txt.inc_level()
        # print(f"Text: {self.current_txt.out_txt(self.prev_level)}")
        return self.current_txt.out_txt()

    def c_dec_level(self):
        self.current_txt.dec_level()
        # print(f"Text: {self.current_txt.out_txt(self.prev_level)}")
        return self.current_txt.out_txt()

    def c_set_level(self, user_in):
        self.current_txt.set_level(user_in)
        # print(f"self.current_txt.get_level() = {self.current_txt.get_level()}")
        return self.current_txt.out_txt()

    def memorpy_exit(self):
        exit()

    # For CLi only (deprecated)
    def loop(self, filename):
        self.add(filename)
        self.current_txt = self.texts[-1]
        print(f"first print: {self.current_txt.out_txt(self.prev_level)}")
        while(True):
            self.interpret()

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


class List_Stored_Texts:
    """
    A list of Stored_Text objs (self.texts) with a reference self.curr_text which points to a item in self.texts. Allows for quick searching and swapping of the curr_text with the help of the Stored_Text Class.
    """

    def __init__(self):
        self.texts = []
        self.curr_text = None

    def get_texts(self) -> list:
        return self.texts
    
    def add(self, name, parsed_text:Text) -> None:
        """
        Adds a raw Text obj to it list of texts by containing it in a Stored_Text obj and storing that Stored_text obj alongside an id and name for simple searches.
        """
        id = len(self.texts)
        self.texts.append(Stored_Text(name, id, parsed_text))
    
    def get_curr_text(self) -> Text:
        """
        Returns reference to the Text obj of the current self.curr_text
        """
        return self.curr_text
    
    def chng_curr_text(self, attr) -> None:
        """
        Based on an attr provided (name or id) searches for a text Stored_Text obj with those attrs and sets self.curr_text to the Text obj of the matching Stored_Text obj.
        """
        if isinstance(attr, int):
            self.curr_text = self.search(attr, Stored_Text.get_id)
        elif isinstance(attr, str):
            self.curr_text = self.search(attr, Stored_Text.get_name)
        else:
            raise InvalidSearchArg(attr)
    
    def search(self, attr, func) -> Text:
        """
        Method for searching for a given Text obj based on Stored_Text obj attr passed.
        """
        for st_text in self.texts:
            if func(st_text) == attr:
                return st_text.get_text_obj()
        print(f"No st_text found with the attr: {attr}")

# Might be too much abstraction, 2d list might be better

class Stored_Text:
    """
    Obj that contains a Text obj and just includes a name and id for the text. has methods for direct passing of the Text obj ref. Serves as an abstraction to simplify storage and avoid the use of multi dimensional lists.
    """

    def __init__(self, name:str, id:int, text:Text) -> None:
        #TODO add self.dir
        self.name = name
        self.id = id
        self.text_obj = text

    # Getters
    @staticmethod
    def get_name(st_text) -> str:
        """
        Static get name method for use with List_Stored_Text.search()
        """
        return st_text.get_name()
    
    def get_name(self):
        """
        Returns self.name
        """
        return self.name
    
    @staticmethod
    def get_id(st_text) -> int:
        """
        Static get id method for use with List_Stored_Text.search()
        """
        return st_text.get_id()
    
    def get_id(self):
        """
        Returns self.id
        """
        return self.id
    
    def get_text_obj(self) -> Text:
        """
        Returns the reference to the Text obj passed to the Stored_Text obj at creation.
        """
        return self.text_obj

# Exception Classes
class InvalidSearchArg (Exception):
    """
    Exception for when attr passed to List_Stored_Texts.search() isn't an int or str

    EX:

    """
    def __init__(self, input, message="Error expected arg of type int or str, GIVEN="):
        super().__init__(f"{message}{type(input)}")

class InvalidCommandArg (Exception):
    """
    Exception for a command is arg is of the wrong type

    EX:

    """
    def __init__(self, input, message="Error expected arg of type int for second arg, GIVEN="):
        super().__init__(f"{message}{input}")