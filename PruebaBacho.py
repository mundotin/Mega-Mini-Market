# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:44:10 2020

API_KEY = "AIzaSyCwT0s0nEXsgRfIZmpplUfwhDoauiHadlo"
PROYECT_CX = "006662431015372263036:po8ilu4yrsd"

@author: Franco - Tin balin
"""
import csv, sys
from google_images_download import google_images_download 

def process(d,n,p):
    sys.stdout.write("\nFecha: " + d + " Nombre: " + n + " Precio: " + str(p))
    
def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":1-3, 
                 "print_urls":True, 
                 "size": "medium", 
                 } 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg|gif|png", 
                     "limit":1, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass


print("Comenzando proceso:")
_search_queries = []

with open('archivo_csv.txt', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
#        date = row[0]
        date =""
        nombre = row[0]
        closing_price = float(row[1])
        
        _search_queries.append(nombre)
        process(date, nombre, closing_price)

response = google_images_download.googleimagesdownload()
  
# Driver Code 
for query in _search_queries: 
    downloadimages(query)  
    print()


print("\n\nProceso finalizado")
        