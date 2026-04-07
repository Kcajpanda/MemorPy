from classes.Text import Text

parsed_without_punc = ["hi", ",", "lets", "learn", ":", "this", "string"]

text = Text(parsed_without_punc)
print(f"text.text = {text.text}")
# print(f"text.blanked = {text.blanked}")
# print(f"text.full_blanked = {text.full_blanked}")
print(f"text.rand_lst = {text.rand_lst}")

text.set_level(0)
print(text.display_txt())
text.set_level(3)
print(text.display_txt())

# print(text.max_level)
# print(text.display_txt())