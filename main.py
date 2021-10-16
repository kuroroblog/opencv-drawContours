# 1. 画像を読み込む
# cv2(OpenCV)を利用する宣言を行う。
import cv2

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 戻り値 : 行 x 列 x 色の三次元配列(numpy.ndarray)が返される。
img = cv2.imread('./input.png')

# 2. しきい値を用いて二値画像へ変更する

# cvtColor : 画像の色空間(色)の変更を行う関数。
# cvtColorについて : https://kuroro.blog/python/7IFCPLA4DzV8nUTchKsb/
# 第一引数 : 多次元配列(numpy.ndarray)
# 第二引数 : 変更前の画像の色空間(色)と、変更後の画像の色空間(色)を示す定数を設定。
# cv2.COLOR_BGR2GRAY : BGR(Blue, Green, Red)形式の色空間(色)を持つ画像をグレースケール画像へ変更する。
# グレースケールとは? : https://www.shinkohsha.co.jp/blog/monochrome-shirokuro-grayscale/
# 戻り値 : 多次元配列(numpy.ndarray)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold : しきい値を用いて画像を二値画像へ変更する関数。
# thresholdについて : https://kuroro.blog/python/jofbNumJ9HtfTxnM8QHJ/
# 第一引数 : 多次元配列(numpy.ndarray)
# 第二引数 : しきい値
# 第三引数 : しきい値を超えた画素(点)に対して、色の値を指定。255(白色)とする。
# 第四引数 : 二値画像を判定する条件のタイプを設定する。
# cv2.THRESH_BINARY : (画素(点)の値 <= 第二引数)の場合、画素(点)に対して、0(黒色)の値を与える。(画素(点)の値 > 第二引数)の場合、画素(点)に対して、第三引数の値(白色)を与える。
# 戻り値 #################
# ret :  しきい値を返す。
# thresh : 多次元配列(numpy.ndarray)
########################
ret, thresh = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)

# 3. findContours関数を用いて輪郭の検出を行う
# findContours : 輪郭の検出を行う関数
# findContoursについて : https://kuroro.blog/python/nSvll3vvUPah6Et2rJqG/
# 第一引数 : 二値画像情報
# 第二引数 : 輪郭を検出するタイプを指定する。
# cv2.RETR_EXTERNAL : 一番外側の輪郭のみ抽出する。
# 第三引数 : 輪郭を形成する、画素(点)を近似する方法のタイプを指定する。##############
# cv2.CHAIN_APPROX_SIMPLE : 冗長な画素(点)の情報を削除し、メモリの使用を抑えて輪郭の検出を行う。
# cv2.CHAIN_APPROX_NONE : 全画素(点)の情報を利用し、輪郭の検出を行う。画素数が多い場合に、メモリの使用量が大きくなり、重くなるので注意が必要。
###############################################
# 戻り値  #######################
# image : 輪郭付き画像情報
# contours : 輪郭を形成する画素(点)情報
# hierarchy : オブジェクト(物体)の階層構造情報
###############################
# OpenCVのバージョンが4.0より小さい場合
# image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# OpenCVのバージョンが4.0以上の場合
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. 3の輪郭の検出情報をもとに、輪郭を描画する
# drawContours : 輪郭の検出情報をもとに、輪郭の描画を行う関数
# 第一引数 : 画像情報
# 第二引数 : 輪郭を形成する画素(点)情報
# 第三引数 : 輪郭を形成する画素(点)のインデックス番号を指定する。例えば0を指定すると、1番目の輪郭を形成する画素(点)のみを描画する。1を指定すると、2番目の輪郭を形成する画素(点)のみを描画する。輪郭を形成する画素(点)を全て描画したい場合は、-1を指定する。
# 第四引数 : 輪郭を形成する画素(点)の色。RGB指定。
# RGBとは? : https://ja.wikipedia.org/wiki/RGB
# 第五引数(任意) : 輪郭を形成する画素(点)の大きさを設定。デフォルト1。
# 戻り値 : 画像情報
output = cv2.drawContours(img, contours, -1, (255, 255, 0), 5)

# 5. 画像を書き出す
# imwrite : 画像の書き出しを行う関数
# 第一引数 : 書き出し先の画像ファイル名
# 第二引数 : 画像情報
cv2.imwrite('./output.png', output)
