# BOOM

## Blur Outside Of Mask

COCOフォーマットのアノテーションと画像を受け取り、マスク画像で囲っている対象以外にBlur処理をかけることで学習の邪魔になることを防ぎます。

You can blur images outside of segmentation mask. This repo is grounded in COCO format annotation.

## Quick Start

`python BOOM.py`

## Edit config.yaml

プロジェクトに合わせてyamlファイルを適宜書き換えてください。

Please edit config.yaml according to your task.

sample: 

```yaml
//config.yaml
config:
  imageDir: "./data/demo/images/base/original"
  annotationPath: "./data/demo/annotations/annotation.json"
  picCategory: "person"
  karnelSize: 25
```