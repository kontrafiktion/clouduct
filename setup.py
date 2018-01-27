from setuptools import setup, find_packages

setup(name='clouduct',
      version='0.1',
      description='Create AWS setups for common use cases',
      url='https://github.com/kontrafiktion/clouduct',
      author='Victor Volle',
      author_email='victor.volle@beta-thoughts.org',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      # test_suite='pytest.collector',
      scripts=['bin/clouduct'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      python_requires='>=3.4.1',
      install_requires=[
        'boto3==1.5.18',
        'cookiecutter==1.6.0',
        'npyscreen==4.10.5',
        'click==6.7',
        'click-completion==0.2.1'
      ],
      classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        'Topic :: Software Development :: Code Generators',
        'Topic :: System :: Systems Administration',

        'License :: OSI Approved :: MIT License',

        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ])