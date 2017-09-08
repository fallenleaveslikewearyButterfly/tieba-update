import csv,threading
class file_outputer():
    def __init__(self):
        noteinfo_header= ["帖子主题","帖子作者","作者贴吧水平","帖子内容","帖子发布平台","帖子发布时间"]
        repleyinfo_header=["回复数量","帖子地址","帖子主题","帖子作者","作者主页","帖子创建时间","最后回复人","最后回复时间"]
        noteinfo_path=r"C:\Users\enqrrwi\Desktop\noteinfo.csv"
        repleyinfo_path=r"C:\Users\enqrrwi\Desktop\repleyinfo.csv"
        noteinfo_on=open(noteinfo_path,'w', newline="",encoding="utf-8")
        repleyinfo_on=open(repleyinfo_path,'w', newline="",encoding="utf-8")
        self.noteinfo_writer=csv.DictWriter(noteinfo_on, noteinfo_header)
        self.repleyinfo_writer=csv.DictWriter(repleyinfo_on, repleyinfo_header)
        self.noteinfo_writer.writeheader()
        self.repleyinfo_writer.writeheader()
        self.note_lock=threading.Lock()
        self.reply_lock = threading.Lock()

    def noteinfo_write(self,noteinfodic):
        self.note_lock.acquire()
        if not len(noteinfodic)==0:
            self.noteinfo_writer.writerow(noteinfodic)
        self.note_lock.release()

    def replyinfo_write(self,repleyinfoeinfodic):
        self.reply_lock.acquire()
        self.repleyinfo_writer.writerows(repleyinfoeinfodic)
        self.reply_lock.release()
