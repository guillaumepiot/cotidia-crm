from setuptools import find_packages, setup


setup(
    name="cotidia-crm",
    description="CRM for Cotidia base project.",
    version="1.0",
    author="Guillaume Piot",
    author_email="guillaume@cotidia.com",
    url="https://code.cotidia.com/cotidia/crm/",
    packages=find_packages(),
    package_dir={'crm': 'crm'},
    package_data={
        'cotidia.cms': [
            'templates/admin/crm/*.html',
            'templates/admin/crm/*/*.html',
            'templates/notification/*.html',
            'templates/notification/*.txt'
        ]
    },
    namespace_packages=['cotidia'],
    include_package_data=True,
    install_requires=[
        'names',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)
