# Poetry lock check

Check the integrity of a poetry.lock and pyproject.toml

Designed to be easily used in CI pipelines.

```
pip install \
    poetry==1.1.2 \ # verson lock of poetry is reccomended but not required
    poetry-lock-check==0.1.0

python -m poetry_lock_check check-lock
```

# Why?

There's an open MR which I want to use, but I do not want to install an
unsupported fork of poetry.

https://github.com/python-poetry/poetry/pull/1954

This small script simply adds a command onto poetry. As long as the features
remain backwards-compatible so will this script. For this reason, your CI
pipeline should also lock down the poetry version to prevent unexpected
failures.

There is an interesting plugin feature-set for poetry but it appears to still
be under conceptual experimentation, so I opted to offer a "plugin" in this
future-compatible way instead.

Once the feature is merged into poetry, this project will be archived.
