from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import variables
import re
import Tkinter as tk
from time import sleep


def fill_time(page, day_off):
    print(day_off)
    wait = WebDriverWait(page, 5)
    page.get("http://www.fieldglass.net")

    page.find_element_by_name("username").send_keys(variables.user)
    page.find_element_by_name("password").send_keys(variables.password)
    page.find_element_by_name("password").send_keys(Keys.RETURN)
    wait.until(EC.presence_of_element_located((By.ID, "ts_0"))).click()
    try:
        page.maximize_window()
        page.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        page.find_element_by_xpath(
            "(//input[@name='cSelCheckBox'])[7]").click()
        page.find_element_by_xpath(
            "(//input[@name='cSelCheckBox'])[5]").click()
        page.find_element_by_xpath(
            "(//input[@name='cSelCheckBox'])[6]").click()
    finally:
        page.find_element_by_xpath(
            "//input[@class='primaryButton' and @value='Continue']").click()
    for n in range(1, 4):
        project = re.findall(r"[\w']+", page.find_element_by_xpath(
            "(//div[@class='sodLabel fl'])[{}]".format(str(n))).text)[3]
        for day in variables.weekday.keys():
            if day in day_off:
                page.find_element_by_id(
                    variables.get_day_cell_id(day, n)).send_keys(0)
                continue
            page.find_element_by_id(variables.get_day_cell_id(
                day, n)).send_keys(variables.hours[project][day])
    page.find_element_by_id("fgTSSubmit").click()


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

        for key in sorted(self.daysDic, key=self.daysDic.__getitem__):
            self.daysDic[key] = tk.IntVar()
            aCheckButton = tk.Checkbutton(self, text=key,
                                          variable=self.daysDic[key])
            aCheckButton.grid(sticky='w')
            self.daysDic[key].set(1)

        submitButton = tk.Button(self, text="Submit",
                                 command=self.query_checkbuttons)
        submitButton.grid(row=5, column=0)
        tk.Button(self, text='Quit', command=self.quit).grid(row=5, column=1)

    def query_checkbuttons(self):
        day_off = []
        for key, value in self.daysDic.items():
            state = value.get()
            if state != 1:
                day_off.append(key)
                self.daysDic[key].set(0)
        fill_time(webdriver.Chrome(), day_off)
        sleep(30)
        self.quit()


def main():
    gui = GUI()
    gui.geometry("250x150")
    gui.title("Auto-Fill fieldglass")
    gui.mainloop()


if __name__ == '__main__':
    main()
