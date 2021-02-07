import hashlib
import string
from itertools import product, count

url_hash2code = {}
code2_url = {}
prefix = 'short.ly/'
url_code_gen = None
def gen_code():
    ret = []
    for i in range(1,5):
        ret.extend([''.join(p) for p in product(*[string.ascii_lowercase] * i)])
    return iter(ret)
def url_shortener(long_url):
    global url_code_gen
    if url_code_gen is None:
        url_code_gen = gen_code()
    hash = hashlib.md5(long_url.encode()).hexdigest()
    if hash in url_hash2code.keys():
        return prefix + url_hash2code.get(hash)
    else:
        new_url_code = next(url_code_gen)
        code2_url.update({new_url_code:long_url})
        url_hash2code.update({hash:new_url_code})
        return prefix + new_url_code

def url_redirector(short_url):
    short_url = short_url[9:]
    return code2_url.get(short_url)

# print(hashlib.md5(b'x').hexdigest())
# print(string.ascii_lowercase)
# print(url_code)
# print(len(url_code))
# print(url_shortener('1234'))
# print(url_shortener('1234'))
# print(url_shortener('1234'))

# print(url_redirector('short.ly/a'))
# print(26**4+26**3+26**2+26)
# print(map())
# print(product(*[string.ascii_lowercase] * 1))
# print(product(*[string.ascii_lowercase] * 2))
# print([''.join(p) for p in product(*[string.ascii_lowercase] * 1)])

# print([d for d in count(1)])