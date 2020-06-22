
# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
    response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')

# Examine the results, then determine element that contains sought info
#print(soup.prettify())

    #title = soup.find_all('div', class_='content_title')

    #title

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')




    title = soup.find_all('div', class_='content_title')
    title[1].text
    titletext = title[1].text.strip()
    titletext

    paragraph = soup.find_all('div', class_='article_teaser_body')
    paragraph[0].text
    ptitle = paragraph[0].text
    ptitle

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup2.find_all('a', id ='full_image')
    featured_image_url

    featured_image_url = soup2.find('a', id ='full_image')
    featured_image_url['data-fancybox-href']
    image_path = featured_image_url['data-fancybox-href']
    image_path

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup3 = BeautifulSoup(html, 'html.parser')



    mars_weather = soup3.find_all('div', lang='en')
    mars_tweet = mars_weather[0].text.strip()
    mars_tweet
   

    url = 'https://space-facts.com/mars/'

    tables = pd.read_html(url)
    mars_tables = tables[0]
    mars_tables.columns = ["Description", "Value"]
    mars_tables = mars_tables.set_index("Description", inplace = True)
    

    table_html = tables[0].to_html()
    table_html

    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)


    featured_image_url4 = browser.find_by_css("a.product-item H3")
    mars_pix = len(featured_image_url4)

    mars_img_list=[]
    for i in range (mars_pix):
        mars_dict={}
        link = browser.find_by_css("a.product-item H3")[i]
        link.click()
        image_links = browser.find_link_by_text("Sample").first
        print(image_links["href"])
        mars_dict["img_url"]=image_links["href"]
        title = browser.find_by_css("h2.title").text
        mars_dict["title"]= title
        mars_img_list.append(mars_dict)
        browser.back()
    print(mars_img_list)

    mars_data = {"News Title": [titletext], 
                 "News Text": [ptitle],
                 "Space Image": [image_path],
                 "Tweet": [mars_tweet],
                 "Mars Table": [table_html],
                 "Mars Pics": [mars_img_list]
                 }
                        
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data