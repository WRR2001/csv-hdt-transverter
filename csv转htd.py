import tkinter as tk
from tkinter import filedialog
import csv
import json
import uuid
import os

# 创建一个全局变量来存储输出目录
output_dir = os.getcwd()  # 默认是当前工作目录

def upload_csv():
    global filename
    # 选择csv文件
    filename = filedialog.askopenfilename(filetypes=[("csv files", "*.csv")])
    # 更新label显示新的文件名
    file_label.config(text=filename)
    # 读取csv文件中的链接
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # 使用全局变量存储链接，以便在convert_links函数中使用
        global links  
        links = list(reader)

def select_output_dir():
    global output_dir
    # 让用户选择一个输出目录，并将其存储在全局变量output_dir中
    output_dir = filedialog.askdirectory(initialdir=output_dir)
    # 更新目录标签显示新的输出目录
    dir_label.config(text=output_dir)

def convert_links():
    try: 
        # 初始化数据结构
        data = [
            {"type": "HDT", "version": "1.2"}
        ]

        # 为每个链接生成一个数据对象并添加到数据结构中
        for link in links:
            data.append({
                "ver": "1.2",
                "title": "waiting... " + link[0],
                "gal_num": link[0],
                "music": False,
                "anime": True,
                "valid": True,
                "dir": "",
                "label_color": None,
                "url": link[0],
                "type": "bili",
                "filesize": 0,
                "pbar": [0, 0, "%v/%m"],
                "time": 1684604277.0325868,
                "version": "3.8c",
                "uid": str(uuid.uuid4()),
                "str_pixmap": "",
                "artist": None,
                "done": False,
                "name_zip": "",
                "urls": [],
                "etc_button": None
            })

        # 将数据结构转换为JSON字符串
        json_str = json.dumps(data, ensure_ascii=False)

        # 保存为.hdt文件
        output_filename = entry.get()  # 从Entry控件获取输出文件名
        with open(os.path.join(output_dir, output_filename + '.hdt'), 'w', encoding='utf-8') as file:
            file.write(json_str)
        print(f"File saved to: {output_dir}/{output_filename}.hdt")
    except Exception as e:
        print(f"An error occurred: {e}")

# 创建Tk窗口
window = tk.Tk()
window.title('Link Converter')
window.geometry('400x360')  # 设置窗口大小

# 创建一个上传按钮
upload_button = tk.Button(window, text='上传CSV文件', command=upload_csv)
upload_button.pack()

# 创建一个label显示上传的文件名
file_label = tk.Label(window, text='')
file_label.pack()

# 创建一个按钮让用户选择输出目录
select_dir_button = tk.Button(window, text='选择输出目录', command=select_output_dir)
select_dir_button.pack()

# 创建一个label显示选择的输出目录
dir_label = tk.Label(window, text=output_dir)
dir_label.pack()

# 创建一个输入框用于输入输出文件名
entry = tk.Entry(window)
entry.pack()

# 创建一个转换按钮
convert_button = tk.Button(window, text='开始转换', command=convert_links)
convert_button.pack()

# 运行Tk事件循环
window.mainloop()
