import requests
import time

def dld_data():

    stock_names_code = {'海特高新':'1002023','国药股份':'0600511', '赤峰黄金':'0600988','财通证券':'0601108'}
    #注意，真正的股票代码为{'海特高新':'002023','国药股份':'600511', '赤峰黄金':'600988','财通证券':'601108'}
    #在前面加上一个数字是批量下载的需要。
    start_time='2019-01-01'
    end_time='2019-12-31'
    st=start_time.replace('-','')
    et=end_time.replace('-','')

    header = {
        'Referer': 'http://quotes.money.163.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'cookie': 'nts_mail_user=ara_homework@163.com:-1:1; _ntes_nnid=7c81b3ec04bd0d7c00db39a27aef36d8,1587821599114; _ntes_nuid=7c81b3ec04bd0d7c00db39a27aef36d8; P_INFO=ara_homework@163.com|1589033086|0|mail163|00&99|jil&1589032463&mail163#hun&null#10#0#0|&0|mail163|ara_homework@163.com; vjuids=adbea96.172f41dcfaf.0.e86b76f8315c9; vjlast=1593233494.1593233494.30; _ntes_stock_recent_=0600988%7C0601108%7C0600511%7C1002023; _ntes_stock_recent_=0600988%7C0601108%7C0600511%7C1002023; _ntes_stock_recent_=0600988%7C0601108%7C0600511%7C1002023; ne_analysis_trace_id=1593239755238; s_n_f_l_n3=9276d15d4883292c1593239755260; pgr_n_f_l_n3=9276d15d4883292c15932397552406666; vinfo_n_f_l_n3=9276d15d4883292c.1.1.1593234338747.1593237230516.1593239760886'
    }
    for code in stock_names_code.values():
        time.sleep(5)
        url="http://quotes.money.163.com/service/chddata.html?code={}&start={}&end={}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP".format(code, st, et)
        r=requests.get(url,headers=header)
        with open("{}.csv".format(code),'wb') as csvfile:
            for chunk in r.iter_content(chunk_size=10000):
                if chunk:
                    csvfile.write(chunk)

if __name__ == "__main__":
     dld_data()


