class Parser:
    """
    Currently just serves as a class to contain the parse method, and keep a history of all things parsed.
    """
    def __init__(self):
        self.hist = []
        self.hist_raw = []

    def get(self, index:int) -> list:
        """
        Returns the parsed text found at self.hist(index)
        """
        return self.hist[index]
    
    def get_raw(self, index:int) -> str:
        """
        Returns the raw text found at self.hist_raw(index)
        """
        return self.hist_raw[index]
    
    def parse(self, filename:str) -> list:
        """
        Opens file of given name in read mode, parses its content based on spaces, then goes through checking the last char of each word and nots it down if a non-alpha character is detected. list of changes is then used to updates the parsed a list, and finally saves the raw and parse to their hist and returns the parsed list.
        """
        #TODO work on more advanced process for identifying  a word

        with open(filename, "r") as file:
            content = file.read()
        self.hist_raw.append(content)

        parsed_text = content.split()

        tracked_chng = []
        
        # Only Searches last char of each, if found it tracks the change
        for w in range(len(parsed_text)):
            word = parsed_text[w]
            if not word[-1].isalpha():
                char = word[-1]
                split_word = word.split(char)
                parsed_text[w] = split_word[0]
                tracked_chng.append([w+1, char])
        
        #adds in detected changes adding spacing to account for index error and things are added
        spacing = 0
        for chng in tracked_chng:
            parsed_text.insert(chng[0]+spacing, chng[1])
            spacing+=1
        
        self.hist.append(parsed_text)
        return parsed_text