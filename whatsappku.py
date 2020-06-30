#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
from autoreply.pacalaku import *
import os
import time

#bot whatsapp using webdriver

apiku = "~D~zlWDwp04W8sLki.a~Tmpxm_vydwCX0f1S8xcW"
Gosend_options = Options()
Gosend_options.add_argument("--user-data-dir=#ganti sama file chrome lu")
Gosend = webdriver.Chrome("#path cromedriver lu disni",options=Gosend_options)
Gosend.get('https://web.whatsapp.com')


ACTIVATE_BOT = "_2iq-U"
MESSAGE_COLUMNS = "_3uMse"  # class name of column input
MESSAGE_BUTTON = "_1U1xa"
CONTACT_NAME = "DP7CM"


def say_hi():
    return ["「Hi im Gosend self bot from Wardana Accounts」"]

def menu():
    return [
        "╔════════════════════╗",
        " ◄]·✪·Gofood_menu·✪·[►",
        "╠════════════════════╝",
        "╠❂➣ " "/menu",
        "╠❂➣ " "/hi",
        "╠❂➣ " "/quit",
        "╠❂➣ " "/sayang",
        "╠❂➣ " "/website :「query",
        "╠❂➣ " "/google  :「query",
        "╠❂➣ " "/images  :「query",
        "╚════════════════════╝"
    ]
def pesan():
    return ["「Turning Off Gosend..」\n", "/bye"]

def turnoff():
    time.sleep(0.5)
    Gosend.quit()

def ping():
    banner = os.system("""echo '╔════════════════════╗\n🍁Network Connection🍁\n╚════════════════════╝'""")
    google = os.system("""ping -qc 1 google.com 2>&1 |   awk -F"/" 'END{ print (/^rtt/? "╠❂➣ Ping Google   : OK "$5" ms":"FAIL") }'""")
    facebook = os.system("""ping -qc 1 whatsapp.com 2>&1 |   awk -F"/" 'END{ print (/^rtt/? "╠❂➣ Ping Facebook : OK "$5" ms":"FAIL") }'""")
    whatsapp = os.system("""ping -qc 1 web.whatsapp.com 2>&1 |   awk -F"/" 'END{ print (/^rtt/? "╠❂➣ Ping Whatsapp : OK "$5" ms":"FAIL") }'""")
    return [ banner , google, facebook, whatsapp]

def fload(count, msg):
    message = msg
    counts = count
    for floading in range(counts):
        send_message([message])
        time.sleep(0.1)

def chat_pacar():
    sayang = Gosend.find_elements_by_class_name("message-in")
    temp_message = []

    try:
        for kasih in sayang:
            msg_pcr = kasih.find_elements_by_class_name("copyable-text")
            for msg in msg_pcr:
                temp_message.append(msg.text.lower())

        if len(temp_message) > 0:
            return temp_message[-1]

    except StaleElementReferenceException as e:
        print(str(e))

    return False

def chat_history():
    text_bubbles = Gosend.find_elements_by_class_name("message-out")
    tmp_message = []

    try:
        for bubble in text_bubbles:
            msg_texts = bubble.find_elements_by_class_name("copyable-text")
            for msg in msg_texts:
                tmp_message.append(msg.text.lower())

        if len(tmp_message) > 0:
            return tmp_message[-1]

    except StaleElementReferenceException as e:
        print(str(e))

    return False


def send_message(msg):
    whatsapp_msg = Gosend.find_element_by_class_name(MESSAGE_COLUMNS)
    for i in msg:
        whatsapp_msg.send_keys(i)
        whatsapp_msg.send_keys(Keys.SHIFT, Keys.RETURN)
        time.sleep(0.2)
    whatsapp_button = Gosend.find_element_by_class_name(MESSAGE_BUTTON)
    whatsapp_button.click()

def is_command_message(command_msg):
    if command_msg[0] == "/":
        return True

    time.sleep(0.5)
    return False

def whatsapp_contacts():
    contacts = Gosend.find_elements_by_class_name(CONTACT_NAME)

    return [contact.text for contact in contacts]


class SearchMachine():
    search_url = False
    attachment_type = "img"

    def __init__(self, **sayang):
        # Goolge search biasa
        self.google_search = sayang.get('search', False)

        # Images Google Search
        self.images_search = sayang.get('images', False)

        # Music Goolge Search
        self.music_search = sayang.get('music', False)

        # Visit Website
        self.website_search = sayang.get('website', False)

    def search(self, query):
        send_message(["Searching Google For: '{query}'".format(query=query)])

        if self.google_search:
            self.search_url = 'https://google.com/search?hl=en&q={query}'.format(query=query)

    def images(self, query):
        send_message(["Searching Images For: '{query}'".format(query=query)])

        if self.images_search:
            self.search_url = 'https://www.google.com/search?hl=en&q={query}&tbm=isch'.format(query=query)

    def website(self, query):
        send_message(["Visiting Website: '{query}'".format(query=query)])

        if self.website_search:
            self.search_url = 'http://{query}'.format(query=query)

    def excecute_search(self):
        # TODO - fungsi untuk menjalankan fungsi search
        if self.search_url:
            Gosend.execute_script("window.open('', '_blank');")
            Gosend.switch_to_window(Gosend.window_handles[1])
            Gosend.get(self.search_url)
            # time.sleep(0.5)
            Gosend.save_screenshot('screenshot.png')
            Gosend.close()
            Gosend.switch_to_window(Gosend.window_handles[0])

            self._attach_and_send_result()

        else:
            send_message(["「Maaf Mas Orderannya Fiktif!, coba cek output server untuk lebih jelasnya」"])

    def _attach_and_send_result(self):
        attach_xpath = '//*[@id="main"]/header/div[3]/div/div[2]/div'
        send_file_attach = "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div"
        reply_btn = "_1qPwk"
        reply_chat = "//*[@id='app']/div/span[4]/div/ul/li[2]/div"

        if self.attachment_type == "img":
            attach_type_xpath = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input"
        elif self.attachment_type == "doc":
            attach_type_xpath = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input"
        elif self.attachment_type == "contact":
            attach_type_xpath = "/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[4]/button/input"

        try:

            # reply bot message
            reply_tbl = Gosend.find_elements_by_class_name(reply_btn)[-1]
            reply_tbl.click()
            time.sleep(0.1)
            reply_msg = Gosend.find_element_by_xpath(reply_chat)
            reply_msg.click()
            #open attach menu
            attach_btn = Gosend.find_element_by_xpath(attach_xpath)
            attach_btn.click()

            # find file attach
            time.sleep(1)
            attach_img_btn = Gosend.find_element_by_xpath(attach_type_xpath)

            # TODO send file img to whatsapp
            attach_img_btn.send_keys(os.getcwd() + "/screenshot.png")
            time.sleep(1)
            send_btn = Gosend.find_element_by_xpath(send_file_attach)
            send_btn.click()

        except (NoSuchElementException, ElementNotVisibleException) as e:
            send_message([str(e)])
            send_message(["「Maaf mas packet yang diminta rusak, mohon coba lagi..」"])


class account(object):
    command_msg = False
    command_msg_id = False

    command_history = []
    last_command = ""

    def __init__(self, contact_list):
        self.contacts = contact_list

    def get_contact(self):
        return self.contacts

    def set_last_chat_message(self, msg, time_message):
        self.command_msg = msg
        self.command_msg_id = time_message

    def get_last_chat_message(self):
        return self.command_msg, self.command_msg_id

    def set_last_command(self, command):
        self.last_command = command
        self.command_history.append(command)

class GosendBucin(object):

    def __init__(self):
        self.bucin = account(contact_list=whatsapp_contacts)
        self.init_bucin()

    # def bucin_looping(self):
    #     while True:
    #         self.init_bucin()

    def init_bucin(self):
        while True:
            last_msg = chat_pacar()
            stop_msg = chat_history()

            if stop_msg != "/stop":
                time_id = time.strftime('%H-%M-%S', time.gmtime())

                last_saved_msg, last_saved_msg_id = self.bucin.get_last_chat_message()
                if last_saved_msg != last_msg and last_saved_msg_id != time_id:
                    self.bucin.set_last_chat_message(msg=last_msg, time_message=time_id)

                    print("╠❂➣Girlfriend  : ", whatsapp_contacts())
                    print("╠❂➣Message     : ", self.bucin.get_last_chat_message())

                    pacalaku = pacarku(apiku, last_msg)
                    value = pacalaku.chatan()
                    send_message([value])

            else:
                break

class GosendDriver(object):
    def __init__(self):
        self.username = account(contact_list=whatsapp_contacts())
        self.init_driver()

    def init_driver(self):
        while True:
            self.gaskeun()

    def gaskeun(self):
        command_msg = chat_history()

        if command_msg:
            time_message = time.strftime("%H-%M-%S", time.gmtime())

            last_saved_msg, last_saved_msg_id = self.username.get_last_chat_message()
            if last_saved_msg != command_msg and last_saved_msg_id != time_message:
                self.username.set_last_chat_message(msg=command_msg, time_message=time_message)

                print("Friend-Chat : ", whatsapp_contacts())
                print("Message     : ", self.username.get_last_chat_message())

                is_command = is_command_message(command_msg=command_msg)
                if is_command:
                    self.username.set_last_command(command_msg)
                    self.bot_options(command=command_msg)

    def bot_options(self, command):
        gofood_menu = {
            "hi": say_hi,
            "quit": pesan,
            "bye": turnoff,
            "menu": menu
        }
        gofood_menu_keys = gofood_menu.keys()

        try:
            command_args = command[1:].split(" ", 1)
            print("Gofood_menu :  {cmd}".format(cmd=(command_args)))

            if len(command_args) == 1 and command_args[0] in gofood_menu_keys:
                send_message(gofood_menu[command_args[0]]())
            else :
                if command_args[0] == "google":
                    if len(command_args) == 1:
                        send_message(["「Usage : /google {query}」"])

                    elif len(command_args) == 2:
                        value = command_args[1] or "empy"
                        if value == "empty":
                            send_message(["「Usage : /google {query}」"])
                        else:
                            query = "".join(command_args[1])
                            g_search = SearchMachine(search=True)
                            g_search.search(query=query)
                            g_search.excecute_search()

                elif command_args[0] == "images":
                    if len(command_args) == 1:
                        send_message(["「Usage : /images {query}」"])

                    elif len(command_args) == 2:
                        value = command_args or "empty"
                        if value == "empty":
                            send_message(["「Usage : /images {query}」"])
                        else:
                            query = "".join(command_args[1])
                            g_images = SearchMachine(images=True)
                            g_images.images(query=query)
                            g_images.excecute_search()

                elif command_args[0] == "website":
                    if len(command_args) == 1:
                        send_message(["「Usage : /website {name of website} change . to ,」"])

                    elif len(command_args) == 2:
                        value = command_args[1] or "empty"
                        if value == "empty":
                            send_message(["「Usage : /website {name of website} change . to ,」"])
                        else:
                            query = "".join(command_args[1].replace(',', '.'))
                            g_web = SearchMachine(website=True)
                            g_web.website(query=query)
                            g_web.excecute_search()

                elif command_args[0] == "fload":
                    if len(command_args) == 1:
                        send_message(["Usage : /fload {count} {message}"])

                    elif len(command_args) == 2:
                        value = command_args[1] or "empty"
                        if value == "empty":
                            send_message(["Usage : /fload {count} {message}"])

                        else:
                            command_arg = command[1:].split(" ", 2)
                            count = command_arg[1]
                            msg = command_arg[2]
                            fload(int(count), msg)

                elif command_args[0] == "sayang":
                        print("\n╔════════════════════╗\n🍁 Bot Pacar Mode On🍁\n╠════════════════════╝")
                        GosendBucin()



        except KeyError as e:
            print("\n Key Error {err}".format(err=str(e)))
            send_message(["Gofood Menu. Gada mas ketik /help"])



if __name__ == "__main__":
    GosendDriver()
