import json 
import os.path
import sys
import io
from unicode_csv import UnicodeWriter

def get_value_from_dict_or_return_NA(dict, key):
    if key in dict and dict[key] != None:
	   return dict[key]
    return "NA"

with io.open('acl_instagram.csv', 'ab') as csv_data:
    writer = UnicodeWriter(csv_data, delimiter='`')
   
    with open('acl_instagram.txt') as instagram_file:
        for insta_data in instagram_file:
            post = json.loads(insta_data)
            writer.writerow([
                get_value_from_dict_or_return_NA(post, 'user'),
                get_value_from_dict_or_return_NA(post, 'post_time'),
                get_value_from_dict_or_return_NA(post, 'post_location'),
                get_value_from_dict_or_return_NA(post, 'likes_count'),
                get_value_from_dict_or_return_NA(post, 'views_count'),
                json.dumps(get_value_from_dict_or_return_NA(post, 'comments'))
            ])
