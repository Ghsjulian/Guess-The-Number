import hashlib

""" ANSI color codes """

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
OKBLUE='\033[94m'
OKRED='\033[91m'
OKGREEN='\033[92m'
OKORANGE='\033[93m'
COLOR1='\033[95m'
COLOR2='\033[96m'
COLOR3='\033[90m'
RESET='\x1b[0m'


color_list = [OKGREEN,
  RED,BLINK,BLACK,LIGHT_CYAN,COLOR2,RESET,OKGREEN,DARK_GRAY,GREEN,RED,BOLD,LIGHT_WHITE,OKORANGE,OKGREEN,OKBLUE
  ]
  

txt = "123456"

encode_pass = txt.encode()
  
hashed_password = hashlib.sha1(encode_pass).hexdigest()

print(hashed_password)
