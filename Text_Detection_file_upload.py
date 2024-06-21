import tkinter
from tkinter import *
import tkinter.messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter.filedialog

import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer



class Text_Analyser:
    def __init__(self):
        self.main=Tk()
        self.main.title("Text Analyser")
        self.main.geometry('700x700')
        self.main.resizable(width=False , height=False)
        self.main.focus()
        self.main.protocol('WM_DELETE_WINDOW',self.callback)

        
        import_button = Button(self.main, text="Import File", command=self.import_file)
        import_button.pack(pady=100)

        
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
        



    def import_file(self):
        file_path = tkinter.filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
           
            with open(file_path,'r',encoding='utf-8') as file:
                
                content=file.read()
                self.run_analysis(content)
                

    def callback(self):
        if tkinter.messagebox.askokcancel("Do you want to exit the website"):
            self.main.destroy()


    
    def run_analysis(self,text):
       
        sid=SentimentIntensityAnalyzer()
        
        sentiment_dictionary=sid.polarity_scores(text)
        filtered_sentiments = {k: v for k, v in sentiment_dictionary.items() if k != "compound"}
        x = max(filtered_sentiments, key=filtered_sentiments.get)
        
        if (x == "neg"):
            self.overall.configure(text="it is a negative statement")
        elif (x == "pos"):
            self.overall.configure(text="it is a positive statement")
        elif (x=="neu"):
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










