# ガウス・ルジャンドル法を用いた円周率計算プログラム@Python  
反復計算により円周率を求める。正確な小数を実装するためDecimalモジュールで数値の表現を行っている。  
Pythonでの実装のため、精度(桁数)に応じて計算速度が大幅に長くなる。

## 内容物  
- Gauss_Legendre.py  
  円周率計算プログラムの本体。  
- CheckDigit.py  
  簡易桁数チェッカ。実行結果のチェック用。使い方↓  
  `$ python3 CheckDigit.py [Calculated] [CorrectValue]`  
- Machin.py
  マチン法を実装した円周率計算プログラム。試作品です。
