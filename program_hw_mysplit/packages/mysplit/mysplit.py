def mysplit(strng):
    if strng.strip(' ') != '':
        tmp_str = str(strng).strip(' ') 
        res = []
        while len(tmp_str) > 0:
            if tmp_str.find(' ') != -1:
                res.append(tmp_str[0:tmp_str.find(' ')])
                tmp_str = tmp_str[tmp_str.find(' ')+1:len(tmp_str)]
            else:
                res.append(tmp_str)
                tmp_str = ''
        return res
    else:
        return []
