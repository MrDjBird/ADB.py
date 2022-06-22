import os

device = ""


def cmd(command):
    cmd_object = os.popen(fr"{command}", "r")
    result = cmd_object.read()
    result.encode("cp866")
    cmd_object.close()
    return result


def shell(shell_command = ""):
    return cmd(f"adb{device} shell {shell_command}")


def devices(full_info=False, wait_for_connect=False, pack_result_to_list=False):
    options = ""
    if full_info:
        options = " -l"
    if wait_for_connect:
        cmd("adb wait-for-device")
        result = cmd(f"adb devices{options}")
        if pack_result_to_list is True:
            if full_info:
                result = result.split("\n", 1)
                result.pop(0)
                if result:
                    full_result = []
                    result = result[0].split()
                    for i in range(int(len(result) / 6)):
                        for i1 in range(6):
                            full_result = full_result + [result[i1]]
                        full_result = [full_result]
                        return full_result
            result = result.split()
            for i in range(4):
                result.pop(0)
            if result:
                n = 0
                for i in result:
                    if n == 1:
                        result.remove(i)
                    else:
                        n = 1
        return result
    else:
        result = cmd(f"adb devices{options}")
        if pack_result_to_list is True:
            if full_info:
                result = result.split("\n", 1)
                result.pop(0)
                if result:
                    full_result = []
                    result = result[0].split()
                    for i in range(int(len(result) / 6)):
                        for i1 in range(6):
                            full_result = full_result + [result[i1]]
                        full_result = [full_result]
                        return full_result
            else:
                result = result.split()
                for i in range(4):
                    result.pop(0)
                if result:
                    n = 0
                    for i in result:
                        if n == 1:
                            result.remove(i)
                        else:
                            n = 1
        return result


def reboot(reboot_to=""):
    if reboot_to == "power" or reboot_to == "":
        return cmd(f"adb{device} shell reboot -p")
    elif reboot_to != "bootloader" and reboot_to != "fastboot":
        return cmd(f"adb{device} reboot {reboot_to}")
    else:
        return cmd(f"adb{device} reboot-{reboot_to}")


def push(pc_file_path, device_directory):
    return cmd(f"adb{device} push {pc_file_path} {device_directory}")


def pull(device_file_path, pc_directory):
    return cmd(f"adb{device} pull {device_file_path} {pc_directory}")


def install(path_to_apk, block_app=False, reinstall_with_save_data=False, install_to_sd=False):
    options = ""
    if block_app:
        options = options + " -l"
    if reinstall_with_save_data:
        options = options + " -r"
    if install_to_sd:
        options = options + " -s"
    return cmd(f"adb{device} install{options} {path_to_apk}")


def uninstall(name_of_package, save_data=False):
    options = ""
    if save_data:
        options = " -k"
    return cmd(f"adb uninstall{options} {name_of_package}")


def select(device_id="", product_name="", only_emulators=False, only_usb_devices=False):
    global device
    if (only_emulators is True and only_usb_devices is True) or (device_id != "" and product_name != ""):
        return "Can't been two options at the same time (only_emulators and only_usb_devices) or (device and product)"
    if only_emulators:
        device = " -e"
    elif only_usb_devices:
        device = " -d"
    if device_id != "":
        device = device + f" -s {device_id}"
    elif product_name != "":
        device = device + f" -p {product_name}"
    return f"Selected device: {device_id}"


def wifi(state, open_settings=False):
    if open_settings:
        cmd(f"adb{device} shell am start -a android.intent.action.MAIN -n com.android.settings/.wifi.WifiSettings")
    return cmd(f"adb{device} shell svc wifi {state}")


def start_server():
    return cmd(f"adb{device} start-server")


def kill_server():
    return cmd(f"adb{device} kill-server")


def get_state():
    return cmd(f"adb{device} get-state")


def get_serialno():
    return cmd(f"adb{device} get-serialno")


def root():
    return cmd(f"adb{device} root")


def usb():
    return cmd(f"adb{device} usb")


def tcpip(port):
    return cmd(f"adb{device} tcpip {port}")


def root_permission():
    return cmd(f"adb root")


def connect(ip, port):
    if port != "":
        port = f":{port}"
    return cmd(f"adb{device} connect {ip}{port}")


def get_android_version():
    return cmd(f"adb{device} shell getprop ro.build.version.release")


def getprop(properties):
    return cmd(f"adb{device} getprop {properties}")


def logcat_clear():
    return cmd(f"adb{device} logcat -c")


def logcat_save(path):
    return cmd(f"adb{device} logcat -d {path}")


def bugreport(path="bugreport.zip"):
    return cmd(f"adb{device} bugreport {path}")


def phone_call(phone_number):
    return cmd(f"adb{device} shell am start -a android.intent.action.CALL -d tel:{phone_number}")


def send_sms(phone_number, text_off_massage=""):
    return cmd(f'adb{device} shell am start -a android.intent.action.SENDTO -d sms:{phone_number}   --es  '
        f'sms_body "{text_off_massage} --ez exit_on_sent false')


def reset_permissions(package_name):
    return cmd(f"adb{device} shell pm reset-permissions -p {package_name}")


def grant_permission(package_name, permission):
    return cmd(f"adb{device} shell pm grant {package_name} {permission}")


def revoke_permission(package_name, permission):
    return cmd(f"adb{device} shell pm revoke {package_name} {permission}")


def print_text(text):
    return cmd(f"adb shell input text '{text}'")


def screenshot(path_on_device, path_on_pc=""):
    result = cmd(f"adb{device} shell screencap -p {path_on_device}")
    if path_on_pc != "":
        pull(path_on_device, path_on_pc)
    return result


def screenrecord(path_on_device, path_on_pc=""):
    result = cmd(f"adb{device} shell screenrecord {path_on_device}")
    if path_on_pc != "":
        pull(path_on_device, path_on_pc)
    return result


def keyevent(key_id):
    return cmd(f"adb{device} shell input keyevent {key_id}")





if __name__ == "__main__":
    reboot()
