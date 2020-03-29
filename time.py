import shutil
import os
import time
import datetime

now = datetime.datetime.now()
print(now)
# 現在の年月日時分秒まで出力できる

print(now.isoformat())
# isoformatは国際標準での出し方。

print(now.strftime('%d/%m/%y-%H%M%f'))
# strftimeは自分でカスタマイズして出力させる
# (%d = 日 / %m = 月 %y = 西暦の2桁(2019なら19) %Y(大文字の場合は西暦4桁全て表示)
# %H = 時間　%M = 分　%S = 秒 %f = マイクロセカンド)


today = datetime.date.today()
print(today)
# 年月日のみの出力
print(today.isoformat())
# 国際標準での出力
print(today.strftime('%d/%m/%y'))
# カスタマイズでの出力


t = datetime.time(hour=1, minute=10, second=5, microsecond=100)
print(t)
print(t.isoformat())
print(t.strftime('%H%M%f'))

print(now)
# d = datetime.timedelta(weeks=1)
d = datetime.timedelta(days=365)
# d = datetime.timedelta(hours=1)
# d = datetime.timedelta(minutes=1)
# d = datetime.timedelta(seconds=1)
# d = datetime.timedelta(microseconds=1)
print(now - d)

# print("###")
# time.sleep(2)
# print("###")
# time.sleep()はprint("###")を2秒後に「()の秒数間の後に」表示する。

print(time.time())
# time.timeはエポックタイムと呼ばれる1970年1月1日から秒数で表現されている物


file_name = 'test.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, "{}.{}".format(
        file_name, now.strftime('%Y_%m_%d_%H_%M_%S')))
# 作成されたtest.txtをバックアップするためにshutil.copyでコピーしている。
with open(file_name, 'w') as f:
    f.write('test')
# with open____でtest.txtファイルが作成される。
