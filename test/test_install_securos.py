import os
import shutil
import os.path
from model.helper import *

def test1():
    version = get_version_number()
    new_version = increment_ver(version)
    path_to_file = '//builder/BUILDS/' + new_version + '/'
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
            time.sleep(5)
            os.remove("C:/builds/" + name)
            time.sleep(5)
            wizard_load_from_json()
        else:
            print("File doesn't exist")
    else:
        print("Directory doesn't exist")
    return filename


