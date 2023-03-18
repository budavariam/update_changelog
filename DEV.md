# DEV notes

## How to build

```bash
# install
python setup.py install
pip install .

# uninstall
pip uninstall update_changelog -y

# reinstall
pip uninstall update_changelog -y && python setup.py install && pip install .
```

## Validate

```bash
twine check dist/*
```


## Publish package

```bash
pip install wheel
pip install twine
python setup.py sdist bdist_wheel
twine upload dist/* 
```
