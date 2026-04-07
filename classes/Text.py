import copy
import random

class Text:

    def __init__(self, parsed_txt:list) -> None:
        self.text = copy.copy(parsed_txt)
        self.blanked, self.full_blanked, self.rand_lst, self.displayed = [], [], [], []
        self.level = 0

        self.text_len = len(self.text)
        
        for word in self.text:
            tmp_str = ""
            for i in range(len(word)-1):
                tmp_str += "_"
            self.blanked.append(word[0] + tmp_str)
            self.full_blanked.append(tmp_str + "_")

        # generates a list of ascending and ordered numbers called tmp_text_nums for as many words as there are in self.text, then loops for as many words as there grabbing a random number each time, adding it to self.rand_nums and then popping it from tmp_text_nums
        tmp_text_nums = []
        for i in range(self.text_len):
            tmp_text_nums.append(i)
        for i in range(self.text_len):
            rand_index = random.randrange(len(tmp_text_nums))
            self.rand_lst.append(tmp_text_nums[rand_index])
            tmp_text_nums.pop(rand_index)

    def inc_level(self, num:int=1):
        if self.level + num <= self.text_len :
            self.level += num

    def dec_level(self, num:int=1):
        if self.level - num >= 0 :
            self.level -= num

    def set_level(self, num:int=0):
        """
        Sets level to val as long as it greater than or equal to zero or si the same as the length of the string.
        """
        if num >= 0 and num <= self.text_len:
            self.level = num

    def display_txt(self) -> str:
        """
        Based on level, display the text but replaces the first [level] words in self.rand_lst with the corresponding word from self.blanked
        """
        for word in self.text:
            self.displayed.append(word)
        for num in range(len(self.rand_lst)):
            self.displayed[num] = self.blanked[num]
        return self.displayed


