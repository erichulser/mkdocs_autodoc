from setuptools import setup, find_packages

setup(
    name = 'mkdocs_autodoc',
    version = '1.0.1',
    author = 'Eric Hulser',
    author_email = 'eric.hulser@projexsoftware.com',
    maintainer = 'Eric Hulser',
    maintainer_email = 'eric.hulser@projexsoftware.com',
    description = 'Auto-documentation for python modules for the mkdocs documentation system.',
    license = 'LGPL',
    keywords = '',
    url = 'https://github.com/erichulser/mkdocs_autodoc',
    include_package_data=True,
    packages = find_packages(),
    install_requires = ['mkdocs'],
    classifiers=[],
)
