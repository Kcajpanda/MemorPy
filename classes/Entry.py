class Entry:

    def __init__(self, val:str) -> None:
        self.val = val
        self.length = len(val)

    def get_val(self) -> str:
        return self.val
    
    def get_len(self) -> int:
        return self.length
    
    def __str__(self) -> str:
        return self.val
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            if self.val == other.val:
                return True
        return False
    
    @staticmethod
    def validate(text):
        if len(text) == 1:
            # Word like: I, a, etc
            if text.isalpha():
                return Word(text)
            #Must be punc
            else:
                return Punc(text)
        elif len(text) > 1:
            # Word like: Hi, Samuel, etc
            if text.isalpha():
                return Word(text)
            # Word Like: H12, H_HU_H, K___
            else:
                num_alpha = 0
                num_punc = 0
                # done this way for more advanced classification later
                for i in range(len(text)):
                    if text[i].isalpha():
                        num_alpha += 1
                    else:
                        num_punc += 1
                if num_alpha > 0:
                    return Word(text)
                else:
                    return Punc(text) #TODO add more advanced classification later
        else:
            # could cause lots of entries instead of words later
            return Entry(text)
    
class Word (Entry):

    def __init__(self, val:str) -> None:
        super().__init__(val)
        self.blank, self.full_blank = "", ""
        self.state = True
        self.curr = self.val
        self.det_blanks()

    def det_blanks(self) -> None:
        if self.get_len() == 1:
            self.blank, self.full_blank = "_", "_"
        else:
            tmp_str = ""
            for i in range(1,self.get_len()):
                tmp_str += "_"
            self.blank = self.get_val()[0] + tmp_str
            self.full_blank = "_" + tmp_str

    def get_val(self) -> str:
        return super().get_val()
    
    def get_len(self):
        return super().get_len()
    
    def get_blank(self):
        return self.blank
    
    # def update_curr(self) -> None:
    #     if self.state:
    #         self.curr = self.val
    #     else:
    #         self.curr = self.blank
    
    # def swap_state(self) -> None:
    #     self.state = not self.state
    #     # self.update_curr()

    # def set_state(self, state:bool) -> None:
    #     self.state = state
        # self.update_curr()

    # def get_curr(self):
    #     self.update_curr()
    #     if self.state:
    #         self.curr = self.val
    #     else:
    #         self.curr = self.blank
    #     return self.curr
    
    def get_blank(self) -> str:
        return self.blank
    
    def get_full_blank(self) -> str:
        return self.full_blank
    
    def __str__(self):
        return self.get_curr()
    
    def __eq__(self):
        return super().__eq__()
    
class Punc (Entry):

    def __init__(self, val:str) -> None:
        super().__init__(val)
    
    def get_val(self) -> str:
        return super().get_val()
    
    def get_blank(self) -> str:
        return super().get_val()
    
    # def get_curr(self) -> str:
    #     return self.get_val()
    
    def get_len(self):
        return super().get_len()
    
    def __str__(self):
        return self.get_curr()
    
    def __eq__(self):
        return super().__eq__()