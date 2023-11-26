mac上的项目复制到win时，会有很多隐藏文件。  
该程序可以提取出这些文件。

参数：  
origin_dir：（必填）需要处理的文件夹  
target_dir: （选填）提取出的文件夹需要保存的位置。如果不提供，会在origin_dir同级目录创建后缀为_mac_cache"的文件夹。
```linux
python remove_mac_cache.py origin_dir
```
