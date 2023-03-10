import requests
from pprint import pprint
from url_id import URL
import os
from dotenv import load_dotenv
load_dotenv()

def search_movie(title):
    pass
    # 여기에 코드를 작성합니다.

    key = os.getenv('API_Key')
    url = URL(key).get_url('/search/movie', region='KR', language='ko-KR', query = title)
    response = requests.get(url).json()
    
    
    if response.get('results'):
        movie_id = response.get('results')[0].get('id')
        return movie_id

    else:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
