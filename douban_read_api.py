# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

class Douban:

    STATUS = {
        'read'    : u'读过',
        'reading' : u'在读',
        'wish'    : u'想读'
    }

    def __init__(self, name):
        self.endpoint = u'https://api.douban.com/v2'
        self.name     = name

    def books(self, file_path):
        uri        = self.endpoint + '/book/user/%s/collections' % self.name
        page_size  = 100

        # 计算总数
        response   = requests.get(uri, params = {'count': 1})
        total      = response.json().get('total')
        page_count = total / page_size + 1

        print 'Total: %d' % total

        with file(file_path, 'a') as f:
            f.write(u'时间, 状态, 标题\n')
            for index in range(0, page_count):
                print '> processing page %d ...' % index
                payload = {
                    'count': page_size,
                    'start': index * page_size
                }
                response = requests.get(uri, params = payload)
                data     = response.json()

                for coll in data.get('collections', []):
                    line = u'%s, %s, %s\n' % (
                        coll.get('updated'),
                        self.STATUS.get(coll.get('status'), '***'),
                        coll.get('book').get('title')
                    )
                    f.write(line)



if __name__ == '__main__':
    d = Douban('icysilence')
    d.books('D:\douban_read.txt')
