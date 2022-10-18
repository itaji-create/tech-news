from tech_news.database import find_news


def orderBy(e):
    return e["comments_count"]


# Requisito 10
def top_5_news():
    news = find_news()
    news.sort(key=orderBy, reverse=True)
    return [(item["title"], item["url"]) for item in news][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
