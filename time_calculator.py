def add_time(start, duration, day=None):
  num_to_day = dict({0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6:"Sunday"})
  
  startSplit = start.split(":")
  h_start = int(startSplit[0])
  m_start = int(startSplit[1][:2])
  am_or_pm = startSplit[1][3:]

  durSplit = duration.split(":")
  h_dur = int(durSplit[0])
  m_dur = int(durSplit[1])

  # compute new minute
  new_m = m_start + m_dur
  carry_over = 0
  if new_m >= 60:
    new_m -= 60
    carry_over = 1
  if new_m < 10:
    new_m = "0" + str(new_m)
  else:
    new_m = str(new_m)

  # compute new hour, AM/PM and day difference
  new_h = (h_start + h_dur + carry_over)%24
  day_diff = (h_start + h_dur + carry_over)//24
  new_am_or_pm = am_or_pm
  if new_h >= 12:
    if am_or_pm == "PM":
      new_am_or_pm = "AM"
      day_diff += 1
    else:
      new_am_or_pm = "PM"
  if new_h > 12:
    new_h -= 12

  # add time
  new_time = "{h}:{m} {am_pm}".format(h=new_h, m=new_m, am_pm=new_am_or_pm)
  
  # add day
  if day != None:
    old_day = day.lower()
    if old_day == "monday":
      old_day_num = 0
    elif old_day == "tuesday":
      old_day_num = 1
    elif old_day == "wednesday":
      old_day_num = 2
    elif old_day == "thursday":
      old_day_num = 3
    elif old_day == "friday":
      old_day_num = 4
    elif old_day == "saturday":
      old_day_num = 5
    elif old_day == "sunday":
      old_day_num = 6
    new_day_num = (old_day_num + day_diff) % 7
    new_day = num_to_day[new_day_num]
    new_time = new_time + ", {new_day}".format(new_day=new_day)

  # add (#days later)
  if day_diff > 1:
    day_diff = str(day_diff)
    new_time = new_time + " ({day_diff} days later)".format(day_diff=day_diff)
  elif day_diff == 1:
    new_time = new_time + " (next day)"
  return new_time