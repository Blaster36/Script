# JupyterHub on Podman

- JupyterHub on Podmantの投稿記事で紹介したCodeを公開中

## 公開ファイル群

### Dockerfile.lab
  - JupyterLabコンテナイメージのビルド用
  - JupyterHub 3.1.1に合わせて連携用Pythonライブラリを追加

### jupyterhub_config.py
  - JupyterHubプロセスの振る舞い定義用

### Dockerfile.hub
  - JupyterHubコンテナイメージのビルド用
  - 工事中、JupyterHub 3.1.1をベースにカスタム予定
