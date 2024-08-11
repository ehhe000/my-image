from setuptools import setup

setup(
    name='my_image_plugin',
    version='0.1',
    packages=['my_image_plugin'],
    install_requires=[
        'dashscope',
    ],
    entry_points={
        'console_scripts': [
            'generate-image-url=my_image_plugin.plugin:generate_image_url',
        ],
    },
)