import requests

class html_download():
    def download(self,urls):
        url = urls.get(timeout=5)
        if  not url.startswith("http"):
            url="http://tieba.baidu.com" +url
        headers = {
            "host": "tieba.baidu.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
        }
        cookie = {
            "after_vcode": "7388f56a1ff97df1a82ddc2a4afe147c411d651b60be5b11f49a426e27db7c0132d5f5656d70840cef6b0e9621dfb31fb7a83a3062ecaa2da3ce3609a9062ec7c69a1fc1fb365a0b3ca656206e87c2d3a3cc3dd8301769e23263854b5794bd5175f872eaed1a4b8f1e9bfbfb2e4380983c0c20d16996d1dfb4335af16bab5d9cdda4bb9ff25afb2e38af26e2c7fe0cdd7447d4a173983a934d7e88fdbd9471dc"}
        resp = requests.get(url=url, headers=headers,cookies=cookie)
        resp.encoding = "utf-8"
        if resp.status_code == 200:
            #print("成功抓取:",url)
            return resp.text
        else:
            return None