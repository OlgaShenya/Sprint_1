def time_sum(time_str):
  time_list = time_str.replace(' ', ',').split(',')
  result = 0
  
  for el in time_list:
    if 'h' in el:
      result += int(el.replace('h', ''))*60
    elif 'm' in el:
      result += int(el.replace('m', '')) 
    else:
      result += int(el.replace('s', ''))/60
  return result    

time_sum('1h 45m,360s,25m,30m 120s,2h 60s')
