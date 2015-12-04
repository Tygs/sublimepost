import setuptools

setuptools.setup(name='sublimepost',
                 version='0.1.0',
                 description='New generation content management system',
                 long_description=open('README.rst').read().strip(),
                 author='Sam, Max & friends',
                 author_email='lesametlemax@gmail.com',
                 url='https://github.com/sametmax/sublimepost/',
                 packages=['sublimepost'],
                 package_dir={'': 'src'},
                 install_requires=['aiohttp', ],
                 extras_require={
                     'dev': ['sphinx', 'tox', 'pytest']
                 },
                 license='WTFPL',
                 zip_safe=False,
                 keywords='sublimepost blogging microblogging async',
                 classifiers=['Development Status :: 1 - Planning',
                              'Intended Audience :: Developers',
                              'Natural Language :: English',
                              'Programming Language :: Python :: 3.5',
                              'Programming Language :: Python :: 3 :: Only',
                              'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
                              'Topic :: Internet :: WWW/HTTP :: Site '
                              'Management',
                              'Operating System :: OS Independent'],)
