# dbt-101

Bootstrap dbt project (with Apache Spark)

# Local Setup

1. Create Project directory and clone the repo

```commandline
    md C:\Projects
    cd  C:\Projects
    git clone https://github.com/skadyan/dbt_201.git
    cd dbt_201
```

1. Create Virtual Environment and setup dependencies. Make sure you have run `pre-commit install`

```commandline
    C:\tools\python38\python -m venv .venv
    .venv\Scripts\activate
    python -m pip install pip --upgrade
    python -m pip install -r reqirements-dev.txt
    pre-commit install
```

1. Create dbt profile as following C:\Users\%USERNAME%\.dbt\profiles.yml

```yaml
dbt_201:
  outputs:
    dev:
      host: localhost
      method: thrift
      port: 10000
      schema: dbt_201_elt
      threads: 4
      type: spark
  target: dev
```

1. Test Profile and dbt connectivity

```commandline
    dbt debug
```

It should produce something similar as below.

```text
(.venv) C:\Projects\dbt_201>dbt debug
19:03:20  Running with dbt=1.3.1
dbt version: 1.3.1
python version: 3.8.10
python path: C:\Projects\dbt_201\.venv\Scripts\python.exe
os info: Windows-10-10.0.22621-SP0
Using profiles.yml file at C:\Users\sankadya\.dbt\profiles.yml
Using dbt_project.yml file at C:\Projects\dbt_201\dbt_project.yml

Configuration:
  profiles.yml file [OK found and valid]
  dbt_project.yml file [OK found and valid]

Required dependencies:
 - git [OK found]

Connection:
  host: localhost
  port: 10000
  cluster: None
  endpoint: None
  schema: dbt_201_elt
  organization: 0
  Connection test: [OK connection ok]

All checks passed!

(.venv) C:\Projects\dbt_201>
```

1. Code Quality Checks

```commandline
    sqlfluff lint
```

You may run ```sqlfluff fix``` command to apply auto-fix. Modified files must be reviewed manually before
committing them.

Alternatively, you may run below command as well to produce a summary instead of too verbose output

```commandline
    diff-quality --violations sqlfluff
```

It produces something similar

```text
-------------
Diff Quality
Quality Report: sqlfluff
Diff: origin/main...HEAD, staged and unstaged changes
-------------
models/example/my_first_dbt_model.sql (100%)
models/example/my_second_dbt_model.sql (100%)
-------------
Total:   16 lines
Violations: 0 lines
% Quality: 100%
-------------
```
