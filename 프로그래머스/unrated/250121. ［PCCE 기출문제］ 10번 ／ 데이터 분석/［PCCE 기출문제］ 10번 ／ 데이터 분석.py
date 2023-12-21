def solution(data, ext, val_ext, sort_by):
    ext = ['code', 'date', 'maximum', 'remain'].index(ext)
    sort_index = ['code', 'date', 'maximum', 'remain'].index(sort_by)
    return sorted([v for v in data if v[ext] < val_ext], key= lambda x: x[sort_index])