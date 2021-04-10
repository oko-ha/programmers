def minTohour(time):
    h = str(time // 60)
    m = str(time % 60)

    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    
    return h +':' + m

def shuttle_bus(n, t, m, timetable):
    # timetable 분 환산
    time_list = []
    for i in timetable:
        temp = i.split(':')
        time_list.append(int(temp[0]) * 60 + int(temp[1]))

    time_list.sort()

    # 버스 운행 시간 분 환산
    bus_list = []
    for i in range(n):
        bus_list.append(540 + (t * i))

    print(time_list)
    print(bus_list)

    # 모든 사람을 다 태울 수 있으면
    if len(timetable) < m:
        return minTohour(bus_list[-1])
    else:
        # bus 시간과 timetable 대조
        start = 0
        for bus in bus_list:
            cap = 0
            for i in range(start, len(time_list)):
                if time_list[i] <= bus:
                    cap += 1
                    # 정원 초과 시
                    if cap == m:
                        # 마지막 버스라면
                        if bus == bus_list[-1]:
                            return minTohour(time_list[i] - 1)
                        else:
                            # 다음 table 부터
                            start = i + 1
                            break
                else:
                    # 현재 table 부터
                    start = i
                    break
        if start >= len(time_list):
            return minTohour(time_list[start - 1] - 1)
        else:
            return minTohour(bus_list[-1])


n = 1
t = 1
m = 3
timetable = ["09:00", "08:59", "08:58", "08:57", "08:56"]
print(shuttle_bus(n, t, m, timetable))
