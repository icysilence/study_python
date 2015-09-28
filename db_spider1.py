#!/usr/bin/python
#! -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def process_page(index):

    response = requests.get('http://movie.douban.com/people/icysilence/collect?start=' + str(index) + '&sort=time&rating=all&filter=all&mode=grid')
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.find_all(class_='item'):
        print '%s, %s, %s' % (item.find('em').get_text(), item.find(class_='date').get_text(), '' if item.find(class_='tags') is None else item.find(class_='tags').get_text().replace(u'标签: ', ''))


def process_all():
	for index in range(0, 18):
		process_page(index * 15)

if __name__ == '__main__':
    process_all()
