# 前言
请熟读中华人民共和国网络安全法，仅限授权安全测试使用,禁止未授权非法攻击站点

# 使用方法
1、使用单个URL尝试上传
```
python3 eoffice_fileupload.py -upload http://10.211.55.3:8082
```
![image](https://user-images.githubusercontent.com/62680449/145143414-7eb0342f-1081-4f02-a25e-561fc05e3427.png)
2、eoffice_logo上传失败，自动尝试theme上传
```
python3 eoffice_fileupload.py -upload http://10.211.55.3:8082  
```
![image](https://user-images.githubusercontent.com/62680449/145143519-d213d5cd-9462-481d-b1c4-521f7498f8a7.png)
3、查看请求
```
python3 eoffice_fileupload.py -h  
```
![image](https://user-images.githubusercontent.com/62680449/145143610-58ca2ae7-547a-44c5-8140-4133753c87d9.png)
