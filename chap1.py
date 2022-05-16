#!/usr/bin/env python3

import math

def check_prime(number):
  sqrt_number = math.sqrt(number)
  number_float = float(number)
  for i in range(2, int(sqrt_number)+1):
    if (number_float / i).is_integer():
      return False
  return True

print ("check_prime(10000000) = ", check_prime(10000000))
print ("check_prime(10000019) = ", check_prime(10000019))

"""
idealize computing vs python VM
idealize computing:
  number -> RAM
  caculate sqrt_number , number_float => send to CPU
  lý tưởng hóa là gửi giá trị number 1 lần, sau đó lưu giữ trong L1/L2 cache rồi CPU tính toán và gửi kết quả trở 
  về RAM để lưu trữ.
  kịch bản này là lý tưởng vì chúng ta tối thiểu số lần đọc number từ RAM. hơn nữa, tối thiểu số lần dữ liệu gửi qua frontside bus, chọn giao tiếp thông backside bus nhanh hơn (kết nối qua cache đến CPU).
  điều này giữ data ở nơi nó cần và dịch chuyển ít nhất có thể để thực hiện tối ưu hóa.
  Khái niệm "heavy data" liên tưởng đến việc mất nhiều thời gian và công sức để di chuyển dữ liệu, điều mà chúng ta cần tránh.
  vòng lặp: thay vì gửi dữ liệu của i mỗi thời gian đến CPU, chung ta sẽ gửi number_float và một số giá trị của i cùng lúc. 
  điều này có thể bởi vì CPU vectorizes operations sẽ không tốn thêm thời gian, có thể làm nhiều tính toán cùng 1 lúc.
  nên chúng ta sẽ gửi number_float đến CPU cache, và thêm nhiều giá trị i có thể mà cache có thể giữ. với mỗi cặp number_float/i ta sẽ chia ra và kiểm tra là số nguyên.. ..
  dựa trên phân tích trên code sẽ đc sửa lại:  
"""
import math
def check_prime(number):
  sqrt_number = math.sqrt(number)
  number_float = float(number)
  numbers = range(2, int(sqrt_number)+1)
  for i in xrange(0, len(numbers), 5):
    # not valid python code
    result = (number_float/numbers[i:i(i+5)]).is_integer()
    if any(result):
      return False
  return True

"""
sử dụng một set 5 dữ liệu để tính toán
"""
# python's VM
"""
optimize thông thường
"""
def search_fast(haystack, needle):
 for item in haystack:
  if item == needle:
   return True
 return False
def search_slow(haystack, needle):
 return_value = False
 for item in haystack:
   if item == needle:
    return_value = True
 return return_value
