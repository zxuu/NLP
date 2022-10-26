# coding=utf-8
"""
目标：提供一个函数能够从网上下载资源
输入：
    url列表
    保存路径
输出：
    保存到指定路径中的文件
要求：
    能够实现下载过程，即从0%到100%可视化
"""
# =====================================================
from six.moves import urllib
import os
import sys


def download_and_extract(filepath, save_dir):
    """根据给定的URL地址下载文件
    Parameter:
        filepath: list 文件的URL路径地址
        save_dir: str  保存路径
    Return:
        None
    """
    for url, index in zip(filepath, range(len(filepath))):
        filename = url.split('/')[-1]
        save_path = os.path.join(save_dir, filename)
        urllib.request.urlretrieve(url, save_path)
        sys.stdout.write('\r>> Downloading %.1f%%' % (float(index + 1) / float(len(filepath)) * 100.0))
        sys.stdout.flush()
    print('\nSuccessfully downloaded')


def _get_file_urls(file_url_txt):
    """根据URL路径txt文件，获取URL地址列表
    Parameter:
        file_url_txt: str  txt文件本地路径
    Return:
        filepath: list  URL列表
    """
    filepath = []
    file = open(file_url_txt, 'r')
    for line in file.readlines():
        line = line.strip()
        filepath.append(line)
    file.close()
    return filepath


if __name__ == '__main__':
    file_url_txt = 'http://openkg1.oss-cn-beijing.aliyuncs.com/8bdf3e4e-e4e5-4ea6-a2e5-1fb217c6b855/smallreldistribution.txt'
    save_dir = 'data/'
    filepath = _get_file_urls(file_url_txt)
    download_and_extract(filepath, save_dir)
