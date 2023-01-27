# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:41:45 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root , text= "Fibonacci Series : ")
input_1=Entry(root)
label_spiral = Label(root)

def Fibonacci() :
    num = int(input_1.get())
    sum_2 = 0
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        sum_2 = sum_2 + sum
        counter += 1
        first_no = sum
        sum = first_no + second_no
        label_series["text"] += str(sum_2) +" "
        label_spiral["text"] = "Fibonacci Sum : " + str(sum_2)
        
btn = Button(root , text= "Show Fibonacci Series " , command=Fibonacci , bg = "White")        
        
input_1.pack()
btn.pack()
label_series.pack()
label_spiral.pack()

root.mainloop()