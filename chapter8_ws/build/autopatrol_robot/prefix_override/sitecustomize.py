import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/scott/chapter8/chapter8_ws/install/autopatrol_robot'
