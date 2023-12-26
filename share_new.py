import glob, time, os
from selenium.webdriver.remote.webelement import WebElement
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 定義好會用到的函式
# 這邊參考了網路上有人提供的拖拉式放檔案的方法，可以用在所有「拖曳你的檔案至此」區塊
# JavaScript: HTML5 File drop
# source            : https://gist.github.com/florentbr/0eff8b785e85e93ecc3ce500169bd676
# param1 WebElement : Drop area element
# param2 Double     : Optional - Drop offset x relative to the top/left corner of the drop area. Center if 0.
# param3 Double     : Optional - Drop offset y relative to the top/left corner of the drop area. Center if 0.
# return WebElement : File input

JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"

def drop_files(element, files, offsetX=0, offsetY=0):
    driver = element.parent
    isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
    paths = []

    # ensure files are present, and upload to the remote server if session is remote
    for file in (files if isinstance(files, list) else [files]) :
        if not os.path.isfile(file) :
            raise FileNotFoundError(file)
        paths.append(file if isLocal else element._upload(file))

    value = '\n'.join(paths)
    elm_input = driver.execute_script(JS_DROP_FILES, element, offsetX, offsetY)
    elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

def share(id,password,path,message):
    WebElement.drop_files = drop_files
    #開啟瀏覽器
    options = webdriver.ChromeOptions() 
    options.add_argument('--headless') # 啟動無頭模式 
    options.add_argument('--disable-gpu') # windowsd必須加入此行 原文網址：https://itw01.com/FYB2UED.html
    options.add_argument('--log-level=1')
    #option=webdriver.ChromeOptions()
    #option=webdriver.EdgeOptions()
    #option.add_argument('--headless')
    driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    driver.implicitly_wait(5)#等待時間
    #driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)

    #登入
    driver.find_element(by=By.NAME, value = "username").send_keys(id)
    driver.find_element(by=By.NAME, value = "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3)').click()
    time.sleep(4)

    #進入主畫面
    url=driver.current_url
    if url=='https://www.instagram.com/accounts/login/':
        return False
    driver.get(url)
    time.sleep(2)
    #跳出儲存訊息
    check_button=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
    check_button.click()
    time.sleep(4)
    '''#跳出訊息顯示#背景執行未跳出
    info_button=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    info_button.click()
    time.sleep(5)'''
    #點擊上傳按鈕
    new_post_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div')
    new_post_button.click()
    time.sleep(2)
    dropzone = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button')
    # 選擇一個圖片、影片
    dropzone.drop_files(path)
    time.sleep(2)
    # 縮放 (這邊選擇原始比例，如果要1:1那可以直接跳過這段)
    #driver.find_element(By.CSS_SELECTOR, '[aria-label="選擇「裁切」"]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button/div').click()
    time.sleep(2)
    # 挑選你要的比例
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]/div').click()
    time.sleep(2)
    # 下一步    
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
    time.sleep(2)
    # 濾鏡選擇，這邊不選擇，直接下一步
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div').click()
    time.sleep(4)
    # 填寫內文
    #post = driver.find_element(By.CSS_SELECTOR, '[aria-label="撰寫說明文字……"]')
    post=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]')
    post.send_keys(message)
    time.sleep(2)

    # 送出
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()

    # 關閉浮動視窗
    #driver.find_element(By.CSS_SELECTOR, '[aria-label="關閉"]').click()
    driver.close()

    return True

#message = """
    #IG_Robot 
    #Python
#    """
#print(share('its_annachen','anna901228ig',"C:/Users/Anna_Chen/Desktop/LINE_ALBUM_20220426-0083_220519_24.jpg",message))