import requests
from bs4 import BeautifulSoup

url='https://ca.indeed.com/jobs?q=software+developer&l=Toronto%2C+ON'
response=requests.get(url)

soup=BeautifulSoup(response.content,'html.parser')

job_titles=soup.find_all('div',class_='jobsearch-SerpJobCard')




print('Here are current jobs being offered')

for job_title in job_titles:
    job=job_title.find('h2',class_='title')
    pay=job_title.find('span',class_='salaryText')
    location=job_title.find('div',class_='location accessible-contrast-color-location')
    company=job_title.find('span',class_='company')

    if None in (job,pay,location,company):
        continue


    print(job.text.strip())
    print(pay.text.strip())
    print(location.text.strip())
    print(company.text.strip())
    print()



