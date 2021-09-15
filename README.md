pre-commit-maven
================

[![Build Status](https://travis-ci.com/ejba/pre-commit-maven.svg?branch=main)](https://travis-ci.com/ejba/pre-commit-maven) [![Code Coverage](https://img.shields.io/codecov/c/github/ejba/pre-commit-maven/main.svg)](https://codecov.io/github/ejba/pre-commit-maven?branch=main)

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-maven with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
-   repo: https://github.com/ejba/pre-commit-maven
    rev: v0.2.1
    hooks:
    -   id: maven
        args: ['clean compile']
    -   id: maven-spotless-apply
    # -   id: ...
```

### Hooks available

#### `maven`
Runs arbitrary maven commands. `args: ['clean compile verify']`.

#### `maven-compile`
Runs compile build lifecycle.

#### `maven-test`
Runs test build lifecycle.

#### `maven-checkstyle`
Runs checkstyle:check.

#### `maven-spotless-check`
Runs spotless:check.

#### `maven-spotless-apply`
Runs spotless:apply.
