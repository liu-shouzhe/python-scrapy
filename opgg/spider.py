# import requests

# cookies = {
#     '_dd_s': '',
# }

# headers = {
#     'authority': 'www.op.gg',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
#     'sec-ch-ua-mobile': '?0',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     # 'cookie': '_dd_s=',
# }

# response = requests.get('https://www.op.gg/champions', cookies=cookies, headers=headers)
# response.encoding = "utf-8"

# with open("response.txt", "w", encoding="utf-8") as f:
#     f.write(response.text)


import requests

cookies = {
    '_dd_s': '',
}

headers = {
    'authority': 'www.op.gg',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'cookie': '_dd_s=',
}

params = {
    'region': 'global',
    'tier': 'emerald_plus',
    'patch': '13.17',
    'position': 'top',
}

response = requests.get('https://www.op.gg/champions', params=params, cookies=cookies, headers=headers)

with open("response1317.html", "w", encoding="utf-8") as f:
    f.write(response.text)