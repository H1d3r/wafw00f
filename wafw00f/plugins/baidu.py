#!/usr/bin/env python

NAME = 'Baidu Yunjiasu'

def is_waf(self):
    # There are some servers which return 'Server: Yunjiasu-nginx'
    if self.matchheader(('Server', 'Yunjiasu(.*)?')):
        return True
    return False