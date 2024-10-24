from setuptools import setup, find_packages

setup(
    name='atoiniumhub',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
        'djangorestframework',
        'django-cors-headers',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'manage.py = manage:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)