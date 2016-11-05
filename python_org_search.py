from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sets import Set
import os
import time
import json
import pdb

# Define driver
chromedriver="/Users/Kenneth/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
# ----------------------------


# Open Instagram
def open_instagram():
	driver.get("https://www.instagram.com/")
	driver.implicitly_wait(5000) 
# ----------------------------


# Log in as "Miskuoted"
def login():
	iguserelem = driver.find_element_by_name("username")
	iguserelem.send_keys("miskuoted")
	igpwelem = driver.find_element_by_name("password")
	igpwelem.send_keys("v4nhalen")
	igpwelem.send_keys(Keys.RETURN)
	driver.implicitly_wait(5)
# ----------------------------


# Wait until element is visible
def visible_element(xpath, timeout=10):
	WebDriverWait(driver, timeout).until(
	    EC.visibility_of_element_located(
	        (By.XPATH, xpath)
	    )
	)





# videos
# div class _tqoyh _pwe27
# 	div class _2tomm
# 		img src https://scontent-lga3-1.cdninstagram.com/t51.2885-15/s640x640/e15/14722976_765058043632088_4344572218353647616_n.jpg?ig_cache_key=MTM3NjQwMjMyMjkxNzk4ODY2Mw%3D%3D.2


# images
# div class _jjzlb
# 	img src https://scontent-lga3-1.cdninstagram.com/t51.2885-15/e35/14677351_950376681740618_8705822812624912384_n.jpg?ig_cache_key=MTM3Njc1MDA2ODQzNDIzNDE4Mw%3D%3D.2







# Checks to see if there are likes
def get_like_element(): 
    try:
        return driver.find_element_by_xpath('//div[@class="'+'_iuf51 _oajsw'+'"]')
    except:
        return None
# ----------------------------


# Gets number of likes
def get_number_of_likes():
    like_element = get_like_element()
    return like_element.text
# ----------------------------


#Checks to see if these are the views
def get_view_element():
    try:
        return driver.find_element_by_xpath('//div[@class="'+'_iuf51 _3sst1'+'"]')
    except:
        return None
# ----------------------------


# Gets the number of views
def get_number_of_views():
    view_element = get_view_element()
    return view_element.text
# ----------------------------


# Checks to see if this is an image
def get_image_element(): 
    try:
        return driver.find_element_by_xpath('//div[@class="_jjzlb"]/img[@src]')
    except:
        return None
# ----------------------------


# Gets image src element
def get_image_src_value(image_element):
    return image_element.get_attribute('src')
# ----------------------------


# Checks to see if this is a video
def get_video_element(): 
    try:
        return driver.find_element_by_xpath('//div[@class="_2tomm"]/img[@src]')
    except:
        return None
# ----------------------------


# Gets image src element
def get_video_src_value(video_element):
    return video_element.get_attribute('src')
# ----------------------------


# Gets post src element
def get_post_src_value():
	image_element = get_image_element()
	if image_element:
		return get_image_src_value(image_element)
	else:
		return get_video_src_value(get_video_element())
# ----------------------------


# Gets last pImage id
def get_last_p_image_tag(): 
    pImage = driver.find_elements_by_xpath('//div[@class="_jjzlb"]/img[@id]')[-1]
    return pImage.get_attribute('id')
# ----------------------------


# Checks to see if there is a user location
def get_location_element():
    try:
        return driver.find_element_by_xpath('//a[@class="'+'_kul9p _rnlnu'+'"]')
    except:
        return None
# ----------------------------

# Gets the user location
def get_user_location():
    location_element = get_location_element()
    if location_element:
        return location_element.text
    else: 
        return None
# ----------------------------

#Clicks "Show more comments" button
def show_all_comments():
    try:
        while driver.find_element_by_xpath('//button[@class="'+'_l086v _ifrvy'+'"]'):
            driver.find_element_by_xpath('//button[@class="'+'_l086v _ifrvy'+'"]').click()
            time.sleep(0.5)
    except:
        return None
# ----------------------------


# Gets all of the comments
def get_comments():
    user_comment_list = []

    users = driver.find_elements_by_xpath('//li[@class="'+'_nk46a'+'"]//a[@class="'+'_4zhc5 notranslate _iqaka'+'"]')
    for u in users:
        user_comment_list.append([u.text])

    comments = driver.find_elements_by_xpath('//li[@class="'+'_nk46a'+'"]//span')
    idx = 0
    for c in comments:
        user_comment_list[idx].append(c.text)
        idx+=1

    comment_dicts = [] 
    for uc in user_comment_list:
        comment = {}
        comment['user'] = uc[0]
        comment['comment'] = uc[1]
        comment_dicts.append(comment)

    return comment_dicts
# ----------------------------

#Gets the post time
def get_post_time():
    return driver.find_element_by_xpath('//time[@class="'+'_379kp'+'"]').get_attribute("datetime")
# ----------------------------


# Gets the OP username
def get_user_name():
    return driver.find_element_by_xpath('//a[@class="'+'_4zhc5 notranslate _ook48'+'"]').text
# ----------------------------


# Scrolls down
def scroll_down():
    print 'scrolling down'
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
# ----------------------------

# Scrolls up
def scroll_up():
    print 'scrolling up'
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
# ----------------------------


# CLICK right arrow
def click_next_arrow():
	driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()
# ----------------------------


# PRESS right arrow
def right_arrow_press():
	right_arrow = driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]')
	right_arrow.send_keys(Keys.ARROW_RIGHT)
# ----------------------------


# CLICK left arrow
def click_left_arrow():
	driver.find_element_by_xpath('//a[@class="'+'_qdy3e coreSpriteLeftPaginationArrow'+'"]').click()
# ----------------------------

# check if left arrow exists
def left_arrow_exists():
	try:
		driver.find_element_by_xpath('//a[@class="'+'_qdy3e coreSpriteLeftPaginationArrow'+'"]')
		return True
	except: 
		return False
# ----------------------------


# CLICK exit button
def click_exit_button():
	driver.find_element_by_xpath('//button[@class="'+'_3eajp'+'"]').click()
# ----------------------------


# opening file to write to
# f is the file it's gonna write to
def grab_user_post(f):
    dict = {}

    if get_like_element():
        dict['likes_count'] = get_number_of_likes()
    else: 
        dict['views_count'] = get_number_of_views()

    dict['user'] = get_user_name()
    dict['post_time'] = get_post_time()
    dict['post_location'] = get_user_location()
    show_all_comments()
    dict['comments'] = get_comments()

    f.write(json.dumps(dict))
    f.write('\n')
# ----------------------------


# Scrolls until more images are loaded
def scroll_until_more_loaded():
    last_p_image_tag = None
    current_p_image_tag = get_last_p_image_tag()
    while(current_p_image_tag == last_p_image_tag):
        last_p_image_tag = current_p_image_tag
        scroll_up()
        scroll_down()
        current_p_image_tag = get_last_p_image_tag()
# ----------------------------


# THIS IS THE ALGORITHM!!!!!!
open_instagram()
login()


# Search based on tag
visible_element(r"""//input[@placeholder='Search']""")

searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)
driver.get("https://www.instagram.com/explore/tags/acl/")
searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
)
# ----------------------------


# WebDriverWait(driver, 10)
# element = driver.find_element_by_tag_name('div').find_element_by_tag_name('a').find_element_by_tag_name('div').find_element_by_tag_name('div').find_element_by_tag_name('img')
# actions = ActionChains(driver)
# actions.move_to_element(element).click().perform()
# WebDriverWait(driver, 10)


# Finds the TOTAL number of hashtags
stop = driver.find_element_by_xpath('//span[@class="'+'_bkw5z'+'"]').text
stop = stop.replace(',', '')
stop = int(stop)
stop -= 1
print 'stopCount = {}'.format(stop)
# ----------------------------


# Click "Load More" button
driver.find_element_by_xpath('//a[@class="'+'_oidfu'+'"]').click()
time.sleep(1)
# ----------------------------


# new algo for grabbing images
with open('acl_instagram_testand.txt', 'a') as f:
    post_src_set = Set()
    # get image paths
    while(len(post_src_set) < stop):
        nodes = driver.find_elements_by_xpath('//div[@class="'+'_ovg3g'+'"]')
        # get last element of selected nodes
        node_count = len(nodes)
        node_count_offset = 1 
        node = nodes[node_count - node_count_offset]
        node.click()
        # check get image src value
        post_src_value = get_post_src_value()
        print post_src_value
        print post_src_set

        print post_src_value not in post_src_set
        print node_count_offset <= node_count

        print node_count_offset
        print node_count
        while((post_src_value not in post_src_set) and (node_count_offset <= node_count)):
            post_src_set.add(post_src_value)
            time.sleep(3)
            pdb.set_trace()
            # grab_user_post(f)
            click_left_arrow()
            print len(post_src_set)
            post_src_value = get_post_src_value()
            node_count_offset += 1
       	click_exit_button()
        scroll_until_more_loaded()


# # Old algorithm :(
# previous_image_count = 0
# nodes = driver.find_elements_by_xpath('//div[@class="'+'_ovg3g'+'"]')
# current_image_count = len(nodes)
# retry_count = 0

# def retry():
#     scroll_up()
#     scroll_down()`

# with open('acl_instagram_testand.txt', 'a') as f:
#   while (current_image_count < stop):
#       nodes = driver.find_elements_by_xpath('//div[@class="'+'_ovg3g'+'"]')
#       current_image_count = len(nodes)

#       # checking to retry
#       if previous_image_count == current_image_count:
#           retry()
#       #     retry_count += 1
#       # elif retry_count >= 5:
#       #     print 'exceeded retry count, giving up.'
#       #     break
#       # retry_count = 0

#       for node_idx in xrange(previous_image_count, current_image_count):
#           nodes[node_idx].click()
#           grab_user_post(f)
#           driver.find_element_by_xpath('//button[@class="'+'_3eajp'+'"]').click()
      
#       print current_image_count
#       print previous_image_count

#       previous_image_count = current_image_count
#       scroll_down()
#       # time.sleep(1)




# driver.find_element_by_xpath('//img@src="'+'_3eajp'+'"]').click()







# driver.quit()






























# like_element = driver.find_element_by_xpath('//span[@class="'+'_9jphp'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_9jphp'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_tf9x3'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# # Pull views

# like_element = driver.find_element_by_xpath('//span[@class="'+'_9jphp'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_tf9x3'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# like_element = driver.find_element_by_xpath('//span[@class="'+'_tf9x3'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()

# time.sleep(2)

# # Pull non-numbered likes

# like_element = driver.find_element_by_xpath('//div[@class="'+'_iuf51 _oajsw'+'"]')
# print like_element.text
# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()


# like_element1 = driver.find_element_by_xpath('//a[@class="'+'_tf9x3'+'"]')
# print like_element1

# driver.find_element_by_xpath('//a[@class="'+'_de018 coreSpriteRightPaginationArrow'+'"]').click()



#element_list = len(like_element.find_elements_by_tag_name("span"))
# print element_list


# driver.find_element_by_id('pImage_0').click()

#.Click "xpath=//input[contains(@data-reactid, '$0.0.0.0.0.1.0')]"
#   .Type "xpath=//input[contains(@data-reactid, '$0.0.0.0.0.1.0')]", "5720 lansdowne ave Philadelphia, PA" 


#driver = webdriver.Firefox()
#driver.get("https://protonmail.com/")
#protonelem = driver.find_element_by_name("u")
#protonelem.send_keys("josiejosiejosie123")
#protonelem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

#driver.implicitly_wait(5)

#loginelem = driver.find_element_by_name("password")
#loginelem.send_keys("v4nhalen")

#logincelem = driver.find_element_by_name("passwordc")
#logincelem.send_keys("v4nhalen")

#mailelem = driver.find_element_by_name("MBpassword")
#mailelem.send_keys("v4nhalen")

#mailcelem = driver.find_element_by_name("MBpasswordc")
#mailcelem.send_keys("v4nhalen")
#mailcelem.send_keys(Keys.RETURN)

#driver.implicitly_wait(5)

#recaptcha1elem = driver.find_element_by_name("11").click()

#driver.implicitly_wait(5)



#driver.get("https://docs.google.com/spreadsheets/d/1xIPLd7UgMcnmocbFfQRsOI58N1SOeDsy0pmsn2P5eAs/edit#gid=0");
#gmailelem = driver.find_element_by_name("Email")
#gmailelem.send_keys("kashmir276@gmail.com")
#gmailelem.send_keys(Keys.RETURN)

#driver.implicitly_wait(5)

#passwordelem = driver.find_element_by_name("Passwd")
#passwordelem.send_keys("Wordsworth69!")
#passwordelem.send_keys(Keys.RETURN)
#driver.findElement(By.xpath("//tr[@id='0-r-column-head-section$3']/td[4]")).click();
#driver.findElement(By.xpath("//table/tbody/tr/td[3]/div/div/div")).click();
#driver.findElement(By.xpath("//table/tbody/tr/td[3]/div/div/div")).sendKeys("Hello World!");
#driver.findElement(By.xpath("//tr[@id='0-r-column-head-section$3']/td[5]")).click();
