from load_data import records
from record_to_sheet import *
import easygui
import datetime

current_time = datetime.datetime.now()
log_file_name = f"log/log_{ current_time.strftime('%Y-%m-%d-%H-%M')}.csv"

open(log_file_name, 'w').close()
for record in records:
    date = record['date']
    school = record['school']
    teacher = record['teacher']
    classroom = record['classroom']
    level = record['level']
    mark = record['mark']
    info = f"{date}\n{school}\n{teacher}\n{classroom}\n{level}\n{mark}"
    print(info.replace('\n', ' '))
    create_sheet(STEM)
    fill_form(record)
    
    status = '已录入' if easygui.ynbox(info, choices=['成功', '失败']) else '未录入'
    with open(f'log/{log_file_name}.csv', 'a', encoding='u8') as f:
        f.write(f"{date},{school},{teacher},{classroom},{level},{mark},{status}\n")
