import tempfile

# 一時的なファイルの作成
with tempfile.TemporaryFile(mode='w+') as t:
    # .TemporaryFile一時的なファイルの作成、オブジェクトを閉じると自動的に削除される。ファイル名は可視化されない
    # モードには'w+'書き込み　+ 読み込み
    t.write('hello')
# 書くことは,hello
    t.seek(0)
# seekで0（最初）に戻り
    print(t.read())
# readで読み取る


# 実際にtempfileを作成する場合

with tempfile.NamedTemporaryFile(delete=False) as t:
    print(t.name)
# どこにtemporaryfileが作られたか確認するためのprint()

    with open(t.name, 'w+') as f:
        f.write('test\n')
        f.seek(0)
        print(f.read())

# 一時的なディレクトリ

with tempfile.TemporaryDirectory() as td:
    print(td)
# TemporaryDirectory()だけだと一時的なディレクトリを作成し終了と同時に削除されてしまう。
# zsh: no such file or directoryとなってしまう。

temp_dir = tempfile.mkdtemp()
print(temp_dir)
# TemporaryDirectory()を一時フォルダとして利用するために.mkdtemp()を使用。