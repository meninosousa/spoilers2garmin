# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:41:25 2016

@author: aspire5737z
"""

import os
import PIL
import shutil

pocket_query = 'Geneva'

geocaching_folder = 'C:/Users/aspire5737z/Desktop/Geocaching'
pocketquery_folder = '%s/%s' % (geocaching_folder, pocket_query)
spoiler_folder = '%s/Spoilers' % pocketquery_folder
garmin_folder = '%s/Garmin/GeocachePhotos' % pocketquery_folder

def convert2jpg(pic2convert):
    PIL.Image.open(pic2convert)\
    .convert('RGB')\
    .save('%sjpg' % pic2convert[:-3])
    

#NOT USED    
#def delete_file(file2delete):
#    os.remove(file2delete)



def main():
    if not os.path.exists(garmin_folder):
        os.makedirs(garmin_folder)
    files = os.listdir(spoiler_folder)
    for file in files:
        if file[-3:]!='jpg' and file[-3:]!='png' and file[-3:]!='gif':
            continue
        elif file[-3:]=='png' or file[-3:]=='gif':
            if os.path.exists('%s/%sjpg' % (spoiler_folder, file[:-3])):
                continue
            convert2jpg('%s/%s' % (spoiler_folder, file))
            file = '%sjpg' % file[:-3]
        print(file)
        space_pos = file.index(' ')
        last_char = file[space_pos-1]
        if space_pos < 4:
            beforelast_char = '0'
        else:
            beforelast_char = file[space_pos-2]
        geocache_code = file[:space_pos]        
        folder2copy = '%s/%s/%s/%s' % \
        (garmin_folder, last_char, beforelast_char, geocache_code)
        if not os.path.exists(folder2copy):
            os.makedirs(folder2copy)        
        shutil.copyfile('%s/%s' % (spoiler_folder, file), \
        '%s/%s' % (folder2copy, file))

main()
