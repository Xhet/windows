#!/usr/bin/python3

# from tkinter import *
# class Checkbar(Frame):
#    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
#       Frame.__init__(self, parent)
#       self.vars = []
#       for pick in picks:
#          var = IntVar()
#          chk = Checkbutton(self, text="pick", variable=var)
#          chk.pack(side=side, anchor=anchor, expand=YES)
#          self.vars.append(var)
# #    def state(self):
# #       return map((lambda var: var.get()), self.vars)
# # if __name__ == '__main__':
# #    root = Tk()
# #    lng = Checkbar(root, ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
# #    tgl = Checkbar(root, ['English','German'])
# #    lng.pack(side=TOP,  fill=X)
# #    tgl.pack(side=LEFT)
# #    lng.config(relief=GROOVE, bd=2)

# #    def allstates(): 
# #       print(list(lng.state()), list(tgl.state()))
# #    Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
# #    Button(root, text='Peek', command=allstates).pack(side=RIGHT)
# #    root.mainloop()


# root = Tk()

# def command():
#     print(lng.cget("text"))
# lng = Checkbar(root, ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
# checkbutton = Checkbutton(root, text="Retrieve This Text")
# button = Button(root, text="Ok", command=command)
# lng.pack(side=TOP, fill=X)
# checkbutton.pack()
# button.pack()
# lng.config(relief=GROOVE, bd=2)
# root.mainloop()


import tkinter as tk

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.daysDic = {
        'monday':0,
        'tuesday':0,
        'wednesday':0,
        'thursday':0,
        'friday':0
        }

        for key in self.daysDic:
            self.daysDic[key] = tk.IntVar()
            aCheckButton = tk.Checkbutton(self, text=key,
                                            variable=self.daysDic[key])
            aCheckButton.grid(sticky='w')

        submitButton = tk.Button(self, text="Submit",
                                        command=self.query_checkbuttons)
        submitButton.grid()
        tk.Button(self, text='Quit', command=self.quit).grid()

    def multiple(self):
        print(non)
        self.quit
    def query_checkbuttons(self):
        non = []
        for key, value in self.daysDic.items():
            state = value.get()           
            if state != 0:
                non.append(key)
                print(key)
                self.daysDic[key].set(0)
                print(non)
        print(non)
        self.quit



gui = GUI()
gui.mainloop()