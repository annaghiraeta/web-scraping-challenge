#!/usr/bin/env python
# coding: utf-8




from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import pandas as pd
import requests
import re 
import time

def scrape_info():
    browser=Browser('chrome')
    mars={}


    # # Scraping

    # # NASA Mars News



    # pull titles from website
    url='https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('div', class_="content_title")
    news_title=titles[1].text
    body = soup.find_all('div', class_="article_teaser_body")
    news_p=body[0].text
    mars["news_title"]=news_title
    mars["news_p"]=news_p




    # pull body from website
    mars




    # pull titles and body from website
    results = soup.find_all('div', class_="slide")
    for result in results:
        titles = result.find('div', class_="content_title")
        title = titles.find('a').text
        bodies = result.find('div', class_="rollover_description")
        body = bodies.find('div', class_="rollover_description_inner").text
        print('----------------')
        print(title)
        print(body)
        


    # # JPL Mars Space Images - Featured Image



    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response = requests.get(url)
    browser.visit(url)
    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.find_link_by_partial_text('more info').click()
    soup = BeautifulSoup(browser.html, 'html.parser')
    result=soup.find('figure',class_='lede')
    featured_image_url='https://www.jpl.nasa.gov'+ result.a.img["src"]
    featured_image_url
    mars["featured_image"]=featured_image_url








    # # Mars Facts



    mars_facts_url = "https://space-facts.com/mars/"
    table = pd.read_html(mars_facts_url)
    table[0]




    df = table[0]
    df.columns = ["Facts", "Value"]
    df.set_index(["Facts"])
    df



    facts_html = df.to_html()
    facts_html = facts_html.replace("\n","")
    facts_html
    mars["facts"]=facts_html


    # # Mars Hemispheres



    hemisphere_image_urls = []


    # Cerberus Hemispheres



    url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')




    # print(soup.prettify())




    cerberus_img = soup.find_all('div', class_="wide-image-wrapper")
    # print(cerberus_img)





    Hemisphere={}
    for img in cerberus_img:
        pic = img.find('li')
        full_img = pic.find('a')['href']
        print(full_img)
    cerberus_title = soup.find('h2', class_='title').text
    print(cerberus_title)
    cerberus_hem = {"Title": cerberus_title, "url": full_img}
    print(cerberus_hem)
    Hemisphere["title"]=cerberus_title
    Hemisphere["img_url"]=cerberus_hem
    hemisphere_image_urls.append(Hemisphere)


    # Schiaparelli Hemisphere



    url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')



    #print(soup.prettify())


    shiaparelli_img = soup.find_all('div', class_="wide-image-wrapper")
    # print(shiaparelli_img)



    for img in shiaparelli_img:
        pic = img.find('li')
        full_img = pic.find('a')['href']
        print(full_img)
    shiaparelli_title = soup.find('h2', class_='title').text
    print(shiaparelli_title)
    shiaparelli_hem = {"Title": shiaparelli_title, "url": full_img}
    print(shiaparelli_hem)
    Hemisphere["title"]=shiaparelli_title
    Hemisphere["img_url"]=shiaparelli_title
    hemisphere_image_urls.append(Hemisphere)


    # Syrtis Hemisphere


    url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    #print(soup.prettify())



    syrtris_img = soup.find_all('div', class_="wide-image-wrapper")
    # print(syrtris_img)



    for img in syrtris_img:
        pic = img.find('li')
        full_img = pic.find('a')['href']
        print(full_img)
    syrtris_title = soup.find('h2', class_='title').text
    print(syrtris_title)
    syrtris_hem = {"Title": syrtris_title, "url": full_img}
    print(syrtris_hem)
    Hemisphere["title"]=syrtris_title
    Hemisphere["img_url"]=syrtris_hem
    hemisphere_image_urls.append(Hemisphere)


    # Valles Marineris Hemisphere


    url = ('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')



    valles_marineris_img = soup.find_all('div', class_="wide-image-wrapper")
    # print(valles_marineris_img)




    for img in valles_marineris_img:
        pic = img.find('li')
        full_img = pic.find('a')['href']
        print(full_img)
    valles_marineris_title = soup.find('h2', class_='title').text
    print(valles_marineris_title)
    valles_marineris_hem = {"Title": valles_marineris_title, "url": full_img}
    print(valles_marineris_hem)
    Hemisphere["title"]=valles_marineris_title
    Hemisphere["img_url"]=valles_marineris_hem 
    hemisphere_image_urls.append(Hemisphere)


    mars["hemisphere"]=hemisphere_image_urls
    return mars

if __name__ == "__main__":
    print(scrape_info())





