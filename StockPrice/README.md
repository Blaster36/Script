# 株価予測 w/LightGBM

## 参考
  - [Pythonで株価のデータ分析｜株価分析を通してpythonによるデータ分析でできることを学びましょう【株価のデータ取得から、データ加工、指標の追加、グラフ化まで】](https://kino-code.com/python_automation_stock_analysis2/)
  - [Pythonのファイナンス（株 , FX）に特化したライブラリの使い方を解説【データ可視化、チャート分析を中心に進めていきます】](https://kino-code.com/python_finance-01/)
  - [【Pythonでファイナンス分析（株・FX）】日本発祥のテクニカル指標「一目均衡表」の作成方法](https://kino-code.com/python_finance-02/)
  - [超簡単Pythonで株価予測（LightGBM 利用）機械学習](https://note.com/10mohi6/n/n4b1196fea816)
  - [超簡単Pythonで株価予測（Optuna・LightGBM 利用）ハイパーパラメータ自動最適化](https://note.com/10mohi6/n/n46d1bb0267b7)

## 公開ファイル群

### Dockerfiles.kinocode
  - JupyterLabコンテナイメージのビルド用
  - Anacondaベース、rootアカウント起動
  - MeCab本体および操作Client（mecab-python3）のPythonライブラリを追加

### predStockPriceKino.ipynb
  - 特徴量設計

### finance_01_code.ipynb
  - 特徴量設計
  - データ可視化

### finance_02_code.ipynb
  - 特徴量設計
  - データ可視化

### predStockPriceKino-LightGBM.ipynb
  - 予測モデルの作成
  - 予測精度の確認
