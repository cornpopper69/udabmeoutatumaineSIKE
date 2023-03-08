from sys import argv

WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"


def get_letter(word, index):
    return word[index]


print(f"{WHITE}Letter {argv[2]} of {argv[1]} is {get_letter(argv[1], int(argv[2])-1)}")
