import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'psutil == 5.*',
    'slackclient == 2.*',
    'python-dotenv == 0.17.*',
]

DEV_REQUIREMENTS = [
    'coveralls == 3.*',
    'flake8',
    'mock == 4.*',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

setuptools.setup(
    name='service-stats',
    version='2.1.0',
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
        'dev': DEV_REQUIREMENTS
    },
    entry_points={
        'console_scripts': [
            'service-stats=service_stats.app:main'
        ]
    },
    python_requires='>=3.6',
)
