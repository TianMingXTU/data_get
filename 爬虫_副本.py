import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 启动 Chrome 浏览器
driver = webdriver.Edge()

# 设置头信息
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'
}
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": header})

# 创建一个空的 DataFrame，用于存储数据
all_data = pd.DataFrame()

for i in range(0, 300):
    # 打开页面
    url = f"https://tieba.baidu.com/f?kw=%E6%B9%98%E6%BD%AD%E5%A4%A7%E5%AD%A6&ie=utf-8&pn={i * 50}"
    driver.get(url)

    # 获取页面源码
    page_source = driver.page_source

    # 解析页面
    soup = BeautifulSoup(page_source, 'html.parser')

    # 找到评论数据
    comments = soup.find_all('a', class_='j_th_tit')
    authors_up = soup.find_all('span', class_='frs-author-name-wrap')
    time_creat = soup.find_all('span', class_='pull-right is_show_create_time')

    authors = []
    comment_s = []
    times = []

    for author in authors_up:
        author_a = author.a
        if author_a:
            author_content = author_a.text
            author_link = 'https://jump2.bdimg.com/' + author_a['href']
            author_data = {
                '作者': author_content,
                '作者链接': author_link
            }
            authors.append(author_data)
        else:
            authors.append({'作者': 'Nan', '作者链接': 'Nan'})

    for comment in comments:
        if comment:
            comment_c = comment.text
            comment_link = 'https://jump2.bdimg.com/' + comment['href']
            comment_data = {
                '内容': comment_c,
                '内容链接': comment_link
            }
            comment_s.append(comment_data)
        else:
            comment_s.append({'内容': 'Nan', '内容链接': 'Nan'})

    for t in time_creat:
        if t:
            time_data = {
                '创建时间': t.text
            }
            times.append(time_data)
        else:
            times.append({
                '创建时间': 'Nan'
            })

    # 创建当前循环迭代的 DataFrame
    df = pd.concat([pd.DataFrame(authors), pd.DataFrame(comment_s)], axis=1)
    df_t = pd.concat([df, pd.DataFrame(times)], axis=1)

    # 将当前循环迭代的数据追加到总的 DataFrame
    all_data = pd.concat([all_data, df_t], ignore_index=True)

    print(i)
    time.sleep(1)

# 将所有数据保存到 Excel 文件
all_data.to_excel('total_副本.xlsx', index=False)

# 关闭浏览器
driver.quit()
