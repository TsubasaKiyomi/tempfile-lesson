tempfile-lesson

- これまで、実際のファイルを作成していたが、tempfile モジュールを使用すると、python がメモリに[i/o バッファ]上に一時的なファイルやディレクトリを作成してくれる

#### tempfile モジュール

##### tempfile モジュールとは

- 一時ファイルを作成する、組み込みモジュール。
- ファイル名が可視化される/されない
- 使い終わりは自動で削除される/自分で削除する。
  目的に応じて使い分けられる関数

### i/o バッファ

#### i/o バッファとは

- 入出力バッファのこと
  一時的にデータを[格納][記憶]する場所。その容量。

- バッファとは、buffer[直訳：緩衝]
  処理速度に差がある装置間に緩衝として設置されるメモリー。

### TemporaryFile

#### TemporaryFile とは

- 一時的なファイルの作成すること。
- オブジェクトを閉じると自動的に削除される。
- ファイル名は可視化されない

### NamedTemporaryFile

#### NamedTemporaryFile とは

- ファイル名のある一時的なファイル。
- ファイルのパスを見ることもできる。（name 属性）

### TemporaryDirectory

#### TemporaryDirectory とは

- 一時的なディレクトリ

##### mkdtemp()

- mkdtemp()とは一時"フォルダ"を作成すること。
- TemporaryDirectory を一時フォルダとしてしばらく利用するために使用。ディレクトリ作成後は PC の電源を落とすまでは消えない。明示的に削除も可能

```
自分で削除する
import shutil
>>> shutil.rmtree(_____)

```

#### mkstemp()

- mkstemp()とは一時"ファイル"を作成すること。
- TemporaryFile()と違うところは、関数によって生成された一時ファイルは自分で削除する必要がある。

```
自分で削除する
import os
os.remove(＿＿＿)
```

### subprocess

#### subprocess とは

- subprocess モジュールは python からコマンドを実行するためのモジュール。

import subprocess

subprocess.run(['ls', '-al'])

### ターミナル上で「ls -al」を実行

- 実行結果はエラーも無くちゃんと表示された。
