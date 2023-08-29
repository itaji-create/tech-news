import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=3, headers=headers)
        if response.status_code != 200:
            return None
        return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links
# ".ui-search-result-image__element ::attr(data-src)"
# scrape_novidades(fetch("https://lista.mercadolivre.com.br/cervejas#D[A:cervejas]"))


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(".next::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary).strip()
    noticia = {
        "url": selector.css('head link[rel="canonical"]::attr(href)').get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "comments_count": len(selector.css(".comment-body").getall()),
        "category": selector.css(".category-style .label::text").get(),
        "summary": summary,
        "tags": selector.css(".post-tags ul li a::text").getall()
    }
    return noticia


# Requisito 5
def get_tech_news(amount):
    noticias = []
    html = fetch("https://blog.betrybe.com/")
    links = scrape_novidades(html)
    while len(links[:amount]) != amount:
        next_link = scrape_next_page_link(html)
        next_page = fetch(next_link)
        links = links + scrape_novidades(next_page)
        html = next_page

    for link in links[:amount]:
        request = fetch(link)
        noticias.append(scrape_noticia(request))
    create_news(noticias)
    return noticias


get_tech_news(5)
