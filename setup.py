from distutils.core import setup

setup(
    name="GitToXApi",
    packages=["GitToXApi"],
    version="0.1",
    license="MIT",
    description="Enable creation and edition of xapi file from git source",
    author="Git4School",
    author_email="",
    url="https://github.com/git4school/gitToXApi",
    download_url="https://github.com/git4school/gitToXApi/archive/refs/tags/v_0.1.tar.gz",
    keywords=[
        "XApi",
    ],
    install_requires=[
        "tincan",
        "GitPython",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",  # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
