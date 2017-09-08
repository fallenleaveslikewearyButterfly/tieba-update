import queue,threading

class url_manager():
    def __init__(self):
        self.urls_reply = queue.Queue()
        self.urls_tiedetails = queue.Queue()
        self.urls_tiedetails_set = set()
        self.lock=threading.Lock()
        #初始化回帖信息的url队列
        for i in range(0, 2416):
            url= "http://tieba.baidu.com/f?kw=%E6%B1%9F%E6%B1%89%E5%A4%A7%E5%AD%A6&ie=utf-8&pn=" + str(i * 50)
            self.urls_reply.put(url)

    def revdupurls_add_details(self,urls_details_get):
        self.lock.acquire()
        for url in urls_details_get:
            if url not in self.urls_tiedetails_set:
                self.urls_tiedetails_set.add(url)
                self.urls_tiedetails.put(url)
        self.lock.release()