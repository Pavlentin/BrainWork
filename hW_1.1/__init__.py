s = int(input("Введите время в секундах: "))
#print(time)
i: int = 60
m: int = s // i
h: int = m // i
d: int = h // 24
y: int = d // 365
if m >= 1:
    s = s % i
if h >= 1:
    m = m % i
if d >= 1:
    h = h % 24
if y >= 1:
    d = d % 365
my_list = [y, d, h, m, s]
time_y = "years"
if y <= 1:
    time_y = "year"
time_d = "days"
if d <= 1:
    time_d = "day"
time_h = "hours"
if h <= 1:
    time_h = "hour"
time_m = "minutes"
if m <= 1:
    time_m = "minute"
time_s = "seconds"
if s <= 1:
    time_s = "second"
print(my_list[0], time_y, my_list[1], time_d, my_list[2], time_h, my_list[3], time_m, my_list[4], time_s)
