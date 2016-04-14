# coding:utf-8

def verifyCode(id):
    if len(id) < 17:
        return ''
    lists = id[0:17]
    verify = "10X98765432"
    factor = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,1]
    sum = 0
    for i in range(0,17):
        sum  = sum + (int(lists[i])-int('0'))*factor[i]
    ret = verify[sum%11]
    return lists,ret

if __name__ == "__main__":
    id = raw_input("input you ic card number:")
    print verifyCode(id)

