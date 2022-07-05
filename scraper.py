import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('a', text = 'citation needed')
    return len(citations)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('a', text = 'citation needed')
    report = []
    for i in citations:
        text = i.find_parents('p')[0].text
        report.append(text)
    return '\n'.join(report).strip()

if __name__ == '__main__':
    count = get_citations_needed_count(url)
    citation_report = get_citations_needed_report(url)

    print(f"Citations needed: {count} \n")
    print(citation_report)