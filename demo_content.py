__author__ = 'chenwei'

import sqlite3
import hashlib

def test():
    conn = sqlite3.connect('2081374195.db')

    # cursor = conn.cursor()
    # print(cursor)

    cursor = conn .execute('SELECT _id,msgData,time from mr_friend_C135CD0F840B8EBFB46A1F868D493D9C_New')
    # cursor = conn .execute('SELECT extStr from mr_friend_BCEFE97517DACC9C14864EE0D686FA4B_New')

    tmp = ''

    for row in cursor:

        print(type(row[1]),row[1])

        # try:
        #     tmp = row[1].decode(encoding='utf-8');
        #     print(tmp)
        #     test_3(tmp)
        # except Exception as e:
        #     print(e)
        #     pass


    # print(cursor)
    # print('success')
    # print( cursor.fetchone())


def test_1():
    '''异或'''
    pass;

    # tmp = 'a'
    # print(tmp) # chr
    # print(ord(tmp))   # chr ----> ascii
    # print(bin(ord(tmp)))  # 10进制-----> 二进制

    # print('hello',ord('aa'))

    # a = 'aa'
    # for x in a :
    #     print(ord(x))

    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    # RTYSRXQTVQTUXTPRTYSRXQTVQTUXTP

    # tmp = ord('a')^ord('R')
    # print(tmp)
    # print(chr(tmp))
    # print(bin(tmp))

    # x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    # z = 'RTYSRXQTVQTUXTPRTYSRXQTVQTUXTP'
    # y = '';
    #
    # for i in range(0,len(x)-1):
    #     rst = ord(x[i])^ord(z[i])
    #     y += chr(rst)
    #
    # print(y)

    x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    z = 'RTYSRXQTVQTUXTPRTYSRXQTVQTUXTPRTYSRXQTVQTUXTPRTYSRXQTVQTUXTPRTYSRXQTVQTUXTPRTYSRXQTVQTUXTPRTYSRXQTVQTUXTPRTYSRXQTVQTUXTP'
    y = '';

    for i in range(0,len(x)):
        rst = ord(x[i])^ord(z[i])
        y += chr(rst)

    print(y)

def test_2():
    '''
    x^y = z
    已知 y,z  ,求ｘ
    '''

    x = ''
    y = '358239057054951'
    z = 'K\Q['

    keyindex=0

    for i in range(0,len(z)):

        if keyindex == len(y):
            keyindex = 0

        rst = ord(z[i])^ord(y[keyindex])
        keyindex += 1;
        x += chr(rst)

    print(x)


def test_3(z):

    x = ''
    y = '358239057054951'

    keyindex=0

    for i in range(0,len(z)):

        if keyindex == len(y):
            keyindex = 0

        rst = ord(z[i])^ord(y[keyindex])
        keyindex += 1;
        x += chr(rst)

    print(x)


def test_4():
    '''
    utf-8 中文　占几个字节
    '''

    # x = ''
    y = '358239057054951'
    # tmp = 230^213
    # print(chr(tmp))
    #
    # tmp = 136^189
    # print(chr(tmp))
    #
    # tmp = 145^169
    # print(chr(tmp))
    #
    # tmp = 230^212
    # print(chr(tmp))
    #
    # tmp = 136^187
    # print(chr(tmp))
    #
    # tmp = 145^168
    # print(chr(tmp))

    x = '我'
    # bb = x.encode(encoding='utf-8')
    # bb=b'\xd5\xbd\xa9\x00'
    bb=b'\x02\x07\xde\xba\xa2\x0b\x03'

    # print(type(bb))
    # print(len(bb))
    print(bb)

    key = bytearray();

    for i in range(0,len(bb)) :
        key.append(bb[i]^ord(y[i]))

    print(key)
    print(type(key))

    # s = ''.join('{:02x}'.format(x) for x in key)
    # print(type(s))

    print(bytearray.decode(key,encoding='utf-8'))

    # print(key.decode(encoding='utf-8'))

    # x=b'aaa'
    # print(x)
    # print(len(x))

def test_md5(data):
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
        print(md5value)
        return md5value  #

if __name__ == '__main__':

    # test_md5()
    # test_4()
    test_2()


    # test()
    # test_3('ZYWDVMX\DWTY\\')
    # phone imei

    # test_1()

    # tmp = b'RTYSRX'
    # print(type(tmp))
    # print(tmp)
    #
    # tmp = tmp.decode(encoding='utf-8')
    # print(type(tmp))
    # print(ord(tmp[0]))


    # key = 358239057054951
    #
    # tmp = '2'
    # print(tmp) # chr
    # print(ord(tmp))   # chr ----> ascii
    # print(bin(ord(tmp)))  # 10进制-----> 二进制
    pass;