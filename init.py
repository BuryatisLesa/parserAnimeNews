import time

from method import create_absolute_url, next_page, add_title, add_content

if __name__ == '__main__':
    start_time = time.time()
    function = next_page()
    absolute_url = create_absolute_url(function)
    add_title(absolute_url)
    add_content(absolute_url)
    end_time=time.time()
    print(f'На обработку поста всего времени было занято => {(end_time-start_time)/60} минут')


