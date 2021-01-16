pre-commit-maven (WIP)
================

[![Build Status](https://travis-ci.com/ejba/pre-commit-maven.svg?branch=main)](https://travis-ci.com/ejba/pre-commit-maven) [![Code Coverage](https://img.shields.io/codecov/c/github/ejba/pre-commit-maven/main.svg)](https://codecov.io/github/ejba/pre-commit-maven?branch=main)

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-maven with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/ejba/pre-commit-maven
    rev: 0.1.0
    hooks:
    -   id: maven-goals
        args: ['clean compile']
    # -   id: ...
```

### Hooks available

#### `maven-goals`
Runs arbitrary maven goals. `args: ['clean compile verify']`.

#### `maven-spotless-check`
Runs spotless:check.

#### `maven-spotless-apply`
Runs spotless:apply.
