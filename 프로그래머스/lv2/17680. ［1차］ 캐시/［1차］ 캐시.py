def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache[:cacheSize]:
            answer += 1
            cache.remove(city)
            
        else:
            answer += 5
            
        cache.insert(0, city)

    return answer