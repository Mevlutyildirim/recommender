from bs4 import BeautifulSoup
import requests
import mysql.connector
import re 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By


driver_path="/Users/mevlutyildirim/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1729Light",
    database="ml",
    use_pure=True
)


HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}

urls = ["https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=1&sort=user_rating,desc",
        "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=2&sort=user_rating,desc", "https://www.imdb.com/list/ls005750764/?st_dt=&mode=detail&page=3&sort=user_rating,desc"]

for pg in urls:
    driver.get(pg)
    wait = WebDriverWait(driver, 50)
    posters = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.articlecccffafvf")))
    covers = [sp.get_attribute("src") for sp in posters.find_elements_by_css_selector('div.lister-item img')]
    response = requests.get(pg, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    years = [re.findall('\d{4}', sp.text.strip())[0]
             for sp in soup.select('.lister-item span.lister-item-year')]
    names = [sp.text.strip() for sp in soup.select('.lister-item-header a')]
    links = ["https://www.imdb.com"+sp["href"] for sp in soup.select('.lister-item-header a')]
    duration = [sp.text.strip().split()[0]
                for sp in soup.select('.lister-item span.runtime')]
    genre = [sp.text.strip() for sp in soup.select('.lister-item span.genre')]
    rated = [sp.text.strip() for sp in soup.select(
    'div.ipl-rating-star.small span.ipl-rating-star__rating')]
    metascore = [sp.text.strip()
                 for sp in soup.select('.lister-item span.metascore')]
    votes = [sp["data-value"].replace(",", "")
             for sp in soup.select(".lister-item span[name=nv]")]
    details =[sp.text.strip() for sp in soup.select("div.ipl-rating-widget~p:not(.text-muted)")]
    director=[sp.text.strip() for sp in soup.select("div.ipl-rating-widget~p:not(.text-muted)+p.text-muted.text-small :first-child")]
    movies = soup.select(".lister-item")
    mycursor = mydb.cursor()
    for index in range(0, len(movies)):
        print(years[index])
        print(names[index])
        print(links[index])
        print(covers[index])
        print(votes[index])
        print(rated[index])
        print(genre[index])
        print(details[index])
        print(duration[index])
        print(director[index])
        sql = "INSERT INTO movies (year, title, cover, votes, rate , type, duration, link, details, director) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (years[index], names[index], covers[index],
               votes[index], rated[index], genre[index], duration[index], links[index], details[index], director[index])
        mycursor.execute(sql, val)
        mydb.commit()
        print("\n")