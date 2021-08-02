# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
url = 'https://www.sogou.com/'
response = requests.get(url=url)
page_text = response.text
print(page_text)
with open('./sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
    print("打印结束了！")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
