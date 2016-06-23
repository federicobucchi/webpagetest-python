from setuptools import setup

setup(name='webpagetest-python',
      version='0.0.1',
      description='Get assets details from webpagetest',
      author='Federico Bucchi',
      author_email='fbucchi@gopro.com',
      license='MIT',
      install_requires=[
        'requests',
        'threading'
      ])
