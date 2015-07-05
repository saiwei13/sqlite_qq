import hashlib

__author__ = 'chenwei'


###提取工具类

def __xor(z_chats):
    '''
    异或破解　　x^y = z
    :param z_chats:   字节数组
    :return:  字符串
    '''

    x = bytearray();
    y = '358239057054951'  # imei

    keyindex=0

    for i in range(0,len(z_chats)) :

        if keyindex == len(y):
            keyindex = 0

        x.append(z_chats[i]^ord(y[keyindex]))
        keyindex += 1;

    result = bytearray.decode(x,encoding='utf-8')
    # print(result)
    return result

def __xor_str(s):
    '''
    :param s:  字符串
    :return:　　字符串
    '''
    return __xor(str.encode(s))

def __xor_bytes(b):
    '''
    :param b:  字节数组
    :return:　　字符串
    '''
    return __xor(b)

def xor(z_chats):

    result = ''

    if z_chats:
        if type(z_chats) == str:
            # print('---------str--------------')
            result = __xor(str.encode(z_chats))
        elif type(z_chats) == bytes:
            result = __xor(z_chats)

    return result

    # '''
    # 异或破解　　x^y = z
    # :param z_chats:   字节数组
    # :return:  字符串
    # '''
    #
    # x = bytearray();
    # y = '358239057054951'  # imei
    #
    # keyindex=0
    #
    # for i in range(0,len(z_chats)) :
    #
    #     if keyindex == len(y):
    #         keyindex = 0
    #
    #     x.append(z_chats[i]^ord(y[keyindex]))
    #     keyindex += 1;
    #
    # result = bytearray.decode(x,encoding='utf-8')
    # # print(result)
    # return result

def md5(data):
    '''
    md5 加密
    :param data:   字符串
    :return:
    例子：3216083667'　　－－－－－－－> c135cd0f840b8ebfb46a1f868d493d9c
    '''

    if data:
        m = hashlib.md5()
        # m.update(b'3216083667')
        m.update(data.encode(encoding='utf-8'))
        md5value=m.hexdigest()
        # print(md5value)
        return md5value