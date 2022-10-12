# 后端说明文档

## 环境说明
后端计划使用Python 3.9 + django框架完成 + mysql/sqlite3

使用conda完成python相关的环境配置，配置文件见environment.yml

使用下述命令复制python环境（或使用pycharm自动完成配置）
```shell
conda env create -f environment.yml
```

## 数据库相关
在开发过程中，如果使用mysql作为数据库，可能不便于调试和跨机器的使用，故开发中计划先使用本地的sqlite3完成相关任务，待系统完善，需要部署时，再切换mysql。

数据模型的定义文件为db.sql