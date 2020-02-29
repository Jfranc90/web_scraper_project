def makeUrl(job,location):
    basicUrl = "https://www.indeed.com/jobs?q="
    jobList = job.split()
    locationList = location.split()

    if(len(jobList) > 1):
        for i in range(len(jobList)):
            if(i == (len(jobList) - 1)):
                basicUrl = basicUrl + jobList[i]
            else:
                basicUrl = basicUrl + jobList[i] + "+"
    else:
        basicUrl = basicUrl + job

    basicUrl = basicUrl + "&l="

    if(len(locationList) > 1):
        for i in range(len(locationList)):
            if(i == (len(locationList) - 1)):
                basicUrl = basicUrl + locationList[i]
            else:
                basicUrl = basicUrl + locationList[i] + "+"
    else:
        basicUrl = basicUrl + location
    
    basicUrl = basicUrl + "%2C+CA"
    
    return basicUrl