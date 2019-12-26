import glob
import os
import re
import html

import json

#Header ghila qoshqandikin awu Googlening ID sini headerning ichidin izdeymiz
regex = '<!--.*?-->'
recomment = re.compile(regex, re.DOTALL)
new_head = '''
<head>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-143956760-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-143956760-1');
</script>
'''

#linkrep = re.compile("http://www.80halta.com/\?p=([0-9]+?)")

linkrep = re.compile("/\?p=(\d+.*?)")

#linkcat = re.compile("\?cat=(\d+.*?)")
linkcat = re.compile("/\?cat=[^\'\"].*?[\'\"]")

def _linktohtml(mg):
    link = mg.group(1)
    link = './page_{}.html'.format(link)
    return link

def _linktocat(mg):
    link = mg.group(0)
    link = link.replace('/?cat=','cat_')
    link = link.replace('&amp;paged=','_p_')
    link = './'+link[:-1]+'.html'+link[-1:]
    return link



def _replace(alltext):
    alltxt = re.sub(recomment,'',alltext)
    alltxt = linkrep.sub(_linktohtml,alltxt)
    alltxt = linkcat.sub(_linktocat,alltxt)
    alltxt = alltxt.replace('http://www.80halta.com/','')
    alltxt = alltxt.replace('http://www.80halta.com','')

    alltxt = alltxt.replace('http://80halta.com/','')
    alltxt = alltxt.replace('http://80halta.com','')

    alltxt = alltxt.replace('href="/"','href="./top.html"')
    alltxt = alltxt.replace('/?page_id=','#')
    return alltxt


def _linktoasp(mg):
    link = mg.group(0)
    link = link.replace("href=show.asp?id=","href=./asp_")
    link = link + '.html'
    return link


def _linktotitle(mg):
    link = mg.group(0)
    link = link.replace("showtitle.asp?cid=","./title_")
    link = link + '.html'
    return link

def _linkart(mg):
    link = mg.group(0)
    link = link.replace("article/termiler/","")
    link = link.replace("article/hatire/","")
    link = link.replace("article/edebiy-yazmilar/","")
    link = link.replace("article/","")
    link = './asp_'+link + 'l'
    return link



def _linkdefault(mg):
    link = mg.group(0)
    link = link.replace("default.asp?cateID=","./aspcat_")
    #link = link.replace("article/hatire/","")
    #link = link.replace("article/edebiy-yazmilar/","")
    #link = link.replace("article/","")
    link = link + '.html'
    return link


linkasp =   re.compile("href=show.asp\?id=(\d+.*?)")
linktitle = re.compile("showtitle.asp\?cid=(\d+.*?)")
linkart   = re.compile('article/.*?.htm')

linkdef =   re.compile("default.asp\?cateID=(\d+.*?)")

def _replaceasp(alltext):
    alltxt = re.sub(recomment,'',alltext)
    alltxt = alltxt.replace('http://www.ulanma.com/js/to_ulanma.js','')

    alltxt = alltxt.replace('http://www.80halta.com/','')
    alltxt = alltxt.replace('http://www.80halta.com','')
    alltxt = alltxt.replace('http://80halta.com/','')
    alltxt = alltxt.replace('http://80halta.com','')

    alltxt = linkasp.sub(_linktoasp,alltxt)
    alltxt = linktitle.sub(_linktotitle,alltxt)
    alltxt = linkart.sub(_linkart,alltxt)
    alltxt = linkdef.sub(_linkdefault,alltxt)
    alltxt = alltxt.replace('default.asp','./default.html#')
    return alltxt

def Cat():
    root = '.\\www.80halta.com'
    newdir = os.path.join(root,"pages")
    os.makedirs(newdir,exist_ok=True)
    files = glob.glob(os.path.join(root, '_cat=*/*.html'))
    #files = sorted(files)
    unicfile ={}
    for afile in files:
        print(afile, end='')
        tmp = afile.replace('.\\www.80halta.com\\','')
        tmp = tmp.replace('\\index.html','')
        tmp = tmp.replace('_cat=','cat_')
        tmp = tmp.replace('&paged=','_p_')
        newfile = tmp+'.html'
        print(' -> ',newfile)
        unicfile[newfile] = afile

    for key, val in unicfile.items():
        with open(val,'r',encoding='utf_8_sig') as fp:
            alltxt = fp.read()
        alltxt = _replace(alltxt)
        with open(os.path.join(newdir,key),'w',encoding='utf-8') as wf:
            wf.write(alltxt)

    return


def Pages():
    root = '.\\www.80halta.com'
    newdir = os.path.join(root,"pages")
    os.makedirs(newdir,exist_ok=True)
    files = glob.glob(os.path.join(root, '_p=*/*.html'))
    #files = sorted(files)
    unicfile ={}
    for afile in files:
        print(afile, end='')
        tmp = afile[21:]
        pos = tmp.find('&')
        if pos == -1:
            pos = tmp.find('\\')

        newfile = 'page_'+tmp[0:pos] +'.html'
        print(' -> ',newfile)
        unicfile[newfile] = afile

    for key, val in unicfile.items():
        with open(val,'r',encoding='utf_8_sig') as fp:
            alltxt = fp.read()

        alltxt = _replace(alltxt)
        with open(os.path.join(newdir,key),'w',encoding='utf-8') as wf:
            wf.write(alltxt)

    indfl = os.path.join(root,'_','index.html')
    with open(indfl,'r',encoding='utf_8_sig') as fp:
        alltxt = fp.read()

    alltxt = _replace(alltxt)
    with open(os.path.join(newdir,'top.html'),'w',encoding='utf-8') as wf:
        wf.write(alltxt)


    indfl = os.path.join(root,'index.html')
    with open(indfl,'r',encoding='utf_8_sig') as fp:
        alltxt = fp.read()

    alltxt = _replace(alltxt)
    with open(os.path.join(newdir,'index.html'),'w',encoding='utf-8') as wf:
        wf.write(alltxt)

    return



def ShowAsp():
    root = '.\\www.80halta.com'
    newdir = os.path.join(root,"pages")
    os.makedirs(newdir,exist_ok=True)
    files = glob.glob(os.path.join(root, 'show.asp_id=*'))
    #files = sorted(files)
    for afile in files:
        print(afile, end='')
        tmp = afile.replace('.\\www.80halta.com\\show.asp_id=','asp_')
        newfile = tmp +'.html'
        print(' -> ',newfile)

        with open(afile,'r',encoding='utf_8_sig') as fp:
            alltxt = fp.read()

        alltxt = _replaceasp(alltxt)
        with open(os.path.join(newdir,newfile),'w',encoding='utf-8') as wf:
            wf.write(alltxt)


def ShowAspTitle():
    root = '.\\www.80halta.com'
    newdir = os.path.join(root,"pages")
    os.makedirs(newdir,exist_ok=True)
    files = glob.glob(os.path.join(root, 'showtitle.asp_cid=*'))
    #files = sorted(files)
    for afile in files:
        print(afile, end='')
        tmp = afile.replace('.\\www.80halta.com\\showtitle.asp_cid=','title_')
        newfile = tmp +'.html'
        print(' -> ',newfile)

        with open(afile,'r',encoding='utf_8_sig') as fp:
            alltxt = fp.read()
        alltxt = _replaceasp(alltxt)
        with open(os.path.join(newdir,newfile),'w',encoding='utf-8') as wf:
            wf.write(alltxt)


def Acticles():
    root = '.\\www.80halta.com'
    newdir = os.path.join(root,"pages")
    os.makedirs(newdir,exist_ok=True)
    pat = os.path.join(root, 'article\\**\\*.htm')
    files = glob.glob(pat,recursive=True)
    for afile in files:
        print(afile, end='')
        tmp = os.path.basename(afile)
        newfile = "asp_"+tmp +'l'
        print(' -> ',newfile)
        if newfile == 'asp_465.html':
            print(newfile)

        with open(afile,'r',encoding='utf_8_sig') as fp:
            alltxt = fp.read()

        alltxt = _replaceasp(alltxt)
        with open(os.path.join(newdir,newfile),'w',encoding='utf-8') as wf:
            wf.write(alltxt)


def DefaultAsp():
    root = '.\\www.80halta.com'
    newdir = os.path.join(root,"pages")
    os.makedirs(newdir,exist_ok=True)
    files = glob.glob(os.path.join(root, 'default.asp_cateid=*'))
    #files = sorted(files)
    for afile in files:
        print(afile, end='')
        tmp = afile.lower()
        tmp = tmp.replace('.\\www.80halta.com\\default.asp_cateid=','aspcat_',)
        tmp = tmp.replace('&page=','_p_')
        if tmp.find('=') == -1:
            newfile = tmp +'.html'
            print(' -> ',newfile)

            with open(afile,'r',encoding='utf_8_sig') as fp:
                alltxt = fp.read()

            alltxt = _replaceasp(alltxt)
            with open(os.path.join(newdir,newfile),'w',encoding='utf-8') as wf:
                wf.write(alltxt)
    afile = os.path.join(root,'default.asp')
    with open(afile,'r',encoding='utf_8_sig') as fp:
        alltxt = fp.read()

    alltxt = _replaceasp(alltxt)
    with open(os.path.join(newdir,'default.html'),'w',encoding='utf-8') as wf:
        wf.write(alltxt)



regex ='<title>(.*?)</title>'
retitle = re.compile(regex, re.DOTALL)

head ='''
  <html dir="RTL">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style type="text/css">
@font-face {
	font-family: "UKIJ Tuz";
	font-weight: normal;
	src: local("UKIJ Tuz"), url("/UKIJTuz.ttf") format("TrueType"); /* non-IE */

body{
	font-size: 120%;
	font-family: UKIJ Tuz, UKIJ Basma, Boghda Tuz, UKIJ Nasq, Arial Unicode MS,Tahoma;
	text-align: justify;
}
a{
      text-decoration:none;
}
</style>
<title>سەكسەن خالتا توربېتىنىڭ https://archive.org/ دىن ئەسلىگە كەلتۈرۈلگەنلىرى</title>
</head>
<body><ul>
'''

foot ='''
</ul>
</body>
</html>
'''


def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def getTitles():
    root = './www.80halta.com/pages'
    res ={}
    files = glob.glob(os.path.join(root,'*.html'))

    files=sorted(files, key=numericalSort)

    for afile in files:
        try:
            with open(afile,'r',encoding='utf_8_sig') as fp:
                content  = fp.read()
                iters = retitle.finditer(content)
                for mt in iters:
                    strTitle = mt[1]
                    afile = afile.replace('./www.80halta.com/','')
                    strTitle = html.unescape(strTitle)
                    strTitle = strTitle.replace(' - 80 خالتا بلوگى','').replace('| 80 خالتا بلوگى','')
                    strTitle = strTitle.replace(' | 80 خالتا ئۇيغۇر تېبابىتى تور بېكىتى','')
                    strTitle = strTitle.replace(' | 全部文章 - 第','(').replace('页',')')
                    if strTitle =='80Halta.com' or len(strTitle.strip())==0:
                        strTitle = os.path.basename(afile)
                    res[afile] = strTitle
                    break        
        except Exception as ex:
            print("{} -> {}".format(afile,ex))
    return res

def makelist():
    mezmun=''
    res = getTitles()    
    for k,v in res.items():
        mezmun +='<li><a href="{}">{}</a></li>\n'.format(k.replace('\\','/'),v)
    mezmun = head + mezmun + foot
    with open('./www.80halta.com/list.html','w', encoding='utf-8') as fp:
        fp.write(mezmun)


if __name__ == "__main__":
    #Cat()
    #Pages()
    #ShowAsp()
    #ShowAspTitle()
    #DefaultAsp()
    #Acticles()
    makelist()