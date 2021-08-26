
import requests
from bs4 import BeautifulSoup
import sys

lang_map = {
    "0": "all",
    "1": "arabic",
    "2": "german",
    "3": "english",
    "4": "spanish",
    "5": "french",
    "6": "hebrew",
    '7': "japanese",
    "8": "dutch",
    '9': "polish",
    "10": "portuguese",
    "11": "romanian",
    '12': "russian",
    "13": "turkish"
}

args=sys.argv
language_1 = args[1].lower()
language_2 = args[2].lower()
word = args[3].lower()
headers = {'User-Agent': 'Mozilla/5.0'}
urls={}
file=open(f"{word}.txt",'w',encoding='utf-8')
if language_1 not in lang_map.values():
    print(f"Sorry, the program doesn't support {language_1}")
elif language_2 not in lang_map.values():
    print(f"Sorry, the program doesn't support {language_2}")
else:
    if language_2!='all':
        url= f'https://context.reverso.net/translation/{language_1}-{language_2}/{word}'
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        if r.status_code == 200:
            try:
                file.write(f"{language_2} Translations:")
                print(f"{language_2} Translations:")
                file.write("\n")
                translated_words = soup.find("div", {"id": "translations-content"}).find_all('a')
                for i in translated_words:
                    file.write(i.text.strip("\n\r "))
                    print(i.text.strip("\n\r "))
                    file.write("\n")
                file.write("")
                print()
                file.write("\n")
                file.write(f"{language_2} Example:")
                print(f"{language_2} Example:")
                file.write("\n")
                examples = soup.find_all("div", {"class": "example"})
                for j in examples:
                    data1=j.find_all('span', {'class': 'text'})
                    for i in data1:
                        data = i.text.strip("\n\r ")
                        file.write(data)
                        print(data)
                        file.write("\n")
                file.write("")
                print()
            except:
                print(f"Sorry, unable to find {word}")
        elif r.status_code==404:
            print(f"Sorry, unable to find {word}")
        else:
            print("Something wrong with your internet connection")
    else:
        for key,value in lang_map.items():
            if value.lower()!=language_1 and value!='all':
                url=f'https://context.reverso.net/translation/{language_1}-{value.lower()}/{word}'
                r = requests.get(url, headers=headers)
                soup = BeautifulSoup(r.content, 'html.parser')
                if r.status_code == 200:
                    try:
                        file.write(f"{value} Translations:")
                        print(f"{value} Translations:")
                        file.write("\n")
                        translated_words = soup.find("div", {"id": "translations-content"}).find('a').text.strip("\n\r ")
                        file.write(translated_words)
                        print(translated_words)
                        file.write("\n")
                        file.write("")
                        print()
                        file.write("\n")
                        file.write(f"{value} Example:")
                        print(f"{value} Example:")
                        file.write("\n")
                        examples = soup.find("div", {"class": "example"}).find_all('span', {'class': 'text'})
                        for j in examples:
                            data=j.text.strip("\n\r ")
                            file.write(data)
                            print(data)
                            file.write("\n")
                        file.write("")
                        print()
                        file.write("\n")
                    except:
                        print(f"Sorry, unable to find {word}")
                elif r.status_code==404:
                    print(f"Sorry, unable to find {word}")
                else:
                    print("Something wrong with your internet connection")
file.close()
