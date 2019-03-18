from pywinauto.application import Application
from pywinauto.application import timings
import time
import pywinauto
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\"

def test_open_install_file():
    app = Application(backend="uia").start(r'C:\\SecurOSEnterprise_10.2.114_Dev_ISS.exe').connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg.wait('exists')
    dlg.child_window(auto_id="306").select("Русский")
    dlg.OK.click()
    time.sleep(35)
    app1 = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1 = app1.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1.wait('exists')
    dlg1.Далее.click()
    dlg1.Япринимаюусловиялицензионногосоглашения.click()
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Установить.click()
    time.sleep(120)
    dlg1.Готово.click()




def test3():
    app = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    # dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    # dlg.Далее.click()


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
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()
    time.sleep(2)
    dlg.ИнтеграцияиАвтоматизация.click_input()
    l = dlg.button2.click_input()
    # p = pywinauto.findwindows.find_elements(class_name="QAction")

    p = l.child_window(class_name="QAction", top_level_only=False).exists()
    print(p)



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
