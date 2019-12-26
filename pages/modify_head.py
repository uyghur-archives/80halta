import glob
import os
import re
import html
import json

regex = '<html.*?>(.*?)</html>'
retitle = re.compile(regex, re.DOTALL)

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

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def getContent():
    root = './'
    res = {}
    files = glob.glob(os.path.join(root, '*.html'))

    files = sorted(files, key=numericalSort)

    for afile in files:
        try:
            with open(afile, 'r', encoding='utf_8_sig') as fp:
                content = fp.read()
                iters = retitle.finditer(content)
                for mt in iters:
                    strHtml = mt[1]
                    if strHtml.find('UA-143956760-1') > -1:
                        res[afile] = strHtml
                        continue

                    strHtml = html.unescape(strHtml).replace('<head>', '{}'.format(new_head))
                    res[afile] = strHtml
                fp.close()
            with open(afile, 'w', encoding='utf_8') as fp:
                newcontent = '<html dir="rtl">' + res[afile] + '</html>'
                fp.write('{}'.format(newcontent))
                fp.close()
                res[afile] = None

        except Exception as ex:
            print("{} -> {}".format(afile, ex))

if __name__ == "__main__":
    getContent()
