def solution(cacheSize, cities):
    time = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache[:cacheSize]:
            time += 1
            cache.remove(city)
        else:
            time += 5
            
        cache.insert(0, city)

    return time