import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import sqlite3
import sys


# Create the database.
class CreateDatabase:

    def __init__(self):
    
        # Initialize the database and the cursor.
        self.dbConnection = sqlite3.connect('swimmerdbFile.db')
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute('CREATE TABLE IF NOT EXISTS swimmer_info (id PRIMARYKEY text, sName text, gName text, dob text, mob text, yob text, gender text, swimTime text, email text, swimStroke text, swimClub text, swimCoach text)')


    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()


    def Insert(self, id, sName, gName, dob, mob, yob, gender, swimTime, email, swimStroke, swimClub, swimCoach):
        self.dbCursor.execute('INSERT INTO swimmer_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (id, sName, gName, dob, mob, yob, gender, swimTime, email, swimStroke, swimClub, swimCoach))
        self.dbConnection.commit()


    def Update(self, id, sName, gName, dob, mob, yob, gender, swimTime, email, swimStroke, swimClub, swimCoach):
        self.dbCursor.execute('UPDATE swimmer_info SET sName = ?, gName = ?, dob = ?, mob = ?, yob = ?, gender = ?, swimTime = ?, email = ?, swimStroke = ?, swimClub = ?, swimCoach = ? WHERE id = ?',
        (sName, gName, dob, mob, yob, gender, swimTime, email, swimStroke, swimClub, swimCoach, id))
        self.dbConnection.commit()


    def Search(self, id):
        self.dbCursor.execute('SELECT * FROM swimmer_info WHERE id = ?', (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults


    def Delete(self, id):
        self.dbCursor.execute('DELETE FROM swimmer_info WHERE id = ?', (id,))
        self.dbConnection.commit()


    def Display(self):
        self.dbCursor.execute('SELECT * FROM swimmer_info')
        records = self.dbCursor.fetchall()
        return records



class Values:

    def Validate(self, id, sName, gName, swimTime, email, swimClub, swimCoach):
        if not (id.isdigit() and (len(id) == 3)):
            return 'id'
        elif not (sName.isalpha()):
            return 'sName'
        elif not (gName.isalpha()):
            return 'gName'
        elif not (swimTime.isdigit() and len(swimTime) > 3):
            return 'swimTime'
        elif not (email.count('@') == 1 and email.count('.') > 0):
            return 'email'
        elif not (swimClub.isalpha()):
            return 'swimClub'
        elif not (swimCoach.isalpha()):
            return 'swimCoach'
        else:
            return 'SUCCESS'



class InsertWindow:
    def __init__(self, id=None, mode=None): # hzh
        self.window = tk.Tk()
        self.window.wm_title('Insert data')
        self.window.configure(bg='#0c2c4c')

        #tk.Label(self.window,foreground='white', background= '#4484c4', width=50,).grid(pady=20, column=1, row=1)

        # Initializing all the variables
        self.id = tk.StringVar()
        self.sName = tk.StringVar()
        self.gName = tk.StringVar()
        self.swimTime = tk.StringVar()
        self.email = tk.StringVar()
        self.swimClub = tk.StringVar()
        self.swimCoach = tk.StringVar()

        self.genderList = ['Male', 'Female', 'Other']
        self.dateList = list(range(1, 32))
        self.monthList = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December',
        ]

        self.yearList = list(range(1900, 2020))
        self.swimStrokeList = ['Freestyle', 'Backstroke', 'Breatstroke', 'Butterfly']

        # Create labels inside the insert frame.
        tk.Label(self.window, text = 'Swimmer ID', width = 25).grid(pady = 5, column = 1, row = 1)
        tk.Label(self.window, text = 'Given Name', width = 25).grid(pady = 5, column = 1, row = 2)
        tk.Label(self.window, text = 'Surname', width = 25).grid(pady = 5, column = 1, row = 3)
        tk.Label(self.window, text = 'D.O.B', width = 25).grid(pady = 5, column = 1, row = 4)
        tk.Label(self.window, text = 'M.O.B', width = 25).grid(pady = 5, column = 1, row = 5)
        tk.Label(self.window, text = 'Y.O.B', width = 25).grid(pady = 5, column = 1, row = 6)
        tk.Label(self.window, text = 'Gender', width = 25).grid(pady = 5, column = 1, row = 7)
        tk.Label(self.window, text = ' Swimmers Time', width = 25).grid(pady = 5, column = 1, row = 9)
        tk.Label(self.window, text = 'Email ID', width = 25).grid(pady=5, column = 1, row = 10)
        tk.Label(self.window, text = 'Swimmers Stroke', width = 25).grid(pady = 5, column = 1, row = 11)
        tk.Label(self.window, text = 'Swimmers Club', width = 25).grid(pady = 5, column = 1, row = 12)
        tk.Label(self.window, text = 'Swimmers Coach', width = 25).grid(pady = 5, column = 1, row = 13)

        # Fields
        # Create entries inside the insert frame.    
        # Entry widgets

        if mode == None: # hzh - insert
            self.id = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.id)
            self.sName = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.sName)
            self.gName = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.gName)
            self.swimTime = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.swimTime)
            self.email = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.email)
            self.swimClub = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.swimClub)
            self.swimCoach = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.swimCoach)

            self.id.grid(pady = 5, column = 3, row = 1)
            self.sName.grid(pady = 5, column = 3, row = 2)
            self.gName.grid(pady = 5, column = 3, row = 3)
            self.swimTime.grid(pady = 5, column = 3, row = 9)
            self.email.grid(pady = 5, column = 3, row = 10)
            self.swimClub.grid(pady = 5, column = 3, row = 12)
            self.swimCoach.grid(pady = 5, column = 3, row = 13)

            # Combobox widgets
            self.dobBox = tk.ttk.Combobox(self.window, values=self.dateList, width = 20)
            self.mobBox = tk.ttk.Combobox(self.window, values=self.monthList, width = 20)
            self.yobBox = tk.ttk.Combobox(self.window, values=self.yearList, width = 20)
            self.genderBox = tk.ttk.Combobox(self.window, values=self.genderList, width = 20)
            self.swimStrokeBox = tk.ttk.Combobox(self.window, values=self.swimStrokeList, width = 20)

            self.dobBox.grid(pady = 5, column=  3, row = 4)
            self.mobBox.grid(pady = 5, column = 3, row=5)
            self.yobBox.grid(pady = 5, column = 3, row = 6)
            self.genderBox.grid(pady = 5, column = 3, row = 7)
            self.swimStrokeBox.grid(pady = 5, column = 3, row = 11)
            
        else: # hzh - mode is update
            self.database = CreateDatabase() # hzh
            self.searchResults = self.database.Search(id) # hzh

            self.id = tk.Entry(self.window, width = 25, bd = 3, textvariable = self.id)
            self.sName = tk.Entry(self.window, width = 25, bd = 3, textvariable=  self.sName)
            self.gName = tk.Entry(self.window, width = 25, bd = 3, textvariable=self.gName)
            self.swimTime = tk.Entry(self.window, width = 25, bd = 3, textvariable=self.swimTime)
            self.email = tk.Entry(self.window, width = 25, bd = 3,  textvariable=self.email)
            self.swimClub = tk.Entry(self.window, width = 25, bd = 3,  textvariable=self.swimClub)
            self.swimCoach = tk.Entry(self.window, width = 25, bd = 3, textvariable=self.swimCoach)
            self.dobBox = tk.ttk.Combobox(self.window, values=self.dateList, width=20)
            self.mobBox = tk.ttk.Combobox(self.window, values=self.monthList, width=20)
            self.yobBox = tk.ttk.Combobox(self.window, values=self.yearList, width=20)
            self.genderBox = tk.ttk.Combobox(self.window, values=self.genderList, width=20)
            self.swimStrokeBox = tk.ttk.Combobox(self.window, values=self.swimStrokeList, width=20)

            self.id.grid(pady=5, column=3, row=1)
            self.id.insert(0, self.searchResults[0][0])
            
            self.sName.grid(pady=5, column=3, row=2)
            self.sName.insert(0, self.searchResults[0][2])

            self.gName.grid(pady=5, column=3, row=3)
            self.gName.insert(0, self.searchResults[0][1])

            self.swimTime.grid(pady=5, column=3, row=9)
            self.swimTime.insert(0, self.searchResults[0][7])
            
            self.email.grid(pady=5, column=3, row=10)
            self.email.insert(0, self.searchResults[0][8])

            self.swimClub.grid(pady=5, column=3, row=12)
            self.swimClub.insert(0, self.searchResults[0][10])

            self.swimCoach.grid(pady=5, column=3, row=13)
            self.swimCoach.insert(0, self.searchResults[0][11])

            self.dobBox.grid(pady=5, column=3, row=4)
            self.dobBox.insert(0, self.searchResults[0][3])

            self.mobBox.grid(pady=5, column=3, row=5)
            self.mobBox.insert(0, self.searchResults[0][4])

            self.yobBox.grid(pady=5, column=3, row=6)
            self.yobBox.insert(0, self.searchResults[0][5])

            self.genderBox.grid(pady=5, column=3, row=7)
            self.genderBox.insert(0, self.searchResults[0][6])

            self.swimStrokeBox.grid(pady=5, column=3, row=11)
            self.swimStrokeBox.insert(0, self.searchResults[0][9])

        # Button widgets
        if mode == 'update': # hzh - conditionals dependent on mode
            tk.Button(self.window, width=20, text='Update', command=self.Update).grid(
                pady=15, padx=5, column=1, row=14)
            tk.Button(self.window, width=20, text='Reset', command=self.Reset).grid(
                pady=15, padx=5, column=2, row=14)
            tk.Button(self.window, width=20, text='Close', command=self.window.destroy).grid(
                pady=15, padx=5, column=3, row=14)
        else: # hzh - default mode - i.e. insert
            tk.Button(self.window, width=20, text='Insert', command=self.Insert).grid(
                pady=15, padx=5, column=1, row=14)
            tk.Button(self.window, width=20, text='Reset', command=self.Reset).grid(
                pady=15, padx=5, column=2, row=14)
            tk.Button(self.window, width=20, text='Close', command=self.window.destroy).grid(
                pady=15, padx=5, column=3, row=14)

        self.window.mainloop()


    def Insert(self):
        self.values = Values()
        self.database = CreateDatabase()
        self.test = self.values.Validate(
            self.id.get(),
            self.gName.get(),
            self.sName.get(),
            self.swimTime.get(),
            self.email.get(),
            self.swimClub.get(),
            self.swimCoach.get(),
        )

        if self.test == 'SUCCESS':
            self.database.Insert(
                self.id.get(),
                self.gName.get(),
                self.sName.get(),
                self.dobBox.get(),
                self.mobBox.get(),
                self.yobBox.get(),
                self.genderBox.get(),
                self.swimTime.get(),
                self.email.get(),
                self.swimStrokeBox.get(),
                self.swimClub.get(),
                self.swimCoach.get()
                )

            tk.messagebox.showinfo('Inserted data', 'Successfully inserted the above data in the database')
        else:
            self.valueErrorMessage = 'Invalid input in field ' + self.test

            tk.messagebox.showerror('Value Error', self.valueErrorMessage)


    def Update(self): # hzh - can refactor this section so the validation is in a separate function so not to repeat code
        self.values = Values()
        self.database = CreateDatabase()
        self.test = self.values.Validate(
            self.id.get(),
            self.gName.get(),
            self.sName.get(),
            self.swimTime.get(),
            self.email.get(),
            self.swimClub.get(),
            self.swimCoach.get(),
        )

        if self.test == 'SUCCESS':
            self.database.Update( # hzh
                self.id.get(), # hzh
                self.gName.get(), # hzh
                self.sName.get(), # hzh
                self.dobBox.get(), # hzh
                self.mobBox.get(), # hzh
                self.yobBox.get(), # hzh
                self.genderBox.get(), # hzh
                self.swimTime.get(), # hzh
                self.email.get(), # hzh
                self.swimStrokeBox.get(), # hzh
                self.swimClub.get(), # hzh
                self.swimCoach.get() # hzh
            ) # hzh
            tk.messagebox.showinfo('Updated data', 'Successfully updated the above data in the database')
        else:
            self.valueErrorMessage = 'Invalid input in field ' + self.test

            tk.messagebox.showerror('Value Error', self.valueErrorMessage)


    def Reset(self):
        self.idEntry.delete(0, tk.END)
        self.sNameEntry.delete(0, tk.END)
        self.sNameEntry.delete(0, tk.END)
        self.dobBox.set('')
        self.mobBox.set('')
        self.yobBox.set('')
        self.genderBox.set('')
        self.swimTimeEntry.delete(0, tk.END)
        self.emailEntry.delete(0, tk.END)
        self.swimStrokeBox.set('')
        self.swimClubEntry.delete(0, tk.END)
        self.swimCoachEntry.delete(0, tk.END)



class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tk.Tk()
        self.databaseViewWindow.wm_title('Database View')
        self.databaseViewWindow.configure(bg='#0c2c4c')

        # Label widgets
        tk.Label(
            self.databaseViewWindow, text='Database View Window', width=25).grid(pady=5, column=1, row=1)

        # Create tags for treeview.
        self.databaseView = tk.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView['show'] = 'headings'
        self.databaseView['columns'] = (
            'id',
            'gName',
            'sName',
            'dob',
            'mob',
            'yob',
            'gender',
            'swimTime',
            'email',
            'swimStroke',
            'swimClub',
            'swimCoach',
        )

        # Treeview column headings
        self.databaseView.heading('id', text='ID')
        self.databaseView.heading('gName', text='Given Name')
        self.databaseView.heading('sName', text='Surname')
        self.databaseView.heading('dob', text='D.O.B')
        self.databaseView.heading('mob', text='M.O.B')
        self.databaseView.heading('yob', text='Y.O.B')
        self.databaseView.heading('gender', text='Gender')
        self.databaseView.heading('swimTime', text='SwimmTime')
        self.databaseView.heading('email', text='Email ID')
        self.databaseView.heading('swimStroke', text='swimStroke')
        self.databaseView.heading('swimClub', text='swimClub')
        self.databaseView.heading('swimCoach', text='swimCoach')

        # Treeview columns
        self.databaseView.column('id', width=40)
        self.databaseView.column('gName', width=100)
        self.databaseView.column('sName', width=100)
        self.databaseView.column('dob', width=60)
        self.databaseView.column('mob', width=60)
        self.databaseView.column('yob', width=60)
        self.databaseView.column('gender', width=60)
        self.databaseView.column('swimTime', width=100)
        self.databaseView.column('email', width=200)
        self.databaseView.column('swimStroke', width=100)
        self.databaseView.column('swimClub', width=100)
        self.databaseView.column('swimCoach', width=100)

        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()


class SearchDeleteWindow:
    def __init__(self, task):
        window = tk.Tk()
        window.wm_title(task + ' data')

        # Initializing all the variables
        self.id = tk.StringVar()
        self.sName = tk.StringVar()
        self.gName = tk.StringVar()
        self.heading = 'Please enter Swimmer ID to ' + task

        # Labels
        tk.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tk.Label(window, text='Swimmer ID', width=10).grid(pady=5, row=2)

        # Entry widgets
        self.idEntry = tk.Entry(window, width=5, textvariable=self.id)

        self.idEntry.grid(pady=5, row=3)

        # Button widgets
        if task == 'Search':
            tk.Button(window, width=20, text=task, command=self.Search).grid(pady=15, padx=5, column=1, row=14)
        elif task == 'Delete':
            tk.Button(window, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

    def Search(self):
        self.database = CreateDatabase()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = CreateDatabase()
        self.database.Delete(self.idEntry.get())



class HomePage:
    def __init__(self):
        self.homePageWindow = tk.Tk()
        self.homePageWindow.wm_title('Swimmer Information Manager')
        self.homePageWindow.configure(bg='#0c2c4c')

        tk.Label(self.homePageWindow,text='Home Page', width=100, foreground='white', bg= '#4484c4',).grid(pady=20, column=1, row=1)
        tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=25,height=3, text="Insert Swimmer's Details", cursor= 'plus',bd=7, command=self.Insert).grid(pady=15, column=1, row=2)
        tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=25,height=3, text="Update Swimmer's Details", cursor= 'pencil', command=self.Update).grid(pady=15, column=1, row=3)
        tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=25,height=3, text="Search for Swimmer", command=self.Search).grid(pady=15, column=1, row=4)
        tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=25,height=3, text="Delete Swimmer", command=self.Delete).grid(pady=15, column=1, row=5)
        tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=25,height=3, text="Display All Swimmers", command=self.Display).grid(pady=15, column=1, row=6)
        tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=25,height=3, text='Exit', cursor='pirate', command=sys.exit, bd=5).grid(pady=15, column=1, row=7)
        
       # tk.Button(self.homePageWindow, font=('arial',16,'bold'), width=20, text='Logout', bd=5).grid(pady=15, column=2, row=8)
        
        # create logout button
       # logout_btn = Button(root_3, text="Logout", command=root_3.destroy)
       # logout_btn.grid(row=0, column=1, sticky=NE, padx=300, pady=20)
        #command= self.head.destroy
        # self.homePageWindow.mainloop() # hzhs


    def Insert(self):
        self.insertWindow = InsertWindow()

    def Update(self):
        self.updateIDWindow = tk.Tk()
        self.updateIDWindow.wm_title('Update data')
        #self.updateIDWindow.configure(bg='#0c2c4c')

        # Initializing all the variables
        self.id = tk.StringVar()

        # Label
        tk.Label(self.updateIDWindow, text = 'Enter the ID to update', width = 50).grid(pady = 20, row = 1)

        # Entry widgets
        self.idEntry = tk.Entry(self.updateIDWindow, width = 5, textvariable=self.id)

        self.idEntry.grid(pady = 10, row = 2)

        # Button widgets
        tk.Button(self.updateIDWindow, width = 20, text='Update', command=self.updateID).grid(pady=10, row=3)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = InsertWindow(id=self.idEntry.get(), mode='update') # hzh - insert and update same window - different modes - less repetition of code
        self.updateIDWindow.destroy()


    def Search(self):
        self.searchWindow = SearchDeleteWindow('Search')


    def Delete(self):
        self.deleteWindow = SearchDeleteWindow('Delete')


    def Display(self):
        self.database = CreateDatabase()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)


# homePage = HomePage() hzh
