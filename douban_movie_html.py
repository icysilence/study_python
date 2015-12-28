#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup


def process_page(index, f):

    response = requests.get('http://movie.douban.com/people/2824734/collect?start=' + str(index) + '&sort=time&rating=all&filter=all&mode=grid')
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for item in soup.find_all(class_='item'):

        line = (u'%s#%s#%s\n' % (
            item.find('em').get_text(), 
            item.find(class_='date').get_text(), 
            '' if item.find(class_='tags') is None else item.find(class_='tags').get_text()#.replace(u'标签: ', '')
        ))
        f.write(line)

def process_all(file_path):
    with file(file_path, 'a') as f:
        for index in range(0, 71):
            print '> processing page %d ...' % index 
            process_page(index * 15, f)
            

if __name__ == '__main__':
    process_all('D:\douban_movie_birdman.txt')

