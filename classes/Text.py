import copy
import random

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

    def __init__(self, parsed_txt:list) -> None:
        """
        Creates a Text object, see __init__() comments or class descr for more details.
        """
        #TODO add ability to use blanked and full blanked

        self.text = copy.copy(parsed_txt)
        self.blanked, self.full_blank, self.rand_lst, self.displayed = [], [], [], []
        self.level = 0
        self.text_len = len(self.text)

        tmp_num = 0
        for word in self.text:
            if word.isalpha():
                tmp_num += 1
        self.max_level = tmp_num
        
        # Generates two lists, both have the same numbers of words as the original text except full_blank has every char replaced with '_' where blanked has all chars except the first replaced with '_'. So that for the el "word", full_blank would have it as "____" and blanked as "w___"
        for word in self.text:
            if word.isalpha():
                tmp_str = ""
                for i in range(len(word)-1):
                    tmp_str += "_"
                self.blanked.append(word[0] + tmp_str)
                self.full_blank.append(tmp_str + "_")
            else:
                # to keep index continuity with self.text we add the punctuation unaltered, even though we never call it
                self.blanked.append(word)
                self.full_blank.append(word)

        # Generates a list of ascending and ordered numbers called tmp_text_nums for as many words as there are in self.text, then loops for as many words as there grabbing a random number each time, adding it to self.rand_nums and then popping it from tmp_text_nums
        tmp_text_nums = []
        for i in range(self.text_len):
            if self.text[i].isalpha():
                tmp_text_nums.append(i)
        for i in range(len(tmp_text_nums)):
            rand_index = random.randrange(len(tmp_text_nums))
            self.rand_lst.append(tmp_text_nums[rand_index])
            tmp_text_nums.pop(rand_index)

    # Level Methods
    def inc_level(self, num:int=1):
        """
        Adds given num to self.level as long as it keep its in range.

        EX:
        """
        if self.level + num <= self.text_len :
            self.level += num

    def dec_level(self, num:int=1):
        """
        Subtracts given num to self.level as long as it keep its in range.

        EX:
        """
        if self.level - num >= 0 :
            self.level -= num

    def set_level(self, num:int=0):
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
    def display_txt(self) -> str:
        """
        Based on level, display the text but replaces the first [level] words in self.rand_lst with the corresponding word from self.blanked
        """
        self.displayed = []
        for word in self.text:
            self.displayed.append(word)

        for num in range(self.level):
            # print(f"num: {num}")
            # print(f"self.blanked[num] = {self.blanked[num]}")
            index = self.rand_lst[num]
            # print(f"self.rand_lst[num] = {self.rand_lst[num]}")
            self.displayed[index] = self.blanked[index]
        return self.displayed
    
    def is_punc(self, val:str):
        return val.isalpha()

class OutOfLevelError (Exception):
    """
    Exception for when level is outside of range.

    EX:

    """
    def __init__(self, input, message="Error level negative, GIVEN="):
        super().__init__(f"{message}{input}")
