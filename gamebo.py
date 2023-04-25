import time
from pprint import pprint
from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:/Users/paulw/Documents/Developement/chromedriver.exe'
running = True
driver = webdriver.Chrome(executable_path=chrome_driver_path)


count_id = 'money'
cps_id = 'cps'
store_id = 'store'
cookie_button_id = 'cookie'

q_url = 'http://orteil.dashnet.org/experiments/cookie/'

driver.get(q_url)

def click_cookie():
    driver.find_element_by_id('cookie').click()


def update_data(_store):
    _game_data = {
        'cookies': driver.find_element_by_id(count_id).text,
        'store': _store.find_elements_by_css_selector('div b')
    }
    _game_data['store'].pop()
    return _game_data


def update_prices(_game_data):
    _costs = []
    for items in _game_data['store']:
        temp = items.text.split(" ")
        new_cost = temp[-1].replace(",", "")
        _costs.append(new_cost)

    return _costs


while True:
    time.sleep(0.5)
    click_cookie()
    store = driver.find_element_by_id('store')
    game_data = update_data(store)

    string_costs = update_prices(game_data)

    costs = [int(cost) for cost in string_costs]
    costs.reverse()

    if ',' in game_data['cookies']:
        game_data['cookies'] = game_data['cookies'].replace(',', "")

    score = int(game_data['cookies'])
    game_data['store'].reverse()

    for item in range(len(costs)):
        if score >= costs[item]:
            game_data['store'][item].click()
