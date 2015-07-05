__author__ = 'chenwei'

import sqlite3
import hashlib
import utils

db = '2081374195.db'
table = 'mr_friend_C135CD0F840B8EBFB46A1F868D493D9C_New'

# CREATE TABLE `mr_friend_C135CD0F840B8EBFB46A1F868D493D9C_New` (
# 	`_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	`extInt`	INTEGER,
# 	`extLong`	INTEGER,
# 	`extStr`	TEXT,
# 	`extraflag`	INTEGER,
# 	`frienduin`	TEXT,
# 	`isValid`	INTEGER,
# 	`isread`	INTEGER,
# 	`issend`	INTEGER,
# 	`istroop`	INTEGER,
# 	`longMsgCount`	INTEGER,
# 	`longMsgId`	INTEGER,
# 	`longMsgIndex`	INTEGER,
# 	`msgData`	BLOB,
# 	`msgId`	INTEGER,
# 	`msgUid`	INTEGER,
# 	`msgseq`	INTEGER,
# 	`msgtype`	INTEGER,
# 	`selfuin`	TEXT,
# 	`sendFailCode`	INTEGER,
# 	`senderuin`	TEXT,
# 	`shmsgseq`	INTEGER,
# 	`time`	INTEGER,
# 	`uniseq`	INTEGER,
# 	`versionCode`	INTEGER,
# 	`vipBubbleID`	INTEGER
# );

class Contents:
    _id = '_id'
    frienduin = 'frienduin'
    msgData = 'msgData'
    msgId = 'msgId'
    msgUid = 'msgUid'
    selfuin = 'selfuin'
    senderuin = 'senderuin'
    time = 'time'

##表的映射
PROJECT = [
    Contents._id,
    Contents.frienduin,
    Contents.msgData,
    Contents.msgId,
    Contents.msgUid,
    Contents.selfuin,
    Contents.senderuin,
    Contents.time
]

def test_chat(db):
    conn = sqlite3.connect(db)

    sql = 'SELECT {seq} from {table}'.format(seq=','.join(PROJECT),table=table)
    # cursor = conn .execute('SELECT _id,msgData,time from mr_friend_C135CD0F840B8EBFB46A1F868D493D9C_New')
    cursor = conn .execute(sql)

    for row in cursor:

        tmp = row[PROJECT.index(Contents.frienduin)]
        # print(type(tmp),tmp)
        print(Contents.frienduin,'=',utils.xor(tmp))



        tmp = row[PROJECT.index(Contents.msgData)]
        # print(type(tmp),tmp)
        print(Contents.msgData,'=',utils.xor(tmp))





if __name__ == '__main__':
    test_chat(db)
    # s = test_xor('K\Q['.encode(encoding='utf-8'))
    # s = utils.xor(str.encode('K\Q['))
    # print(s)
    pass