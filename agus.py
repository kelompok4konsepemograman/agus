button6 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button6))
button6.grid(row=2, column=2,sticky = S+N+E+W)
button7 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button7))
button7.grid(row=3, column=0,sticky = S+N+E+W)
button8 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button8))
button8.grid(row=3, column=1,sticky = S+N+E+W)
button9 = Button(tk,text=" ",font=('Times 26 bold'), heigh = 4, width = 8, command=lambda:checker(button9))
button9.grid(row=3, column=2,sticky = S+N+E+W)
tk.mainloop()