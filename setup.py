import setuptools

PACKAGE_VERSION = "0.4"

setuptools.setup(
    name='mytoolbox',
    version='0.4',
    author='Pavlis',
    author_email='pavlis.konecny@gmail.com',
    description='Testing installation of Package',
    long_description="My tool box",
    long_description_content_type="text",
    url='https://github.com/pavliskonecny/mytoolbox',
    project_urls={
        "Bug Tracker": "https://github.com/pavliskonecny/mytoolbox/issues"
    },
    license='MIT',
    packages=['mytoolbox'],
    # install_requires=['requests'],
)
