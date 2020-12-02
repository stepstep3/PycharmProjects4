import time
def screenshot(d):
    folder="C:\\Users\\NASA7\\PycharmProjects\\untitled5\\screenshoot\\"
    time_string=time.asctime().replace(":","")
    file_name=folder+time_string+".png"
    d.save_screenshot(file_name)
    d.get_screenshot_as_file(file_name)