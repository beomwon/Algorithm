def solution(id_pw, db):
    db = {info[0]:info[1] for info in db}
    if id_pw[0] in db.keys():
        if id_pw[1] == db[id_pw[0]]:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail'