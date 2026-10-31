## Project overview

This is a small Python JWT-authentication module: `auth.py` implements login, token refresh, token generation, and token decoding. `vie.md` contains only a short prose sentence, not operational instructions. [[1]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L33) [[2]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/vie.md#L1-L1)

## Architecture

- `login(email, password)` calls `authenticate`, reads `user.id`, and returns `{"token": ..., "expires_in": 3600}`. `authenticate` is only a stub; implement it before treating login as functional. [[3]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L13) [[4]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L31-L33)
- `refresh(current_token)` decodes the supplied token and issues another token for the same `user_id`, with a new one-hour expiry. It uses the same token-generation path as login, not a separate refresh-token mechanism. [[5]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L15-L26)
- `generate_jwt` encodes `user_id` and `exp` using HS256. `decode_jwt` uses the same module-level key and explicitly permits HS256. The module imports `jwt` and standard-library datetime utilities. [[6]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L4) [[7]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L24-L29)

## Commands and validation

Suggested syntax-only check for this Python module; this does **not** exercise authentication or validate security: [[1]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L33)

```sh
python -m py_compile auth.py
```

The source does not specify dependency installation or a test runner; do not present an invented install/test command as established project practice. The security-validation baseline is **not established by this guide**: no runtime tests were executed. The authentication stub also prevents a meaningful successful-login baseline without an implementation or test double. [[1]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L1-L33)

For security-validation work, add tests around the existing behavior: token claims and expiry, response shape, refresh identity preservation, and rejection of expired, malformed, wrong-key, and non-HS256 tokens. Treat these as recommended coverage, not existing tests or verified outcomes. [[8]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L29)

## Conventions

Follow the module's existing snake_case functions, parameter/return annotations where present, and short function docstrings. Preserve the `token`/`expires_in` response contract and `user_id`/`exp` claim names unless deliberately changing the API. [[8]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L29)

## Gotchas

- `SECRET_KEY` is the hard-coded placeholder `"your-secret-key"`. Replace this configuration before production use; do not treat it as a provisioned secret. [[9]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L4-L4)
- Login assumes authentication returns an object with `.id`; the stub supplies no such object or credential checks. Define failure behavior when implementing authentication. [[3]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L6-L13) [[4]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L31-L33)
- Login and refresh both hard-code `3600` in generation and response metadata. Keep those values consistent if changing token lifetime. [[10]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L9-L22)
- Decode and refresh contain no local exception handling, revocation check, or separate refresh credential. Do not assume those protections exist when extending this module. [[11]](https://github.com/pentesting-org/meow/blob/d3b0cfb11eaa54d0a116f2a3db16cf052055dc2e/auth.py#L15-L29)
