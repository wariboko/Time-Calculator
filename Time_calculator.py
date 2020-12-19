def add_time(start, duration, days=None):
  meridiem_later = 0

  week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#Splitting the AM-PM
  meridiem = start.split(" ")[1]
  initial_meridiem = meridiem

  start = start.split(" ")
  start.pop(1)
  start = ''.join(start)
#Splitting the hours and minutes
  plus_hours = int(duration.split(':')[0])
  plus_minutes = int(duration.split(':')[1])

  new_hour = int(start.split(':')[0])
  new_minutes = int(start.split(':')[1])
# Total hours / minutes
  hour = new_hour + plus_hours
  minute = new_minutes + plus_minutes
# converting minutes
  if minute > 59:
      minute -= 60
      hour += 1

  hour_meridiem = hour
# converting hours
  while hour > 12:
      hour -= 12
# Time switch from AM to PM and PM to AM
  while hour_meridiem > 11:
      hour_meridiem -= 12
      # From Ternary operator to check meridiem
      meridiem = "PM" if meridiem == "AM" else "AM"
      meridiem_later += 1

  if meridiem_later % 2 != 0:
      if initial_meridiem == "PM":
          meridiem_later += 1
      else:
          meridiem_later -= 1

  days_later = meridiem_later/2
# New time
  new_time = f"{hour}:{str(minute).zfill(2)} {meridiem}"

  if days:
      daysofweek = week_days.index(days.title())
      daysofweek_new = int((daysofweek + days_later) % 7)
      new_time += f", {week_days[daysofweek_new]}"
# New time
  if days_later == 1:
      new_time += " (next day)"

  if days_later > 1:
      new_time += f" ({int(days_later)} days later)"



  return new_time