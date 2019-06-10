#encoding=utf-8
import requests

import urllib.request

from bs4 import BeautifulSoup

import os

import time

import sys

from selenium import webdriver

import urllib.request

import base64

from selenium.webdriver.common.keys import Keys

word = sys.argv[1]

url = 'https://www.google.com.tw/search?num='+sys.argv[2]+'&q='+word+' &rlz=1C1CAFB_enTW617TW621&source=lnms&tbm=isch&sa=X&ved=0ahUKEwienc6V1oLcAhVN-WEKHdD_B3EQ_AUICigB&biw=1128&bih=863'
# url = 'https://www.pixiv.net/'

photolimit = int(sys.argv[2])


folder_path ='./photo/'

if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

    os.makedirs(folder_path) #Create folder


driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url)
# itmes=driver.find_elements_by_tag_name('img')

# driver.find_elements_by_class_name('rg_bx')

# urls = []
# for r in driver.find_elements_by_class_name('rg_bx'):
#     urls.append(r.find_element_by_tag_name('a').get_attribute('href'))

# for i in range(1, len(urls)):
#     #  print(urls[i])
#     driver.get(urls[i])
#     print( driver.find_element_by_class_name('irc_mi').get_attribute("src") )
#     urllib.request.urlretrieve(driver.find_element_by_class_name('irc_mi').get_attribute("src"), filename= "%s %s.png" % (folder_path, i ) ) 
for i in range( int(photolimit/2)) :
    driver.find_element_by_tag_name('html').send_keys(Keys.SPACE) 
    time.sleep(0.1)

for i in range(1,photolimit+2) :
        #html = requests.get(itmes[i].get_attribute("src")) # use 'get' to get photo link path , requests = send request
        
        
        # print(driver.find_elements_by_tag_name('img')[i].get_attribute("src"))
        img_name = folder_path + str(i-1) + '.png'
        # print(type(driver.find_elements_by_tag_name('img')[i].get_attribute("src")))
        if driver.find_elements_by_tag_name('img')[i].get_attribute("src") is not None:
            if driver.find_elements_by_tag_name('img')[i].get_attribute("src").find('data:image/jpeg;base64,') !=-1:
                # print(str(base64.b64encode(driver.find_elements_by_tag_name('img')[i].get_attribute("src").split('data:image/jpeg;base64,')[1])))
                with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入

                    file.write(base64.b64decode(driver.find_elements_by_tag_name('img')[i].get_attribute("src").split('data:image/jpeg;base64,')[1]))

                    file.flush()

                file.close() #close file
            else:
                # print("image %s %s" % ( i, driver.find_elements_by_tag_name('img')[i].get_attribute("src") ))
                urllib.request.urlretrieve(driver.find_elements_by_tag_name('img')[i].get_attribute("src"), filename=img_name)
            
            print('第 %d 張' % ( i+ 1))


        # with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入

        #     file.write(base64.b64decode(itmes[i].get_attribute("src")))

        #     file.flush()

        # file.close() #close file




# headers = {'User-Agent': 'Mozilla/5.0'}


# response = requests.get(url,headers = headers,verify = False,stream=True) #使用header避免訪問受到限制

# soup = BeautifulSoup(response.content, 'html.parser')

# # print(soup.find_all('img'))

# items = soup.find_all('img')

# folder_path ='./photo/'

# if (os.path.exists(folder_path) == False): #判斷資料夾是否存在

#     os.makedirs(folder_path) #Create folder



# for index , item in enumerate (items):

#     if (item and index < photolimit ):

#         html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request

#         img_name = folder_path + str(index + 1) + '.png'



#         with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入

#             file.write(html.content)

#             file.flush()

#         file.close() #close file
    

#         # length=1000 
#         # for i in range(0,2): 
#         #     js="var q=document.body.scrollTop="+str(length)  
#         #     driver.execute_script(js)  
#         #     time.sleep(0.2) 
#         #     length+=length

#         print('第 %d 張' % (index + 1))

#         time.sleep(0.1)



print('完成')
driver.close()