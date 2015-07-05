__author__ = 'chenwei'

import sqlite3
import hashlib

db = '2081374195.db'
table = 'Friends'

# remark 备注
# uin qq号
# name qq昵称
# mCompareSpell  rtokie-2081374195
# @classmethod
class Friends:
    _id = '_id'
    uin = 'uin'
    name = 'name'
    remark = 'remark'

def test_friends(db):

    # project = ['_id','uin','name','remark']
    project = [Friends._id,Friends.uin,Friends.name,Friends.remark]
    str1 = ','.join(project)
    print(str1)
    print(project.index('uin'))
    # return;
    sql = 'SELECT {seq} from {table}'.format(seq=','.join(project),table=table)
    print(sql)

    return;

    conn = sqlite3.connect(db)

    cursor = conn .execute(sql)
    tmp = ''
    for row in cursor:
        # print(type(row[1]),row[1])

        print(row[project.index(Friends._id)])
        # print(row[])
        # print(test_md5(test_xor(str.encode(row[1]))))
        #bytearray(b'\xd5\xbd\x9a\xd4\xab\xa3')
        # try:
        #     print(test_xor(str.encode(row[5])))
        # except Exception as e:
        #     print(e)
        #     pass





if __name__ == '__main__':

    test_friends(db)
    pass