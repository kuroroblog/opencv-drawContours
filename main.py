import cv2

# 1. 画像を読み込む
# imread : 指定した画像ファイルパスを読み込んで、画像に対してcv2(OpenCV)を利用できるようにする。
# 第一引数 : 画像ファイルパス
# 戻り値 : リスト型にて、画像情報を返す。
# リスト型とは? : https://atmarkit.itmedia.co.jp/ait/articles/1905/31/news015.html
img = cv2.imread('./input.png')

# 2. しきい値を用いて二値画像へ変更する

# cvtColor : 画像の色を変更する関数
# 第一引数 : 画像情報
# 第二引数 : 画像の色を変更するタイプの指定
# cv2.COLOR_BGR2GRAY : 画像をグレースケールへ変更する。
# グレースケールとは? : https://www.shinkohsha.co.jp/blog/monochrome-shirokuro-grayscale/
# 画像の色を変更するタイプ一覧情報 : https://docs.opencv.org/4.2.0/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab
# 戻り値 : リスト型にて、画像情報を返す。
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold : しきい値を用いて画像を二値画像へ変更する関数。
# 第一引数 : 画像情報(グレースケールでないといけない。二値画像へ変更できないため。)
# 第二引数 : しきい値
# 第三引数 : しきい値を超えた画素(点)に対して、与える色の値を指定。黒色とする。
# 第四引数 : 二値画像を判定する条件のタイプを設定する。
# cv2.THRESH_BINARY : (画素(点)の値 <= 第二引数)の場合、画素(点)に対して、0(白色)の値を与える。(画素(点)の値 > 第二引数)の場合、画素(点)に対して、第三引数の値(黒色)を与える。
# 二値画像を判定する条件のタイプ一覧情報 : https://pystyle.info/opencv-image-binarization/
# 戻り値 #################
# ret :  しきい値を返す。
# thresh : リスト型にて、二値画像情報を返す。
#########################
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
