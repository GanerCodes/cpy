set -e && cd "${0%/*}"

echo -------- Building Python --------
unset PYTHONHOME PYTHONSTARTUP PYTHONPATH
cd ../cpython-fork
    make -s -j14 distclean || :
    echo -------- Cleaned --------
    # ./configure -q --with-ensurepip=install --with-pydebug
    ./configure -q --with-ensurepip=install
    echo -------- Configured --------
    make -s -j14 regen-token
    make -s -j14 regen-pegen
    make -s -j14 regen-global-objects
    make -s -j14 regen-all
    make -s -j14
    echo -------- Built executable --------
    ./python -m ensurepip --default-pip
    echo -------- Installed pip --------
cd -
echo -------- Running tests --------
../cpy_tool -r ./tests
echo -------- Finished! --------