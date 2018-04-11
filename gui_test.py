#!/usr/bin/python3
import pdb
import tkinter as tk


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.daysDic = {
            'monday': 1,
            'tuesday': 2,
            'wednesday': 3,
            'thursday': 4,
            'friday': 5
        }
        # pdb.set_trace()
        for key in sorted(self.daysDic, key=self.daysDic.__getitem__):
            self.daysDic[key] = tk.IntVar()
            aCheckButton = tk.Checkbutton(
                self, text=key, variable=self.daysDic[key])
            aCheckButton.grid(sticky='w')
            self.daysDic[key].set(0)

        submitButton = tk.Button(self, text="Submit",
                                 command=self.query_checkbuttons)
        submitButton.grid()
        tk.Button(self, text='Quit', command=self.quit).grid()

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
