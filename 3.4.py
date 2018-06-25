import requests

# AUTH_URL = 'https://oauth.yandex.ru/authorize'
# APP_ID = 'a5c1df0de4fe47e7987be8a449dc4b92'
#
# TOKEN = 'AQAAAAABHBaxAASt0yT51Qj13UOgtBeZLNq1RsE'


class Counter:
    def __init__(self, token):
        self.token = token
        self.counter_id = self.get_counter_id()

    def get_counter_id(self):
        url = 'https://api-metrika.yandex.ru/management/v1/counters'
        headers = {
            'Authorization': 'OAuth {}'.format(self.token)
        }
        response = requests.get(url, headers=headers)

        return response.json()['counters'][0]['id']

    def get_stats(self, data):
        url = ('https://api-metrika.yandex.ru/stat/v1/data?id={}&'
               'metrics=ym:s:{}&oauth_token={}').format(self.counter_id,
                                                        data,
                                                        self.token)
        response = requests.get(url)

        return int(response.json()['totals'][0])

    def get_visits(self):
        return self.get_stats('visits')

    def get_pageviews(self):
        return self.get_stats('pageviews')

    def get_users(self):
        return self.get_stats('users')


if __name__ == '__main__':
    AUTH_URL = 'https://oauth.yandex.ru/authorize'
    APP_ID = 'a5c1df0de4fe47e7987be8a449dc4b92'

    params = {
        'response_type': 'token',
        'client_id': APP_ID
    }


token = input('Token: ')
ya_api = Counter(token)
print('Visits:', ya_api.get_visits())
print('Page views:', ya_api.get_pageviews())
print('Users:', ya_api.get_users())