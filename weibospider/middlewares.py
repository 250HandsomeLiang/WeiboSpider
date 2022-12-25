# encoding: utf-8
import random
class RandomUserAgentMiddleware():
    '''
    随机设置User-Agent
    '''
    def __init__(self):
        self.user_agent=[
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
           'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'
        ]
    
    def process_request(self,request,spider):
        pass
        request.headers['User-Agent']=random.choice(self.user_agent)
    def process_exception(self, request, exception, spider):
        '''
        请求错误时调用
        '''
        spider.logger.error(
            f"[Exception]{exception}\n请求头设置错误,当前的请求头为{request.headers['User-Agent']}")
        return request

class IPProxyMiddleware(object):
    """
    代理IP中间件
    """

    @staticmethod
    def fetch_proxy():
        """
        获取一个代理IP
        """
        # You need to rewrite this function if you want to add proxy pool
        # the function should return an ip in the format of "ip:port" like "12.34.1.4:9090"
        proxy_list=[
        '49.88.150.206:21489',
        '27.158.112.98:35910'
        ]
        res=random.choice(proxy_list)
        return res

    def process_request(self, request, spider):
        """
        将代理IP添加到request请求中
        """
        proxy_data = self.fetch_proxy()
        if proxy_data:
            current_proxy = f'http://{proxy_data}'
            spider.logger.debug(f"current proxy:{current_proxy}")
            request.meta['proxy'] = current_proxy

