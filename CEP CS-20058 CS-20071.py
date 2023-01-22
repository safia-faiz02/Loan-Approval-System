from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import re

class MainPage():

    def __init__(self):
        self.root = Tk()
        self.root.geometry('1366x768+50+50')
        self.root.title('Loan Approval System')
        self.root.configure(bg = '#ABCECF')

        # frame 1
        self.frame1 = Frame(self.root, padx = 20, pady = 20, width = 100)
        self.frame1.pack(padx = 50, pady = 70)

        self.heading = Label(self.frame1, text = 'LOAN APPROVAL SYSTEM', font = ('Helvetica', 30, 'bold underline'))
        self.heading.pack(pady = 20)

        self.description = Text(self.frame1, height=8, bg = '#8FC9AE', font = ('Arial', 15), width = 100, padx = 20, pady = 20)
        self.description.pack()
        self.description.tag_configure("center", justify='center')
        self.description.insert(1.0, " ")
        self.description.tag_add("center", "1.0", "end")
        quote = "Loan Approval System is an application which lets you input your required personal details and let you know if you are \neligible to to be granted a loan, or not using the techniques of Neural Networks. This application is created by two junior year students of CIS - NEDUET as their Complex Engineering Problem, namely Safia Faiz and S. M. Mubashir Rizvi, to facilitate \ncompanies who are finding biases or difficulties to decide whether to grant this person or their employee a loan or not. The \nsystem takes an input of various parameters, such as, if the person is married or not, if they're employed, and several others too. The decision-making of this system is done by the software 'EasyNN-plus', which is an Artificial Neural Network (ANN) \nsystem. EasyNN-plus predicts or makes the decision whether or not the person should be granted a loan or not, by training it \non a relevant set of similar data and then adding in your test data and EasyNN-plus lets you know the latter."
        self.description.insert(END, quote)
        self.description.config(state=DISABLED)

        # frame 2   
        self.frame2 = Frame(self.root, background = "#ABCECF", padx = 10, pady = 20)
        self.frame2.pack(fill = BOTH, padx = 50, pady = 12)

        self.button1 = Button(self.frame2, text = 'ADD RECORD(S)', font = ('Helvetica', 15, 'bold'), padx = 50, pady = 20, width = 17, command = self.addQueries)
        self.button1.pack(side = LEFT, padx = 50, pady = 20)

        self.button2 = Button(self.frame2, text = 'VIEW RESULTS', font = ('Helvetica', 15, 'bold'), padx = 50, pady = 20, width = 17, command = self.viewResults)
        self.button2.pack(side = LEFT, padx = 50, pady = 20)

        self.button3 = Button(self.frame2, text = 'USER GUIDE/HELP', font = ('Helvetica', 15, 'bold'), padx = 50, pady = 20, width = 17,command = self.helpPage)
        self.button3.pack(side = LEFT, padx = 50, pady = 20)

        self.root.mainloop()

    def helpPage(self):
        self.root.destroy()
        self.helppage = HelpPage()

    def addQueries(self):
        self.root.destroy()
        self.addQuery = AddQueries()

    def viewResults(self):
        self.root.destroy()
        self.viewResult = ViewResults()


class AddQueries():        
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1366x768+50+50')
        self.root.title('Add Your Details')
        self.root.configure(bg = '#ABCECF')

        # FILE INFO FRAME
        self.file_info = Frame(self.root, height = 80, width = 700, bg = '#8FC9AE')
        self.file_info.grid(row = 0, padx = 300, pady = 15)
        self.file_info.grid_propagate(False)

        self.file_label = Label(self.file_info , text="Enter file name (without extension): ",font= ("Helvetica",18,"bold"), \
                                        fg = "black", bg = '#8FC9AE')
        self.file_label.grid(row = 1  ,padx = 20, pady = 20)
        self.file_entry = Entry(self.file_info ,font = ("Times New Roman",14))
        self.file_entry.grid(row = 1 , column = 1 ,padx = 10)

        # COLUMN INFORMATION MAIN FRAME
        self.info_frame = Frame(self.root , height = 300, width = 1200, bg = '#ABCECF', pady = 10)
        self.info_frame.grid(row = 1, padx = 65)
        self.info_frame.pack_propagate(False) 



        # frame 1 inside main frame
        self.info_f1 = Frame(self.info_frame , height = 500, width = 600, bg = '#8FC9AE', padx = 20, pady = 20)
        self.info_f1.grid(row = 1 , column = 0, padx = 15)
        self.info_f1.grid_propagate(False)

        self.lab1 = Label(self.info_f1 , text = "Gender \n(Male/Female)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab1.grid(row = 0 , column = 0, pady = 20)
        self.e1_genderDefault = StringVar()
        self.e1_genderDefault.set('')
        self.genderOptions = ['Male', 'Female']
        self.drop_gender = OptionMenu(self.info_f1, self.e1_genderDefault, *self.genderOptions)
        self.drop_gender.grid(row = 0, column = 1, padx = 30)
        self.drop_gender.config(width = 25)

        self.lab2 = Label(self.info_f1 , text = "Married \n(Y/N)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab2.grid(row = 1 , column = 0, pady = 20)
        self.e2_marriedDefault = StringVar()
        self.e2_marriedDefault.set('')
        self.marriedOptions = ['Yes', 'No']
        self.drop_married = OptionMenu(self.info_f1, self.e2_marriedDefault, *self.marriedOptions)
        self.drop_married.grid(row = 1, column = 1, padx = 30)
        self.drop_married.config(width = 25)

        self.lab3 = Label(self.info_f1 , text = "Dependents \n(In Numbers)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab3.grid(row = 2 , column = 0, pady = 20)
        self.e3 = Entry(self.info_f1 ,font = ("Times New Roman",14))
        self.e3.grid(row = 2 , column = 1, padx = 30)

        self.lab4 = Label(self.info_f1 , text = "Education\n(Graduate/Not Graduate)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab4.grid(row = 3 , column = 0, pady = 20)
        self.e4_eduDefault = StringVar()
        self.e4_eduDefault.set('')
        self.eduOptions = ['Undergraduate', 'Graduate']
        self.drop_edu = OptionMenu(self.info_f1, self.e4_eduDefault, *self.eduOptions)
        self.drop_edu.grid(row = 3, column = 1, padx = 30)
        self.drop_edu.config(width = 25)

        self.lab5 = Label(self.info_f1 , text = "Self-Employed\n(Y/N)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab5.grid(row = 4 , column = 0, pady = 20)
        self.e5_selfEmpDefault = StringVar()
        self.e5_selfEmpDefault.set('')
        self.selfEmpOptions = ['Yes', 'No']
        self.drop_selfEmp = OptionMenu(self.info_f1, self.e5_selfEmpDefault, *self.selfEmpOptions)
        self.drop_selfEmp.grid(row = 4, column = 1, padx = 30)
        self.drop_selfEmp.config(width = 25)



        # frame 2 inside main frame
        self.info_f2 = Frame(self.info_frame , height = 500, width = 600, bg = '#8FC9AE', padx = 20, pady = 20)
        self.info_f2.grid(row = 1 , column = 1, padx = 10)
        self.info_f2.grid_propagate(False)

        self.lab6 = Label(self.info_f2 , text = "Applicant Income\n(In Thousands)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab6.grid(row = 0 , column = 0, pady = 12)
        self.e6 = Entry(self.info_f2 ,font = ("Times New Roman",14))
        self.e6.grid(row = 0 , column = 1, padx = 30)

        self.lab7 = Label(self.info_f2 , text = "Co-Applicant Income\n(In Thousands)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab7.grid(row = 1 , column = 0, pady = 12)
        self.e7 = Entry(self.info_f2 ,font = ("Times New Roman",14))
        self.e7.grid(row = 1 , column = 1, padx = 30)

        self.lab8 = Label(self.info_f2 , text = "Loan Amount\n(In Thousands)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab8.grid(row = 2 , column = 0, pady = 12)
        self.e8 = Entry(self.info_f2 ,font = ("Times New Roman",14))
        self.e8.grid(row = 2 , column = 1, padx = 30)

        self.lab9 = Label(self.info_f2 , text = "Loan Amount Term\n(In Months)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab9.grid(row = 3 , column = 0, pady = 12)
        self.e9 = Entry(self.info_f2 ,font = ("Times New Roman",14))
        self.e9.grid(row = 3 , column = 1, padx = 30)

        self.lab10 = Label(self.info_f2 , text = "Credit History Meets Guidelines?\n(Y/N)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab10.grid(row = 4 , column = 0, pady = 12)
        self.e10_creditDefault = StringVar()
        self.e10_creditDefault.set('')
        self.creditOptions = ['Yes', 'No']
        self.drop_credit = OptionMenu(self.info_f2, self.e10_creditDefault, *self.creditOptions)
        self.drop_credit.grid(row = 4, column = 1, padx = 30)
        self.drop_credit.config(width = 25)

        self.lab11 = Label(self.info_f2 , text = "Property Area\n(Urban/Semi-Urban/Rural)",font= ("Times New Roman",15,"bold"), fg = "black", bg = '#ABCECF', width = 25)
        self.lab11.grid(row = 5 , column = 0, pady = 12)
        self.e11_propertyDefault = StringVar()
        self.e11_propertyDefault.set('')
        self.propertyOptions = ['Urban', 'Semi-Urban', 'Rural']
        self.drop_property = OptionMenu(self.info_f2, self.e11_propertyDefault, *self.propertyOptions)
        self.drop_property.grid(row = 5, column = 1, padx = 30)
        self.drop_property.config(width = 25)



        # Buttons/Options Frame
        self.button_frame = Frame(self.root , height = 100, width = 1000, bg = '#ABCECF', pady = 10)
        self.button_frame.grid(row = 2, pady = 10)
        self.button_frame.pack_propagate(False) 

        self.home = Button(self.button_frame, text = "HOME" ,font = ("Helvetica",15, 'bold'), fg = "#000000", height = 2, width = 10, command = self.toHome)
        self.home.grid(row = 0, column = 0, padx = 50, pady = 10)

        self.save_row = Button(self.button_frame, text = "SAVE\nRECORD",font = ("Helvetica",15, 'bold'), fg = "#000000", height = 2, width = 10, command = self.saveEntry)
        self.save_row.grid(row = 0, column = 1, padx = 50, pady = 10)

        self.delete_entry = Button(self.button_frame, text = "CLEAR\nENTRY" ,font = ("Helvetica",15, 'bold'), fg = "#000000",  height = 2, width = 10, command = self.clearEntry)
        self.delete_entry.grid(row = 0,column = 2, padx = 50, pady = 10)
        
        self.root.mainloop()


    def toHome(self):
        self.root.destroy()
        self.main = MainPage()


    def clearEntry(self):
        to_delete = [self.e3, self.e6, self.e7, self.e8, self.e9]
        for entry in to_delete:
            entry.delete(0, "end")
        
        to_empty = [self.e1_genderDefault, self.e2_marriedDefault, self.e4_eduDefault, self.e5_selfEmpDefault, \
                    self.e10_creditDefault, self.e11_propertyDefault]
        for entry in to_empty:
            entry.set('')
            
    
    def saveEntry(self):        # no check for FILENAME
        from tkinter import messagebox
        confirm = messagebox.askyesno(title = "Confirmation" ,message = "Save data in file?")
        if confirm == True:

            self.filename = self.file_entry.get()
            if len(self.filename) == 0:
                self.filename = 'queries.txt'
            if len(self.filename) != 0:
                regexp = re.compile('[^0-9a-zA-Z]+')
                if regexp.search(self.filename):
                    messagebox.showerror('Invalid File Name', 'Please remove any special characters, use only alphabets and numbers. \nEnter file name without extension.')
                    return
            else:
                self.filename = self.filename + ".txt"

            self.gender = self.e1_genderDefault.get();                  self.married = self.e2_marriedDefault.get();                
            self.dependents = self.e3.get();                            self.education = self.e4_eduDefault.get();                  
            self.selfEmployed = self.e5_selfEmpDefault.get();           self.applicantIncome = self.e6.get();                       
            self.coApplicantIncome = self.e7.get();                     self.loanAmount = self.e8.get();                            
            self.loanTerm = self.e9.get();                              self.creditHistory = self.e10_creditDefault.get();          
            self.propertyArea = self.e11_propertyDefault.get()


            # check for gender 
            if self.gender not in self.genderOptions:   
                messagebox.showerror('Gender Input Error', 'Please select one of the given options') 
                return   

            # check for married
            if self.married not in self.marriedOptions:
                messagebox.showerror('Married Input Error', 'Please select one of the given options') 
                return

            # check for dependents
            try:
                self.dependents = int(self.dependents)

            except:
                messagebox.showerror('Dependents Input Error', 'Please enter an integer for this field')
                return
            
            # check for education
            if self.education not in self.eduOptions:
                messagebox.showerror('Education Input Error', 'Please select one of the given options') 
                return
            
            # check for self-employed
            if self.selfEmployed not in self.selfEmpOptions:
                messagebox.showerror('Self-Employed Input Error', 'Please select one of the given options') 
                return
            
            # check for applicant income
            try:
                self.applicantIncome = int(self.applicantIncome)
            except:
                messagebox.showerror('Applicant Income Input Error', 'Please enter an integer for this field')
                return
            
            # check for co-applicant income
            try:
                self.coApplicantIncome = int(self.coApplicantIncome)
            except:
                messagebox.showerror('Co-Applicant Income Input Error', 'Please enter an integer for this field')
                return

            # check for loan amount
            try:
                self.loanAmount = int(self.loanAmount)
            except:
                messagebox.showerror('Loan Amount Input Error', 'Please enter an integer for this field')
                return
            
            # check for loan amount term
            try:
                self.loanTerm = int(self.loanTerm)
            except:
                messagebox.showerror('Loan Amount Term Input Error', 'Please enter an integer for this field')
                return

            # check for credit history
            if self.creditHistory not in self.creditOptions:
                messagebox.showerror('Credit History Input Error', 'Please select one of the given options')
                return
            
            # check for property area
            if self.propertyArea not in self.propertyOptions:
                messagebox.showerror('Property Area Error', 'Please select one of the given options')
                return


            self.data = [self.gender, self.married, self.dependents, self.education, self.selfEmployed, self.applicantIncome, \
                      self.coApplicantIncome, self.loanAmount, self.loanTerm, self.creditHistory, self.propertyArea, ""]

            self.record = []
            for item in self.data:
                item = str(item)
                self.record.append(item)


            with open(self.filename, 'a+') as f:
                f.seek(0)
                content = f.readlines()
                if len(content) == 0:
                    headers = 'Gender,Married,Dependents,Education,Self_Employed,Applicant_Income,Coapplicant_Income,Loan_Amount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status'
                    f.write(headers)
                    f.write('\n')

                    self.record = ",".join(self.record)
                    f.write(self.record)
                    f.write("\n")
                
                else:
                    self.record = ",".join(self.record)
                    f.write(self.record)
                    f.write('\n')

            confirm2 = messagebox.askyesno(title = "Confirmation" ,message = "Remove previous data?")
            if confirm2 == True:
                self.clearEntry()
            if confirm2 == False:
                pass


class HelpPage():       
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1366x768+50+50')
        self.root.title('Help')
        self.root.configure(bg = '#ABCECF')

        self.frame1 = Frame(self.root, padx = 20, pady = 10, width = 100,bg = '#ABCECF')
        self.frame1.pack(padx = 50, pady = 15)

        self.heading = Label(self.frame1, text = 'USER GUIDE FOR THE SYSTEM', font = ('Helvetica', 20, 'bold underline'),bg = '#ABCECF')
        self.heading.pack(pady=10)

        self.frame2 = Frame(self.root, background = "#ABCECF", padx = 10, pady = 5)
        self.frame2.pack(fill = BOTH, padx = 50, pady = 5)

        self.instructions1 = Text(self.frame2, height=5, bg = '#8FC9AE', font = ('Arial', 15), width = 100, padx = 20, pady = 20)
        self.instructions1.pack(pady = 15)
        self.instructions1.tag_configure("center", justify='center')
        self.instructions1.insert(1.0, " ")
        self.instructions1.tag_add("center", "1.0", "end")
        quote = """ HOW TO RUN THE APPLICATION:

        1. Go to 'Add Record(s)'                                   2. Input your data, make sure it is correct
        3. Save your record by clicking on 'Save Record' and clear your form by clicking on 'Clear Form'
        4. To display your result, go to 'View Results', and choose the file which contains your output"""
        self.instructions1.insert(END, quote)
        self.instructions1.config(state=DISABLED)

        self.instructions2 = Text(self.frame2, height=7.5, bg = '#8FC9AE', font = ('Arial', 15), width = 100, padx = 20, pady = 20)
        self.instructions2.pack(pady= 15)
        self.instructions2.tag_configure("center", justify='center')
        self.instructions2.insert(1.0, " ")
        self.instructions2.tag_add("center", "1.0", "end")
        quote = """ HOW TO RUN EASYNN-PLUS:

1. Launch the EasyNN-plus app
2. Go to File > Import > Select file (either named by you or default 'queries.txt')
3. Check only 'Commas' in the 'Columns' section, and check 'Querying' in the 'Examples row types' section and press 'OK'
4. Press 'Set names' and close the interface that pops up, scroll down and you'll find your data entered in EasyNN-plus
5. Click on 'Query' button (capital Q in purple), an interface pops up, leave the values as is and close the tab and you'll 
        find your desired results"""
        self.instructions2.insert(END, quote)
        self.instructions2.config(state=DISABLED)

        self.button1 = Button(self.frame2, text = 'HOME', font = ('Helvetica', 15, 'bold'), padx = 10, pady = 20, width = 17, command = self.Homepage)
        self.button1.pack(side = BOTTOM, padx = 10, pady = 20)

    def Homepage(self):
        self.root.destroy()
        self.main = MainPage()


class ViewResults():

    def __init__(self):
        self.root = Tk()
        self.root.title('View Results')
        self.root.geometry('1366x768+50+50')
        self.root.config(bg = '#ABCECF')


        self.button_frame = Frame(self.root, bg = "#ABCECF")
        self.button_frame.pack(fill = BOTH, padx = 50, pady = 12)

        self.home_btn = Button(self.button_frame, text = 'HOME', font = ('Helvetica', 15, 'bold'), command = self.toHome, padx = 10, pady = 10, width = 15)
        self.home_btn.grid(row = 0, column = 0, padx = 250, pady = 20)
        # Button to open File Dialog Box
        self.button = Button(self.button_frame, text = 'BROWSE FILE',font= ("Helvetica",15, 'bold'),  command = self.selection, padx = 10, pady = 10, width = 15)
        self.button.grid(row = 0, column = 1, padx = 80, pady = 20)

        self.root.mainloop()


    def selection(self):
        self.filename = filedialog.askopenfilename(initialdir = "./" , title = "Select A File" , filetypes = (("Text Files","*.txt"), ("CSV Files","*.csv")))  
        self.make_record_list()
        self.make_list_box()

    def make_record_list(self):
        self.records = [  ]
        #['Gender', 'Married', 'Dependents', 'Education', 'Self-Employed', 'Applicant Income', \
                          #'Co-Applicant Income', 'Loan Amount', 'Loan Term', 'Credit History', 'Property Area', 'Loan Status']

        with open(self.filename, 'r') as f:
            content = f.readlines()
            for record in content[1: ]:
                record = record.split(',')
                gender = record[0];                     married = record[1];                dependents = record[2];             
                education = record[3];                  selfEmp = record[4];                applicantIncome = record[5];        
                coApplicantIncome = record[6];          loanAmount = record[7];             loanTerm = record[8];                   
                creditHistory = record[9];              propertyArea = record[10];
                loanStatus = record[11];
                loanStatus = loanStatus[0: len(loanStatus) - 1]     # excluding \n in the last

                self.records.append( [ gender, married, dependents, education, selfEmp, applicantIncome, coApplicantIncome, \
                                       loanAmount, loanTerm, creditHistory, propertyArea, loanStatus ] )

        

    def make_list_box(self):

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background="#8FC9AE", fieldbackground="#8FC9AE", foreground="white")
        columns = ('c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12')

        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady = 10)
        self.tree = ttk.Treeview(self.tree_frame, column = columns, show = 'headings', height = 5, padding=10, selectmode = 'none')

        self.tree.column("# 1", anchor = CENTER, width = 80)
        self.tree.heading("# 1", text = 'Gender')
        self.tree.column("# 2", anchor = CENTER, width = 60)
        self.tree.heading("# 2", text = 'Married')

        self.tree.column("# 3", anchor = CENTER, width = 90)
        self.tree.heading("# 3", text = 'Dependents')
        self.tree.column("# 4", anchor = CENTER, width = 130)
        self.tree.heading("# 4", text = 'Education')

        self.tree.column("# 5", anchor = CENTER, width = 130)
        self.tree.heading("# 5", text = 'Self Employed')
        self.tree.column("# 6", anchor = CENTER, width = 140)
        self.tree.heading("# 6", text = 'Applicant Income')

        self.tree.column("# 7", anchor = CENTER, width = 140)
        self.tree.heading("# 7", text = 'Co-Applicant Income')
        self.tree.column("# 8", anchor = CENTER, width = 130)
        self.tree.heading("# 8", text = 'Loan Amount')

        self.tree.column("# 9", anchor = CENTER, width = 100)
        self.tree.heading("# 9", text = 'Loan Term')
        self.tree.column("# 10", anchor = CENTER, width = 90)
        self.tree.heading("# 10", text = 'Credit History')

        self.tree.column("# 11", anchor = CENTER, width = 100)
        self.tree.heading("# 11", text = 'Property Area')
        self.tree.column("# 12", anchor = CENTER, width = 100)
        self.tree.heading("# 12", text = 'Loan Status')

        self.tree.insert('', 'end', text="1", values=('Female', 'Yes', 2, 'Under-Graduate', 'Yes', 25231, 0, 190, 360, 'Yes', 'Semi-Urban', 'Approved'),\
                          tags = ('ttk'))
        self.tree.insert('', 'end', text="2", values=('Male', 'No', 1, 'Graduate', 'No', 12534, 123, 125, 300, 'No', 'Urban', 'Approved'),\
                          tags = ('ttk'))
        self.tree.insert('', 'end', text="3", values=('Female', 'No', 0, 'Graduate', 'Yes', 53231, 0, 200, 260, 'Yes', 'Urban', 'Disapproved'),\
                          tags = ('ttk'))

        self.tree.tag_configure('ttk', background = '#434242', foreground = 'white')
        self.tree.grid(row = 1)


    def toHome(self):
        self.root.destroy()
        main = MainPage()

main = MainPage()
