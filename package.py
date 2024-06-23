from setuptools import setup, find_packages

setup(
    name='HospitalManagementSystem',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['run'],
    install_requires=[
        'Flask~=3.0.3',
        'psycopg2',
    ],
    package_data={
        '': ['templates/*.html',  'database.sql', 'app/*.py'],  # 包含所有需要的文件
    },
    entry_points={
        'console_scripts': [
            'run_app=run:main',
        ],
    },
)
