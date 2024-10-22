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
        soup = BeautifulSoup(req.text, 'html.parser')
        container = soup.find_all('a', 'news_card_link')
        # получаем ссылки с страницы
        post_url = []
        for mini in container:
            post_url.append([mini])
        for url in post_url:
            absolute_url.append(str(url)[33:49])
            count += 1
            print(f'[{count}]Обработан и добавлен:[{str(url)[33:49]}]')
    print((f'Обработано постов => {count}'))
    end_time = time.time()
    print((f'Время обработки ссылок => {(end_time - start_time)/60} минут'))
    return absolute_url

def add_title(url):
    pass

def add_content(url):
    pass

def add_image_post(url):
    pass








