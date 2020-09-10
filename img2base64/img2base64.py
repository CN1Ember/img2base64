import base64
import os

class img2base64(object):
    @staticmethod
    def encode(img_name):
        full_name = os.path.split(img_name)[1]
        print(full_name)
        fname = os.path.splitext(full_name)[0]
        print(fname)
        encode_str = base64.b64encode(fname.encode())
        print(encode_str)
        txt_str = encode_str.decode()
        with open('{}.txt'.format(txt_str),'w') as fout:
            with open(img_name, 'rb') as fin:
                encode_img = base64.b64encode(fin.read())
            fout.write(encode_img.decode())

    @staticmethod
    def decode(txt_name):
        full_name = os.path.split(txt_name)[1]
        fname = os.path.splitext(full_name)[0]
        img_name = base64.b64decode(fname.encode()).decode()
        with open('{}.png'.format(img_name), 'wb') as fout:
            with open(txt_name, 'r') as fin:
                fout.write(base64.b64decode(fin.read().encode()))


# img2base64.encode('your_name.png')
# img2base64.decode('eW91cl9uYW1l.txt')

test_code=img2base64()
test_code.encode('test.png')
# test_code.encode('eW91cl9uYW1l.txt')
# test_code.decode('ZVc5MWNsOXVZVzFs.txt')
# test_code.decode('dGVzdA==.txt')



