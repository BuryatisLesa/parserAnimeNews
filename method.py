import time

from lib_use import *


st_accept = 'text/html' #Вывод

st_useragent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36"
                ) #браузер

headers = {
    "Accept": st_accept,
    'User-Agent': st_useragent
}

main_url = 'https://kg-portal.ru' #сайт с которого мы собираем информацию


def next_page():
    # метод перехода на другую страницу,
    # так, как у сайт определенная логика на перемещение страничек
    # мы добавляем каждую 20-ю к url
    add_page = []
    for num in range(20, 4000, 20):
        add_page.append(num)
    return add_page

def create_absolute_url(f):
    # создание абсолютного адреса, к каждому посту
    start_time = time.time()
    absolute_url = []
    count = 0
    for num_f in f:
        req = requests.get(f'{main_url}/news/anime/{num_f}', headers)  # запрос сайт/пользователь
        src = req.text
        soup = BeautifulSoup(src, 'html.parser')
        container = soup.find_all('a', 'news_card_link')
        # получаем ссылки с страницы
        post_url = []
        for mini in container:
            post_url.append([mini])
        for url in post_url:
            absolute_url.append(str(url)[33:49])
            count += 1
            print(f'[{count}]Обработан и добавлен:[{str(url)[33:49]}]')
            time.sleep(1)
    print((f'Обработано постов => {count}'))
    end_time = time.time()
    print((f'Время обработки ссылок => {(end_time - start_time)/60} минут'))
    return absolute_url

def add_title(urls):
    title = []
    count = 0
    start_time = time.time()
    for url in urls:
        req = requests.get(f'{main_url}{url}', headers)  # запрос сайт/пользователь
        src = req.text
        soup = BeautifulSoup(src, 'html.parser')
        container = soup.find_all('h1', 'news_title')
        for title_container in container:
            title.append(str(title_container.text))
            print(f'[{count}]Добавлен заголовок ["{title_container.text}"]')
            count+=1
            time.sleep(1)
    end_time = time.time()
    print(f'Добавлено заголовков => [{count}]\n',
          f'Время на обработку => {(end_time-start_time)/60} минут')
    return title


def add_content(urls):
    content = []
    content_join = []
    count = 0
    start_time = time.time()
    for url in urls:
        req = requests.get(f'{main_url}{url}', headers)  # запрос сайт/пользователь
        src = req.text
        soup = BeautifulSoup(src, 'html.parser')
        container = soup.find('div','news_text').select('p')
        for content_container in container:
            result = ''.join(content_container.text)
            content_join.append(result)
            content.append(content_join)
            time.sleep(1)
        count += 1
        print(f'[{count}]Добавлен текст ["{content_join}"]')
    end_time = time.time()
    print(f'Добавлено текст => [{count}]\n',
          f'Время на обработку => {(end_time-start_time)/60} минут')
    return content

def add_image_post(urls):
    pass






