PB Shipping API Alexa Integration Code
-----------------------------------------------------------------------------


## Local Environment Set Up
1. Clone project.  Make sure this is RECURSIVE.  Either clone recursively 
`git clone git@github.com:my_user/my_repo.git --recursive`
or update submodules recursively after a regular clone 
`git submodule update --init --recursive`
2. Python version 2.7

NOTE: In case Python Path is needed, also add this project directory to your Python Path.
`export PYTHONPATH=$PYTHONPATH:{YOUR_PROJECT_DIRECTORY}`

## Using the Python Console
It is possible to test out python functions via the Python console:
`python`

    Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
    [GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> test="abcdefg"
    >>> test[:3]
    'abc'
    >>>

## Running in AWS Lambda
1. Compress the contents of the root folder 
2. Upload the zip folder in AWS lambda project
3. Make sure your ARN of Lambda project is linked to Alexa Skill
