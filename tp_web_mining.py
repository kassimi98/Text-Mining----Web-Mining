import numpy as np
import pandas as pd
import requests
import bs4
import lxml.etree as xml

#chercher dans URL 
URL = "https://github.com/psf/requests"
requests.get(URL)

#Reponse de l'URL (code source de la page web)
requests.get(URL, {}).text

#avoir une bonne format du fichier (lxml) par le package "bs4.BeautifulSoup"
web_page = bs4.BeautifulSoup(requests.get(URL, {}).text, "lxml")
web_page

#avoir des elements dans un fichier sous formt xml
#dans cette exemple en aura le titre de la page 
print(web_page.head.title.text)

#avoir le "body" de la page 
web_page.body

#avoir une liste des elements ayant comme nom et attribut (class, id ...) les memes que dans le script ci dessous par fint_all()/ on peut avoir un seul element par find()

sub_web_page = web_page.find_all(name="nom-element", attrs={"class": "valeur-de-la-classe"})
sub_web_page

#avoir les element sous format texte sans balises 
#exemple l'element (li)

[wp.text.strip("\n ").replace(",", "")
    for wp in sub_web_page.find_all("li")]
#avoir les texte a l'interieur des enfants d'un element Div par exemeple
#Remarque__ navigable string ca veut dire un element qui contient du texte et un autre element

tags_elements = web_page.find_all(name="div", attrs={"class":"f6"})[6]
tags_elements
tags_text = [elem.text.strip("\n ")  for elem in tags_elements.children if type(elem) != bs4.NavigableString]
tags_text

#les expressions regulieres 
#avoir des liens qui contient une chaine et des simboles

import re

[e.text.strip("\n ") for e in 
 web_page.find_all(name="a", 
                   attrs={"href": re.compile("/topics/.+")})]

#recuperer un lien a partir d'une balise "a"
content=file_row.find(name="td", attrs={"class": "content"})\
                      .find(name="a")
href      = content.attrs["href"]

