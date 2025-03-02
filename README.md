# Fastapi - JWT authentication template code

This is a template project of a simple REST API which handles the authentication of users using JWT access and refresh tokens. My only intention with publishing this code is to provide an example of how such a service could be implemented in a "good enough" way. I didn't manage to find any guides online which provided a well structured example code where the full project strutcure was visible. (Most likely I didn't look hard enough and/or I just wanted to write my own solution)

If you found this code and would like to use it, keep in mind that this codebase is not perfect.

## Test coverage report

```
$ pytest --cov

---------- coverage: platform linux, python 3.13.2-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
src/auth/__init__.py          0      0   100%
src/auth/api.py              22      0   100%
src/auth/controller.py       26      1    96%
src/main.py                   6      0   100%
src/users/__init__.py         0      0   100%
src/users/api.py             11      2    82%
src/users/model.py            5      0   100%
src/users/repository.py       5      0   100%
src/utils/__init__.py         0      0   100%
src/utils/logging.py          3      0   100%
src/utils/security.py        55      8    85%
src/utils/settings.py        16      0   100%
tests/__init__.py             0      0   100%
tests/test_auth.py           36      5    86%
---------------------------------------------
TOTAL                       185     16    91%
```
