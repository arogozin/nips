#!/usr/local/bin/python
import json
import urllib2

class YQL:
    
    url = ''
    xpath = ''
    
    baseurl = 'https://query.yahooapis.com/v1/public/yql?q='
    query = ''
    diagnostics = '&diagnostics='
    outputformat = '&format='
    env = '&env='
    callback = '&callback='
    
    def __init__(self, url, xpath):
        
        self.url = url
        self.xpath = xpath
        
        self.query = urllib2.quote('select * from html where url="' + self.url +'" and xpath="'+ self.xpath +'"')
        
        self.diagnostics += 'true'
        self.outputformat += 'json'
        self.env += 'store://datatables.org/alltableswithkeys'
        self.callback += ''
        
        self.url =  self.baseurl + \
                    self.query + \
                    self.diagnostics + \
                    self.outputformat + \
                    self.env + \
                    self.callback
    
    def get_json(self):
        return json.loads(urllib2.urlopen(self.url).read())
