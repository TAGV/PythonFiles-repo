import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

url = "https://www.youtube.com/c/CodingTech/videos"
driver = webdriver.Firefox()

driver.get(url)

video_list = []

videos = driver.find_elements(By.CLASS_NAME,'style-scope ytd-grid-video-renderer')
for video in videos:
    title = video.find_element(By.XPATH,'.//*[@id="video-title"]').text             #Check the prefixxed dot symbol to loop through all xpath
    views = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    uploadtime = video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    #print(views)
    vid_items = {
        'title':title,
        'views':views,
        'uploadtime':uploadtime
    }
    video_list.append(vid_items)

#print(len(videos))
df = pd.DataFrame(video_list)
print(df)



time.sleep(10)
driver.quit()