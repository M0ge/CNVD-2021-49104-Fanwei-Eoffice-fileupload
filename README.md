漏洞名称 : 泛微 E-Office 文件上传漏洞 
组件名称 : 泛微 E-Office  
影响范围 : 泛微 E-Office  V9.0  
漏洞类型 : 文件上传 
利用条件 :  
1、用户认证：不需要用户认证  
2、触发方式：远程 
综合评价 :  
<综合评定利用难度>：容易，无需授权即可文件上传  
<综合评定威胁等级>：高危，能上传 webshell  

# 前言
请熟读中华人民共和国网络安全法，仅限授权安全测试使用,禁止未授权非法攻击站点

本工具基于python，无危害检测漏洞是否存在，文件上传成功后，可以通过访问URL，查看返回值是否是 8942939b31e8dd5d331784f609e7098a 进行判断

与市面上不同的是，此工具检测2种上传接口，2种均无法使用后才返回上传失败

支持批量检测，只需将IP地址或域名放到txt文件中即可（需要带上http:// 或 https:// ）

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
3、查看帮助
```
python3 eoffice_fileupload.py -h  
```
![image](https://user-images.githubusercontent.com/62680449/145143610-58ca2ae7-547a-44c5-8140-4133753c87d9.png)
