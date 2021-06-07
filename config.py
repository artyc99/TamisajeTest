from enum import Enum


class Url(Enum):
    ROOT_URL = 'https://primorye.ldpr.ru/api/pb/articles?site_key=primorye&aggregate=full&limit=12&page=1'


class LastArticle(Enum):
    DATE = '2021-06-01'
