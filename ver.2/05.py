import requests
from pprint import pprint
from url_id import URL
import os
from dotenv import load_dotenv
load_dotenv()

def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    key = os.getenv('API_Key')
    movie_id = URL(key).movie_id(title)
    url = URL(key).get_url(f'/movie/{movie_id}/recommendations', region='KR', language='ko-KR')
    response = requests.get(url).json()
    movie_dict = response.get('results')
    if movie_dict == None:
        return None
    
    recommend_movies = [movie.get('title') for movie in movie_dict]

    return recommend_movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
