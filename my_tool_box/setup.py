import setuptools

setuptools.setup(
    name='my_tool_box',
    version='0.0.1',
    author='Pavlis',
    author_email='pavlis.konecny@gmail.com',
    description='Testing installation of Package',
    long_description="My tool box",
    long_description_content_type="text",
    url='https://github.com/pavliskonecny/my_tool_box',
    project_urls={
        "Bug Tracker": "https://github.com/pavliskonecny/my_tool_box/issues"
    },
    license='MIT',
    packages=['my_tool_box'],
    # install_requires=['requests'],
)
