from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import variables
from time import sleep

page = webdriver.Firefox()
wait = WebDriverWait(page, 10)
page.get("http://www.fieldglass.net")
assert "fieldglass" in page.title
username = page.find_element_by_name("username")
password = page.find_element_by_name("password")
password.clear()
username.clear()
username.send_keys(variables.user)
password.send_keys(variables.password)
username.send_keys(Keys.RETURN)
try:
    click = wait.until(EC.presence_of_element_located((By.ID, variables.testr[0])))
finally:
    click.click()

time.sleep(5)

try:
	glob = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cSelCheckBox' and @value='{}']".format(variables.codes[0]))))
	ebonding = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cSelCheckBox' and @value='{}']".format(variables.codes[1]))))
	aws = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cSelCheckBox' and @value='{}']".format(variables.codes[2]))))
finally:
	page.implicitly_wait(5)
	ebonding.click()
	page.implicitly_wait(5)
	aws.click()
	page.implicitly_wait(5)
	glob.click()

ebonding.click()
aws.click()
glob.click()


conti = page.find_element_by_xpath("//input[@class='primaryButton' and @value='Continue']")
# glob = page.find_element_by_xpath("//input[@name='cSelCheckBox' and @value='z1611151626282762828590b&z1611181808392235474182b&z1803072201115031420892e&z16123115494271934691922&z17120617390860963784919&Wireline IT|00VZ007747~Virtual Services~PCCIO~C|23720~Global Change Management|FUNCTIONALITY TESTING & INSTALL - EXCLUDES UAT~06A~SOW_SOP~193132~5320']")
# ebonding = page.find_element_by_xpath("//input[@name='cSelCheckBox' and @value='z1611151626282762828590b&z1611181808392235474182b&z1803072201115031420892e&z16123115494271934691922&z17120617390860963784919&Wireline IT|00VZ007898~Global eBonding Deals~PCCIO~C|14815~Verizon Business Ebonding Solu|FUNCTIONALITY TESTING & INSTALL - EXCLUDES UAT~06A~SOW_SOP~193132~5320']")
# aws = page.find_element_by_xpath("//input[@name='cSelCheckBox' and @value='z1611151626282762828590b&z1611181808392235474182b&z1803072201115031420892e&z16123115494271934691922&z17120617390860963784919&Wireline IT|00VZ007942~AWS Migration (Expense)~PCCIO~E|19443~Verizon Enterprise Center|FUNCTIONALITY TESTING & INSTALL - EXCLUDES UAT~06A~SOW_EXPENSE~780025~']")




monday = t_z17102516194911574423935_b_2_r1
monday2 = t_z17102516194911574423935_b_2_r2


task = page.find_element_by_id("task_by_worker_cost_center_taskCode_sch")
# task.send_keys("proj01")
# task.send_keys(Keys.RETURN)
# task_name = page.find_element_by_id("task_by_worker_cost_center_taskName_sch")
# task_name.send_keys("wireline")
# task_name.send_keys(Keys.RETURN)


#codes = ["z1611151626282762828590b&z1611181808392235474182b&z1803072201115031420892e&z16123115494271934691922&z17120617390860963784919&Wireline IT|00VZ007747~Virtual Services~PCCIO~C|23720~Global Change Management|FUNCTIONALITY TESTING & INSTALL - EXCLUDES UAT~06A~SOW_SOP~193132~5320", "z1611151626282762828590b&z1611181808392235474182b&z1803072201115031420892e&z16123115494271934691922&z17120617390860963784919&Wireline IT|00VZ007898~Global eBonding Deals~PCCIO~C|14815~Verizon Business Ebonding Solu|FUNCTIONALITY TESTING & INSTALL - EXCLUDES UAT~06A~SOW_SOP~193132~5320", "z1611151626282762828590b&z1611181808392235474182b&z1803072201115031420892e&z16123115494271934691922&z17120617390860963784919&Wireline IT|00VZ007942~AWS Migration (Expense)~PCCIO~E|19443~Verizon Enterprise Center|FUNCTIONALITY TESTING & INSTALL - EXCLUDES UAT~06A~SOW_EXPENSE~780025~"]
# sele.send_keys("00VZ007747")
# sele.send_keys(Keys.ARROW_DOWN)
# sele.send_keys(Keys.RETURN)