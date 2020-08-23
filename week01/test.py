import requests
from bs4 import BeautifulSoup as bs


# 获得前10个电影链接列表
def moviesurl(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'

    header = {'user-agent': user_agent}

    response = requests.get(myurl, headers=header)

    bs_info = bs(response.text, 'html.parser')

    # 获取前10个电影链接
    urls = []
    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
        for atag in tags.find_all('a', ):
            urls.append(f'https://maoyan.com' + atag.get('href'))
    return urls


# 获得全部电影信息
def moviesinfo(urls):
    mylist = []
    for url in urls:
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'

        header = {'user-agent': user_agent}

        response = requests.get(url, headers=header)

        bs_info = bs(response.text, 'html.parser')

        # 获取电影名称
        movie_name = bs_info.find('h1', attrs={'class': 'name'}).text

        # 类型
        movie_cate_list = bs_info.find_all('a', attrs={'class': 'text-link'})
        movie_cates = ''
        for movie_cate in movie_cate_list:
            movie_cates += movie_cate.text

        # 上映时间
        movie_release_date = bs_info.find_all('li', attrs={'class': 'ellipsis'})[2].text[:10]

        info_list = [movie_name, movie_cates, movie_release_date]
        mylist.append(info_list)
    return mylist

import pandas as pd


urls = moviesurl(f'https://maoyan.com/films')
movie_info_list = moviesinfo(urls)
movie_data = pd.DataFrame(data=movie_info_list)
movie_data.to_csv('./maoyan.csv', encoding='utf8', index=False, header=False)