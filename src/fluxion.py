import os
class reset:
    os.system('cls') # Making current colors work + u don't have to use os urself now
    
class Colors:
    Black = '\033[0;30m'
    Red = '\033[0;31m'
    Green = '\033[0;32m'
    Yellow = '\033[0;33m'
    Blue = '\033[0;34m'
    Magenta = '\033[0;35m'
    Cyan = '\033[0;36m'
    White = '\033[0;37m'

    Light_Black = '\033[1;30m'
    Light_Red = '\033[1;31m'
    Light_Green = '\033[1;32m'
    Light_Yellow = '\033[1;33m'
    Light_Blue = '\033[1;34m'
    Light_Magenta = '\033[1;35m'
    Light_Cyan = '\033[1;36m'
    Light_White = '\033[1;37m'
    
    Dark_Grey = '\033[1;30m'
    Dark_Red = '\033[2;31m'
    Dark_Green = '\033[2;32m'
    Dark_Yellow = '\033[2;33m'
    Dark_Blue = '\033[2;34m'
    Dark_Magenta = '\033[2;35m'
    Dark_Cyan = '\033[2:36m'

    BG_Black = '\033[40m'
    BG_Red = '\033[41m'
    BG_Green = '\033[42m'
    BG_Yellow = '\033[43m'
    BG_Blue = '\033[44m'
    BG_Magenta = '\033[45m'
    BG_Cyan = '\033[46m'
    BG_White = '\033[47m'