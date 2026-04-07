class Parser:
    """
    Currently just serves as a class to contain the parse method, and keep a history of all things parsed.
    """
    def __init__(self):
        self.hist = []
        self.hist_raw = []

    def get(self, index):
        """
        Returns the parsed text found at self.hist(index)
        """
        return self.hist[index]
    
    def get_raw(self, index):
        """
        Returns the raw text found at self.hist_raw(index)
        """
        return self.hist_raw[index]
    
    def parse(self, filename:str) -> list:
        """
        Opens file of given name in read mode, parses its content based on spaces, saves the raw and parse to their hist and thn returns the parsed.
        """
        with open(filename, "r") as file:
            content = file.read()
        self.hist_raw.append(content)

        parsed_text = content.split()

        tracked_chng = []
        
        for w in range(len(parsed_text)):
            word = parsed_text[w]
            if not word[-1].isalpha():
                char = word[-1]
                split_word = word.split(char)
                parsed_text[w] = split_word[0]
                tracked_chng.append([w+1, char])
        
        spacing = 0
        for chng in tracked_chng:
            parsed_text.insert(chng[0]+spacing, chng[1])
            spacing+=1
        
        self.hist.append(parsed_text)
        return parsed_text