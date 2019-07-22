import os
import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup


app = Flask(__name__)

app.secret_key = "KjJPe35tQKY2YLRzm7vhm3aJdqqh8YHR"


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")

    facts = soup.find_all("div", id="content")
    return facts[0].getText()


def pig_latin(fact):
    send = {'input_text': fact}
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/', data=send)
    url = response.url
    return "<a>Here is a pig-latinized fact:</a><a href={}> {}</a>".format(url, url)


@app.route('/')
def home():

    fact = get_fact()
    pig = pig_latin(fact)
    return pig


if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 6787))
    host = os.environ.get("HOST", "127.0.0.1")
    app.run(host=host, port=port)
    

 #   app.run(host='0.0.0.0', port=port
