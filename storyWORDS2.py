# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:30:53 2018

@author: Alex
"""


from urllib.request import urlopen

TEXT=['abc vbfrt rtyge','cdffr grtdw rtdew ','ddf frewa rtyre']
TEXT1=open(r'C:\Users\Alex\Desktop\sixtynorth.txt')
TEXT2=urlopen('http://sixty-north.com/c/t.txt')
def fetch_words(story):

       story_words=[]
       for line in story:
           line_words=line.split()
           
           for word in line_words:
               story_words.append(word)
               
       return story_words


def print_items(items):
        for item in items:
            print(item)
        return    
        
def main():
    if __name__=='__main__':
       
        print_items(fetch_words(TEXT))
        print_items(fetch_words(TEXT1))
        print_items(fetch_words(TEXT2))
        
main()
        
        
        