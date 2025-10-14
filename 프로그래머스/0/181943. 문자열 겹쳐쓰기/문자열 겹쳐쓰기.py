def solution(my_string, overwrite_string, s):
    front_part = my_string[:s]
    overwrite_part = overwrite_string
    end_part = my_string[len(overwrite_string)+s:]
    return front_part + overwrite_part +end_part