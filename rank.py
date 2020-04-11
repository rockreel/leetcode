from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def get_score(pos, n):
    if n == 0:
        return 0
    z = 1.96
    phat = pos / n
    return (phat + z*z/(2*n) - z * math.sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)


def get_problem(driver):
    problem = None
    try:
        title = [
            d for d in driver.find_elements_by_tag_name('div') 
            if d.get_attribute('data-cy') == 'question-title'][0]
        info = title.find_element_by_xpath('..').find_elements_by_tag_name('div')[1]
        title_text = title.text
        difficulty = info.find_elements_by_tag_name('div')[0].text
        up = int(info.find_elements_by_tag_name('button')[0].find_element_by_tag_name('span').text)
        down = int(info.find_elements_by_tag_name('button')[1].find_element_by_tag_name('span').text)
        problem = [get_score(up, up+down), title_text, difficulty, up, down]
    except Exception as e:
        print('Error during fetching problem: %s' % e)
    return problem

    
driver = webdriver.Chrome()
driver.get('https://leetcode.com/problemset/all/')
time.sleep(1)

page = driver.find_elements_by_tag_name('tbody')[1].find_element_by_tag_name('select')
Select(page).select_by_visible_text('all')
time.sleep(5)

table = driver.find_elements_by_tag_name('tbody')[0]
rows = [r.find_elements_by_tag_name('td')[2].find_element_by_tag_name('div') for r in table.find_elements_by_tag_name('tr')]
urls = [
    r.find_element_by_tag_name('a').get_property('href')
    for r in rows if not r.find_elements_by_tag_name('span')]

problems = []
with open('problem.csv', 'w') as f:
    for url in urls:
        try:
            driver.get(url)
            problem = None
            count = 0
            while problem is None and count < 5:
                time.sleep(2)
                problem = get_problem(driver)
                count += 1
            if problem is None:
                raise Exception('Error fetching problem.')
            problems.append(problem)
            print(problem)
            f.write('%s\n' % '|'.join(['%.4f' % problem[0], str(problem[1]), problem[2], problem[3][0], str(problem[4]), str(problem[5])]))
        except Exception as e:
            print('Error during fetching %s: %s' % (url, e))

driver.quit()

problems = sorted(problems, reverse=True)
with open('rank.csv', 'w') as f:
    f.write('\n'.join(['|'.join(['%.4f' % p[0], str(p[1]), p[2], p[3][0], str(p[4]), str(p[5])]) for p in problems]))