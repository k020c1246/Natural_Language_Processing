!apt install aptitude
!aptitude install mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file -y
!pip install mecab-python3==0.7
import MeCab

tg=MeCab.Tagger("-Ochasen")# -O　マイナスオー

text="OKグーグル、明日の東京の天気を教えて"

output=tg.parse(text)

print(output)

#ファイルの読み込み
f = open('neko1.txt')
data = f.read()
#print(data)

#形態素解析
tg = MeCab.Tagger("-Ochasen")
output=tg.parse(data)
#print(output)

f = open("output.txt", mode='w')
f.write(output)

#1行単位に分割
list_a=output.split("\n")

#あとで使うリストを定義
list0=[]#単語
list1=[]#読み
list2=[]#原形
list3=[]#品詞
list_count=[]

#全行をループ
for i in range(len(list_a)):


  #タブで分割
  list_buf=list_a[i].split("\t")

  #形態素解析が正確にできているかどうかを要素数で判定
  if len(list_buf) > 3:

    #各要素をリストに追加
    list0.append(list_buf[0])
    list1.append(list_buf[1])
    list2.append(list_buf[2])
    list3.append(list_buf[3])


#同じ単語（形態素、原形）をカウント
for i in range(len(list2)):
  count=0
  for j in range(len(list2)):
    if list2[i]==list2[j]:
      count=count+1
  list_count.append(count)

#上位50個を表示
for i in range(50):
  #print(list2[i],list_count[i])
  index=list_count.index(sorted(set(list_count))[-1*(i+1)])
  print(list2[index],":",list_count[index],":",list3[index])