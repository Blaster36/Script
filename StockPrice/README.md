# 株価予測 w/TA-Lib+LightGBM+Optuna

## 参考
  - [Pythonで将来予測｜株価データを使ってpythonで機械学習をしてみよう【データ加工、データ整形、予測モデル作成、株価データの分類予測、予測精度の確認まで】](https://www.youtube.com/watch?v=asfWaVpCyl8)
  - [Pythonで株価のデータ分析｜株価分析を通してpythonによるデータ分析でできることを学びましょう【株価のデータ取得から、データ加工、指標の追加、グラフ化まで】](https://kino-code.com/python_automation_stock_analysis2/)
  - [Pythonのファイナンス（株 , FX）に特化したライブラリの使い方を解説【データ可視化、チャート分析を中心に進めていきます】](https://kino-code.com/python_finance-01/)
  - [【Pythonでファイナンス分析（株・FX）】日本発祥のテクニカル指標「一目均衡表」の作成方法](https://kino-code.com/python_finance-02/)
  - [超簡単Pythonで株価予測（LightGBM 利用）機械学習](https://note.com/10mohi6/n/n4b1196fea816)
  - [超簡単Pythonで株価予測（Optuna・LightGBM 利用）ハイパーパラメータ自動最適化](https://note.com/10mohi6/n/n46d1bb0267b7)
  - [機械学習による株価予測（LightGBM）](https://book-read-yoshi.hatenablog.com/entry/2021/04/19/AI-machine-learning-stock-prediction-lightgbm)
  - [機械学習で株価予測（TA-LibとLightGBMを使った学習モデル構築）](https://nehori.com/nikki/2020/01/26/post-15231/)
  - [年利30%超え！！！！！LightGBMを用いたトヨタ株自動売買シミュレーション](https://qiita.com/kt38k/items/3c0ee4251475b6407007)

## 公開ファイル群

### Dockerfiles.kinocode
  - JupyterLabコンテナイメージのビルド用
  - Anacondaベース、rootアカウント起動
  - MeCab本体および操作Client（mecab-python3）のPythonライブラリを追加

### predStockPrice-LightGBM1.ipynb
  - データの収集および整形
  - 特徴量設計

### predStockPrice-LightGBM2.ipynb
  #### predStockPrice-LightGBM2-1.ipynb
  - 予測モデルの作成（含むハイパーパラメータのチューニング）
  - 予測精度の確認
  #### predStockPrice-LightGBM2-2.ipynb
  - 特徴量重要度の確認（可視化）
  - lightgbm.plot_importance（棒グラフ図）とlightgbm.Booster.trees_to_dataframe（DataFrame）を利用

### download.ipynb
### download2.ipynb
  - Yahoo!ファイナンスから株価データを取得

### predStockPrice-Prophet1.ipynb
  - データの収集および整形
  - 予測モデルの作成
  - 予測結果の確認
