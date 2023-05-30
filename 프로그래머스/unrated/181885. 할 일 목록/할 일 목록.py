def solution(todo_list, finished):
    return [v for v, b in zip(todo_list, finished) if not b]