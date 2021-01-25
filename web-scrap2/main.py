#scrap real website
from bs4 import BeautifulSoup

import requests
import time

#search for unfamiliar skills
print('Put some skill that you are not unfamiliar with')
unfamiliar_skills = input('>')
print(f"Filtering out {unfamiliar_skills}")

#storing the search result in another file

def find_jobs():

    #use get method
    #if use .text its wil print the web source code
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    #response 200 meaning ok
    # print(html_text)

    #use beautiful soup
    #lxml is html to python parser
    soup = BeautifulSoup(html_text, 'lxml')

    #fins spesific class name in html
    # job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
    # print(job)

    #create for loop to print all jobs, compant name and date posted 

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    #this will indexing the search result in the text file use enumerate and index method
    for index, job in enumerate (jobs):


        #find spesific tag in job variable above
        #remove unnecesary space in the search result

        #filter/sort for spesific time post
        published_time = job.find('span', class_ = 'sim-posted').span.text

        #find search result in few times mode
        if 'few' in published_time:


            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')


            #adding link for the more information
            #the value meaning find from jobs variabel then go to header tag -> h2 tag -> and find <a> tag

            more_info = job.header.h2.a['href'] #filter just link only

            # job_published_day = job.find('span', class_ = 'sim-posted').text.replace(' ','')
            # print(company_name)
            # print(skills)
            # print(job_published_day)


            # # print with better view using f strings
            # print(f'''

            # Company Name : {company_name}
            # Required Skills : {skills}
            # Date Published : {published_time}

            # ''')

            #looping for infamiliar skills
            #this will print if we in[ut unfmiliar skill in input first, we will not find according from we input before
            if unfamiliar_skills not in skills:
                
                #this will store the search result in text file 
                with open(f'dump/{index}.txt', 'w') as f:

                    # print(f"company name: {company_name.strip()}")
                    # print(f"required skills: {skills.strip()}")
                    # print(f"more info: {more_info}")

                    # print('')

                    f.write(f"company name: {company_name.strip()} \n")
                    f.write(f"required skills: {skills.strip()} \n")
                    f.write(f"more info: {more_info}\n")

                print(f'file saved: {index}.txt')

                    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes.')
        time.sleep(time_wait * 60)