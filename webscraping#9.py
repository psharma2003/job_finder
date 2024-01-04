from bs4 import BeautifulSoup
import requests
import time
print("put some skill that you are not familiar with")
unfamiliar_skill=input('>')
print(f'filtering out the skill that user doesnt have{unfamiliar_skill}')

def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        publish_date = job.find('span', class_='sim-posted').span.text
        if 'few' in publish_date:  # to filter jobs that weere posted a few days ago
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')

            # more_info_about_a_job=job.header.h2.a#a tag is inside h2 h2 is inside header .we want to
            # fetch the link to give us job description
            more_info_about_a_job = job.header.h2.a['href']  # now we will only see link not the tag
            if unfamiliar_skill not in skills:
                print(f"company name:{company_name.strip()}")

                print(f"required skills:{skills.strip()}")
                print(f"job description:{more_info_about_a_job}")

                print('')


if __name__=='__main__':
  while True:
    find_jobs()
     #   time_wait=10
     # print(f"waiting {time_wait} seconds...")
        #time.sleep(time_wait)#to wait a certain amt of time



#this fucntion will execute only if this file is ran directly