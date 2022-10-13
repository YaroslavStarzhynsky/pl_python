import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('pl')
page_py = wiki_wiki.page('Kapibara_wielka')
print(page_py.links)
for key in page_py.links:
    print(key)
    next_page = wiki_wiki.page(key)
    print(next_page.links)