city_and_road = list(map(int, input().split()))
road_cnt = city_and_road[1]
n = road_cnt
road_list = []
cities_set =set()
while n>0:
    cities_and_len_road = list(map(int, input().split()))
    road_list.append(cities_and_len_road)
    n-=1
for i in range(1, road_cnt):
    for j in range(road_cnt):
        if road_list[i][2]>road_list[j][2]:
            road_list[i], road_list[j]= road_list[j], road_list[i]
k =0
while len(cities_set)<city_and_road[0]:
    cities_set.add(road_list[k][0])
    cities_set.add(road_list[k][1])
    k+=1
print(road_list[k-1][2]-1)