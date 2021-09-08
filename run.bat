@ECHO OFF
set BUILD_ID=%date:~-4%_%date:~3,2%_%date:~0,2%__%time:~0,2%_%time:~3,2%_%time:~6,2%
set BUILD_ID=%BUILD_ID: =0%
set BASE_PATH=F:\Python_files\FWNew\tests
set ENV=PRD
set URL=https://www.amazon.com/
set USER=Guest
set PWD=12345
set REPORT_HOME=%BASE_PATH%\%ENV%\%BUILD_ID%
set BROWSER=local

mkdir %REPORT_HOME%

cd F:\Python_files\FWNew\tests\functional_tests

pytest -v --ignore-glob="test_add_items_e2e_2.py" --html=%REPORT_HOME%\results.html --self-contained-html --url=%URL% --un=%USER% --pwd=%PWD% --browser=%BROWSER% --report_home=%REPORT_HOME%
:-k "e2e"
pause
