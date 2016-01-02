
import setuptools
import re


def get_requirements():

    setuppy_pattern = \
        'https://github.com/{user}/{repo}/tarball/master#egg={egg}'

    dependency_links = []
    install_requires = []
    with open('requirements.txt') as f:
        for line in f:

            if line.startswith('-e'):
                url_infos = re.search(
                    r'github.com/(?P<user>[^/.]+)/(?P<repo>[^.]+).git#egg=(?P<egg>.+)',
                    line).groupdict()
                dependency_links.append(setuppy_pattern.format(**url_infos))
                install_requires.append(url_infos['egg'])
            else:
                install_requires.append(line.strip())

    print(install_requires, dependency_links)
    return install_requires, dependency_links

install_requires, dependency_links = get_requirements()

setuptools.setup(name='sublimepost',
                 version='0.1.0',
                 description='New generation content management system',
                 long_description=open('README.rst').read().strip(),
                 author='Sam, Max & friends',
                 author_email='lesametlemax@gmail.com',
                 url='https://github.com/sametmax/sublimepost/',
                 packages=setuptools.find_packages('src'),
                 package_dir={'': 'src'},
                 install_requires=install_requires,
                 dependency_links=dependency_links,
                 extras_require={
                     'dev': ['sphinx', 'tox', 'pytest', 'requests',
                             'pytest-cov']
                 },
                 include_package_data=True,
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
