#!/usr/local/bin/python
import json
import urllib2
import re

from yql import YQL

class Committee:
    
    url = ''
    year = ''
    xpath = ''
    json = {}
    reviewers = []
    
    def __init__(self, year, xpath = None):
        
        self.year = year
        self.url = 'http://nips.cc/Conferences/'+ str(self.year) +'/Committees'
        
        if xpath is None:
            self.xpath = "//*[@id='yui-main']/div/div/p[8]/text()"
        else:
            self.xpath = xpath
        
        self.json = YQL(self.url, self.xpath).get_json()
    
    def get_json(self):
        return self.json
    
    def get_reviewers(self):
        str = " ".join(self.json['query']['results'].split())
        
        for item in str.split(')'):
            split = " ".join(item.split()).split(' (')
            if len(split) > 1:
                reviewer = {}
                reviewer['name'] = split[0]
                reviewer['affiliation'] = split[1]
                self.reviewers.append(reviewer)
        
        print self.reviewers
        
    

committee = Committee(2013)

committee.get_reviewers()