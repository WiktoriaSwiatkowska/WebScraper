import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

product_code = input("Provide product code:")
page = 1 
next = True

headers={
    "Host":"www.ceneo.pl",
    "Cookie":"sv3=1.0_93efd37a-3cbb-11f1-9d77-b84196259956; urdsc=2; userCeneo=ID=a541d403-862d-4e9c-b180-af974ce32055; __RequestVerificationToken=_uX3KevP-1uwnWq4ennUh0KqvYhsm6a1Wp2WwqcSXJp2dWElj8juK9WxaPrHCz0As05LmIKs4KFmzZl-vfi3oocgm_V5bRSR3cmXgICdqTU1; st2=sref%3dhttps%3a%2f%2fwww.bing.com%2f%2c_t%3d63912295176%2cencode%3dtrue; ai_user=072Gb|2026-04-20T13:19:37.762Z; __utmf=364726cdbe2e8437518b57e7b5f0d525_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; ai_session=CG5LT|1776691179295.2|1776691179295.2; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T13%3A19%3A39.821Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%2293efd37a-3cbb-11f1-9d77-b84196259956%22%2C%22expiryDate%22%3A%222027-04-20T13%3A19%3A39.821Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22LRQObGlJElJufAmjKeJm%22%2C%22expiryDate%22%3A%222027-04-20T13%3A19%3A39.822Z%22%7D; browserBlStatus=0; ga4_ga=GA1.2.93efd37a-3cbb-11f1-9d77-b84196259956; _gcl_au=1.1.650485059.1776691181; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlJekpEN0JiRkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUFRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJQUFBQUFBQUFBQUFCQkdZQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFCWUtBREFBRUVaZ2tBR0FBSUl6Qm9BTUFBUVJtRVFBWUFBZ2pNS2dBd0FCQkdZWkFCZ0FDQ013NkFEQUFFRVppRUFHQUFJSXpFb0FNQUFRUm1LUUFZQUFnak1XZ0F3QUJCR1kuSUl6SkQ3QmJGTFVGQXdGaGpZS3NRTUlFVFVNQ0FBb1FBQUFhQkFDQUJRQUtRSUFRQ2trQVFCQVNnQkFBQ0FBQUFJQ1JCSVFBTUFBQUFDRUFBUUFBQUlBQUVBQUNRQVFBSUFBQUFnQUFRQUFBWUFBQWlBSUFBQUFBSWdBSUFFQUFBbVFoQUFBSUFFRUFBaEFBRUlBQUFBQUFBQUFBQUFnQUFBQUFDQUFJQUFBQUFBQ0FBQUlBQUFBQUFBQUFBQUJBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.ZfsGawJ7CPanegOVYv8inicEWee%2BRwiqu5vb1NKjAJc%3D; FPLC=V%2Bsf2URKkbD9hAaprGHZg5O75ZyvdQbm9bcLJfiiN1DRx1GomYqSetNHWLVAZpOlgL11BAuDrZ7q6QC5rfYF4lAdJdl2E5Qz4fQ2HNP1FJHfAR0%3D; ga4_ga_K2N2M0CBQ6=GS2.2.s1776691179$o1$g1$t1776691199$j41$l0$h1030216410",
    "User":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",

}
url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"

path_to_driver = "D:\WŚ\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
s = Service(path_to_driver)
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.maximize_window()
driver.find_element(by="xpath", value='//*[@id="js_cookie-consent-general"]/div/div[2]/button[1]').click()

all_opinions=[]
while next:
    url = f"https://www.ceneo.pl/{product_code}/opinie-{page}"
    print(url)
    response = requests.get(url, headers = headers)
    if response.status_code ==200:
        page_dom = BeautifulSoup(response.text,'html.parser')

        product_name = page_dom.select_one('h1').get_text() if page == 1 else product_name
        
        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")
        print(len(opinions))
    
    for opinion in opinions:
        single_opinion = {
            "opinion_id": opinion.get ("data-entry-id"),
            "author":opinion.select_one("span.user-post__author-name").get_text().strip(),
            "reccomendation":opinion.select_one("span.user-post__author-recomendation > em").get_text().strip() if ("span.user-post__author-recomendation > em") else None, 
            "score":opinion.select_one("span.user-post__score-count").get_text().strip(), 
            "content":opinion.select_one("div.user-post__text").get_text().strip(),
            "pros":[p.get_text() for p in opinion.select("div.review-feature__item--positive")],
            "cons":[c.get_text() for c in opinion.select("div.review-feature__item--negative")],
            "helpful":opinion.select_one("button.vote-yes[data-total-vote]").get_text().strip(),
            "unhelpful":opinion.select_one("button.vote-no[data-total-vote]").get_text().strip(),
            "publish_date":opinion.select_one("span.user-post__published > time:nth-child(1)").get("datetime").strip(),
            "purchase_date":opinion.select_one("span.user-post__published > time:nth-child(2)").get("datetime").strip() if opinion.select_one("span.user-post__published > time:nth-child(2)") else None,
        }
    all_opinions.append(single_opinion)
    print(all_opinions)

    next = True if page_dom.select_one('button.pagination_next') else False

    if next: 
        page += 1 
        driver.find_element(by="xpath", value='//*[@id="js_cookie-consent-general"]/div/div[2]/button[1]').click()

if not os.path.exists("./opinions"):
    os.mkdir("./opinions")

with open(f"./opinions/{product_code}.json", "w", encoding = "UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)