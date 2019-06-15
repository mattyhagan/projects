'''
Matty Hagan
Summer Camp Form
ICS 3U1 Performance Task
'''

#imports
from tkinter import *
from tkinter import messagebox

#lists
global names, birthdays, genders, info, parent1names, parent1phone, parent1email, parent1relationship, parent2names, parent2phone, parent2email, parent2relationship, weeks
names = []
birthdays = [] #in m/d/y format
genders = []
info = []
parent1names = []
parent1phone = []
parent1email = []
parent1relationship = []
parent2names = []
parent2phone = []
parent2email = []
parent2relationship = []
weeksChild = []

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9']
yearList = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
dayList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
dayListFeb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
dayListFebLeapYear = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
dayListThirtyDays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
monthList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
relationshipList = ['Mother', 'Father', 'Other']
relationshipList2 = ['Mother', 'Father', 'Other', 'n/a']

#functions
def birthdayList(*args):
    if birthdayMonthVar.get() == 2 and birthdayYearVar.get() not in [2008, 2012]:#leap years
        if birthdayDayVar.get() > 28:
            birthdayDayVar.set(28)
        birthdayDayMenuNew = OptionMenu(camperInfoFrame, birthdayDayVar, *dayListFeb)
        birthdayDayMenuNew.grid(row = 2, column = 3, padx = 8, sticky=W)
    elif birthdayMonthVar.get() == 2:
        if birthdayDayVar.get() > 29:
            birthdayDayVar.set(29)
        birthdayDayMenuNew = OptionMenu(camperInfoFrame, birthdayDayVar, *dayListFebLeapYear)
        birthdayDayMenuNew.grid(row = 2, column = 3, padx = 8, sticky=W)
    elif birthdayMonthVar.get() not in [1, 3, 5, 7, 8, 10, 12]:
        if birthdayDayVar.get() > 30:
            birthdayDayVar.set(30)
        birthdayDayMenuNew = OptionMenu(camperInfoFrame, birthdayDayVar, *dayListThirtyDays)
        birthdayDayMenuNew.grid(row = 2, column = 3, padx = 8, sticky=W)
    else:
        birthdayDayMenuNew = OptionMenu(camperInfoFrame, birthdayDayVar, *dayList)
        birthdayDayMenuNew.grid(row = 2, column = 3, padx = 8, sticky=W)

def activateEntry():
    if genderVar.get() == 'Other':
        genderOtherEntry.config(state = 'normal')
    else:
        genderOtherEntry.config(state = 'disabled')

def deactivateEntries(*args):
    if relationshipVar2.get() == 'n/a':
        parentNameEntry2.config(state = 'disabled')
        phoneEntry2.config(state = 'disabled')
        emailEntry2.config(state = 'disabled')
    else:
        parentNameEntry2.config(state = 'normal')
        phoneEntry2.config(state = 'normal')
        emailEntry2.config(state = 'normal')

def weekCount(weeks):
    sum = 0
    for week in weeks:
        if week != '':
            sum +=1
    if sum > 5 or sum == 0:
        return False
    else:
        return True

def weekSelection(weeks):
    weekList = []
    for week in weeks:
        if week != '':
            weekList.append(f'week {week}')
    return weekList

def formCheck():
    if camperNameVar.get() == '' or ' ' not in camperNameVar.get():
        messagebox.showwarning('Invalid entry', 'Please enter the first and last name of the camper')
    elif parentNameVar.get() == '' or ' ' not in parentNameVar.get():
        messagebox.showwarning('Invalid entry', 'Please enter the first and last name of the first parent/guardian')
    elif phoneVar.get() == '' or phoneVar.get().isdigit() == False:
        messagebox.showwarning('Invalid entry', 'Please enter the phone number of the first parent/guardian (numbers only).')
    elif emailVar.get() == '' or '@' not in emailVar.get() or '.' not in emailVar.get():
        messagebox.showwarning('Invalid entry', 'Please enter a valid email for the first parent/guardian.')
    elif relationshipVar.get() ==  '':
        messagebox.showwarning('Invalid entry', 'Please select campers relationship to the first parent/guardian.')
    elif weekCount([weekVar1.get(), weekVar2.get(), weekVar3.get(), weekVar4.get(), weekVar5.get(), weekVar6.get(), weekVar7.get(), weekVar8.get(), weekVar9.get()]) == False:
        messagebox.showwarning('Invalid entry', 'Please enter a valid number of weeks (1-5)')
    elif relationshipVar2.get() != 'n/a':
        if parentNameVar2.get() == '' or ' ' not in parentNameVar2.get():
            messagebox.showwarning('Invalid entry', 'Please enter the first and last name of the second parent/guardian or select \'n/a\' under \'Relationship to Camper\' ')
        elif phoneVar2.get() == '' or phoneVar2.get().isdigit() == False:
            messagebox.showwarning('Invalid entry', 'Please enter the phone number of the second parent/guardian (numbers only) or select \'n/a\' under \'Relationship to Camper\'')
        elif emailVar2.get() == '' or '@' not in emailVar2.get() or '.' not in emailVar2.get():
            messagebox.showwarning('Invalid entry', 'Please enter a valid email for the second parent/guardian or select \'n/a\' under \'Relationship to Camper\'')
        elif relationshipVar2.get() ==  '':
            messagebox.showwarning('Invalid entry', 'Please select campers relationship to the second parent/guardian.')
        else:
            confirmForm()
    else:
        confirmForm()

def confirmForm():     
    confirmation = messagebox.askyesno('Confirmation', 'Are you sure you would like to register this camper?')
    if confirmation == True:
        register()
        messagebox.showinfo('Success', f'You have successfully registered {camperNameVar.get()}')
        clearForm()

def register():
    names.append(camperNameVar.get())
    nameListVar.set(names)
    birthdays.append([birthdayMonthVar.get(), birthdayDayVar.get(), birthdayYearVar.get()])
    if genderVar.get() == 'Other' and genderVar.get() != '':
        gender = genderOtherEntryVar.get()
    else:
        gender = genderVar.get()
    genders.append(gender)
    info.append(additionalInfoEntry.get("1.0", 'end-1c'))
    parent1names.append(parentNameVar.get())
    parent1phone.append(phoneVar.get())
    parent1email.append(emailVar.get())
    parent1relationship.append(relationshipVar.get())
    parent2names.append(parentNameVar2.get())
    parent2phone.append(phoneVar2.get())
    parent2email.append(emailVar2.get())
    parent2relationship.append(relationshipVar2.get())
    weekListChild = weekSelection([weekVar1.get(), weekVar2.get(), weekVar3.get(), weekVar4.get(), weekVar5.get(), weekVar6.get(), weekVar7.get(), weekVar8.get(), weekVar9.get()])
    weeksChild.append(weekListChild)   

def clearForm():
    camperNameVar.set('')
    birthdayMonthVar.set(1)
    birthdayDayVar.set(1)
    birthdayYearVar.set(2007)
    genderOtherEntryVar.set('')
    parentNameVar.set('')
    phoneVar.set('')
    emailVar.set('')
    relationshipVar.set('')
    parentNameVar2.set('')
    phoneVar2.set('')
    emailVar2.set('')
    relationshipVar2.set('')
    weekVar1.set('')
    weekVar2.set('')
    weekVar3.set('')
    weekVar4.set('')
    weekVar5.set('')
    weekVar6.set('')
    weekVar7.set('')
    weekVar8.set('')
    weekVar9.set('')
    additionalInfoEntry.delete('1.0', END)

def showChildren(*event):
    tupleIndex = weekBox.curselection()
    index = tupleIndex[0]

    childrenInWeek = []
    if weeksChild != []:
        for list in weeksChild:
            if f'week {index+1}' in list:
                childrenInWeek.append(names[weeksChild.index(list)])
        if childrenInWeek == []:
            messagebox.showinfo('Week view', f'There is no one registered in week {index+1}.')
        else:
            weekInfoString = f''
            nameSum = 0
            for name in childrenInWeek:
                
                if name == childrenInWeek[-1]:
                    weekInfoString += f'{name} '
                elif name == childrenInWeek[-2]:
                    weekInfoString += f'{name}, and '
                else:
                    weekInfoString += f'{name}, '
                nameSum +=1
            
            
            if nameSum > 1:
                weekInfoString += 'are'
            else:
                weekInfoString += 'is'

            messagebox.showinfo('Week view', f'{weekInfoString} registered in week {index+1}.')
            
    else:
        messagebox.showinfo('Week view', f'There is no one registered in week {index+1}.')

def showChildInfo(*event):
    try:
        tupleIndex = nameBox.curselection()
        index = tupleIndex[0]
    except:
        messagebox.showerror('Error', 'Please select a child name')
    else:
        if genders[index] == 'M':
            pronouns = ['him', 'His']
        elif genders[index] == 'F':
            pronouns = ['her', 'Her']
        else:
            pronouns = ['them', 'Their']
            
        weekString = f'{names[index]} is registered for '

        for week in weeksChild[index]:
            if week == weeksChild[index][-1]:
                weekString += f'{week}.'
            elif week == weeksChild[index][-2]:
                weekString += f'{week}, and '
            else:
                weekString += f'{week}, '
        if info[index] != '':
            infoString = f'Additional info for {pronouns[0]} is:\n{info[index]}.\n{pronouns[1]} date of birth is {getBirthdayString(index)}'
        else:
            infoString = ''

        parent1relationshipString = getParentRelationship(index, 1)
        
        if parent2relationship[index] != 'n/a':
            parent2relationshipString = getParentRelationship(index, 2)
            if parent1relationshipString == parent2relationshipString:
                parent2String = f'{pronouns[1]} other {parent2relationshipString}\'s name is {parent2names[index]}, their phone number is {parent2phone[index]} and their email is {parent2email[index]}.'
            else:
                parent2String = f'{pronouns[1]} {parent2relationshipString}\'s name is {parent2names[index]}, their phone number is {parent2phone[index]} and their email is {parent2email[index]}.'
        else:
            parent2String = ''

        parentString = f'{pronouns[1]} {parent1relationshipString}\'s name is {parent1names[index]}, their phone number is {parent1phone[index]} and their email is {parent1email[index]}.'
        messagebox.showinfo(f'{names[index]} Info', f'{weekString} {infoString}\n{parentString}\n{parent2String}')

def getParentRelationship(index, parent):
    if parent == 1:
        relationshipList = parent1relationship
    else:
        relationshipList = parent2relationship
    if relationshipList[index] == 'Mother':
        return 'mother'
    elif relationshipList[index] == 'Father':
        return 'father'
    else:
        return 'guardian'

def getBirthdayString(index):
    birthdays[index]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    days = []
    for number in range(1, 32):
        if number in [1, 21, 31]:
            days.append(f'{number}st')
        elif number in [2, 22]:
            days.append(f'{number}nd')
        else:
            days.append(f'{number}th')
    
    monthIndex = birthdays[index][0] - 1
    dayIndex = birthdays[index][1] - 1
    
    birthdayString = f'{months[monthIndex]} {days[dayIndex]} {birthdays[index][2]}'
    return birthdayString
    
def deleteChild():

    try:
        tupleIndex = nameBox.curselection()
        index = tupleIndex[0]
    except:
        messagebox.showerror('Error', 'Please select a camper name in the list box')
    else:
        childName = names[index]

        names.pop(index)
        birthdays.pop(index)
        genders.pop(index)
        info.pop(index)
        parent1names.pop(index)
        parent1phone.pop(index)
        parent1email.pop(index)
        parent1relationship.pop(index)
        parent2names.pop(index)
        parent2phone.pop(index)
        parent2email.pop(index)
        parent2relationship.pop(index)
        weeksChild.pop(index)

        nameListVar.set(names)
        messagebox.showinfo('Camper deleted', f'{childName} has been deleted from the camper registry.')



#frames
root = Tk()
root.title('Summer Day Camp 2019 Registration')
root.iconbitmap(r'ontarioIcon.ico')

mainframe = Frame(root)
introFrame = Frame(root)
camperInfoFrame = LabelFrame(root, text = 'Camper Info')
parentFrame = LabelFrame(root, text = 'Parent/Guardian 1')
parentFrame2 = LabelFrame(root, text = 'Parent/Guardian 2')
weekFrame = LabelFrame(root, text = 'Weeks of Camp(5 max)')
listBoxFrame = Frame(root)
registerFrame = Frame(root)

#widgets
titleLabel = Label(introFrame, text = 'SUMMER DAY CAMP 2019 REGISTRATION', font=('Arial 12 bold'))
descriptionLabel = Label(introFrame, font = ('Arial', 8), text = 'Day camp registration forms can be dropped off at the Kiwanis BGC location from June 11 – June 22; all \nforms received during this period will be processed after June 23, 2019\n\n\n- Forms will be accepted between the hours of 9:00 am – 9:00 pm Monday – Friday and 9:00 am – 4:00 pm on Saturday\n\n- Forms will not be accepted between June 25 - 29\n\n- Starting July 1, registration for the remaining spots will be available on a first come, first serve basis\n\n- Payment will be accepted by pre-authorized payments, debit, credit or cash\n\n- Communication regarding camp acceptance will be made through email or phone')
noteLabel = Label(introFrame, font = ('Arial', 8, 'italic'), text = '*note: If there is no second guardian, select \'n/a\' under \'Relationship to Camper\'')


fullNameLabel = Label(camperInfoFrame, text = 'Full Name:')
camperNameVar = StringVar()
camperNameEntry = Entry(camperInfoFrame, textvariable = camperNameVar)

birthdayLabel = Label(camperInfoFrame, text = 'Birthday(m/d/y):')
birthdayYearVar = IntVar()
birthdayYearVar.set(2007)
birthdayYearMenu = OptionMenu(camperInfoFrame, birthdayYearVar, *yearList, command = birthdayList)
birthdayDayVar = IntVar()
birthdayDayVar.set(1)
birthdayDayMenu = OptionMenu(camperInfoFrame, birthdayDayVar, *dayList)
birthdayMonthVar = IntVar()
birthdayMonthVar.set(1)
birthdayMonthMenu = OptionMenu(camperInfoFrame, birthdayMonthVar, *monthList, command = birthdayList)

genderVar = StringVar()
genderVar.set('M')
genderLabel = Label(camperInfoFrame, text = 'Gender:')
genderMale = Radiobutton(camperInfoFrame, text = 'M', variable = genderVar, value = 'M', command = activateEntry)
genderFemale = Radiobutton(camperInfoFrame, text = 'F', variable = genderVar, value = 'F', command = activateEntry)
genderOther = Radiobutton(camperInfoFrame, text = 'Other:', variable = genderVar, value = 'Other', command = activateEntry)
genderOtherEntryVar = StringVar()
genderOtherEntry = Entry(camperInfoFrame, state = 'disabled', textvariable = genderOtherEntryVar)

additionalInfoLabel = Label(camperInfoFrame, text = 'Additional info (allergies, restricted activities, medications, behavioural, etc.):')
additionalInfoEntry = Text(camperInfoFrame, height = 5, font=('Arial'), wrap = 'word')

parentNameVar = StringVar()
parentNameLabel = Label(parentFrame, text = 'Full Name:')
parentNameEntry = Entry(parentFrame, textvariable = parentNameVar)

phoneVar = StringVar()
phoneLabel = Label(parentFrame, text = 'Phone:')
phoneEntry = Entry(parentFrame, textvariable = phoneVar)

emailVar = StringVar()
emailLabel = Label(parentFrame, text = 'Email:')
emailEntry = Entry(parentFrame, textvariable = emailVar)

relationshipVar = StringVar()
relationshipLabel = Label(parentFrame, text = 'Relationship to camper:')
relationshipMenu = OptionMenu(parentFrame, relationshipVar, *relationshipList)


parentNameVar2 = StringVar()
parentNameLabel2 = Label(parentFrame2, text = 'Full Name:')
parentNameEntry2 = Entry(parentFrame2, textvariable = parentNameVar2)

phoneVar2 = StringVar()
phoneLabel2 = Label(parentFrame2, text = 'Phone:')
phoneEntry2 = Entry(parentFrame2, textvariable = phoneVar2)

emailVar2 = StringVar()
emailLabel2 = Label(parentFrame2, text = 'Email:')
emailEntry2 = Entry(parentFrame2, textvariable = emailVar2)

relationshipVar2 = StringVar()
relationshipLabel2 = Label(parentFrame2, text = 'Relationship to camper:')
relationshipMenu2 = OptionMenu(parentFrame2, relationshipVar2, *relationshipList2, command = deactivateEntries)

weekVar1 = StringVar()
weekVar2 = StringVar()
weekVar3 = StringVar()
weekVar4 = StringVar()
weekVar5 = StringVar()
weekVar6 = StringVar()
weekVar7 = StringVar()
weekVar8 = StringVar()
weekVar9 = StringVar()
weekCheck1 = Checkbutton(weekFrame, text = 'Week 1', variable = weekVar1, onvalue = '1', offvalue = '')
weekCheck2 = Checkbutton(weekFrame, text = 'Week 2', variable = weekVar2, onvalue = '2', offvalue = '')
weekCheck3 = Checkbutton(weekFrame, text = 'Week 3', variable = weekVar3, onvalue = '3', offvalue = '')
weekCheck4 = Checkbutton(weekFrame, text = 'Week 4', variable = weekVar4, onvalue = '4', offvalue = '')
weekCheck5 = Checkbutton(weekFrame, text = 'Week 5', variable = weekVar5, onvalue = '5', offvalue = '')
weekCheck6 = Checkbutton(weekFrame, text = 'Week 6', variable = weekVar6, onvalue = '6', offvalue = '')
weekCheck7 = Checkbutton(weekFrame, text = 'Week 7', variable = weekVar7, onvalue = '7', offvalue = '')
weekCheck8 = Checkbutton(weekFrame, text = 'Week 8', variable = weekVar8, onvalue = '8', offvalue = '')
weekCheck9 = Checkbutton(weekFrame, text = 'Week 9', variable = weekVar9, onvalue = '9', offvalue = '')


nameListVar = StringVar(value = names)
nameBox = Listbox(listBoxFrame, height = 6, listvariable = nameListVar)
nameBox.bind('<Double-Button-1>', showChildInfo)
nameScroller = Scrollbar(listBoxFrame, orient = VERTICAL, command = nameBox.yview)
nameBox.config(yscrollcommand=nameScroller.set)

weekBox = Listbox(listBoxFrame, height = 6)
weekBox.bind('<Double-Button-1>', showChildren)
for item in weeks:
    weekBox.insert(END, item)
weekScroller = Scrollbar(listBoxFrame, orient = VERTICAL, command = weekBox.yview)
weekBox.config(yscrollcommand=weekScroller.set)

viewButton = Button(listBoxFrame, text = 'View camper', command = showChildInfo)
deleteButton = Button(listBoxFrame, text = 'Delete camper', command = deleteChild)

registerButton = Button(registerFrame, text = 'Register', command = formCheck)

#grid
mainframe.grid(padx = 10, pady = 10)
introFrame.grid(row = 1, column = 1, rowspan = 2)
camperInfoFrame.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = W)
parentFrame.grid(row = 1, column = 2, padx = 10, pady = 10)
parentFrame2.grid(row = 2, column = 2, padx = 10, pady = 10)
weekFrame.grid(row = 3, column = 2, padx = 10, pady = 10, sticky = W+N+S+E)
registerFrame.grid(row = 4, column = 2, padx = 10, pady = 10, sticky = W+E)
listBoxFrame.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = W+E)


titleLabel.grid(row = 2, column = 1, columnspan = 3, pady = 20)
descriptionLabel.grid(row = 3, column = 1, columnspan = 3)
noteLabel.grid(row = 4, column = 1, columnspan = 3)


fullNameLabel.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)
camperNameEntry.grid(row = 1, column = 2, columnspan = 4, padx = 10, pady = 5, sticky = W+E)

birthdayLabel.grid(row = 2, column =1, padx = 10, pady = 5, sticky = W)
birthdayMonthMenu.grid(row = 2, column = 2, padx = 8, pady = 5, sticky=W)
birthdayDayMenu.grid(row = 2, column = 3, padx = 8, pady = 5, sticky=W)
birthdayYearMenu.grid(row = 2, column = 4, padx = 8, pady = 5, sticky=W)

genderLabel.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)
genderMale.grid(row = 3, column = 2, padx = 8, pady = 5, sticky = W)
genderFemale.grid(row = 3, column = 3, padx = 8, pady = 5, sticky = W)
genderOther.grid(row = 3, column = 4, padx = 8, pady = 5, sticky = W)
genderOtherEntry.grid(row = 3, column = 5, pady = 5, sticky = W)

additionalInfoLabel.grid(row = 4, column = 1, columnspan = 5, padx = 10, pady = 5, sticky = W)
additionalInfoEntry.grid(row = 5, column = 1, rowspan = 2, columnspan = 5, padx = 10, pady = 10, sticky = W)


parentNameLabel.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)
parentNameEntry.grid(row = 1, column = 2, padx = 8, pady = 5, sticky = W)

phoneLabel.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)
phoneEntry.grid(row = 2, column = 2, padx = 8, pady = 5, sticky = W)

emailLabel.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)
emailEntry.grid(row = 3, column = 2, padx = 8, pady = 5, sticky = W)

relationshipLabel.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)
relationshipMenu.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = W+E)


parentNameLabel2.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)
parentNameEntry2.grid(row = 1, column = 2, padx = 8, pady = 5, sticky = W)

phoneLabel2.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)
phoneEntry2.grid(row = 2, column = 2, padx = 8, pady = 5, sticky = W)

emailLabel2.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)
emailEntry2.grid(row = 3, column = 2, padx = 8, pady = 5, sticky = W)

relationshipLabel2.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)
relationshipMenu2.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = W+E)


weekCheck1.grid(row = 1, column = 1, padx = 30, pady = 10)
weekCheck2.grid(row = 2, column = 1, padx = 30, pady = 10)
weekCheck3.grid(row = 3, column = 1, padx = 30, pady = 10)
weekCheck4.grid(row = 4, column = 1, padx = 30, pady = 10)
weekCheck5.grid(row = 5, column = 1, padx = 30, pady = 10)
weekCheck6.grid(row = 1, column = 2, padx = 30, pady = 10)
weekCheck7.grid(row = 2, column = 2, padx = 30, pady = 10)
weekCheck8.grid(row = 3, column = 2, padx = 30, pady = 10)
weekCheck9.grid(row = 4, column = 2, padx = 30, pady = 10)


nameBox.grid(row = 1, column = 3)
nameScroller.grid(row = 1, column = 4, sticky = N+S)
weekBox.grid(row = 1, column = 1)
weekScroller.grid(row = 1, column = 2, sticky = N+S)


viewButton.grid(row = 1, column = 5, rowspan = 2, padx = 30, ipady = 2, ipadx = 4)
deleteButton.grid(row = 1, column = 6, rowspan = 2, ipady = 2, ipadx = 4)

registerButton.pack(ipadx = 66, ipady = 7)

root.mainloop
