##
## ***************************************************
## Summarize News Articles with Machine Learning in Python 
## April 30 2024 
##  ***************************************************
## 

#GUI 
import tkinter as tk 
#For  Natural Language Processes: 
import nltk 
#Sentiment Analysis
from textblob import TextBlob
#Extracting Articles 
from newspaper import Article

#nltk.download('punkt') only need to call it once, not all the time 


def clear(): 
    '''
        Clear all text fields, that is title, author, publication date, summary 
        and sentiment analysis
    '''

    title.delete('1.0', 'end')
    author.delete('1.0', 'end') 
    publication.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')
    print('This works!')


def summarize(): 
    '''
        Summarizes article using NLP
    
    '''
    url = utext.get('1.0', 'end').strip()
                    
    article = Article(url)
    article.download()
    article.parse()
    article.nlp() 
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    sentiment_analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Sentiment: {"Positive" if sentiment_analysis.polarity > 0 else "Negative" if sentiment_analysis.polarity < 0 else "Neutral" }')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

#GUI begins here 
root = tk.Tk()
root.title("Article Summarizer")
root.geometry("720x600")


#Text Fields
tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#DDDDDD') #to prevent users to write anything 
title.pack() 


alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=2, width=140)
author.config(state='disabled', bg="#DDDDDD")
author.pack()


plabel = tk.Label(root, text="Publishing Date")
plabel.pack() 

publication = tk.Text(root, height=2, width=140)
publication.config(state='disabled', bg="#DDDDDD")
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.pack() 

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#DDDDDD')
summary.pack() 


selabel = tk.Label(root, text="Sentiment")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg="#DDDDDD")
sentiment.pack() 


ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.config(bg="#DDDDDD")
utext.pack() 

#Buttons 
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack() 

btn_clear = tk.Button(root, text="Clear", command=clear)
btn_clear.pack() 


root.mainloop()