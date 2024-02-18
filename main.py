# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import os
import concurrent.futures
import json
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path, 
        image_path, 
        search_key, 
        number_of_images, 
        headless, 
        min_resolution, 
        max_resolution, 
        max_missed)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)
    
    #Release resources
    del image_scraper

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(set(["Alabama landscape", "Alaska landscape", "Arizona landscape", "Arkansas landscape", "California landscape", "Colorado landscape", "Connecticut landscape",
            "Delaware landscape", "Florida landscape", "Georgia landscape", "Hawaii landscape", "Idaho landscape", "Illinois landscape", "Indiana landscape", "Iowa landscape", "Kansas landscape", 
            "Kentucky landscape", "Louisiana landscape", "Maine landscape", "Maryland landscape", "Massachusetts landscape", "Michigan landscape", "Minnesota landscape", 
            "Mississippi landscape", "Missouri landscape", "Montana landscape", "Nebraska landscape", "Nevada landscape", "New Hampshire landscape", "New Jersey landscape", 
            "New Mexico landscape", "New York landscape", "North Carolina landscape", "North Dakota landscape", "Ohio landscape", "Oklahoma landscape", "Oregon landscape", 
            "Pennsylvania landscape", "Rhode Island landscape", "South Carolina landscape", "South Dakota landscape", "Tennessee landscape", "Texas landscape", "Utah landscape",
            "Vermont landscape", "Virginia landscape", "Washington landscape", "West Virginia landscape", "Wisconsin landscape", "Wyoming landscape", "Alabama landscape", "Alaska urban",
            "Arizona urban", "Arkansas urban", "California urban", "Colorado urban", "Connecticut urban",
            "Delaware urban", "Florida urban", "Georgia urban", "Hawaii urban", "Idaho urban", "Illinois urban", "Indiana urban", "Iowa urban", "Kansas urban", 
            "Kentucky urban", "Louisiana urban", "Maine urban", "Maryland urban", "Massachusetts urban", "Michigan urban", "Minnesota urban", 
            "Mississippi urban", "Missouri urban", "Montana urban", "Nebraska urban", "Nevada urban", "New Hampshire urban", "New Jersey urban", 
            "New Mexico urban", "New York urban", "North Carolina urban", "North Dakota urban", "Ohio urban", "Oklahoma urban", "Oregon urban", 
            "Pennsylvania urban", "Rhode Island urban", "South Carolina urban", "South Dakota urban", "Tennessee urban", "Texas urban", "Utah urban",
            "Vermont urban", "Virginia urban", "Washington urban", "West Virginia urban", "Wisconsin urban", "Wyoming urban"]))

    #Parameters
    number_of_images = 500                # Desired number of images
    headless = True                     # True = No Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (1920, 1080)       # Maximum desired image resolution
    max_missed = 10                     # Max number of failed images before exit
    number_of_workers = 1               # Number of "workers" used
    keep_filenames = False              # Keep original URL image filenames

    #Run each search_key in a separate thread
    #Automatically waits for all threads to finish
    #Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
