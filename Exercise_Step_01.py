# 問2.1(組み込み関数)
# 組み込み関数を適切に使うことでコードを簡潔に記せます。a=[4, 8, 3, 4, 1] というリストに対して以下の操作を行う組み込み関数を公式ドキュメントからそれぞれ探し、適用して下さい。すなわち、以下のコードセル中の FUNC の部分を適切な組み込み関数に置き換えてください。
a = [4, 8, 3, 4, 1]
# リスト a の長さを求めて表示する。
print(len(a))

# リスト a に含まれる値の最大値を求める。
print(max(a))

# リスト a に含まれる値の最小値を求める。
print(min(a))

# リスト a に含まれる値の合計値を求める。
print(sum(a))

# リスト a をソートして、[1, 3, 4, 4, 8] というリストを返す。
print(sorted(a))

# 問2.2(演算)
# 以下の演算や関数をそれぞれ評価したとき、結果の値と型が何になるか予想してください。実際にコードを実行して、結果が予想と合うか確かめてください。型の確認には type() 関数を使用しましょう。
# 1.2 + 3.8
print(type(1.2 + 3.8))

# 10 // 100
print(type(10 // 100))

# 1 >= 0
print(type(1 >= 0))

# 'Hello World' == 'Hello World'
print(type('Hello World' == 'Hello World'))

# not 'Chainer' != 'Tutorial'
print(type(not 'Chainer' != 'Tutorial'))

# all([True, True, False]) (all の定義は公式ドキュメントを参照)
print(type(all([True, True, False])))
print(all([True, True, False]))
print(any([True, True, False]))

# any([True, True, False]) (any の定義は公式ドキュメントを参照)
print(type(any([True, True, True])))
print(all([True, True, True]))
print(any([True, True, True]))

# abs(-3) (abs の定義は公式ドキュメントを参照)
print(type(abs(-3)))

# 2 // 0
# print(type(2 // 0))

# 問2.3 (リストの基本操作)
# 機械学習では大量のデータを扱うことが多いため、リストの扱いに慣れておくと便利なことが多いです。 a=[4, 8, 3, 4, 1] というリストに対して以下の操作を行うコードを書いて下さい。
# リスト a の先頭の要素を取り除いて、[8, 3, 4, 1] となるようにして下さい。
a = [4, 8, 3, 4, 1]
a.pop(0)
print(a)

# リスト a の末尾の要素を取り除いて、[4, 8, 3, 4] となるようにして下さい。
a = [4, 8, 3, 4, 1]
a.pop()
print(a)

# リスト a の末尾に 100 という値を追加して、[4, 8, 3, 4, 1, 100] となるようにして下さい。
a = [4, 8, 3, 4, 1]
a.append(100)
print(a)

# 問2.4 (リスト内包表記)
# リスト内包表記はリストを生成するための簡潔な手段です。例えば、平方数のリスト [0, 1, 4, 9, 16, ...] を構成したいとき、
squares = [x**2 for x in range(10)]
print(squares)

# a=[4, 8, 3, 4, 1] というリストに対し、要素が偶数なら 0, 奇数なら 1 に変換するコードをリスト内包表記を用いて書いて下さい。この結果、このリストは [0, 0, 1, 0, 1] に変換されるべきです。
# 上記で書いたコードと組み込み関数を組み合わせて、リスト a に含まれる奇数の個数を数えるコードを書いて下さい。
# リスト内包表記では、if 文を用いることで条件を満たす要素だけをリストに残すことができます。例えば
# b = [x for x in range(10) if x > 5]と記すと、b は要素が 5 より大きいもののみが残り [6, 7, 8, 9] となります。
# リスト内包表記を使ってリスト a から奇数の要素だけを残すコードを書いて下さい。
a = [4, 8, 3, 4, 1]
a = [0 if x % 2 == 0 else 1 for x in a]
print(a)
print(a.count(1))

# 問2.5 (文字列)
# Python では文字列型に対して便利な組み込み関数が多数定義されています(公式のドキュメント)。組み込み関数を使って以下の処理を行って下さい。
# str.join() を使って、0 から 99 までの数をスペース区切りで並べた文字列 "0 1 2 3 4 ... 99" を構成して下さい。
print(' '.join([str(x) for x in range(100)]))
# str.format() を使って float の値 (1.0 / 7.0) の小数点以下9桁までを表示して下さい。
print('{:.9f}'.format(1.0 / 7.0))

# 問2.6 (クラス)
# クラスを実装する練習として、データを管理するクラスを実装してみましょう。 次のメソッドを全て持つクラス DataManager を記述して下さい。
# __init__(self, x, y, z): 3つの数 x, y, z をコンストラクタで受け取り、インスタンスの属性でそれぞれの値を記憶する。
# add_x(self, delta): x に delta だけ足して、値を更新する。
# add_y(self, delta): y に delta だけ足して、値を更新する。
# add_z(self, delta): z に delta だけ足して、値を更新する。
# sum(self): x, y, z の3つの数の合計値を返す。
class DataManager:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def add_x(self, delta):
        self.x += delta
    
    def add_y(self, delta):
        self.y += delta
    
    def add_z(self, delta):
        self.z += delta
    
    def sum(self):
        return self.x + self.y + self.z

data_manager = DataManager(2, 3, 5)
print(data_manager.sum())  # => 10
data_manager.add_x(4)      # => data_manager.x の値が 2 から 6 に更新される
print(data_manager.sum())  # => 14
data_manager.add_y(0)      # => data_manager.y の値が 3 から 3 に更新される
print(data_manager.sum())  # => 14
data_manager.add_z(-9)     # => data_manager.z の値が 5 から -4 に更新される
print(data_manager.sum())  # => 5

# 問2.7 (関数呼び出し)
# 以下で定義される関数 f, g があるとします。

def f(a):
    a = [6, 7, 8]

def g(a):
    a.append(1)
# これらに対し、次のコードの実行結果がどうなるか予想して下さい。実際にコードを実行して予想と一致しているか確認し、なぜそのような結果になったのか説明して下さい。

def somefunction():
    a0 = [1, 2, 3]
    f(a0)
    print(a0)

    a1 = [1, 2, 3]
    g(a1)
    print(a1)

somefunction()

# 問2.8 (制御構文)
# 2以上の整数 p が素数であるとは、「どんな 2 以上 p-1 以下の整数 k に対しても p は k で割り切れない」が成り立つことを指します。素数を小さい順から列挙すると、2, 3, 5, 7, 11, 13, 17, … となります。 チュートリアルで学んだ制御構文である if や for を用いて、2 から 100 からまでに含まれる素数を列挙して下さい。
print([x for x in range(2, 101) if all(x % y != 0 for y in range(2, x))]) 

# 問5.1 (プログラムにおけるベクトル・行列の計算)
# Pythonコード上でベクトルや行列に関する演算を行うことを考えてみよう。
# ベクトルはfloatのリスト、行列はfloatのリストのリストとして表現することにする。
# ベクトルx = [3, 7, 2]と行列 y=[[1,2,3][4,5,6]]とする。
# 2つのベクトルx,yを受け取り、その和x+yを返す関数を書いてください。
def add_vector(x, y):
    return [x[i] + y[i] for i in range(len(x))]

x = [1, 2, 3]
y = [8, 1, 2]
anser = add_vector(x, y)
print(anser)
# 2つの行列 X, Yを受け取り、その和 X+Yを返す関数を書いて下さい。コードは例えば以下のようになります。
def add_matrix(X, Y):
    return [add_vector(X[i], Y[i]) for i in range(len(X))]
X = [[1, 2, 3], [4, 5, 6]]
Y = [[8, 1, 2], [-1, 0, -2]]
answer = add_matrix(X, Y)
print(answer)
# 行列 Xとベクトル yを受け取り、その積 Xyを返す関数を書いて下さい。
def mul_matrix_vector(X, y):
    return [sum([X[i][j] * y[j] for j in range(len(y))]) for i in range(len(X))]
X = [[1, 2, 3],[4, 5, 6]]
y = [8, 1, 2]
answer = mul_matrix_vector(X, y)
print(answer)
# 2つの行列 X, Yを受け取り、その積 XYを返す関数を書いて下さい。
def mul_matrix(X, Y):
    return [mul_matrix_vector(X, Y[i]) for i in range(len(Y))]
X = [[1, 2, 3],[4, 5, 6]]
Y = [[8, 1],[-1, 0],[0, 1]]
anwer = mul_matrix(X, Y)
print(anwer)
