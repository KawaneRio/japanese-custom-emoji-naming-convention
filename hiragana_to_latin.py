import sys

# ファイルから変換テーブルを読み込む
conversion_table_path = '/home/kawanerio/jumanpp-1.01/Japanese-Latin_Conversion_Table2'

def load_conversion_table(file_path):
    table = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 各行を分割して変換テーブルに格納
            hiragana, romanization = line.strip().split(' = ')
            table[hiragana.strip()] = romanization.strip()
    return table

conversion_table = load_conversion_table(conversion_table_path)

# ひらがなをラテンアルファベットに変換する関数
def hiragana_to_latin(text):
    latin_text = []
    i = 0
    while i < len(text):
        # 二重母音（拗音）をチェック
        if i + 1 < len(text) and text[i:i+2] in conversion_table:
            latin_text.append(conversion_table[text[i:i+2]])
            i += 2
        # 単一の文字をチェック
        elif text[i] in conversion_table:
            latin_text.append(conversion_table[text[i]])
            i += 1
        else:
            # 変換テーブルに存在しない場合はそのまま通す
            latin_text.append(text[i])
            i += 1
    # 末尾のアンダースコアを削除（存在する場合）
    if latin_text and latin_text[-1] == '_':
        latin_text.pop()
    return ''.join(latin_text)

# 標準入力からひらがなのテキストを読み込む
hiragana_text = sys.stdin.read().strip()

# ひらがなをラテンアルファベットに変換し、拗音を処理する
latin_text = hiragana_to_latin(hiragana_text)
print(latin_text)
