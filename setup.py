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
    version='1.0.1',
    description='Service serves savvy server stats.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/service',
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
            'pylint >= 2.5.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'service=service.app:main'
        ]
    },
    python_requires='>=3.6',
)
