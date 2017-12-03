from setuptools import setup


setup(
    name="Finger balabolka",
    version='1.0.6',
    description="A project of flood chat.",
    long_description="A flood chat project on ptyhon 3 and PyQt5",
    author="Artem Sukharenko",
    author_email="truecyxapic@yandex.ru",
    url="https://github.com/Cyxapic/fb_client",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Flood chat for lern',
    packages=['fb_client'],
    install_requires=[
        "certifi==2017.11.5",
        "chardet==3.0.4",
        "click==6.7",
        "coverage==4.4.1",
        "dparse==0.2.1",
        "idna==2.6",
        "mccabe==0.6.1",
        "packaging==16.8",
        "pkg-resources==0.0.0",
        "py==1.4.34",
        "pycodestyle==2.3.1",
        "pyflakes==1.5.0",
        "pyparsing==2.2.0",
        "PyQt5==5.9",
        "requests==2.18.4",
        "safety==1.6.1",
        "sip==4.19.3",
        "six==1.11.0",
        "SQLAlchemy==1.1.14",
        "termcolor==1.1.0",
        "urllib3==1.22",
    ],
    extras_require={
        'dev': ['flake8==3.4.1'],
        'test': ["pytest==3.2.2",
                 "pytest-cov==2.5.1",
                 "pytest-sugar==0.9.0",
                 "PyYAML==3.12",],
    },
    entry_points={
        'gui_scripts': [
            'finger_balabolka = fb_client:main',
        ]
    },
)