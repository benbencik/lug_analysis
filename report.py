import pyautogui
import tkinter
import time
import os

import scheme
import calc

def generate_report(single_report, root, report_name, dir_path):
    global report_num
    xpos1 = root.winfo_x()+13
    xpos2 = root.winfo_width()-10
    ypos1 = root.winfo_y()
    ypos2 = root.winfo_height()+38

    im = pyautogui.screenshot(region=(xpos1, ypos1, xpos2, ypos2))
    if single_report:
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension='.png')
        im.save(file_path)
    else:
        im.save(os.path.join(dir_path, r'{}.png'.format(report_name)))


def multiple_reports(dname, entry_id, d_entry, g, font, bg, err_lab_scheme, root, calc_args, report_label):
    # time_now = datetime.datetime.now()
    # dir_name = '{}/{}/{}/{}:{}:{}'.format(time_now.year, time_now.day,
    #                                   time_now.month, time_now.hour, time_now.minute, time_now.second)
    dir_path = tkinter.filedialog.asksaveasfilename()
    os.mkdir(dir_path)

    test_data = tkinter.filedialog.askopenfile(mode='r')
    
    while True:
        line = test_data.readline()
        if line == '': break

        line = line.split('\t')
        line = [d.strip().replace(',', '.') for d in line]

        for i in range(1, len(line)):
            d_entry[entry_id[i-1]].delete(0, 'end')
            d_entry[entry_id[i-1]].insert(0, line[i])
        
        report_name = line[0]
        print("report name = ", report_name)
        report_label.delete(0, 'end')
        report_label.insert(0, report_name)
        scheme.create(None, d_entry, g, font, bg, err_lab_scheme, False, [])
        calc.calculate(*calc_args)
        g.update() # first refresh the screen than generate the report
        time.sleep(0.2)
        generate_report(False, root, report_name, dir_path)
