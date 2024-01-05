# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 171 ust. 1–3 ustawy Prawo bankowe (wykonywanie czynności bankowych, w szczególności przyjmowanie wkładów pieniężnych w celu obciążania ich ryzykiem, bez zezwolenia KNF)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 178 ustawy o obrocie instrumentami finansowymi (prowadzenie działalności w zakresie obrotu instrumentami finansowymi bez wymaganego zezwolenia lub upoważnienia)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 178 w zw. z art. 79 ustawy o obrocie instrumentami finansowymi (wykonywanie działalności bez wpisu do rejestru agentów firm inwestycyjnych)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 287 i art. 290–296 ustawy o funduszach inwestycyjnych

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 99 i art. 99a ustawy z dnia 29 lipca 2005 r. o ofercie publicznej i warunkach wprowadzania instrumentów finansowych do zorganizowanego systemu obrotu oraz o spółkach publicznych (dokonanie oferty publicznej papierów wartościowych bez wymaganego ustawą zatwierdzonego przez KNF prospektu emisyjnego/memorandum informacyjnego/dokumentu informacyjnego lub dokonanie emisji obligacji bez zachowania ustawowych warunków)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 56a i art. 57 ustawy o giełdach towarowych (prowadzenie giełd towarowych bez zezwolenia)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 430 ustawy o działalności ubezpieczeniowej i reasekuracyjnej (przed 1 stycznia 2016 r. - art. 225 ustawy o działalności ubezpieczeniowej) (wykonywanie czynności ubezpieczeniowych lub działalności reasekuracyjnej bez zezwolenia)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 89 i art. 90 ustawy o dystrybucji ubezpieczeń (przed 23 lutego 2018 r. - art. 47 i art. 48 ustawy o pośrednictwie ubezpieczeniowym)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art 59h i art. 59i ustawy o kredycie konsumenckim (prowadzenie działalności w charakterze instytucji pożyczkowej lub w charakterze pośrednika kredytowego bez wymaganego wpisu do rejestru)

# Zawiadomienia o podejrzeniu popełnienia przestępstwa z art. 150 i art. 151 ustawy o usługach płatniczych (nieuprawniona działalność w zakresie świadczenia usług płatniczych lub w zakresie wydawania pieniądza elektronicznego)

# biblioteki requests, beautifulsoup, pyinstaller, tkinter

import requests
from bs4 import BeautifulSoup
import csv
import time
import tkinter
from tkinter import simpledialog


def scrape_and_export():
    response = requests.get(
        "https://www.knf.gov.pl/dla_konsumenta/ostrzezenia_publiczne")
    target_selector = r"#\35 1301 > td:nth-child(2)"

    soup = BeautifulSoup(response.content, 'html.parser')
    selected_element = soup.select_one(target_selector)

    if selected_element:
        content = selected_element.get_text(strip=True)
    else:
        content = "Element not found"

    with open('output.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([content])


if __name__ == "__main__":
    numerek = simpledialog.askinteger(
        "knf-scraper", "Co ile godzin dane mają być pobierane?", initialvalue=10)
    while True:
        scrape_and_export()

        print(numerek)
    # interwał wybrany przez użytkownika (w godzinach)
        time.sleep(numerek * 60 * 60)
