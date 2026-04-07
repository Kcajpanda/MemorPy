from classes.Text import Text

parsed_without_punc = ["hi", "lets", "learn", "this", "string"]

text = Text(parsed_without_punc)
print(f"text.text = {text.text}")
print(f"text.blanked = {text.blanked}")
print(f"text.full_blanked = {text.full_blanked}")
print(f"text.rand_lst = {text.rand_lst}")
print(text.display_txt())
text.set_level(2)
print(text.display_txt())
text.set_level(6)
print(text.max_level)
print(text.display_txt())
text.set_level(-1)