import time,threading
import traceback,sys
from file_outputer import file_outputer
from html_download import html_download
from html_parser import html_parser
from url_manager import url_manager
from concurrent.futures import ThreadPoolExecutor

class spider_main():

    def __init__(self):
        self.file_outputer=file_outputer()
        self.html_download=html_download()
        self.parser=html_parser()
        self.url_manager=url_manager()

    def craw_reply(self):
        urls_reply_que = self.url_manager.urls_reply
        while not urls_reply_que.empty():
            try :
                html_replyinfo=self.html_download.download(urls_reply_que)
                if html_replyinfo==None:
                    print("reply is None")
                else:
                    infos, urls_details_get=self.parser.replyinfoparser(html_replyinfo)
                    self.file_outputer.replyinfo_write(infos)
                    self.url_manager.revdupurls_add_details(urls_details_get)
                    time.sleep(120)
            except:
                print("捕获reply异常")
        else:
            pass
            #print(urls_reply_que.qsize(),"***************************")
            #print(self.url_manager.urls_tiedetails.qsize(),"12323231312")
    def craw_note(self):
        urls_tiedetails_que = self.url_manager.urls_tiedetails
        while not urls_tiedetails_que.empty():
            #print("帖子抓取",urls_tiedetails_que.qsize())
            try:
                html_note = self.html_download.download(urls_tiedetails_que)
                if html_note is None:
                    print("html_note is None")
                else:
                    notedic = self.parser.noteparser(html_note)
                    self.file_outputer.noteinfo_write(notedic)
            except:
                print("捕获note异常")
        else:
            pass
            #print(urls_tiedetails_que.qsize(),"----------------------")
if __name__=="__main__":
    spider=spider_main()
    # spider.craw_reply()
    #spider.craw_note()
    threadspool = ThreadPoolExecutor(max_workers=(48+96))
    for i in range(0,48):
        threadspool.submit(spider.craw_reply,)
    time.sleep(30)
    for i in range(0,96):
        threadspool.submit(spider.craw_note,)
    spider.url_manager.urls_tiedetails.join()
    spider.url_manager.urls_tiedetails.task_done()