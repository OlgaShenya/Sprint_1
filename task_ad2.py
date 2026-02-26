def digit_root(num):
  if num < 1 or num > 10 ** 7:
    str_num = str(num)
    digit_root_num = 0
    for i in range(len(str_num)):
      digit_root_num += int(str_num[i])
    if len(str(digit_root_num)) > 1:
      return digit_root(digit_root_num)
    else:
      return digit_root_num
  else:
    print('wrong number for function')
    return num
      


digit_root(791)