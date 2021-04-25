import os
import shutil
keyword = 'SecurOS'
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\"

import os.path
from model.helper import *

def test12():
    if os.path.exists("Y:\\10.10.10"):
        print("Directory exist")
    else:
        print("Directory doesn't exist")

def test55():
    import win32api

    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)

def test1():
    version = get_version_number()
    new_version = increment_ver(version)

    path_to_file = 'Y:/' + new_version + '/'
    name = 'SecurOSEnterprise_' + new_version + '_Dev_ISS.exe'
    filename = path_to_file + name


    if os.path.exists(path_to_file):
        print("Directory exist")
        if os.path.isfile(filename):
            #print(filename)
            print("File exist")
            shutil.copyfile(filename, "C:/builds/" + name)
            stop_securos_service()
            kill_client_exe()
            securos_uninstall()
            stop_postgres_service()
            install_securos(name)
        else:
            print("File doesn't exist")
    else:
        print("Directory doesn't exist")

    #dir_list = os.listdir('Z:\\' + new_version)
    #print(dir_list)

    #shutil.copyfile(filename, "C:/builds/"+name)
    return filename

def test121():
    dir_list = os.listdir("Y:\\10.10.10\\")
    print(dir_list)

def test():
    install_securos(name="SecurOSEnterprise_10.10.19_Dev_ISS.exe")


def test4_wizard_setup():
    Application(backend="uia").start(path + "client.exe")
    time.sleep(5)
    app = Application(backend="uia").connect(title='   Мастер первоначальной настройки')
    dlg1 = app.window(title='   Мастер первоначальной настройки')
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Подтвердитьпароль.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Завершить.click()
    time.sleep(1)
    dlg1.ОК.click()

def test_create_iidk():
    #Application(backend="uia").start(path + "client.exe")
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    d = dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()
    dlg.ИнтеграцияиАвтоматизация.click_input()
    time.sleep(1)
    app.window_().print_control_identifiers()
    #pywinauto.send_keys('ctrl+N')

    #dlg.ИнтерфейсIIDK.click()
    #time.sleep(2)
    #l = dlg.button2.click_input()
    # p = pywinauto.findwindows.find_elements(class_name="QAction")
    #time.sleep(25)

    #app1.window_().Edit2.type_keys("securos")
    #app1.window_().Авторизоваться.click()
    #app1.window().print_control_identifiers()

    #p = l.child_window(class_name="QAction", top_level_only=False).exists()
    #print(p)
    """    
def test_2():
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()
    dlg.Оповещение.click_input()
    ef = dlg.Оповещение.MMS.Exists(timeout=1)
    #elements = dlg.children()
    #len(elements)
    # dlg.MMS.exists()
    # o = object.child
    """
    # показывает внутри родительского диалога, а не нужного dlg.ИнтерфейсIIDK.click_input()
    #time.sleep(1)
    # menu_service = dlg.child_window(name="Интерфейс IIDK", control_type="UIA_MenuItemControlTypeId")
    # n = dlg1.children()
    # print(n)
    # dlg.child_window(auto_id="", top_level_only=False).select("Интерфейс IIDK")
    #p = dlg.find_elements()
    # elements = pywinauto.findwindows.find_elements(class_name="QAction")
    # len(elements)
    # print(elements)
    # pywinauto.findwindows.find_element(class_name="QAction", title="Интерфейс IIDK", top_level_only=False)

    # menu_service.select()

    # item_backup = dlg.child_window(title="Интерфейс IIDK", control_type="MenuItem")
    # item_backup.select()
    #dlg.ИнтерфейсIIDK.click()

    # title = 'Создать(Ctrl+N)'


    # dlg1.click()
