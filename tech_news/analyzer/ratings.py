from collections import Counter

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
    news = find_news()
    categories = [item["category"] for item in news]
    categories.sort()
    categories_most_commom = Counter(categories).most_common(5)
    result = [item[0] for item in categories_most_commom]
    return result
