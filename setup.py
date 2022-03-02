from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except:
    pass

try:
    with open('LICENSE.txt') as f:
        license = f.read()
except:
    pass

setup(
    name='HouseMonitorLGB',
    version='1.0.0',
    description='Collection and use of environmental sensors around house',
    long_description=README,
    long_description_content_type = 'text/markdown',
    author='Logan Balkwill',
    author_email='lgb0020@gmail.com',
    url='https://github.com/loganbalkwill/house-monitor',
    license="MIT",
    packages=find_packages(exclude=('tests')),
    include_package_data = True,
    install_requires = ["PlantNannyDB"]
)