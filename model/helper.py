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

def install_securos(name):
    app = Application(backend="uia").start(r"C:/builds/" + name).connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg = app.window(title='SecurOS Enterprise - InstallShield Wizard')
    time.sleep(10)
    #dlg.wait('exists')
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
    time.sleep(550)
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
