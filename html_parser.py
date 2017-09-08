from bs4 import BeautifulSoup as bs
import re
class html_parser():
    def replyinfoparser(self,html_con):
        html_con = html_con.replace("<!--", "")
        html_con = html_con.replace("-->", "")
        html_con = html_con.replace("\r", "")
        html_con = html_con.replace("\n", "")
        soup = bs(html_con, "html.parser")
        everytie = soup.find_all("div", class_="t_con cleafix")
        patternrnum = 'title="回复">(\d+)</span>'
        patternhref = 'href="(/p/.*?)"'
        patternauth = 'title="主题作者: (.*?)"'
        patternauthhpage = '主题作者:[\s\S]*?href="(/home/main/.*?)"'
        patterncreatime = 'title="创建时间">(.*?)</span>'
        patternlrely = '最后回复人: (.*?)">'
        patternreplytime = '最后回复时间">(.*?)</span>'
        patterntopic='href="/p/.*?" title="(.*?)"'
        infos = []
        urls_details_get = []
        for i in everytie:
            infodic = {}
            infodic["回复数量"] = (re.findall(patternrnum, str(i)))[0]
            url =(re.findall(patternhref, str(i)))[0]
            infodic["帖子地址"] = url
            urls_details_get.append(url)
            infodic["帖子主题"]= (re.findall(patterntopic, str(i)))[0]
            if len(re.findall(patternauth, str(i)))==0:
                infodic["帖子作者"]=" "
            else:
                infodic["帖子作者"] = (re.findall(patternauth, str(i)))[0]
            if len(re.findall(patternauthhpage, str(i)))==0:
                infodic["作者主页"]=" "
            else:
                infodic["作者主页"] =(re.findall(patternauthhpage, str(i)))[0]
            infodic["帖子创建时间"] = (re.findall(patterncreatime, str(i)))[0]
            if len(re.findall(patternlrely, str(i)))==0:
                infodic["最后回复人"] =" "
            else:
                infodic["最后回复人"] = (re.findall(patternlrely, str(i)))[0]
            if len(re.findall(patternreplytime, str(i))) == 0:
                infodic["最后回复时间"] = " "
            else:
                infodic["最后回复时间"] = (re.findall(patternreplytime, str(i)))[0]
            infos.append(infodic)
        return infos, urls_details_get

    def noteparser(self,html_con):
        soup = bs(html_con, "html.parser")
        onefloor = (soup.find_all("div", class_=re.compile(r"l_post j_l_post l_post_bright.*?")))
        try:
            if len(onefloor)==0:
                print(html_con)
                onefloorinfodic = {}
            else:
                patterntopic = 'class="core_title_txt .*?title="(.*?)"'
                patternauth = 'author="(.*?)"'
                patternlevel = '<div class="d_badge_lv">(\d+)</div>'
                patterncontent = 'clearfix".*?>([\s\S]*?)</div>'
                patternplatfom = '"open_type":"(.*?)"'
                patterndate = 'date":"(.*?)"'
                onefloorinfodic = {}
                if len(re.findall(patterntopic, str(soup)))==0:
                    onefloorinfodic["帖子主题"]=" "
                else:
                    onefloorinfodic["帖子主题"] = (re.findall(patterntopic, str(soup)))[0]
                if len(re.findall(patternauth, str(onefloor)))==0:
                    onefloorinfodic["帖子作者"]=""
                else:
                    onefloorinfodic["帖子作者"] = (re.findall(patternauth, str(onefloor)))[0]
                if len(re.findall(patternlevel, str(onefloor)))==0:
                    onefloorinfodic["作者贴吧水平"]="0"
                else:
                    onefloorinfodic["作者贴吧水平"] = (re.findall(patternlevel, str(onefloor)))[0]
                onefloorinfodic["帖子内容"] = (re.findall(patterncontent, str(onefloor)))[0]
                if len(re.findall(patternplatfom, str(onefloor)))==0:
                    onefloorinfodic["帖子发布平台"] =" "
                else:
                    onefloorinfodic["帖子发布平台"] = (re.findall(patternplatfom, str(onefloor)))[0]
                onefloorinfodic["帖子发布时间"] = (re.findall(patterndate, str(onefloor)))[0]
        except:
            print("有异常",onefloor)
            onefloorinfodic = {}
        return onefloorinfodic