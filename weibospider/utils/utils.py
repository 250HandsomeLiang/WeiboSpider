import emoji
import re
def emoji_filter(content):
    '''
    表情包过滤
    '''
    content=emoji.demojize(content)
    print(content)
    content=re.sub('\:(.*?)\:','',content)
    print(content)
    return content
if __name__=='__main__':
    emoji_filter('🍉电影《了不起的她》近日丽江开机\n根据张桂梅校长事迹改编\n主演：海清、胡歌（客串')