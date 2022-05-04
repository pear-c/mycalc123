import setuptools

setuptools.setup (
  include_package_data = True,
  name='mycalc123',
  version='1.0.0',
  description='oss-dev my calculator 0001',
  author='tjdghks',
  author_email='zxcv9676@naver.com',
  url = "https://github.com/pear-c/mycalc123",
  download_url = "https://github.com/pear-c/mycalc123/archive/refs/tags/v1.0.1.zip",
  install_requires=['pytest'],
  long_description = 'oss-dev calculator python module',
  long_description_content_type = 'text/markdown',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
  ],
)
