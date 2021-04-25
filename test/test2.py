import os
import time

## тут попытки разными способами подключить билдер через питон, ничего не получилось
"""
def test18():
    os.system('net use z: \\\\Builder\\builds /user:office/d-efremov "an47%"')
    time.sleep(1)
    time.sleep(1)

def test12():
    import winrm

    sess = winrm.Session('//Builder/builds/10.10.30/', auth=('d-efremov', 'an47%'), transport='kerberos')
    result = sess.run_cmd('ipconfig', ['/all'])

def test13():
    import os, ntpath, posixpath

    def transfer_files_task():
        source_file = "//Builder/builds/10.10.30/SecurOSEnterprise_10.10.30_Dev_ISS.exe"
        dest_file = "C:/builds/SecurOSEnterprise_10.10.30_Dev_ISS.exe"
        #assert os.path.exists(source_file), f"{source_file} does not exists"
        shutil.copyfile(source_file, dest_file)

    transfer_files_task()

def test14():
    import speedcopy
    src = "//Builder/builds/10.10.30/SecurOSEnterprise_10.10.30_Dev_ISS.exe"
    dst = "C:/builds/SecurOSEnterprise_10.10.30_Dev_ISS.exe"
    speedcopy.copyfile(src, dst)

def test15():
    import time
    password = "an47%"
    domain_name = "office"
    user_name = "d-efremov"

    #os.system(r"net use Y: \\Builder\builds\10.10.30 %s /USER:%s\%s" % (password, domain_name, user_name))
    os.system("net use Z: \\\\Builder\\builds /user:office\d-efremov an47%")
    #time.sleep(5)
    #os.system(r"NET USE D: /DELETE")

def test16():
    user = "office\d-efremov"
    password = "an47%"
    networkPath = "\\\\Builder\\builds"
    winCMD = 'net use Z: ' + networkPath + ' /User:' + user + ' ' + password
    subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)
    shutil.copy2(networkPath + '\\SecurOSEnterprise_10.10.30_Dev_ISS.exe', 'C:\\builds\\SecurOSEnterprise_10.10.30_Dev_ISS.exe"')

def test17():
    username = "office\d-efremov"
    passwd = "an47%"
    #cmd = "C:\\Windows\\System32\\net.exe net use Z: \\\\Builder\\builds /persistent:no /user:office\d-efremov an47%"
    #os.system(cmd)
    import traceback

    try:
        cmd = "C:\\Windows\\System32\\net.exe net use Z: \\\\Builder\\builds /persistent:no /user:office\d-efremov an47%"

        os.system(cmd)
    except Exception as e:
        print('Ошибка:\n', traceback.format_exc())

def test18():

    username = "office\d-efremov"
    passwd = "an47%"
    try:
        os.system(f"C:/Windows/System32/net.exe use Z: \\\\Builder\\builds /persistent:no /user:{username} {passwd}")
        time.sleep(1)
    except Exception as e:
        print(e)
    
def test4():
    import win32api
    import win32net
    ip = '192.168.1.18'
    username = 'office\d-efremov'
    password = 'an47%'

    use_dict = {}
    #use_dict['remote'] = unicode('\\\\172.16.0.48\\builds')
    #use_dict['password'] = unicode(password)
    #use_dict['username'] = unicode(username)
    win32net.NetUseAdd(None, 2, use_dict)
        
def test5():
    import win32api
    import win32net
    import win32netcon, win32wnet

    username = 'office\d-efremov'
    password = 'an47%'
    host = 1
    try:
        win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, 'Z:', host, None, username, password, 0)
        print("connection  established successfully")
    except:
        print("connection not established")
        
def test9():
    source_file = '//Builder/builds/10.10.30/SecurOSEnterprise_10.10.30_Dev_ISS.exe'
    username = "office/d-efremov"
    password = "an47%"
    import win32wnet
    win32wnet.WNetAddConnection2(0, None, + host, None, username, password)
    shutil.copy(source_file, '\\\\' + host + dest_share_path + '\\')
    win32wnet.WNetCancelConnection2('\\\\' + host, 0, 0)  # optional disconnect
    
    
    def test10():
    import win32wnet

    win32wnet.WNetAddConnection2(0, None, '\\\\' + host, None, username, password)
    shutil.copy(source_file, '\\\\' + host + dest_share_path + '\\')
    win32wnet.WNetCancelConnection2('\\\\' + host, 0, 0)  # optional disconnect
    
    
def test11():
    networkPath  = '//Builder/builds/10.10.30/'
    user = "office/d-efremov"
    password = "an47%"
    winCMD = 'NET USE ' + networkPath + ' /User:' + user + ' ' + password
    subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)

    #import shutil
    #shutil.copy2(networkPath + 'SecurOSEnterprise_10.10.30_Dev_ISS.exe', 'C:/builds/SecurOSEnterprise_10.10.30_Dev_ISS.exe')
    
        """
