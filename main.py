from classes.Text import Text
from classes.Parser import Parser
import copy

parse_obj = Parser()
parsed_text = parse_obj.parse("./test_text/test_2.txt")

text = Text(parsed_text)
# print(f"text.text = {text.text}")
# # print(f"text.blanked = {text.blanked}")
# # print(f"text.full_blanked = {text.full_blanked}")
# print(f"text.rand_lst = {text.rand_lst}")

# # text.set_level(0)
# # print(text.display_txt())
text.set_level(4)
print(text.gen_display_txt())
print(text.out_txt())

# # print(text.max_level)
# # print(text.display_txt())

# test = "hi, my name is jack."
# split_list = test.split()
# split_list_copy = copy.copy(split_list)
# tracked_chng = []
# print(split_list)

# for w in range(len(split_list)):
#     word = split_list[w]
#     for c in range(len(word)):
#         if not word[c].isalpha():
#             char = word[c]
#             # print(f"char: {char}")
#             split_word = word.split(char)
#             # print(f"split_word = {split_word}")
#             split_list[w] = split_word[0]
#             tracked_chng.append([w+1, char])

# print(tracked_chng)
# spacing = 0
# for chng in tracked_chng:
#     split_list.insert(chng[0]+spacing, chng[1])
#     spacing+=1

# print(split_list)
