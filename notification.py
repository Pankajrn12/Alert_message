from plyer import notification
import requests


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C://Users//Ravita Prajapaty//Desktop//python_project//virus.ico",
        timeout = 10
    )
def getData(url):
    r = requests.get(url)
    return r.text    

if __name__ == '__main__':
    notifyMe("Ravita", "Lets stop the spread of the virus together")
    myHtmlData = getData('https://www.mygov.in/covid-19')
    print(myHtmlData)
        