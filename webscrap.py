from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import sele, url

companies = []
jobTitles = []
location = []
monies = []

userJob = input("What type of job are you looking for? ")
driver = webdriver.Chrome(ChromeDriverManager().install())
sele.searchJob(userJob,driver)
searchURL = url.makeUrl(userJob,"Los Angeles")
driver.get(searchURL)
driver.implicitly_wait(20)
content = driver.page_source
soup = BeautifulSoup(content,"html.parser")
for i in soup.findAll('div', attrs = {"class":"jobsearch-SerpJobCard unifiedRow row result clickcard"}):
    title = i.find('a', attrs = {'class':'jobtitle turnstileLink'}).text.replace("\n","")
    company = i.find('span', attrs = {'class':'company'}).text.replace("\n","")
    #salary = i.find('div', attrs = {'class':'salarySnippet holisticSalary'}).text.replace("\n","")
    loc =  i.find('div', attrs = {'class':'sjcl'}).text.replace('\n',"")
    #company = companySpan
    companies.append(company)
    jobTitles.append(title)
    #monies.append(salary)
    location.append(loc)

    
print(companies)
print(jobTitles)
#print(monies)
print(location)