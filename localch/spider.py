from selenium.webdriver import Chrome
import openpyxl as op

fileName = 'test.xlsx'
wb = op.Workbook()  # 创建工作簿对象
ws = wb['Sheet']  # 创建子表
ws.append(['Name', 'Street', 'PLZ', 'City', 'Business', 'Phone', 'Mobile', 'Email', 'Website'])  # 添加表头

# 创建浏览器驱动并指定路径
web = Chrome(executable_path="C:/Users/12848/Desktop/spider/localch/chromedriver.exe")

url = "https://www.local.ch/de"

# 打开对应网址
web.get(url)

web.implicitly_wait(2)
web.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
# web.find_element_by_xpath('//*[@id="what-input-1"]').send_keys("Alles")
# web.find_element_by_xpath('//*[@id="where-input-1"]').send_keys("in allen Regionen")
web.find_element_by_xpath('//*[@id="search-submit-btn-1"]').click()

web.implicitly_wait(2)
content = web.find_elements_by_xpath('//*[@id="page-content"]/div/div[1]/div[2]/div[4]/div[@class="SearchResultList_listElementWrapper__KRuKD"]')
count_of_divs = len(content)
print(count_of_divs)
page = 1
res = list()
while(1):
    for i in range(count_of_divs):
        web.implicitly_wait(10)
        content = web.find_elements_by_xpath('//*[@id="page-content"]/div/div[1]/div[2]/div[4]/div[@class="SearchResultList_listElementWrapper__KRuKD"]')
        content[i].click()
        web.implicitly_wait(10)
        # 创建字典保存数据
        dic = dict()
        # Name
        title = web.find_element_by_xpath('//*[@id="page-content"]//div[@class="DetailHeaderRow_pageTitleCol__oeydp"]/h1')
        dic["Name"] = str(title.text)
        # Street
        address = web.find_element_by_xpath('//*[@id="page-content"]//a[@class="l--link DetailMapPreview_addressValue__pQROv"]')
        street = str(address.text).split(",")[0]
        dic['Street'] = street
        # PLZ
        PLZ = str(address.text).split(",")[1].strip().split(" ")[0]
        dic['PLZ'] = PLZ
        # City
        City = str(address.text).split(",")[1].strip().split(" ")[1]
        dic['City'] = City
        # Business
        try:
            Business = web.find_element_by_xpath('//*[@id="page-content"]//dd[last()]').text
            dic['Business'] = str(Business)
        except:
            dic['Business'] = ""
        # Phone
        try:
            Phone = web.find_element_by_xpath('//*[@id="page-content"]//label[contains(text(), "Telefon")]/parent::*//a').text
            dic['Phone'] = str(Phone)
        except:
            dic['Phone'] = ""
        # Mobile
        try:
            Mobile = web.find_element_by_xpath('//*[@id="page-content"]//label[contains(text(), "Mobiltelefon")]/parent::*//a').text
            dic['Mobile'] = str(Mobile)
        except:
            dic['Mobile'] = ""
        # Email
        try:
            Email = web.find_element_by_xpath('//*[@id="page-content"]//label[contains(text(), "Email")]/parent::*//a').text
            dic['Email'] = str(Email)
        except:
            dic['Email'] = ""
        # Website
        try:
            Website = web.find_element_by_xpath('//*[@id="page-content"]//label[contains(text(), "Website")]/parent::*//a').text
            dic['Website'] = str(Website)
        except:
            dic['Website'] = ""
        d = dic["Name"], dic["Street"], dic["PLZ"], dic["City"], dic["Business"], dic["Phone"], dic["Mobile"], dic["Email"], dic["Website"]
        ws.append(d)  # 每次写入一行    
        web.back()
    page += 1
    try:
        xpathstr = '//*[@id="pagination-page-'+str(page)+'"]'
        web.find_element_by_xpath(xpathstr).click()
        web.implicitly_wait(10)
        content = web.find_elements_by_xpath('//*[@id="page-content"]/div/div[1]/div[2]/div[4]/div[@class="SearchResultList_listElementWrapper__KRuKD"]')
        count_of_divs = len(content)
        print("page"+str(page)+"begins")
    except:
        # finish
        break

wb.save(fileName)