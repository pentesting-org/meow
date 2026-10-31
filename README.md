A small Python authentication example built around JWTs. `auth.py` provides login, token refresh, token generation, and token decoding using HS256; login and refresh return a token with a one-hour lifetime. [[1]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L31)

**This is a scaffold, not a complete authentication service.** `authenticate()` is an unimplemented stub, while `login()` expects its result to have an `id` attribute. The signing key is the literal placeholder `"your-secret-key"`. Implement authentication and replace that key before using the login flow with real users. [[2]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L4-L13) [[3]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L31-L33)

## Setup and installation

1. Make `auth.py` available in your Python working directory or import path. It imports `datetime`, `timedelta`, and a module named `jwt`. [[4]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L2)
2. Install a JWT dependency in your Python environment that provides the `jwt.encode` and `jwt.decode` interfaces used here, including support for HS256 and the `algorithms` argument. The source does not specify a dependency version. [[4]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L2) [[5]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L24-L29)
3. Replace `SECRET_KEY` with your own signing key; the same value is used to encode and decode tokens. [[6]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L4-L4) [[5]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L24-L29)
4. Implement `authenticate(email, password)` so successful authentication returns an object with an `id` attribute, as required by `login()`. [[7]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L13) [[3]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L31-L33)

## Usage

### Generate, decode, and refresh a token

The token helpers can be called directly without the authentication stub. Tokens contain `user_id` and `exp`; `expires_in` is expressed in seconds. `refresh()` decodes the supplied token and issues a new token for the same user with a fresh one-hour expiry. [[8]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L15-L29)

```python
from auth import generate_jwt, decode_jwt, refresh

token = generate_jwt(user_id="example-user", expires_in=3600)
payload = decode_jwt(token)
print(payload["user_id"])

renewed = refresh(token)
print(renewed["expires_in"])  # 3600
```

This example follows the helper signatures and refresh return structure in `auth.py`. [[8]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L15-L29)

### Log in

After implementing `authenticate()`, call `login(email, password)`. It returns `{"token": token, "expires_in": 3600}`. Neither `login()` nor `refresh()` catches authentication or decoding errors, so callers should provide their own error handling. [[9]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L23)

## Contribution basics

For changes to this scaffold, use these review checks:

- Keep the authentication implementation compatible with `login()`'s expected user object, or update the caller alongside it. [[7]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L13) [[3]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L31-L33)
- When changing token behavior, check encoding and decoding together: both use `SECRET_KEY` and HS256. [[5]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L24-L29)
- Include verification of the affected token payload, expiry, and login/refresh return values with proposed changes. These are the current interface points to preserve or explicitly document when changing them. [[10]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L31)
