import warnings

warnings.filterwarnings("ignore")

from duckduckgo_search import DDGS
import requests
import re
import nltk
from bs4 import BeautifulSoup

import os

nltk_data_path = os.environ["APPDATA"] + "\\nltk_data"
if not os.path.exists(nltk_data_path + "\\tokenizers\\punkt"):
    try:
        nltk.download("punkt")
    except FileExistsError:
        pass


def search_links(query, domain, max_results=20):
    results = DDGS().text(query, max_results=max_results)
    links = [result["href"] for result in results if domain in result["href"]]
    return links[:3]


def get_answer(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    raw_text = soup.get_text()

    clean_text = re.sub(r"\s+", " ", raw_text).strip()

    sentences = nltk.sent_tokenize(clean_text)

    organized_text = []

    for sentence in sentences:
        cleaned_sentence = re.sub(r"[^\w\s]", "", sentence)
        organized_text.append(cleaned_sentence)

    return organized_text


while True:
    query = str(input("Enter Your query: "))
    domain = str(
        input(
            "Enter the domain you want to scrape from (e.g., wikipedia.com, reddit.com): "
        )
    )
    links = search_links(query + " " + domain, domain)
    answers = ""
    for link in links:
        print("URL: ", link)
        answer_list = get_answer(link)
        answer_text = "\n".join(answer_list)
        answers += f"================================\nReference: {link}\nAnswer: {answer_text}\n================================\n"
    print(answers)
