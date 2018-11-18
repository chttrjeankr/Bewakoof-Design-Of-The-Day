import requests
import bs4
import webbrowser

def dod():
    """
    Fetches the images of men's products of design of the day from the website www.bewakoof.com
    :return: the title, the soup object from bs4
    """
    file = requests.get("https://www.bewakoof.com/design-of-the-day")
    soup = bs4.BeautifulSoup(file.text, "lxml")
    # print(soup)

    linkList = soup.select("a[class='col-sm-4 col-xs-6'] > div > div > div > img:nth-of-type(2)]")
    # soup.select("div[id=foo] > div > div > div[class=fee] > span > span > a")
    for i in linkList:
        if "t-shirt-men" in str(i):
            # print(i.get('src'))
            webbrowser.open(i.get('src'))

if __name__ == "__main__":
    dod()
