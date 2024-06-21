import tkinter
from tkinter import *
import tkinter.messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from nltk.sentiment.vader import SentimentIntensityAnalyzer



class Text_Analyser:
    def __init__(self):
        self.main=Tk()
        self.main.title("Text Analyser")
        self.main.geometry('700x700')
        self.main.resizable(width=False , height=False)
        self.main.focus()
        self.main.protocol('WM_DELETE_WINDOW',self.callback)

        self.input_label=Label(self.main,text="Type in a sentence")
        self.input_label.pack()
        self.text_box=Entry(self.main,width=100)
        self.text_box.pack()
        self.text_box.bind("<Key>",self.edited_text)
        self.text_box.bind("<Return>",self.run_by_enter)
        self.typed_text=Label(self.main,text="")
        self.typed_text.pack()
        self.negative=Label(self.main,text="negaivity:")
        self.negative.pack()
        self.negative_percentage=Label(self.main,text="")
        self.negative_percentage.pack()
        self.positive=Label(self.main,text="positivity:")
        self.positive.pack()
        self.positive_percentage=Label(self.main,text="")
       
        self.positive_percentage.pack()
        self.neutral=Label(self.main,text="neutral:")
        self.neutral.pack()
        self.neutral_percentage=Label(self.main,text="")
        self.neutral_percentage.pack()
        self.overall=Label(self.main,text="")
        self.overall.pack()
        




    def callback(self):
        if tkinter.messagebox.askokcancel("Do you want to exit the website"):
            self.main.destroy()

    def edited_text(self,event):
        self.typed_text.configure(text =self.text_box.get()+event.char)
    def run_by_enter(self,event):
        self.run_analysis()
    
    def run_analysis(self):
        sentences=[]
        sentences.append(self.text_box.get())
        sid=SentimentIntensityAnalyzer()
        for sentence in sentences:
            sentiment_dictionary=sid.polarity_scores(sentence)
            if sentiment_dictionary["compound"]<=-0.05:
                self.overall.configure(text="it is a negative statement")
            elif sentiment_dictionary["compound"]>=0.05:
                self.overall.configure(text="it is a positive statement")
            else:
                self.overall.configure(text="it is a neutral statement")

        for k in sentiment_dictionary:
            self.set_result(k,sentiment_dictionary[k])

    def set_result(self,type,val):
        if (type == "neg"):
            self.negative_percentage.configure(text  =str(val)) 
        elif (type == "pos"):
            self.positive_percentage.configure( text= str(val) )
        elif (type == "neu"):
            self.neutral_percentage.configure(text =  str(val) )
         
        


        
   






test=Text_Analyser()
mainloop()










