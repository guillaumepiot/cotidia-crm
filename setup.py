import os

from setuptools import find_packages, setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        # Only keep the last directory of the path
        path = path.replace(directory, directory.split("/")[-1])
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths


template_files = package_files('cotidia/crm/templates')

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
        'cotidia.crm': template_files
    },
    namespace_packages=['cotidia'],
    include_package_data=True,
    install_requires=[
        'names',
        'django-countries==5.0.*',
    ],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
)
