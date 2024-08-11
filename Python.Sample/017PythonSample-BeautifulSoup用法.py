html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
print(type(soup.p))

#（1）获取名称
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print(tag.name)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#（2）获取属性
soup = BeautifulSoup(html_doc, 'html')
print(soup.p.attrs)
print(soup.p.attrs['name'])
#（4）获取子节点
soup = BeautifulSoup(html_doc, 'html')
print(soup.head.title)
print(soup.head.title.string)
#(6)关联选择
soup = BeautifulSoup(html_doc, 'html')
print(soup.p.contents)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b>
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html')
print(soup.p.contents)



html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>


<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html')
print(soup.p.children)
print(list(soup.p.children))
for i in soup.p.children:
    print(i)
    
    
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>


<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span>Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.p.descendants)
for child in soup.p.descendants:
    print(child)
    
    
#父节点和祖先节点
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>


<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<p>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.a.parent)




html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>


<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
<p>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.a.parents)
for i, parent in enumerate(soup.a.parents):
    print(i, parent)
    
#兄弟节点
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>


<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.a.next_sibling)
print(list(soup.a.next_siblings))
print(soup.a.previous_sibling)
print(list(soup.a.previous_siblings))


#方法选择器
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.find_all('a'))
print(len(soup.find_all('a')))


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.find_all('a'))
for a in soup.find_all('a'):
    print(a.find_all('span'))
    print(a.string)
    
#属性选择
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.find_all(attrs={'id': 'link1'}))
print(soup.find_all(attrs={'name': 'Dormouse'}))

soup = BeautifulSoup(html_doc, 'html')
print(soup.find_all(class_ = 'sister'))
soup = BeautifulSoup(html_doc, 'html')
print(soup.find_all(id = 'link2'))


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="Dormouse"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.find(name='a'))
print(type(soup.find(name='a')))


#CSS选择器
html_doc = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello World</h4>   
    </div>
    
    <div class="panel-body">
        <ul class="list" id="list-1">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
        
        <ul class="list list-samll" id="list-2">
           <li class="element">Foo</li>
           <li class="element">Bar</li>
           <li class="element">Jay</li>
        </ul>
    </div>
    </div>
</div>
"""

soup = BeautifulSoup(html_doc, 'html')
print(soup.select('.panel .panel-heading')) # 获取class为panel-heading的节点
print(soup.select('ul li')) # 获取ul下的li节点
print(soup.select('#list-2 li')) # 获取id为list-2下的li节点
print(soup.select('ul'))    # 获取所有的ul节点
print(type(soup.select('ul')[0]))

#嵌套选择

soup = BeautifulSoup(html_doc, 'html')
for ul in soup.select('ul'):
    print(ul.select('li'))
    
#属性选择
soup = BeautifulSoup(html_doc, 'html')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
    
#获取文本
soup = BeautifulSoup(html_doc, 'html')
for li in soup.select('li'):
    print('String:', li.string)
    print('get text:', li.get_text())