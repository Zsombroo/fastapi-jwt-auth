# Fastapi - JWT authentication template code

This is a template project of a simple REST API which handles the authentication of users using JWT access and refresh tokens. My only intention with publishing this code is to provide an example of how such a service could be implemented in a "good enough" way. I didn't manage to find any guides online which provided a well structured example code where the full project strutcure was visible. (Most likely I didn't look hard enough and/or I just wanted to write my own solution)

If you found this code and would like to use it, keep in mind that this codebase is not perfect.

## How to run

Set up a new env
```
$ python -m venv venv
$ source venv/bin/acivate
$ pip install -r requirements.txt
```

Run the code
```
$ fastapy dev --root-path . src/main.py
```

## How to test

Run tests one time
```
$ pytest
```

Run tests automatically when you edit the code
```
$ pytest-watch
```

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

## FAQ

### Why do you return the access token in the response content and why do you set the refresh token as a cookie?

I tried to find the answer online to the question of **_Where do I store JWT tokens on client side?_**, but I mostly got confused by all the contradicting answers from the bootcamp security experts. The only thing I am fairly certain at is that the refresh token should be stored in a http-only cookie. Maybe the access token should live there too, idk I am not a frontend expert. I decided to store the access token in memory on the client instead, maybe because I found more answers saying that. If you know the most secure way of storing JWT tokens and you have the time to write it down in an issue, then please open one and provide something that supports your claim, so I can understand the threats and considerations.

### Why JWT? Why not sessions?

JWT doesn't require storing anything extra on the backend and so it is less of a headache for me.

If you wan't someone to convince you, here are two videos:

[Session vs JWT](https://www.youtube.com/watch?v=fyTxwIa-1U0)

[Why is JWT popular?](https://www.youtube.com/watch?v=P2CPd9ynFLg)

### So what is actually a JWT?

Probably the best resource to answer this question would be [RFC 7519 - JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519#section-11)
