# Alexander Dietz
# Brittani Kiger
# Christopher Lytle

# Import tkinter
import tkinter
import tkinter.messagebox

# Import other
from calu_bot import login
import calu_bot

class commentGUI:
    def __init__(self):

        # Create main window widget.
        self.main_window = tkinter.Tk()

        # Create window frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create widgets and labels.
        self.label1 = tkinter.Label(self.top_frame, text = 'Enter a subreddit to search.')
        self.text1 = tkinter.Entry(self.top_frame, width = 15)
        self.label2 = tkinter.Label(self.mid_frame1, text = 'Enter a string to search for.')
        self.text2 = tkinter.Entry(self.mid_frame1, width = 15)
        self.label3 = tkinter.Label(self.mid_frame2, text = 'Enter the number of posts to search.')
        self.text3 = tkinter.Entry(self.mid_frame2, width = 15)
        self.submit1 = tkinter.Button(self.bottom_frame, text = 'Submit', command=self.getFields)

        # Pack widgets
        self.label1.pack(side = 'left')
        self.text1.pack(side = 'right')
        self.label2.pack(side = 'left')
        self.text2.pack(side = 'right')
        self.label3.pack(side= 'left')
        self.text3.pack(side = 'right')
        self.submit1.pack()

        # Pack frames
        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack()

        # Enter tkinter main loop.
        tkinter.mainloop()

    # Function that searches for string within comments on a given subreddit
    def commentsParser(self, obj, sub1, str1, num1):
        counter = 0
        for comment in obj.subreddit(sub1).comments(limit=num1):
            if str1 in comment.body:
                counter += (counter + 1)
        
        popupMessage = 'Found', str1, counter, 'times in /r/', sub1
        
        tkinter.messagebox.showinfo('Search', popupMessage)

    # Get strings from the GUI
    def getFields(self):
        sub1 = str(self.text1.get())
        str1 = str(self.text2.get())
        num1 = int(self.text3.get())
        
        # Create an instanace of calu_bot
        obj = calu_bot.login()

        self.commentsParser(obj, sub1, str1, num1)