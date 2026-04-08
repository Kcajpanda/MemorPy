import copy
import random
from classes.Entry import Entry, Word, Punc

class Text:
    """
    Serves as an object Containing the relevant data and metadata for the memorization UI.

    - self.text : List of full parsed text.
    - self.blanked : Contains every entry from self.text but replaces every letter, except the first letter, in each word with '_'. Punctuation is added unaltered.
        - EX: self.text[0] = "Word", self.blanked[0] = "W___"
    - self.full_blank : Contains every entry from self.text but replaces every letter in each word with '_'. Punctuation is added unaltered.
        - EX: 
                self.text[0] = "Word", self.blanked[0] = "____"
    - self.rand_lst : Contains a list of numbers, with each number referencing an index in self.text of a non-punctuation entry; its used with level to tell which indexes of self.displayed should be replaced with blanked text.
    - self.level : Used to tell how many elements of self.rand_lst to reference.
        - EX: 
                self.text = ['hi', ',', 'lets', 'learn', ':', 'this', 'string']
                self.rand_lst = [5, 6, 3, 2, 0]

                # if level is 0
                self.display_txt() => ['hi', ',', 'lets', 'learn', ':', 'this', 'string']

                # if level is 3
                self.display_txt() => ['hi', ',', 'lets', 'l____', ':', 't___', 's_____']
        
    - self.max_level : The total number of non punctuation entries in self.text.        
    - self.displayed : Var that is used to display the text thats printed, initially its equal to self.text, but base don self.level and self.rand_lst is mutated to show the final text.
        - EX: 
                self.text = ['hi', ',', 'lets', 'learn', ':', 'this', 'string']
                self.rand_lst = [3, 2, 0, 5, 6]

                # if level is 3
                self.display_txt() => ['h_', ',', 'l___', 'l____', ':', 'this', 'string']
    """

    def __init__(self, valid_txt:list) -> None:
        """
        Creates a Text object, see __init__() comments or class descr for more details.
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
            self.displayed.append(entry.get_val())

        # for debug
        # debug = True
        
        # if debug:
        #     print(f"{self.text}")
        #     print(f"Contains {self.text_len} entries")
        #     print(f"{self.max_level} valid words detected, max level set")
        # end debug
        
        # # Generates two lists, both have the same numbers of words as the original text except full_blank has every char replaced with '_' where blanked has all chars except the first replaced with '_'. So that for the el "word", full_blank would have it as "____" and blanked as "w___"
        # # for word in self.text:

        # #     if word.isalpha():
        # #         tmp_str = ""
        # #         # Normal length word
        # #         if len(word) > 1:
        # #             for i in range(len(word)-1):
        # #                 tmp_str += "_"
        # #             self.blanked.append(word[0] + tmp_str)
        # #             self.full_blank.append(tmp_str + "_")
        # #         # Single char word. EX I, a, etc
        # #         elif len(word) == 1:
        # #             self.blanked.append("_")
        # #             self.full_blank.append("_")
        # #         # Shouldn't be possible at this point in execution, but error raised just in case
        # #         else:
        # #             raise InvalidWordLength(word)
        # #     else:
        # #         # to keep index continuity with self.text we add the punctuation unaltered, even though we never call it
        # #         self.blanked.append(word)
        # #         self.full_blank.append(word)
        # # for word in self.text:
        # #     tmp_str = ""
        # #     if self.is_word(word):
        # #         if len(word) > 1:
        # #             for i in range(len(word)-1):
        # #                 tmp_str += "_"
        # #             self.blanked.append(word[0] + tmp_str)
        # #             self.full_blank.append(tmp_str + "_")
        # #         elif len(word) == 1:
        # #             self.blanked.append("_")
        # #             self.full_blank.append("_")
        # #         else:
        # #             raise InvalidWordLength(word)
        # #     else:
        # #         self.blanked.append(word)
        # #         self.full_blank.append(word)

        # # Generates a list of ascending and ordered numbers called tmp_text_nums for as many words as there are in self.text, then loops for as many words as there grabbing a random number each time, adding it to self.rand_nums and then popping it from tmp_text_nums
       

        # for debug
        # if debug:
        #     print(f"order of removal: {self.rand_lst}")
        #     self.indexes = {}
        #     for nums in range(self.text_len):
        #         self.indexes.update({nums: self.text[nums].get_val()})
        #     print(f"self.indexes: {self.indexes}")
        # end debug

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
        Adds given num to self.level as long as it keep its in range.

        EX:
        """
        # print(f"level: {self.level} + {num} <= self.max_level: {self.max_level} => {self.level + num <= self.max_level}")
        if self.level + num <= self.max_level:
            self.level += num
        if self.level == self.max_level: print("Max Level")

    def dec_level(self, num:int=1) -> None:
        """
        Subtracts given num to self.level as long as it keep its in range.

        EX:
        """
        if self.level - num >= 0 :
            self.level -= num
        if self.level == 0: print("Easiest level")

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
        
    #TODO add an update method so it just re-scans instead of recreating display each time
        
    # Text Methods

    def out_txt(self, prev_level) -> str:
        """
        Gens display text and then goes through looking for non alpha chars, but not blanked words (words with '_" at the end), and readds appropriate spacing.
        """
        # self.gen_display_txt()
        pretty_out = ""
        # for i in range(len(self.displayed)):
        #     # Avoids out of bounds
        #     if i+1 != len(self.displayed):
        #         # Is current word a punc mark?
        #         curr_item = self.displayed[i]
        #         next_item = self.displayed[i+1]
        #         if curr_item[-1].isalpha() or curr_item[-1].__contains__("_"):
        #             # Is the second word a punc mark?
        #             if next_item[-1].isalpha() or next_item.__contains__("_"):
        #                 pretty_out += f"{self.displayed[i]} "
        #             else:
        #                 pretty_out += f"{self.displayed[i]}"
        #         else:
        #             pretty_out += f"{self.displayed[i]} "
        #     else:
        #         pretty_out += self.displayed[i]
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

    def gen_display_txt(self) -> str:
        """
        Based on level, display the text but replaces the first [level] words in self.rand_lst with the corresponding word from self.blanked
        """
        self.reset_displayed()

        if self.level != 0:
            for num in range(1, self.level+1):
                index = self.rand_lst[num]

        print(f"len(self.rand_lst) = {len(self.rand_lst)}")
        print(f"Pre-add text level : {self.level}, self.level: {self.level} > 0 => {self.level > 0}")
        if self.level > 0:
            for num in range(1, self.level+1):
                print(f"num: {num}")
                index = self.rand_lst[num]
                print(f"self.rand_lst[num] / index to remove = {self.rand_lst[num]}")
                self.displayed[index] = self.blanked[index]

        return self.displayed
    
    def update(self, prev_level: int) -> None:
        diff = self.level - prev_level
        # print(f"diff = {diff}")
        if diff > 0:
            # print(f"Working in range: {self.rand_lst[prev_level+1: self.level+1]}")
            for num in self.rand_lst[prev_level+1: self.level+1]:
                # index = self.rand_lst[num]
                # print(f"index to change: {index}, corresponds to => {self.text[index]}")
                # print(f"num: {num}, corresponds to {self.text[num].get_blank()}")
                self.displayed[num] = self.text[num].get_blank()
        else:
            # print(f"Working in range: {self.rand_lst[self.level+1: prev_level+1]}")
            for num in self.rand_lst[self.level+1: prev_level+1]:
                # index = self.rand_lst[num]
                # print(f"index to change: {index}, corresponds to => {self.text[index]}")
                # print(f"num: {num}, corresponds to {self.text[num].get_val()}")
                self.displayed[num] = self.text[num].get_val()
        

class OutOfLevelError (Exception):
    """
    Exception for when level is outside of range.

    EX:

    """
    def __init__(self, input, message="Error level negative, GIVEN="):
        super().__init__(f"{message}{input}")

class InvalidWordLength (Exception):
    """
    Exception for when a entry in self.text has len of 0.

    EX:

    """
    def __init__(self, input, message="Error entry cannot be of length 0, GIVEN="):
        super().__init__(f"{message}{input}")
