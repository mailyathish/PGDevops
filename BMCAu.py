from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains	
from selenium.webdriver.support.ui import Select
import time
import sys
import os  # 43702465. 9980207796. 9148096596

file = open("Incident.txt","r")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get('http://jwebhome.jcpenney.com/')
time.sleep(12)
driver.get('http://itsmweb.jcpenney.com/arsys/forms/itsmapps/SRS:ServiceRequestConsole')
driver.find_element_by_id("username-id").click()
driver.find_element_by_id("username-id").clear()
driver.find_element_by_id("username-id").send_keys("kdevegow")
driver.find_element_by_id("pwd-id").clear()
driver.find_element_by_id("pwd-id").send_keys("Mypassword6.")
driver.find_element_by_id("login").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@id='WIN_0_303053400']/div").click()
driver.find_element_by_xpath("//a[@id='WIN_0_304324300']/div/div").click()
time.sleep(5)
alert = Alert(driver)
alert.accept()
time.sleep(10)

for line in file:
	
	driver.find_element_by_id("arid_WIN_0_302258625").click()
	driver.find_element_by_id("arid_WIN_0_302258625").clear()
	driver.find_element_by_id("arid_WIN_0_302258625").send_keys(line)
	time.sleep(10)
	print(line)
	#driver.find_element_by_xpath("//a[@id='WIN_0_302259032']/div").click()
	time.sleep(20)
	#source=driver.find_element_by_id("//*[@id='arid_WIN_3_302300623']")
	#print(source)
	#source= driver.find_element_by_xpath("//div[@id='WIN_0_304255802']/fieldset/div/div")
	source= driver.find_element_by_xpath("//table[@id='T1000003952']/tbody/tr[2]/td[3]/nobr/span")
	#print(source)
	action = ActionChains(driver)
	action.double_click(source).perform()
	time.sleep(20)
	driver.find_element_by_xpath("//*[@id='WIN_4_7']/div").click()
	driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Resolved'])[1]/following::td[2]").click()
	driver.find_element_by_id("arid_WIN_4_7").send_keys("Closed")
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='WIN_4_1000000881']").click()
	#driver.find_element_by_id("arid_WIN_4_1000000881").click()
	time.sleep(2)
	driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Infrastructure Change Created'])[1]/following::td[2]").click()
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000000881").send_keys("Automated Resolution Reported")
	time.sleep(2)
	driver.find_element_by_id("arid_WIN_4_1000000156").click()
	driver.find_element_by_id("arid_WIN_4_1000000156").send_keys("Issue has been resolved")
	time.sleep(2)
	driver.find_element_by_link_text("Categorization").click()
	driver.find_element_by_xpath("//a[@id='WIN_4_304287770']/div/div").click()
	driver.find_element_by_id("arid_WIN_4_1000002488").send_keys("Batch Processing")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003889").send_keys("UNIX")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003890").send_keys("Application Erorr")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003891").send_keys("Software")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003892").send_keys("Application")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003893").send_keys("Other")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003894").send_keys("Active Directory Janitor")
	time.sleep(1)
	driver.find_element_by_id("arid_WIN_4_1000003895").send_keys("1.2")
	time.sleep(5)
	driver.find_element_by_xpath("//a[@id='WIN_4_301614800']/div/div").click()
	time.sleep(20)
	driver.find_element_by_xpath("//*[@id='WIN_0_304248710']/fieldset/div/dl/dd[3]/span[2]/a").click()
	time.sleep(5)
driver.find_element_by_xpath("//a[@id='WIN_0_300000044']/div/div").click()



"""

//*[@id="arid_WIN_4_1000000881"]


select = Select(driver.find_element_by_xpath("//*[@id='WIN_4_7']/div").click())
select.select_by_visilbe_test('Closed')



driver.find_element_by_xpath("//*[@id='WIN_4_7']/div").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Resolved'])[1]/following::td[2]").click()
driver.find_element_by_id("arid_WIN_4_7").clear()
driver.find_element_by_id("arid_WIN_4_7").send_keys("Closed")
driver.find_element_by_id("arid_WIN_4_7").clear()
driver.find_element_by_id("arid_WIN_4_7").send_keys("Closed")


//*[@id="arid_WIN_4_1000000881"]

"""



"""

//*[@id = 'WIN_0_304255502'

//*[@id="T1000003952"]/tbody/tr[2]/td[3]/nobr/span/b/span

//*[@id="T1000003952"]/tbody/tr[2]/td[3]/nobr/span/b/span

//*[@id="arid_WIN_3_302300623"]



//*[@id="T1000003952"]/tbody/tr[2]/td[1]/nobr/span



//*[@id="arid_WIN_3_302300623"]

"""