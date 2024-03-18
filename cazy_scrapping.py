import requests
from bs4 import BeautifulSoup

for cbm_family in range(0, 102):
    url = 'http://www.cazy.org/CBM'+str(cbm_family)+'_structure.html'

    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

    site = requests.get(url, headers= headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    links_ncbi = soup.find_all('a', href=lambda href: href and href.startswith("http://www.ncbi"))

    genbank_ids = []
    for row in links_ncbi:
        genbank_ids.append(row.find('b').string) if row.find('b') is not None else None

    with open(r'C:\\Users\\Maninho\\Desktop\\CAZY\\genbank_ids.txt', 'a') as f:
        for id in genbank_ids:
            f.write(f"{id}\n")
