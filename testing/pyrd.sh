set -e
rm ./pyrd_test.py || :
pyrdg ./pyrd_test.grammar ./pyrd_test.cpy
cpy ./pyrd_test
