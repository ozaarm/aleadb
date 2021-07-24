import time
import random
from random import choice

def strTimeProp(start, end, format, prop):
        
    """@stackoverflow: 
    Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formated in the given format (strftime-style), 
    giving an interval [start, end]. prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M', prop)

def randomDOB(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)

def pwd_gen(numCharacters):
    charac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#^?_-"
    allchar_list = charac
    alpha_list = charac[0:52] #52 is excluded, so 0 to 51
    alpha_list.split()
    allchar_list.split()
    genkey=""
    genkey+=choice(alpha_list)
    for i in range(0,int(numCharacters)-1):
        genkey+=choice(allchar_list)
    return genkey

def randomString(stringLength=8):
    #Generate a random string of fixed length
    chars = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.sample(chars,stringLength))