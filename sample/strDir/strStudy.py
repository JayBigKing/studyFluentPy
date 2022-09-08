import struct
import re

def test1():
    fmt = '<3s3sHH'
    with open('testStr0.jpg', 'rb') as fp:
        img = memoryview(fp.read())

    header = img[:10]
    print(bytes(header))
    print(struct.unpack(fmt, header))

    del header
    del img

def test2():
    str0 = "hello world"
    print(r'%s,%s,%s'%(str0,str0[::-1],str0[-1:]))

def test3():
    print(r'你好')
    print(rb'nihao')

def test4():
    re_number_str = re.compile(r'\d+')
    re_words_str = re.compile(r'\w+')
    re_number_bytes = re.compile(rb'\d+')
    re_words_bytes = re.compile(rb'\w+')

    text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
                "as 1729 = .....")
    text_bytes = text_str.encode('utf_8')

    print('Text',repr(text_str),sep='\n    ')
    print('Numbers')
    print(r'str : {0:}'.format(re_number_str.findall(text_str)))
    print(r'byte: {0:}'.format(re_number_bytes.findall(text_bytes)))

    print('Words')
    print(r'str : {0:}'.format(re_words_str.findall(text_str)))
    print(r'byte: {0:}'.format(re_words_bytes.findall(text_bytes)))

def main():
    test4()

if __name__ == '__main__':
    main()