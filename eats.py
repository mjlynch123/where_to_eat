import time
import links
from random import choice
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/mj/Desktop/python/chromedriver")

restaurants = ['pancheros', 'taco bell', 'dominos', 'hardees', 'wendys', 
               'chick fil a', 'subway', 'panda express', 'arbys', 'pizza hut',
               'panera', 'mcdonalds', 'burger king', 'happy wok']

def restChoice(restaraunt):
    if where_to_eat == 'pancheros':
        driver.get(links.panchysLink)
    elif where_to_eat == 'taco bell':
        driver.get(links.tacoLink)
    elif where_to_eat == 'dominos':
        driver.get(links.dominosLink)
    elif where_to_eat == 'hardees':
        driver.get(links.hardeesLink)
    elif where_to_eat == 'wendys':
        driver.get(links.wendysLink)
    elif where_to_eat == 'chick fil a':
        driver.get(links.chickLink)
    elif where_to_eat == 'subway':
        driver.get(links.subwayLink)
    elif where_to_eat == 'panda express':
        driver.get(links.pandaLink)
    elif where_to_eat == 'arbys':
        driver.get(links.arbyLink)
    elif where_to_eat == 'pizza hut':
        driver.get(links.pizzahutLink)
    elif where_to_eat == 'panera':
        driver.get(links.paneraLink)
    elif where_to_eat == 'mcdonalds':
        driver.get(links.mcdicks)
    elif where_to_eat == 'burger king':
        driver.get(links.bk)
    elif where_to_eat == 'happy wok':
        driver.get(links.happywok)
    else:
        print('No restaraunt selected')
        driver.close()

while True:
    where_to_eat = choice(restaurants)
    print(where_to_eat.title())
    restChoice(where_to_eat)

    close = input('Are you finished: ')
    if close == 'y':
        driver.close()
        quit()
    else: 
        continue