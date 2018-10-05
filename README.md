段义文-日常工作工具集
-------------------------
-------------------------

* analysis 数据分析包
    * dicom_ratio.py 批量分析dicom数据标签不同占比情况
    * watch-view.py 对dicom文件进行二维成像

* search 数据搜索包
    * 搜索指定日期内，未预测数据集合

* send 信号发送包
    * 通过config.py配置发送信息，将预测信号json发送到REDIS的频道中

* sql_guzhe 数据调研包
    * DAL.py 数据库封装类
    * sql_guze.py 查询符合要求的骨折数据，格式化保存
    * filter.py 数据过滤工具，过滤不符合重建算法的数据

* STATISTIC 数据统计包
    * 统计相关模块的运行时间

