import time

def str2date(date_str):
      return time.strftime("%y/%m/%d",time.strptime(date_str,"%d%m%y"))

def str2float(float_str, separator=None):
     try:
         if separator:
             float_str = float_str.replace(separator, '.')
         return float(float_str)
     except:
         return 0.0

def list2float(lst):
     try:
        return str2float((lambda s : s[:-2] + '.' + s[-2:])(lst))
     except:
        return 0.0

def list2str(lst):
     return str(lst).strip('[]').replace(',','').replace('\'','')

