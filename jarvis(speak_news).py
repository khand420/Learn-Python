import request
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Today's Hadlines are!")
    url = "put news api int this string from website"  

    news = request.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"]) #this is news api articles
    arts = news_dict['articles']
    for articles in arts:
        speak(articles['title'])
        print(articles['title'])
        speak("Moving on to the next...Listen Carefully!")

    speak("Thank You For Listening..!")    