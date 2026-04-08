class Entry:
    """
    Abstraction of a single piece of text. Contains 
    - self.val : The text used in creation.
    - self.length : the length of self.val
    
    The class is designed to serve as a parent with children exercising a wider functionality. instances of Entry and all children can only be created by the static method Entry.validate, making it so you can trust that the class type of an entry to reflects what it contains (based on the rules set forth in validate) without having to examine the self.val further.
    """

    def __init__(self, val:str) -> None:
        """
        __init__ for Entry parent class, see Entry descr:

        Abstraction of a single piece of text. Contains 
        - self.val : The text used in creation.
        - self.length : the length of self.val
        
        The class is designed to serve as a parent with children exercising a wider functionality. instances of Entry and all children can only be created by the static method Entry.validate, making it so you can trust that the class type of an entry to reflects what it contains (based on the rules set forth in validate) without having to examine the self.val further.
        """
        self.val = val
        self.length = len(val)

    def get_val(self) -> str:
        """
        Returns self.val.
        """
        return self.val
    
    def get_len(self) -> int:
        """
        Returns self.length.
        """
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
        """
        Used for Creation of a instance type Entry or any of its children classes. The current rules are:
        - single char alpha str are defined as Word objs (Case 1.1).
            - EX: I, a, etc.
        - single char non-alpha str are defined as Punc objs (Case 1.2).
            - EX: ", -, etc.
        - multi char all alpha str are defined as Word objs (Case 2.1).
            - EX: Hello, wow, HI, etc.
        - multi char mixed alpha / non-alpha str are defined as Word objs (Case 2.2.1).
            - EX: I___, (Hello), W__wo, etc.
        - multi char non-alpha str are defined as Punc objs (Case 2.2.1).
            - EX: ____, (__*), ?:"{}}, etc.
        - Anything else that mannages to slip through is made a Entry obj (Case 3.)
        """
        if len(text) == 1:
            # Case 1.1 Word like: I, a, etc
            if text.isalpha():
                return Word(text)
            # Case 1.2 Must be punc
            else:
                return Punc(text)
        elif len(text) > 1:
            # Case 2.1 Word like: Hi, Samuel, etc
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
                # Case 2.2.1
                if num_alpha > 0:
                    return Word(text)
                # Case 2.2.2
                else:
                    return Punc(text) #TODO add more advanced classification later
        else:
            # Case 3. could cause lots of entries instead of words later
            return Entry(text)
    
class Word (Entry):
    """
    A child of the Entry class. Serves as storage for the base string (self.val) but also has two specialized versions. Each instance has a pointer self.curr pointed at one of its text versions (val, blank, full) which can be swapped to other using self.state and its related methods. The pointer is used so that other classes only need interact with one aspect of the obj and then send commands to swap or update state as needed.
    """

    def __init__(self, val:str) -> None:
        """
        __init__ for Word class, see class descr:

        A child of the Entry class. Serves as storage for the base string (self.val) but also has two specialized versions. Each instance has a pointer self.curr pointed at one of its text versions (val, blank, full) which can be swapped to other using self.state and its related methods. The pointer is used so that other classes only need interact with one aspect of the obj and then send commands to swap or update state as needed. This style is maintained among all children of the Entry class so looping over a list of Entry objs is easy.
        - self.blank : Contains a str of the same len as self.val but with all chars except the first replaced with "_".
        - self.full_blank :  Contains a str of the same len as self.val but with all chars replaced with "_".
        - self.state : A bool used to switch between which of the text alternates self.curr points to, see update_curr().
        - self.curr : Pointer for whatever text alternate is currently set by self.state, see update_curr().
        """
        super().__init__(val)
        self.blank, self.full_blank = "", ""
        self.state = True
        self.curr = self.val
        self._det_blanks()

    def _det_blanks(self) -> None:
        """
        Method used by __init__ to set the alternate versions of self.val. Single char Words have an identical self.blank and self.full_blank. For multi-char words self.blank retains the first char but blanks "_" all other chars. self.full_blank fully blanks all chars.
        """
        if self.get_len() == 1:
            self.blank, self.full_blank = "_", "_"
        else:
            tmp_str = ""
            for i in range(1,self.get_len()):
                tmp_str += "_"
            self.blank = self.get_val()[0] + tmp_str
            self.full_blank = "_" + tmp_str

    def get_val(self) -> str:
        """
        Uses parent method to return it's self.val. 
        """
        return super().get_val()
    
    def get_len(self):
        """
        Uses parent method to return it's self.length. 
        """
        return super().get_len()
    
    def update_curr(self) -> None:
        """
        Checks curr value of state as updates self.curr to point at the corresponding var.
        """
        if self.state:
            self.curr = self.val
        else:
            self.curr = self.blank
    
    def swap_state(self) -> None:
        """
        Inverts value of the bool self.state then calls an update via self.update_curr() to update self.curr
        """
        self.state = not self.state
        self.update_curr()

    def set_state(self, state:bool) -> None:
        """
        Directly sets the value of the bool self.state then calls an update via self.update_curr() to update self.curr
        """
        self.state = state
        print(f"state changed to {state}")
        # self.update_curr()

    def get_curr(self):
        """
        My call of other objs for this class, forces update of self.state to ensure self.curr is pointed right then returns self.curr.
        """
        self.update_curr()
        return self.curr
    
    def __str__(self):
        return self.get_curr()
    
    def __eq__(self):
        return super().__eq__()
    
class Punc (Entry):
    """
    A child of the Entry class. Serves meant to contain data an metadata similar to Word, but since punctuation doesn't need alternates like a Word obj does most of methods that mirror a Word just return self.val. hence why this class doesn't have a self.state.
    """

    def __init__(self, val:str) -> None:
        """
        __init__ for Punc class. See class descr:

        A child of the Entry class. Mant to contain data an metadata similar to Word, but since punctuation doesn't need alternates like a Word obj does most of methods that mirror a Word just return self.val. It mirrors the Word class only in ways that make looping over a list of Entry child objects easy. hence why this class doesn't have a self.state.
        """
        super().__init__(val)
    
    def get_val(self) -> str:
        """
        Uses parent method to return it's self.val. 
        """
        return super().get_val()
    
    def get_curr(self) -> str:
        """
        A mirror of the Word class's get_curr(). Since Punc instances don't have state or alt text versions it just return self.val.
        """
        return self.get_val()
    
    def swap_state(self) -> None:
        """
        Inverts value of the bool self.state then calls an update via self.update_curr() to update self.curr
        """
        pass

    def set_state(self, state:bool) -> None:
        """
        Directly sets the value of the bool self.state then calls an update via self.update_curr() to update self.curr
        """
        pass
    
    def get_len(self):
        """
        Uses parent method to return it's self.length. 
        """
        return super().get_len()
    
    def __str__(self):
        return self.get_val()
    
    def __eq__(self):
        return super().__eq__()