from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
# with codecs_open('README.rst', encoding='utf-8') as f:
#     long_description = f.read()


setup(name='sportscraper',
      version='0.2',
      description=u"A Tool to pull raw data from sport performance sources and place into database.",
      # long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Michael Lucas",
      author_email='michael@desktopninjas.com',
      url='https://github.com/nubbthedestroyer/sportscraper',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'pybaseball',
          'gitpython',
          'sqlalchemy',
          'pandas'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      sportscraper=sportscraper.scripts.cli:cli
      """
      )
