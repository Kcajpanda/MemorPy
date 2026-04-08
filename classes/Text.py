import copy
import random
from classes.Entry import Entry, Word, Punc

class Text:
    """
    Serves as an object Containing the relevant data and metadata for the memorization UI.

    - self.text : List of parsed text, stored as Entry instances (or a child class of Entry), given by the Parser class. This list is never mutated, but  has its Entry obj instances and their properties accessed by lists like self.displayed.
    - self.text_len : length of self.text.
    - self.rand_lst : Contains a list of numbers, with each number referencing an index of a Punc obj instance in self.text. The list stores the indexes ins a random order. Its used with self.level to tell which indexes of self.displayed should be replaced with blanked text.
    - self.level : Used to tell how many elements of self.rand_lst to reference. The first self.level (excluding the first) number of indexes are grabbed to tell self.displayed which indexes to update with blanked or unblanked text. See self.update().
        - EX: 
                self.text = ['hi', ',', 'lets', 'learn', ':', 'this', 'string']
                self.rand_lst = [5, 6, 3, 2, 0]

                # if level is 0
                self.out_txt(0) => ['hi', ',', 'lets', 'learn', ':', 'this', 'string']

                # if level is 3
                self.out_txt(0) => ['hi', ',', 'lets', 'l____', ':', 't___', 's_____']
        
    - self.max_level : The total number of Word obj instances in self.text.        
    - self.displayed : List used to store each .get_curr() of each Entry obj in self.text. Relies on self.rand_lst and self.level to know which indexes to request and updated .get_curr() from.
        - EX: 
                self.text = ['hi', ',', 'lets', 'learn', ':', 'this', 'string']
                self.rand_lst = [3, 2, 0, 5, 6]

                # if level is 3
                self.out_txt(0) => ['h_', ',', 'l___', 'l____', ':', 'this', 'string']
    """

    def __init__(self, valid_txt:list) -> None:
        """
        Creates a Text object, see class descr:

        Serves as an object Containing the relevant data and metadata for the memorization UI.

        - self.text : List of parsed text, stored as Entry instances (or a child class of Entry), given by the Parser class. This list is never mutated, but  has its Entry obj instances and their properties accessed by lists like self.displayed.
        - self.text_len : length of self.text.
        - self.rand_lst : Contains a list of numbers, with each number referencing an index of a Punc obj instance in self.text. The list stores the indexes ins a random order. Its used with self.level to tell which indexes of self.displayed should be replaced with blanked text.
        - self.level : Used to tell how many elements of self.rand_lst to reference. The first self.level (excluding the first) number of indexes are grabbed to tell self.displayed which indexes to update with blanked or unblanked text. See self.update().
            - EX: 
                    self.text = ['hi', ',', 'lets', 'learn', ':', 'this', 'string']
                    self.rand_lst = [5, 6, 3, 2, 0]

                    # if level is 0
                    self.out_txt(0) => ['hi', ',', 'lets', 'learn', ':', 'this', 'string']

                    # if level is 3
                    self.out_txt(0) => ['hi', ',', 'lets', 'l____', ':', 't___', 's_____']
            
        - self.max_level : The total number of Word obj instances in self.text.        
        - self.displayed : List used to store each .get_curr() of each Entry obj in self.text. Relies on self.rand_lst and self.level to know which indexes to request and updated .get_curr() from.
            - EX: 
                    self.text = ['hi', ',', 'lets', 'learn', ':', 'this', 'string']
                    self.rand_lst = [3, 2, 0, 5, 6]

                    # if level is 3
                    self.out_txt(0) => ['h_', ',', 'l___', 'l____', ':', 'this', 'string']
        """
        #TODO add ability to use blanked and full blanked

        self.text = copy.copy(valid_txt)
        self.rand_lst, self.displayed = [], []
        self.text_len = len(self.text)
        self.level = 0

        self.num_words, self.num_punc = 0, 0
        self.words, self.punc = [], []

        for index, entry in enumerate(self.text):
            if isinstance(entry, Word):
                self.words.append(index)
                self.rand_lst.append(index)
            elif isinstance(entry, Punc):
                self.punc.append(index)

        self.num_words = len(self.rand_lst)
        self.num_punc = len(self.punc)
        self.max_level = self.num_words
        
        random.shuffle(self.rand_lst)
        self.rand_lst.insert(0, None)

        for entry in self.text:
            self.displayed.append(entry.get_curr())

    # Getters
    def get_level(self) -> int:
        """
        Getter for self.level.
        """
        return self.level
    
    def get_max_level(self) -> int:
        """
        Getter for self.max_level.
        """
        return self.max_level
    
    def get_text(self) -> list:
        """
        Getter for self.text, used to access raw array.
        """
        return self.text

    # Level Methods
    def inc_level(self, num:int=1) -> None:
        """
        Adds given num to self.level as long as it keeps it less than or equal to self.max_level.
        """
        # print(f"level: {self.level} + {num} <= self.max_level: {self.max_level} => {self.level + num <= self.max_level}")
        if self.level + num <= self.max_level:
            self.level += num
        # if self.level == self.max_level: print("Max Level")

    def dec_level(self, num:int=1) -> None:
        """
        Subtracts given num to self.level as long as it keep its greater than or equal to 0.
        """
        if self.level - num >= 0 :
            self.level -= num
        # if self.level == 0: print("Easiest level")

    def set_level(self, num:int=0) -> None:
        """
        Sets level to val as long as it greater than or equal to zero. Any passed num larger than max level just sets level to max_level.
        """
        if num >= 0:
            if num >= self.max_level:
                self.level = self.max_level
            else:
                self.level = num
        else:
            raise OutOfLevelError(num)
        
    # Text Methods
    def out_txt(self, prev_level:int=0) -> str:
        """
        Forces self.displayed to update self, then goes through looking for non alpha chars, but not blanked words (words with '_" at the end), and re-adds appropriate spacing. In essence it un-parses the text but this time includes the changes made to blank out the text.
        """
        pretty_out = ""

        self.update(prev_level)
        for i in range(len(self.displayed)):
            # Avoids out of bounds
            if i+1 != len(self.displayed):
                # Is current word a punc mark?
                curr_item = self.displayed[i]
                next_item = self.displayed[i+1]
                if curr_item[-1].isalpha() or curr_item[-1].__contains__("_"):
                    # Is the second word a punc mark?
                    if next_item[-1].isalpha() or next_item.__contains__("_"):
                        pretty_out += f"{self.displayed[i]} "
                    else:
                        pretty_out += f"{self.displayed[i]}"
                else:
                    pretty_out += f"{self.displayed[i]} "
            else:
                pretty_out += self.displayed[i]
        return pretty_out
    
    def update_curr(self, start:int, stop:int) -> None:
        """
        Based on start and stop args (presumably self.level and prev_level, or ranges that allow for looping all fo self.rand_lst) loops through and updates the .get_curr() ref for each item in self.displayed base don the indexes returned from self.rand_lst.
        """
        for num in self.rand_lst[start:stop]:
            self.text[num].swap_state()
            self.displayed[num] = self.text[num].get_curr()
    
    def update(self, prev_level: int) -> None:
        """
        Compares the level of the previous out_txt (passed as an arg), and the current level request (via a live self.level call), to determine which indexes of self.displayed need to make update what they point to via .get_curr(). Compares the curr and prev level to understand which direction to iterate in.
        """
        diff = self.level - prev_level
        # print(f"diff = {diff}")
        if diff > 0:
            # print(f"Working in range: {self.rand_lst[prev_level+1: self.level+1]}")
            self.update_curr(prev_level+1, self.level+1)
        else:
            # print(f"Working in range: {self.rand_lst[self.level+1: prev_level+1]}")
            self.update_curr(self.level+1, prev_level+1)
    
    def full_update(self):
        """
        Runs through and fully updates each .get_curr() for self.displayed instead of just checking for ones that have been changed. Makes use of update_curr() to run the loop
        """
        self.update_curr(self.level+1)

class OutOfLevelError (Exception):
    """
    Exception for when level is outside of range.

    EX:

    """
    def __init__(self, input, message="Error level negative, GIVEN="):
        super().__init__(f"{message}{input}")