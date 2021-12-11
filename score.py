from collections import namedtuple
import csv
import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

Problem = namedtuple('Problem', ['num', 'title', 'difficulty', 'up_vote', 'down_vote','score'])

def calculate_score(up, total):
    if total == 0:
        return 0
    z = 1.96
    phat = up / total
    return (phat + z*z/(2*total) - z * math.sqrt((phat*(1-phat)+z*z/(4*total))/total))/(1+z*z/total)


def get_problem(driver, url):
    driver.get(url)
    time.sleep(3)
    problem = None
    try:
        title = driver.find_element_by_css_selector('div[data-cy="question-title"]')
        title_text = title.text.split('.')[1].strip()
        num = int(title.text.split('.')[0].strip())
        info = title.find_element_by_xpath('..').find_elements_by_tag_name('div')[1]
        difficulty = info.find_elements_by_tag_name('div')[0].text
        up = int(info.find_elements_by_tag_name('button')[0].find_element_by_tag_name('span').text)
        down = int(info.find_elements_by_tag_name('button')[1].find_element_by_tag_name('span').text)
        problem = Problem(num, title_text, difficulty, up, down, calculate_score(up, up + down))
    except Exception as e:
        print('Error during fetching problem (%s): %s' % (url, e))
    return problem


def get_problem_urls(driver, page, collect_premium):
    driver.get('https://leetcode.com/problemset/all/?page=%s' % page)
    time.sleep(3)
    rows = driver.find_elements_by_css_selector('div[role="row"]')[1:]
    urls = []
    for r in rows:
        url = r.find_elements_by_css_selector('div[role="cell"]')[1].find_element_by_tag_name('a').get_property('href')
        icon = r.find_elements_by_css_selector('div[role="cell"]')[0].find_element_by_tag_name('svg')
        is_premium = 'text-brand-orange' in icon.get_property('className').get('animVal', '')
        if collect_premium or not is_premium:
            urls.append(url)
    return urls


driver = webdriver.Chrome()
total_page = 42
collect_premium = False
problems = []

for i in range(1, total_page + 1):
    urls = get_problem_urls(driver, i, collect_premium)
    for url in urls:
        problem = get_problem(driver, url)
        if not problem:
            continue
        problems.append(problem)
        print(problem)

problems = sorted(problems, key=lambda p: p.num)
with open('problem.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(('num', 'title', 'difficulty', 'up_vote', 'down_vote','score'))
    w.writerows([(p.num, p.title, p.difficulty, p.up_vote, p.down_vote, p.score) for p in problems])

driver.quit()