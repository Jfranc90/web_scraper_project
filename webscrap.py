from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import sele, url
import os

def clean(linksList):
    newList  = []
    for i in linksList:
        if("/pagead/" in i):
            linko = "www.indeed.com" + i
            newList.append(linko)
    return newList


def scrapeTheWeb(titleJob):
    companies = []
    jobTitles = []
    jobLinks = []

    driver = webdriver.Chrome(ChromeDriverManager().install())
    sele.searchJob(titleJob,driver)
    searchURL = url.makeUrl(titleJob,"Los Angeles")
    driver.get(searchURL)
    driver.implicitly_wait(20)
    content = driver.page_source
    soup = BeautifulSoup(content,"html.parser")
    for i in soup.findAll('div', attrs = {"class":"jobsearch-SerpJobCard unifiedRow row result clickcard"}):
        title = i.find('a', attrs = {'class':'jobtitle turnstileLink'}).text.replace("\n","")
        company = i.find('span', attrs = {'class':'company'}).text.replace("\n","")
        #location = i.find('div', attrs = {"class" : "location accessible-contrast-color-location"}).text.replace("\n","")
        companies.append(company)
        jobTitles.append(title)

    for link in soup.findAll('a' ,target = "_blank"):
        jobLink = link.get("href")
        jobLinks.append(jobLink)

    newLinks = clean(jobLinks)

    #print(newLinks)
    #print(companies)
    #print(jobTitles)
    driver.quit()
    coSeries = pd.Series(companies, name = "Company")
    jobSeries = pd.Series(jobTitles, name = "Job Title")
    urlSeries = pd.Series(newLinks, name = "URL Link")
    df = pd.concat([coSeries,jobSeries,urlSeries], axis= 1)


# define the name of the directory to be created
    path = "/Job_CSV_Files"

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    #else:
       # print ("Successfully created the directory %s " % path)

    csvName = "/Job_CSV_Files " + titleJob + ".csv"
    df.to_csv(csvName, index=False, encoding="utf-8")

    