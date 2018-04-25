# Alexander Dietz
# Brittani Kiger
# Christopher Lytle

# Import Tkinter
from tkinter import *

root = Tk()
root.geometry("400x200")

def retreive_input():
        
    subreddit_input = subreddit.get("1.0", "end-1c")
    print(subreddit_input)

    string_search_input = string_search.get("1.0", "end-1c")
    print(string_search_input)


instructions = ['Enter a subreddit name:', 'Enter a string to search for:']


subreddit_label = Label(root, text="Enter a subreddit name:")
subreddit_label.pack()


subreddit = Text(root, height=2, width=15)
subreddit.pack()

string_search_label = Label(root, text="Enter a string to search for:")
string_search_label.pack()

string_search = Text(root, height=2, width=15)
string_search.pack()


buttonSearch=Button(root, height=1, width=10, text="Search", command=lambda: retreive_input())
buttonSearch.pack()


mainloop()