from pprint import pprint
import json

import requests

import config


def main():

    for article in json.loads(requests.get(config.Url.ROOT_URL.value).text)['info']:
        if config.LastArticle.DATE.value < article['date']:
            print(article['title'])
            print()
            pprint(article['content'])
            print('\n')


if __name__ == '__main__':
    main()
