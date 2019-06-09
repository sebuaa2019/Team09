from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
import json
import os
import socket
import multiprocessing
import time

# Create your views here.

try:
    HOST = '127.0.0.1'  # 服务器的主机名或者 IP 地址
    PORT = 65432        # 服务器使用的端口

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
except:
    pass


# def write_file(content):
#     home_path = os.popen('echo $HOME').readlines()[0].strip()
#     path = home_path + '/ros_test/src/my_control/src/keys'
#     fw = open(path,'a')
#     fw.write(content)

def write_file(content):
    try:
        s.sendall(content.encode())
    except:
        pass


def save_map():
    os.system('rosrun map_server map_saver -f map')


def move_map():
    home_path = os.popen('echo $HOME').readlines()[0].strip()
    rootdir = home_path
    ori_dir = rootdir + '/catkin_ws/src/team_109/myweb'
    goaldir = rootdir + '/catkin_ws/src/team_109/clean_module/config'
    websrc = rootdir + '/catkin_ws/src/team_109/myweb/static/img'
    os.system('cp ' + ori_dir + '/map.pgm' + ' ' + websrc + '/map.pgm')
    os.system('cp ' + ori_dir + '/map.pgm' + ' ' + goaldir + '/map.pgm')
    os.system('cp ' + ori_dir + '/map.yaml' + ' ' + goaldir + '/map.yaml')



def move(request):
    if request.method != "POST":
        return HttpResponseNotAllowed()
    json_data = json.loads(request.POST['json_data'])
    type = json_data['type']
    if type == 'Turn Left':
        write_file('l')
    elif type == 'Forwards':
        write_file('w')
    elif type == 'Turn Right':
        write_file('r')
    elif type == 'Move Left':
        write_file('a')
    elif type == 'Backwards':
        write_file('s')
    elif type == 'Move Right':
        write_file('d')
    elif type == 'KILL':
        os.system('rosnode kill rviz')
    elif type == 'Begin':
        os.system('roslaunch my_map_package move_control.launch')
    elif type == 'Stop':
        write_file('t')
    elif type == 'Begin Mapping':
        os.system('roslaunch my_map_package my_gmapping.launch')
    elif type == 'Save Your Map':
        save_map()
        move_map()
    return JsonResponse({"status": "ok"})
