from setuptools import setup, find_packages

setup(
    name='my_image_plugin',
    version='0.1',
    packages=find_packages(where='src'),  # 指定包所在的目录
    package_dir={'': 'src'},  # 指定包目录相对于项目根目录的位置
    install_requires=[
        'dashscope',
    ],
    entry_points={
        'console_scripts': [
            'generate-image-url=my_image_plugin:generate_image_url',  # 注意这里的路径
        ],
    },
)