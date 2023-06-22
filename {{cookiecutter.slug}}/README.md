# {{cookiecutter.project}}

[![PyPI - Version](https://img.shields.io/pypi/v/demo-project.svg)](https://pypi.org/project/demo-project)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/demo-project.svg)](https://pypi.org/project/demo-project)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install {{cookiecutter.slug}}
```

## License

{%if cookiecutter.license == 'MIT'%}
`{{cookiecutter.slug}}` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
{%-elif cookiecutter.license == 'BSD'%}
`{{cookiecutter.slug}}` is distributed under the terms of the [BSD](https://spdx.org/licenses/BSD-3-Clause.html) license.
{%-elif cookiecutter.license == 'GPLv3'%}
`{{cookiecutter.slug}}` is distributed under the terms of the [GPLv3](https://spdx.org/licenses/GPL-3.0-or-later.html) license.
{%-elif cookiecutter.license == 'Apache Software License 2.0'%}
`{{cookiecutter.slug}}` is distributed under the terms of the [Apache Software License 2.0](https://spdx.org/licenses/Apache-2.0.html) license.
{%-endif%}
