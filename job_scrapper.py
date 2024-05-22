import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_job_listings(driver, url):
    driver.get(url)
    
    job_listings = []
    
    jobs = driver.find_elements(By.CLASS_NAME, 'jobs-list')
    print(jobs,"jjjj")
    for job_element in jobs:
        job = {}
        job['job_title'] = job_element.find_element(By.CSS_SELECTOR, '.job-left-col h4.hidden-xs a').text.strip()
        job['company_name'] = job_element.find_element(By.CSS_SELECTOR, '.job-left-col .company.hidden-xs a').text.strip()
        job['job_location'] = job_element.find_element(By.CSS_SELECTOR, '.boxes .box:first-child span').text.strip()
        job['job_type'] = job_element.find_element(By.CSS_SELECTOR, '.boxes .box:nth-child(2) span').text.strip()
        job['salary'] = job_element.find_element(By.CSS_SELECTOR, '.boxes .box:nth-child(4) span').text.strip() if len(job_element.find_elements(By.CSS_SELECTOR, '.boxes .box:nth-child(4) span')) > 0 else None
        job['description_url'] = job_element.find_element(By.CSS_SELECTOR, '.job-left-col h4.hidden-xs a').get_attribute('href')
        print(job,"job")
        job_details = get_job_details(driver, job['description_url'])
        job.update(job_details)
        
        job_listings.append(job)
    
    return job_listings

def get_job_details(driver, url):
    driver.get(url)
    print(url,"URL")
    job_details = {}
    job_details['detailed_description'] = driver.find_element(By.CLASS_NAME, 'job').text.strip()
    
    company_info = driver.find_element(By.CLASS_NAME, 'job-company')
    if company_info:
        job_details['company_website'] = company_info.find_element(By.CLASS_NAME, 'job-company').get_attribute('href') if company_info.find_elements(By.CLASS_NAME, 'website') else None
        job_details['company_logo_url'] = company_info.find_element(By.CLASS_NAME, 'logo').get_attribute('src') if company_info.find_elements(By.CLASS_NAME, 'logo') else None
        job_details['company_description'] = company_info.find_element(By.CLASS_NAME, 'company-description').text.strip() if company_info.find_elements(By.CLASS_NAME, 'company-description') else None
        job_details['company_funding_info'] = company_info.find_element(By.CLASS_NAME, 'funding-info').text.strip() if company_info.find_elements(By.CLASS_NAME, 'funding-info') else None
    print(job_details,"Details")
    return job_details

def main():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    url = "https://www.workingnomads.com/jobs"
    job_listings = get_job_listings(driver, url)
    print(job_listings,"Jobs")
    print(json.dumps(job_listings, indent=2))
    
    driver.quit()

if __name__ == "__main__":
    main()
