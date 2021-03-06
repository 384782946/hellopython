# coding:utf-8

import os
from poplib import POP3
from email import parser
from email.header import decode_header
from email.utils import parseaddr

def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def parse_parts(msg):
    indent = 0
    if (msg.is_multipart()):
        # 如果邮件对象是一个MIMEMultipart,
        # get_payload()返回list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            parse_parts(part)
    else:
        # 邮件对象不是一个MIMEMultipart,
        # 就根据content_type判断:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            # 纯文本或HTML内容:
            content = msg.get_payload(decode=True)
            # 要检测文本编码:
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            # 不是文本,作为附件处理:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# indent用于缩进显示:
def print_info(msg):
    # 邮件的From, To, Subject存在于根对象上:
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header=='Subject':
                # 需要解码Subject字符串:
                value = decode_str(value)
            else:
                # 需要解码Email地址:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
        print('%s%s: %s' % ('  ', header, value))
    parse_parts(msg)

if __name__ == "__main__":
    usr = raw_input('input your 163 email user name:')
    psw = raw_input('input your password:')
    p = POP3('pop.163.com')
    p.user(usr)
    p.pass_(psw)
    #list = p.stat()
    #print list
    #rsp,msg,siz = p.retr(list[0])
    resp,mails,octets = p.list()
    print mails
    index = len(mails)
    resp,lines,octets = p.retr(index)
    msg_content = os.linesep.join(lines)
    msg = parser.Parser().parsestr(msg_content)
    print_info(msg)
    p.quit()