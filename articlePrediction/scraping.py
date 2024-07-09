from bs4 import BeautifulSoup
import requests

#guardian -real
# url = 'https://www.theguardian.com/politics/2022/feb/24/britons-living-in-eu-cant-keep-pre-brexit-rights-european-court-advised'

# cnn
# url = 'https://edition.cnn.com/2022/02/10/politics/donald-trump-gop-incumbents-impeach-votes/index.html' 

# bbc
# url ='https://www.bbc.com/news/av/60334905'

#ratopati
# url ='https://www.ratopati.com/story/220582/2022/2/10/congress'

#kathmandu post ----> yesma error aayo
# url = 'https://kathmandupost.com/national/2022/02/10/will-people-from-kalapani-region-get-to-exercise-their-franchise'

#nepalnews -----> yesma paragraph lina sakena
# url = 'https://nepalnews.com.np/s/nation/mohp-records-1-369-new-covid-cases-12-deaths-on-thursday'

#online khabar
# url = 'https://www.onlinekhabar.com/2022/02/1077033'

#nytimes
# url = 'https://www.nytimes.com/2022/02/10/us/politics/jan-6-trump-calls.html'

#foxnews
# url = 'https://www.foxnews.com/politics/democrats-scramble-reverse-course-covid-restrictions-midterms'

#nbcnews ----> error occured
# url = 'https://www.nbcnews.com/news/world/u-s-intel-nine-probable-russian-routes-ukraine-full-scale-n1288922'

#gaurdians news
# url = 'https://www.theguardian.com/football/2022/feb/10/chelsea-braced-for-kepa-arrizabalaga-bids-and-open-to-summer-exit'

#abc news
# url = 'https://abcnews.go.com/Politics/pressure-builds-biden-democrats-move-past-covid/story?id=82754983'

# url = 'https://edition.cnn.com/2022/02/10/politics/biden-ukraine-things-could-crazy/index.html'


def getUrl(url): #get the response 
    pageContent = requests.get(url)
    print(pageContent)
    return pageContent



# def cleanWord(text):
#   text = text.lower()
#   text = re.sub('\[.*?\]', '', text)
#   text = re.sub("\\W", " ", text)
#   text = re.sub('https?://\S+|www\.\S+', '', text)
#   text = re.sub('<.*?>+', '', text)
#   text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#   text = re.sub('\n', '', text)
#   text = re.sub('\w*\d\w*', '', text)
#   return text

# def remove_html_tags(text):
#     """Remove html tags from a string"""
#     import re
#     clean = re.compile('<.*?>')
#     return re.sub(clean, '', text)



def parse(pagecontent):
    data = []
    if pagecontent.status_code != 200: #beside response 200 for all response show page not found
        print('Page not found')
        return 0
    coup = BeautifulSoup(pagecontent.content, 'html.parser') #Parse the content using bs4
    #print(coup)
    try:
        if coup.find('article') is not None: #if news article is in article tag
            #print('article')
            contentParse = coup.find('article')
            # print(contentParse)

        # elif coup.find('section') is not None:
        #     print('section')
            # contentParse = coup.find('section')

        elif coup.find('div') is not None: #if news article is in div tag
            print("div")
            #searching for the right div is left here
            contentParses = coup.find_all('div')
            # print(len(contentParses))
            # print('xir2')
            flag = 0
            for contentParse in contentParses:
                if contentParse.find('h1') is not None:
                    # print('xir3')
                    headline = contentParse.find('h1').text
                    # print(f'Title: {headline}')
                    break
                flag +=1
            count = 0
            newsArticles = contentParses[flag].find_all('p')
            for newsArticle in newsArticles:
                if count == 5:
                    break
                # print(newsArticle.text, end=' ')
                data.append(newsArticle.text)
                count +=1
            data.insert(0, headline)
            data = ' '.join(data)
            dictt = {
            # 'title': headline,
            'article': data
        }
            print(dictt)
            return dictt # to process only the article which is in div tag
        else:
            errormessage = 'No content found'
            print(errormessage)
        print(contentParse)
        
        # print('teha gayana')
        # print(contentParse)
# to process the article which is in article tag
        headline = contentParse.find('h1')
        if headline:
            headline= headline.text
        else:
            headline=""
        print(f"Title: {headline}")

        newsArticles = contentParse.find_all('p')
    # print(len(newsArticles))
      #  print("hello")
        for newsArticle in newsArticles:
            # print(newsArticle.text, end=' ')
            data.append(newsArticle.text)
        # dictt = {
        #     'title': headline,
        #     'article': data
        # }
        data.insert(0, headline)
        data = ' '.join(data)
        dictt = {
            'article': data
        }

        print(dictt)
        return dictt

    except: #any error occured during the process 
        print("Error Occured")

    # data = cleanWord(newsArticles)
    # data = remove_html_tags(newsArticles)
    
    
def printArticle(art):
    print('Output: '+art)


# parse(getUrl(url))