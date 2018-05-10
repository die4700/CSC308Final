# Alexander Dietz
# Brittani Kiger
# Christopher Lytle

# Import tkinter
import tkinter
import tkinter.messagebox

# Import other
from calu_bot import login
import calu_bot

class scoreGUI:
    def __init__(self):

        # Create main window widget.
        self.main_window = tkinter.Tk()

        # Create window frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create widgets and labels.
        self.label1 = tkinter.Label(self.top_frame, text = 'Enter a subreddit to search.')
        self.text1 = tkinter.Entry(self.top_frame, width = 15)
        self.label2 = tkinter.Label(self.mid_frame, text = 'Enter how many posts to average.')
        self.text2 = tkinter.Entry(self.mid_frame, width = 15)
        self.submit1 = tkinter.Button(self.bottom_frame, text = 'Submit', command=self.getData)

        # Pack widgets
        self.label1.pack(side = 'left')
        self.text1.pack(side = 'right')
        self.label2.pack(side = 'left')
        self.text2.pack(side = 'right')
        self.submit1.pack()

        # Pack frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter tkinter main loop.
        tkinter.mainloop()

    def scoreParser(self, obj, sub1, num1):
        score = 0
        average = 0
        for submission in obj.subreddit(sub1).hot(limit=num1):
            score += submission.score
            average = (score/num1)

        popupMessage = 'The average score of the top ' + str(num1) + ' hot posts on /r/ ' + str(sub1) + ' is: ' + str(average)
        
        tkinter.messagebox.showinfo('Average', popupMessage)

    # Get strings from the GUI
    def getData(self):
        sub1 = str(self.text1.get())
        num1 = int(self.text2.get())

        # Create an instanace of calu_bot
        obj = calu_bot.login()

        self.scoreParser(obj, sub1, num1)