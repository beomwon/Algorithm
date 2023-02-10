def solution(s, skip, index):
    answer = ''
    alphabet_list = [askii_num for askii_num in range(97,97+26) if askii_num not in [ord(skip_word) for skip_word in skip]] * index
    for w in s:
        answer += chr(alphabet_list[alphabet_list.index(ord(w)) + index])
    return answer