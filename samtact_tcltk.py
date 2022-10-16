
from tkinter import *
from turtle import bgcolor


main_window = Tk()
right_frame = Frame()
right_frame.pack(side=LEFT)
left_frame = Frame()
left_frame.pack(side=LEFT)

# right side
# add name part:
name_frame = Frame(right_frame)
name_frame.pack()
name_label = Label(name_frame, text='Full Name', width=12, height=2, bg = 'dark grey')
name_label.pack(side=LEFT, padx=10)
name_entry = Entry(name_frame, bg = 'light cyan')
name_entry.pack(side=LEFT)

#add number part:
number_frame = Frame(right_frame)
number_frame.pack()
number_label = Label(number_frame, text='Phone Number', width=12, height=2, bg = 'dark grey')
number_label.pack(side=LEFT, padx=10)
number_entry = Entry(number_frame, bg = 'light cyan')
number_entry.pack(side=LEFT)

#add birth year:
year_frame = Frame(right_frame)
year_frame.pack()
year_label = Label(year_frame, text='Birth of year', width=12, height=2, bg = 'dark grey')
year_label.pack(side=LEFT, padx=10)
year_entry = Entry(year_frame, bg = 'light cyan')
year_entry.pack(side=LEFT)

#add city of birth:
city_frame = Frame(right_frame)
city_frame.pack()
city_label = Label(city_frame, text='City of birth', width=12, height=2, bg = 'dark grey')
city_label.pack(side=LEFT, padx=10)
city_entry = Entry(city_frame, bg = 'light cyan')
city_entry.pack(side=LEFT)

#add email:
email_frame = Frame(right_frame)
email_frame.pack()
email_label = Label(email_frame, text='Email', width=12, height=2, bg = 'dark grey')
email_label.pack(side=LEFT, padx=10)
email_entry = Entry(email_frame, bg = 'light cyan')
email_entry.pack(side=LEFT)

#end of right frame

check_bottun = Checkbutton()

# left side
save_frame = Frame(left_frame)
save_frame.pack()
save_bottun = Button(save_frame, text = 'Save', width=7, height=2, bg = 'dark grey')
save_bottun.pack(padx= 10)


main_window.mainloop()