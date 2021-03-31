import sys
import argparse
import csv
import pandas as pd
import Levenshtein

def com_string(args):
    print("dist =", Levenshtein.distance(args.string[0], args.string[1]))
    print("ratio =", Levenshtein.ratio(args.string[0], args.string[1]))

def com_file(args):
    input_csv = pd.read_csv(args.file, names=['文字列1', '文字列2', 'dist', 'ratio'])
    input_csv = input_csv.drop(0)
    for index, row in input_csv.iterrows():
        str1 = row[0]
        str2 = row[1]
        dist = Levenshtein.distance(str1, str2)
        ratio = Levenshtein.ratio(str1, str2)
        input_csv.at[index, 'dist'] = dist
        input_csv.at[index, 'ratio'] = ratio

    input_csv.to_csv(args.file, index=False)



parser = argparse.ArgumentParser(description='レーベンシュタイン距離計算')
parser.add_argument('-s', dest='string', type=str, nargs=2, 
                    help='コマンドライン引数に入力した二つの文字列のレーベンシュタイン距離と類似度を計算します．')
parser.add_argument('-f', dest='file', type=str,
                    help='csvファイルを読み込み，ファイル内に記載されている文字列の組に対するレーベンシュタイン距離と類似度を計測し, csvファイルで出力します．')

args = parser.parse_args()
if(args.string != None):
    com_string(args)
elif(args.file != None):
    com_file(args)
else:
    parser.print_help()