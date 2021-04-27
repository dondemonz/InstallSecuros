import time
import winapps
import psutil
from pywinauto import Application
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import win32serviceutil
import subprocess


def get_version_data(filename):
    try:
        info = GetFileVersionInfo(filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return "Unknown version"

def get_version_number():
    version = ".".join([str(i) for i in get_version_data(r'C:\Program Files (x86)\ISS\SecurOS\securos.exe')])
    #print(version)
    version = version[:-2]
    #print(version)
    return (version)

def increment_ver(version):
    version = version.split('.')
    version[2] = str(int(version[2]) + 1)
    return '.'.join(version)
"""
def test():
    app = Application(backend="uia").start(r"C:/builds/SecurOSEnterprise_10.10.30_Dev_ISS.exe").connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    time.sleep(15)
    dlg.window(best_match='ComboBox', auto_id="306").select("Русский")
    app = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg.OK.click()
"""
def install_securos(name):
    app = Application(backend="uia").start(r"C:/builds/" + name).connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    time.sleep(2)
    #dlg.wait('exists')
    #раньше работало так как закомментированно ниже, потом почемуто начало работать через раз
    #dlg.wait('exists')
    #dlg.print_control_identifiers()
    #dlg.child_window(best_match='ComboBox', auto_id="306").select("Русский")
    dlg.window(best_match='ComboBox', auto_id="306").select("Русский")
    #app = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    #dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg.OK.click()

    #неудачные попытки обойти sleep и смену окон
    #app.WindowSpecification.Далее.wait('enabled').click()
    #OpenDialog = pwa_app.window(best_match=u'Open', class_name='#32770').wait('visible', timeout=20, retry_interval=0.5)
    #app.wait_for_process_exit(timeout=150)
    #dlg.wait('visible', timeout=150)
    #window = pywinauto.timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=Win))
    #dlg.Далее.wait('visible', timeout=150)

    time.sleep(150)
    app1 = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1 = app1.window(title='SecurOS Enterprise - InstallShield Wizard')
    time.sleep(10)
    dlg1.Далее.click()
    time.sleep(2)
    #dlg1.Далее.wait('visible', timeout=100).click()
    dlg1.Япринимаюусловиялицензионногосоглашения.click()
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
    dlg1.Далее.click()
    time.sleep(2)
    dlg1.Установить.click()
    #dlg1.Готово.wait('visible', timeout=550)
    time.sleep(520)
    dlg1.Готово.click()

def kill_client_exe():
    PROCNAME = "client.exe"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()



def stop_securos_service():
    serviceName = "SecurOS Control Service"
    win32serviceutil.StopService(serviceName)

def securos_uninstall():
    #в папку с тестом, в данном случае C:\Devel\InstallSecuros\test, должен находиться msiexec.exe
    winapps.uninstall("SecurOS Enterprise", args=['/quiet'])

def stop_postgres_service():
    service_name = "postgresql-x64-12"
    try:
        win32serviceutil.QueryServiceStatus(service_name)
    except:
        print("Windows service NOT installed")
    else:
        print("Windows service installed")
        win32serviceutil.StopService(service_name)
        uninstall_postgres()
        time.sleep(10)

def uninstall_postgres():
    subprocess.run(r"C:\Program Files\PostgreSQL\12\uninstall-postgresql.exe --mode unattended")
    #сам процесс удаления продолжается некоторое время после завершения теста, нужен слип, чтобы раньше времени не начался следующий этап
    time.sleep(10)

path = "C:\\Program Files (x86)\\ISS\\SecurOS\\"

def wizard_setup():
    Application(backend="uia").start(path + "client.exe")
    time.sleep(15)
    app = Application(backend="uia").connect(title="   Мастер первоначальной настройки")
    dlg1 = app.window(title="   Мастер первоначальной настройки")
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
    time.sleep(5)
    app1 = Application(backend="uia").connect(title="   Мастер первоначальной настройки")
    dlg2 = app1.window(title="   Мастер первоначальной настройки")
    time.sleep(1)
    dlg2.OK.click()

def wizard_load_from_json():
    Application(backend="uia").start(path + "client.exe")
    time.sleep(15)
    app = Application(backend="uia").connect(title="   Мастер первоначальной настройки")
    dlg1 = app.window(title="   Мастер первоначальной настройки")
    dlg1.Импортироватькофигурационныйфайл.click()
    dlg1.Восстановить.click()
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Путькфайлу.click_input()
    dlg1.type_keys('C:\\ProgramData\\ISS\\Sys_config\\new_system_with_iidk.json')
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Завершить.click()

#попытки создать iidk через интерфейс, не получается выбрать конректно объект iidk для создания
    """
from pywinauto import keyboard
import keyboard
def test1123():
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    dlg.ИнтеграцияиАвтоматизация.click_input()
    #time.sleep(1)
    keyboard.press_and_release('ctrl+N')
    time.sleep(5)
    #dlg1 = app.window(title='Панель управления SecurOS Enterprise')
    #dlg.print_control_identifiers()
    pywinauto.findwindows.find_elements_by_name(class_name="CreateAction")
    #dlg.child_window.Интерфейс.click_input()

    #menu_service = dlg.child_window(name="Интерфейс IIDK", control_type="UIA_MenuItemControlTypeId")
    #n = dlg.children()
    #print(n)
    #dlg.child_window(auto_id="", top_level_only=False).select("Интерфейс IIDK")
    #p = dlg.find_elements()
    #elements = pywinauto.findwindows.find_elements(class_name="CreateAction")
    #len(elements)
    #print(elements)
    #pywinauto.findwindows.find_element(class_name="CreateAction", title="Интерфейс IIDK", top_level_only=False)

    # menu_service.select()

    # item_backup = dlg.child_window(title="Интерфейс IIDK", control_type="MenuItem")
    # item_backup.select()

    #hotkey('Ctrl', 'N')
    #pywinauto.keyboard.SendKeys("Ctrl+N")
    time.sleep(1)
    
import pywinauto
def test_create_iidk():
    #Application(backend="uia").start(path + "client.exe")
    app = Application(backend="uia").connect(title='Панель управления SecurOS Enterprise')
    dlg = app.window(title='Панель управления SecurOS Enterprise')
    d = dlg.child_window(auto_id="MainPanelForm.gridLayoutWidget.MainPanelWidget.rightFrame.setupWidget.setupButton").click()
    #после использования визарда "Система" и показывается "SecurOS Enterprise"
    dlg.SecurOSEnterprise.double_click_input(button='left')
    dlg.СерверыиРабочиеместа.double_click_input(button='left')
    dlg.КомпьютерVQA.double_click_input(button='left')
    dlg.child_window(auto_id="MainPanelForm.ObjectEditorWidget.SlaveSetupPanelClass.leftWidget.buttonAddress").click()

    dlg.ИнтеграцияиАвтоматизация.click_input()
    time.sleep(1)
    #app.window_().print_control_identifiers()
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



def test55():
    import win32api

    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)
    
def test12():
    if os.path.exists("Y:/10.10.10"):
        print("Directory exist")
    else:
        print("Directory doesn't exist")
        
def test121():
    dir_list = os.listdir("Y:\\10.10.10\\")
    print(dir_list)


def test121():
    #dir_list = os.listdir("Y:/10.10.26/")
    dir_list = os.listdir("//builder/BUILDS/10.10.26/")
    print(dir_list)
    """

