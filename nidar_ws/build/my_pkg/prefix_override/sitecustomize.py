import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bobbili-jiten-reddy/nidar_ws/install/my_pkg'
