# Developer Instructions

## Onetime Activity:
1. Required Software needs to be installed into local development environment (Windows OS) -
	1. python3 (source url: https://www.python.org/downloads/)
	2. git bash (source url: https://git-scm.com/downloads)
	3. vscode (IDE) (source url: https://code.visualstudio.com/)
	
2. Clone the `smart_algo_trading` from github repo -
	```shell
	git clone https://github.com/easycloudapi/smart_algo_trading.git
    ```

3. Open and goto working directory path by below command in **powershell terminal** -
	```shell
	cd .\smart_algo_trading\
	```
	
4. Create and activate the Python Virtual Environment -
	```shell
	python -m virtualenv .venv
	.\.venv\Scripts\activate

	# if error occured due to about_Execution_Policies for activate.ps1 powershell script,

	# first check, if the execution policy is restricted or not
	Get-ExecutionPolicy

	# if execution policy is restricted, then Unrestrict the policy
	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force

	# then Restrict the policy again
	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted -Force
	```

5. Install the Required Python Packages -
	```shell
	python.exe -m pip install --upgrade pip
	pip install -r requirements.txt
	```

6. Follow the below package development steps -
	1. Write module code inside ".\src\sat\\<package\>"


7. Configure to build the package locally (from ".\algo_trading\" dir) -
	```shell
	py -m pip install --upgrade build
	py -m build
	```

8. Locally install the package for testing (run from root dir where setup.py or setup.cfg available):
	```shell
	pip install -e .
	pip uninstall algo-trading
	```

8. Install twine which will copy the code to `testpypi` and `pypi`:
    ```shell
    py -m pip install --upgrade twine  # will upload distribution archive into testpypi or pypi

    # testPyPi - https://test.pypi.org/project/easycloudapi/0.0.1/
    # create testpypi account (https://test.pypi.org/), activate testPyPi account, 
    # create api token, store it under ".pypirc" as documented or generated.
    cd $Home
    touch .pypirc  # store the token

    # upload the package from local dist to testPyPi
    py -m twine upload --repository testpypi dist/*
    # or 
    py -m twine upload --skip-existing --repository testpypi dist/*

    # PyPi - https://pypi.org/project/easycloudapi/0.0.1/
    # create pypi account (https://pypi.org/), activate PyPi account, 
    # create api token, store it under ".pypirc" as documented or generated.

    # upload the package from local dist to PyPi
    twine upload dist/*  # --repository pypi 
    ```

## Daily activity:
	```shell
	# activate .venv
	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
	.\.venv\Scripts\activate
	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted -Force

	# build the package
	py -m pip install --upgrade build
	py -m build

	# move the built package to testpypi
	py -m twine upload --skip-existing --repository testpypi dist/*

	# move the built package to pypi
	twine upload --skip-existing dist/*
	```

## Execute the code for Stock Market Data and Analysis:
	```shell
	# sample code
	```

## Solved the errors-

### 1. Git Error due to changing the repo name, required permission again (*solved*):
	```shell
	git remote -v
	git remote set-url origin https://easycloudapi@github.com/easycloudapi/smart_algo_trading.git
	```