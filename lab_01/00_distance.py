sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distance = {
    'Moscow=>London' : (((550 - 510) ** 2 + (370 - 510) ** 2) ** 0.5),
    'London=>Paris' : (((510 - 480) ** 2 + (510 - 480) ** 2) ** 0.5),
    'Paris=>Moscow' : (((480 - 550) ** 2 + (480 - 370) ** 2) ** 0.5),
}
print(distance)
