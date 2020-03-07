#!/usr/bin/env python3
import sys
import os
import re
import datetime


def error_search(log_file):
  error = input("Enter ERROR you want to search: ")
  returned_logs = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_logs.append(log)
    file.close()
  return returned_logs

def warn_search(log_file):
  warn = input("Enter WARN you want to search: ")
  returned_logs = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      warn_patterns = ["warn"]
      for i in range(len(warn.split(' '))):
        warn_patterns.append(r"{}".format(warn.split(' ')[i].lower()))
      if all(re.search(warn_pattern, log.lower()) for warn_pattern in warn_patterns):
        returned_logs.append(log)
    file.close()
  return returned_logs  

def info_search(log_file):
  info = input("Enter INFO you want to search: ")
  returned_logs = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      info_patterns = ["info"]
      for i in range(len(info.split(' '))):
        info_patterns.append(r"{}".format(info.split(' ')[i].lower()))
      if all(re.search(info_pattern, log.lower()) for info_pattern in info_patterns):
        returned_logs.append(log)
    file.close()
  return returned_logs  

  
def file_output(returned_logs):
   now = datetime.datetime.now() 
   path = os.path.expanduser('~') + '/Desktop/' + str(now) + 'result.log'  
   with open(path, 'w') as file: 
      for error in returned_logs:
         file.write(error)
      file.close()

if __name__ == "__main__":
  log_file = sys.argv[1]
  log_type = input("Enter LOG type [e = ERROR | w = WARN | i = INFO] :")
  if log_type.lower() == "e":
     returned_logs = error_search(log_file)
     file_output(returned_logs)
  elif log_type.lower() == "w":
      returned_logs = warn_search(log_file)
      file_output(returned_logs)
  elif log_type.lower() == "i":
      returned_logs = info_search(log_file)
      file_output(returned_logs)
  sys.exit(0)
