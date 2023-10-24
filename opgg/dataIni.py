from bs4 import BeautifulSoup
import re
import pandas as pd
def dataIni(fileName, header_list, name_list, class_list, win_rate_list, pick_rate_list, ban_rate_list, weak_against_list, version_list):
    with open(fileName, 'r', encoding='utf-8') as f:
        text = f.read()
        bs_text = BeautifulSoup(text, features='lxml')
        

    # 找到该文件对应的版本
    version_div = bs_text.find_all('div', attrs={'class':'css-e52sg2 ez6zw1e0'})[1]
    version = version_div.find('label').text
    # print(version)

    # 找到所有我们需要的属性，作为表头
    table_headers = bs_text.find_all('th', attrs={'scope':'col'})
    if len(header_list) == 0:
        for item in table_headers:
            header_list.append(item.text)
    # print(header_list)

    # 找到英雄的名字
    name_container = bs_text.find_all('td', attrs={'class':'css-1im1udv e1u05mw02'})
    for item in name_container:
        name_strong = item.find('strong')
        name_list.append(name_strong.text)
    # print(name_list)

    # 找到英雄强度
    class_container = bs_text.find_all('td', attrs={'class':'css-1qn65js e1u05mw05'})
    for item in class_container:
        class_list.append(item.text.split('\n')[-1])
    # print(class_list)

    # 找胜率,ban率,pick率
    rate_container = bs_text.find_all('td', attrs={'class':'css-9aydzo e1tupkk21'})
    flag = 0
    for item in rate_container:
        text = item.text.replace(' ', '')
        text = text.replace('\n', '')
        if flag == 0:
            win_rate_list.append(text)
            flag = 1
        elif flag == 1:
            pick_rate_list.append(text)
            flag = 2
        elif flag == 2:
            ban_rate_list.append(text)
            flag = 0
    # print(ban_rate_list)

    # 找到 Weak Against
    weak_against_container = bs_text.find_all('td', attrs={'class':'css-6jlvp0 e1u05mw06'})
    for item_list in weak_against_container:
        weak_against = list()
        item_list = item_list.find_all('img')
        for item in item_list:
            weak_against.append(item['alt'])
        weak_against_list.append(str(weak_against))
    # print(weak_against_list)

    for i in range(len(name_list)-len(version_list)):
        version_list.append(version) 

if __name__ == '__main__':
    name_list = list()
    class_list = list()
    win_rate_list = list()
    pick_rate_list = list()
    ban_rate_list = list()
    weak_against_list = list()
    version_list = list()
    header_list = list()
    dataIni('response1318.html', header_list, name_list, class_list, win_rate_list, pick_rate_list, ban_rate_list, weak_against_list, version_list)
    dataIni('response1319.html', header_list, name_list, class_list, win_rate_list, pick_rate_list, ban_rate_list, weak_against_list, version_list)
    dataIni('response.html', header_list, name_list, class_list, win_rate_list, pick_rate_list, ban_rate_list, weak_against_list, version_list)



    df = pd.DataFrame(version_list)
    df.columns = ['版本']
    df[header_list[1]] = name_list
    df[header_list[2]] = class_list
    df[header_list[3]] = win_rate_list
    df[header_list[4]] = pick_rate_list
    df[header_list[5]] = ban_rate_list
    df[header_list[6]] = weak_against_list
    df.to_csv('data.csv',index=False,mode='a',header=True)