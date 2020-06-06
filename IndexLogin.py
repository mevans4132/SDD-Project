# Swimming Information Manager

# Just want to recommend the two resources that helped me alot through this Project
# <https://www.youtube.com/watch?v=o-vsdfCBpsU&list=RDCMUCfzlCWGWYyIQ0aLC5w48gBQ&start_radio=1&t=407&t=407>
# <https://www.tutorialspoint.com/python/python_gui_programming.htm>


from tkinter import *                   # tkinter is the standard GUI library for Python.
from tkinter import ttk                 # Tkinter is for python2 , whereas tkinter (lowercase) is for python3
import random                           # imports the random module, which contains a variety of things to do with random number generation
import time                             
import datetime                         
from tkinter import messagebox as ms    
import sqlite3                          
import swimmerinfomgr # hzh            


def test_function(entry):
	print('This is the entry:', entry)

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:   # the program connect to the db User.db 
    c = db.cursor()                       # cursor, does all the excutions
    c.execute('CREATE TABLE IF NOT EXISTS User(username TEXT NOT NULL, password TEXT NOT NULL)') #colums of the data and the data types
db.commit() 
db.close() 




# main Class for Index Module
class user:

    def __init__(self, master):

    	# Window 
        self.master = master # set the window size for Login, Register Account and Login Help

        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()

        # Create Widgets
        self.widgets()
        self.swimmerInfoMgr = swimmerinfomgr # hzh- issue fixed


    # Login Function
    def login(self):

    	# Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = 'Welcome, ' + self.username.get()
            self.head.configure(fg = 'white')
            self.head.pack(fill = BOTH)
            self.swimmerInfoMgr.HomePage() # hzh
        else:
            ms.showerror('Oops!', 'Username Not Found.')


    def new_user(self):

    	# Establish Connections
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!', 'Username Already Exists!')
        else:
            ms.showinfo('Success!', 'Account Registered!')
            self.log()

        # Register New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?, ?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()


    # Frame Packing Methods

    # Function Login
    def log(self):
        self.username.set('')
        self.password.set('')
        self.regf.pack_forget()
        self.hlpf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
 
    # Function Register Account
    def reg(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Register Account'
        self.regf.pack()


    # Function Help
    def hlp(self):
        self.logf.pack_forget() 
        self.head['text'] = 'Need Help?'
        self.hlpf.pack()


    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text = 'LOGIN', fg = 'white', bg = '#0c2c4c', font = ('', 35), pady = 10)
        self.head.pack(fill = BOTH)
       
        self.logf = Frame(self.master, bg = '#4484c4', padx = 10, pady = 10)
        Label(self.logf, text = 'Username: ', bg = '#4484c4', font = ('', 20), pady = 5, padx = 5).grid(sticky = W)
        Entry(self.logf, textvariable = self.username, bd = 5, font = ('', 15)).grid(row = 0, column = 1)
        Label(self.logf, text = 'Password: ', bg = '#4484c4', font = ('', 20), pady = 5, padx = 5).grid(sticky = W)
        Entry(self.logf, textvariable = self.password, bd = 5, font = ('', 15), show = '*').grid(row=1,column=1)
        Button(self.logf, text = ' Login ', bd = 3, font = ('', 15), padx = 5, pady = 5, command = self.login).grid(row = 7, column = 0)
        Button(self.logf, text = ' Register Account ', bd = 3, font = ('', 15), padx = 5, pady = 5,command = self.reg).grid(row = 2,column = 1)
        Button(self.logf, text = ' Need Help? ', bd = 3, font = ('', 15), cursor = 'question_arrow', padx = 5, pady = 5, command = self.hlp).grid(row=  7,column = 3)
       
        self.logf.pack()
        
        self.regf = Frame(self.master, bg = '#4484c4', padx = 10, pady = 10)
        Label(self.regf, text = 'Username: ', bg = '#4484c4', font = ('', 20), pady = 5, padx = 5).grid(sticky = W)
        Entry(self.regf, textvariable = self.n_username, bd = 5, font = ('', 15)).grid(row = 0, column = 1)
        Label(self.regf, text = 'Password: ', bg = '#4484c4', font = ('', 20), pady = 5, padx = 5).grid(sticky = W)
        Entry(self.regf, textvariable = self.n_password, bd = 5, font = ('', 15), show = '*').grid(row = 1, column = 1)
        Button(self.regf, text = 'Register Account', font = ('', 15), padx = 5, pady = 5, command = self.new_user).grid(row = 3, column = 0)
        Button(self.regf, text = 'Go to Login', bd = 3, font = ('', 15), padx = 5, pady = 5, command = self.log).grid(row = 3, column = 2)

        self.hlpf = Frame(self.master, bg = '#4484c4', padx = 10, pady = 10)
        Label(self.hlpf, text = 'If you cant sign into your Account, select the register ', bg = '#4484c4', font = ('',20), pady = 5, padx = 5).grid(sticky = W)
        Label(self.hlpf, text = 'account to test if it is already registered.', bg = '#4484c4', font = ('',20), pady = 5, padx = 5).grid(sticky = W)
        Button(self.hlpf, text = 'Go to Login', bd = 3, font = ('',15), padx = 5, pady = 5, command=self.log).grid(row = 3, column = 3)
        

#====================================================================================================================================

if __name__ == '__main__':
    root = Tk()

#=========================================== Getting Screen Width ==================================================================
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    geometry = '%dx%d+%d+%d'%(w,h,0,0)

   
    
    root.geometry('600x400+500+300')    #Sets the position and size of the login window
    root.configure(bg = '#4484c4')        #Sets the background colour
    root.title('Welcome')               #Sets the login window title name
    application = user(root)            
    root.mainloop()                     #method on login window which executes when application runs.
    bg = '#4484c4'                       #bg stand for backgroud colour, sets the colour of login window

    #self.head.pack_forget() - CUT CONTENT



    