from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def searchJob(userJob, driv):
    #driv
    driv.implicitly_wait(20)
    driv.get("https://www.indeed.com/?from=gnav-jobsearch--jasx")

    search = userJob
    textBox = driv.find_element_by_id("text-input-what")
    textBox.send_keys(search)
    buttonDriver = driv.find_element_by_css_selector(".icl-WhatWhere-buttonWrapper .icl-Button--primary")
    buttonDriver.click()

#driver.quit()