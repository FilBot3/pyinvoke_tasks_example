# pyinvoke_tasks_example

## Overview

How I use PyInvoke, normally

## Requirements

* Python 3.8 or newer
* Poetry [https://python-poetry.org]

## Setup

Use Poetry to install the packages to a virtualenv managed by Poetry.

```bash
poetry add invoke
```

## Usage

How to see available tasks

```bash
poetry run invoke --list
Available tasks:

ex01.hello-world   Hello, World! task
```

Then to run this, execute:

```bash
poetry run invoke ex01.hello-world
```

## Development and Testing

TODO

## Referecnes

* [PyInvoke Documentation](http://www.pyinvoke.org/)
