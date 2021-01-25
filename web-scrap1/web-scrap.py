from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file: # r artinya read only
    content = html_file.read()
    print(content)

    soup = BeautifulSoup(content, 'lxml')
    # # print(soup.prettify())
    # tags = soup.find('h1')
    # print(tags)