# Requisito 12
import sys

from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (search_by_category,
                                              search_by_date, search_by_tag,
                                              search_by_title)
from tech_news.scraper import get_tech_news


def init_database():
    amount = int(input("Digite quantas notícias serão buscadas:"))
    get_tech_news(amount)


def search_title():
    title = str(input("Digite o título:"))
    print(search_by_title(title))


def search_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def search_tag():
    tag = input("Digite a tag:")
    print(search_by_tag(tag))


def search_category():
    category = input("Digite a categoria:")
    print(search_by_category(category))


def top_news():
    print(top_5_news())


def top_categories():
    print(top_5_categories())


def exit_menu():
    print("Encerrando script")


def analyzer_menu():
    menu_option = str(input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    ))

    options = {
        "0": init_database,
        "1": search_title,
        "2": search_date,
        "3": search_tag,
        "4": search_category,
        "5": top_news,
        "6": top_categories,
        "7": exit_menu
    }
    try:
        options[menu_option]()
    except KeyError:
        sys.stderr.write("Opção inválida\n")
