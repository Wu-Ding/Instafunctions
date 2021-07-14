from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


""" ================================ WARNING =================================
The script will log you into your account each time.
Doing so multiple times will result in instagram thinking you are a bot and will lead to a temporary suspension.
I have learned that through personal experience.
Be warned!
~ 90% accuracy. Accuracy increases if target == username.
    ==========================================================================
"""


def check_insta_followers(target, username, password):
    """Checks who doesn't follow you back

    Args:
        target (str)
        username (str)
        password (str)

    Returns:
        list_of_snakes (List of str)
    """
    
    #Open the Chrome browser using webdriver
    browser = webdriver.Chrome(ChromeDriverManager().install())
    
    #Go to instagram.com
    webpage = 'https://www.instagram.com/'
    browser.get(webpage)
    
    #Wait 1 second for the page to load
    time.sleep(1)

    #Find the elements where to input the username and password respectively
    username_input = browser.find_element_by_name('username')
    password_input = browser.find_element_by_name('password')

    #Input the user's username and password and press ENTER
    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    #Wait 3 seconds for the page to load
    time.sleep(3)

    #Find the button that displays "Not Now" and click on it
    for i in browser.find_elements_by_tag_name('button'):
        if i.text=='Not Now':
            i.click()
            break
    
    #Find the button that displays "Not Now" and click on it    
    for i in browser.find_elements_by_tag_name('button'):
        if i.text=='Not Now':
            i.click()
            break

    #Wait 2 seconds for the page to load
    time.sleep(2)
    
    #Find the search bar and enter the target username
    #When it loads, press enter twice
    search_box = browser.find_element_by_xpath("//input[@placeholder='Search']")
    search_box.send_keys(target)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    
    #Find the button that loads the target's followers and click on it
    followers_link = "'/" + target + "/followers/']"
    followers_button = browser.find_element_by_xpath("//a[@href=" + followers_link)
    num_of_followers = followers_button.text
    num_of_followers = num_of_followers.split(" ")[0]
    num_of_followers = int(num_of_followers)
    followers_button.click()
    time.sleep(1)
    
    #Find the first follower
    followers_find = browser.find_element_by_xpath("//div[@aria-label='Followers']")
    first_follower = followers_find.find_element_by_tag_name('a')
    
    #Scroll down to the bottom of the follower list
    for i in range(num_of_followers//12 + 5):
        first_follower.send_keys(Keys.END)
        time.sleep(1)
        first_follower = followers_find.find_element_by_tag_name('a')
        
    #Add all the follower elements to a list    
    followers_element_list = followers_find.find_elements_by_tag_name('a')
    time.sleep(0.5)
    
    #Go through the list and add all non-empty usernames to a separate list
    followers_list = []
    for i in followers_element_list:
        if len(i.text) != 0:
            followers_list.append(i.text)
    followers_list.append("People")
    followers_list.append("Hashtags")
    
    #Find the button to close the follower list and click it
    close_button = followers_find.find_element_by_tag_name('button')
    close_button.click()
    time.sleep(1)
    
    #Find the button that loads the target's following and click on it
    following_link = "'/" + target + "/following/']"
    following_button = browser.find_element_by_xpath("//a[@href=" + following_link)
    num_of_following = following_button.text
    num_of_following = num_of_following.split(" ")[0]
    num_of_following = int(num_of_following)
    following_button.click()
    time.sleep(1)
    
    #Find the first following
    following_find = browser.find_element_by_xpath("//div[@aria-label='Following']")
    time.sleep(1)
    first_find = following_find.find_element_by_tag_name('li')
    first_following = first_find.find_element_by_tag_name('a')
    
    #Scroll down to the bottom of the following list
    for i in range(num_of_following//12 + 5):
        first_following.send_keys(Keys.END)
        time.sleep(1)
        first_following = first_find.find_element_by_tag_name('a')
        
        
    #Add all the following elements to a list     
    following_element_list = following_find.find_elements_by_tag_name('a') 
    time.sleep(0.5)
    
    #Create the list of snakes
    #If a username is in the following category, but not the followers, they are added to the snake list
    snake_list = []
    for i in following_element_list:
        if len(i.text) != 0:
            if (i.text not in followers_list):
                snake_list.append(i.text)
    
    #Close the browser
    browser.close()
    
    #Print and return the snake_list
    print()
    print(snake_list)
    print()
    print(target + " is following " + str(len(snake_list)) + " snakes.")
    return snake_list
        

    
if __name__ == "__main__":
    
    target = "TARGET"       #Enter the username of the target
    username = "USERNAME"   #Enter your username
    password = "PASSWORD"   #Enter your password
    
    check_insta_followers(target, username, password)
    
    
    
    
    