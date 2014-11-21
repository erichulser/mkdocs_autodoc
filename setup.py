from setuptools import setup, find_packages

setup(
    name = 'mkdocs_autodoc',
    version = '1.0.0',
    author = 'Projex Software',
    author_email = 'team@projexsoftware.com',
    maintainer = 'Projex Software',
    maintainer_email = 'team@projexsoftware.com',
    description = 'Auto-documentation for python modules for the mkdocs documentation system.',
    license = 'LGPL',
    keywords = '',
    url = 'http://www.projexsoftware.com',
    include_package_data=True,
    packages = find_packages(),
    install_requires = ['mkdocs'],
    classifiers=[],
)
