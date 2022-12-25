#!/usr/bin/env python
# encoding: utf-8
"""
Author: rightyonghu
Created Time: 2022/10/22
"""
import json
import re
from scrapy import Spider, Request
from spiders.common import parse_tweet_info, parse_long_tweet


class TestSpider(Spider):
    """
    自定义爬虫
    """
    name = "test"
    def start_requests(self):
        """
        爬虫入口
        """
        # 这里keywords可替换成实际待采集的数据
        url=["http://httpbin.org/ip","http://httpbin.org/user-agent"]
        for u in url:
            yield Request(u, callback=self.parse)

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        data=json.loads(response.text)
        if "origin" in data:
            print("ip:"+data["origin"])
        else:
            print("User-Agent:"+data["user-agent"])
