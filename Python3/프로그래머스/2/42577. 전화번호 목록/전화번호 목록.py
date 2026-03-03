def solution(phone_book):
    phone_set = set(phone_book)
    for i in phone_book:
        for j in range(len(i)):
            if i[:j] in phone_set:
                return False
    return True