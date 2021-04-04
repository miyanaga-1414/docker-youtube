# scikit-learnによる初歩の機械学習（Hello, world!"）

# 論理演算（and, or, xor）の機械学習

from sklearn.metrics import accuracy_score

# アルゴリズム
from sklearn.svm       import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble  import RandomForestClassifier

import warnings
warnings.filterwarnings('ignore')

# 学習データ：入力
in_data = [
    [0, 0]
    ,[0, 1]
    ,[1, 0]
    ,[1, 1]
]

# 学習データ：出力（ラベル)
out_data = [0, 0, 0, 1] # and
#out_data = [0, 1, 1, 1] # or
#out_data = [0, 1, 1, 0] # xor

#アルゴリズムの設定
clf = LinearSVC()
#clf = RandomForestClassifier()
#clf = KneighborsClassifier(n_neaigfbors = 1)

#学習
clf.fit(in_data, out_data)

#テストデータ
test_data = [
    [0, 0]
    ,[0, 1]
    ,[1, 0]
    ,[1, 1]
]

#予測
result = clf.predict(test_data)
print("正解：", out_data)
print("予測結果：", result)
print("正解率 = ", accuracy_score(out_data, result) * 100)
print("test")
