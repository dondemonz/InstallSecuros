from pywinauto.application import Application
import time
import os
keyword = 'SecurOS'
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\"


def test_open_install_file():
    for fname in os.listdir('C:\\'):
        if keyword in fname:
            fn = fname
            print(fname, "has the keyword")

    app = Application(backend="uia").start(r'C:\\'+fn).connect(title='SecurOS Enterprise - InstallShield Wizard')  #почему подсвечена fn не знаю, но работает
    dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg.wait('exists')
    dlg.child_window(auto_id="306").select("Русский")
    dlg.OK.click()

    #app.WindowSpecification.Далее.wait('enabled').click()
    #OpenDialog = pwa_app.window(best_match=u'Open', class_name='#32770').wait('visible', timeout=20, retry_interval=0.5)
    #app.wait_for_process_exit(timeout=150)
    #dlg.wait('visible', timeout=150)
    #window = pywinauto.timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=Win))
    #dlg.Далее.wait('visible', timeout=150)

    time.sleep(150)
    app1 = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1 = app1.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1.Далее.wait('visible', timeout=100).click()
    dlg1.Япринимаюусловиялицензионногосоглашения.click()
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Установить.click()
    dlg1.Готово.wait('visible', timeout=250)
    dlg1.Готово.click()



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

    p = l.child_window(class_name="QAction", top_level_only=False).exists()
    print(p)

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
