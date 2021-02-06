import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'psutil >= 5.7.0',
    'slackclient >= 2.7.0',
    'python-dotenv >= 0.13.0',
]

setuptools.setup(
    name='service-stats',
    version='2.0.0',
    description='Service serves savvy server stats.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/service-stats',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest >= 6.0.0',
            'pytest-cov >= 2.10.0',
            'coveralls >= 2.1.2',
            'flake8 >= 3.8.0',
            'mock >= 4.0.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'service-stats=service_stats.app:main'
        ]
    },
    python_requires='>=3.6',
)
