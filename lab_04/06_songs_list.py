violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
a=violator_songs_list[3][1]
b=violator_songs_list[5][1]
c=violator_songs_list[8][1]
time0 = a + b + c
time0 = round(time0,2)

print('три песни звучат', time0, 'минут')
n = violator_songs_dict['Sweetest Perfection']
m = violator_songs_dict['Policy of Truth']
r = violator_songs_dict['Blue Dress']
time1 = n + m + r
time1 =round(time1,1)
print("а другие три песни звучат", time1, "минут")