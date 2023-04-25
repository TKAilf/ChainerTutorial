# 文字列メソッド
name = "Chainer"
print(f"{name}")
name = name.lower()
print(f"{name}")
name = name.upper()
print(f"{name}")
name = name.title()
print(f"{name}")

# 浮動小数点数が持つメソッド
number = 0.5.as_integer_ratio()
print(f"{number}")

# リストが持つメソッド
numbers = [1, 2, 3, 4, 5]
print(f"{numbers}")
numbers.append(6)
print(f"{numbers}")
numbers.pop()
print(f"{numbers}")
numbers.reverse()
print(f"{numbers}")
numbers.sort()
print(f"{numbers}")
print(f"{len(numbers)}")
print(f"{type(numbers)}")
numbers = [4, 5, 6, 7]
numbers[1] = 10
print(f"{numbers[0:2]}")
print(f"{numbers[:2]}")
print(f"{numbers[1:]}")
# numbersとnumbers[:]は同じ結果だが、多次元配列を扱う際に異なる結果を返す
print(f"{numbers[:]}")

# 空のリストを定義
array = []
# 空のリストに要素を追加
array.append('Chainer')
array.append('チュートリアル')
print(array)

# タプル
# tupleはリストと同様に複数の要素をまとめた型
# tupleはリストと異なり、要素の追加や変更ができない
# tupleは()で囲む
# リストよりも高速に処理できる
# 誤って変更することを防ぐことができる
# 辞書のキーとして利用できる
# 関数の引数として利用できる
array = (1, 2, 3, 4, 5)
print(f"{array}")
print(f"{type(array)}")
print(f"{array[0]}")
print(f"{array[1:]}")

# 辞書
# 辞書はキーと値をセットにしたデータ構造
scores = {"Math": 90, "Science": 80, "English": 75}
print(f"{scores}")
print(f"{scores['Math']}")
# keys: キーの一覧をdict_keysというリストで取得
print(f"{scores.keys()}")
# values: 値の一覧をdict_valuesというリストで取得
print(f"{scores.values()}")
# items: キーと値の一覧をdict_itemsというリストで取得
print(f"{scores.items()}")

names = ['佐藤', '鈴木', '高橋']
# enumerate: インデックスと要素を同時に取得(index, value)
for index, name in enumerate(names):
    print(f"{index}番目: {name}さん")

# zip: 複数のリストを同時に取得
# 短いリストの要素がなくなるとループが終了する
names = ['Python', 'Chainer']
versions = ['3.7', '5.3.0']
suffixes = ['!!', '!!', '?']
for name, version, suffix in zip(names, versions, suffixes):
    print(f"{name} {version} {suffix}")

# 条件分岐
# if-elif-else文
a = 0

if a > 0:
    print('0より大きいです')
elif a == 0:
    print('０です')
else:
    print('0より小さいです')

# while文
# while文は条件式がTrueの間、繰り返し処理を行う
count = 0

while 1:
    print(count)
    count += 1

    if count == 3:
        break

# スコープ
# スコープとは変数が参照可能な範囲のこと
# グローバルスコープ: プログラム全体で参照可能な範囲
global GlobalNumber # グローバル変数を定義
GlobalNumber = 2

# クラス
class House:
    # __init__メソッドはコンストラクタ
    def __init__(self, name):
        self.name = name
    def hello(self):
        print(f"Hello, {self.name}")

sato = House("佐藤")
suzuki = House("鈴木")

# 継承
class Link:
    def __init__(self):
        self.a = 1
        self.b = 2

# Linkクラスを継承したChainクラス
# __init__メソッドがない場合は親クラスの__init__メソッドが呼び出される
class Chain(Link):
    def sum(self):
        return self.a + self.b
    
chain = Chain()

# 親クラスの__init__メソッドを呼び出す
class ChainA(Link):
    super().__init__()
    def __init__(self):
        self.c = 5
    def sum(self):
        return self.a + self.b + self.c
    
chainA = ChainA()
