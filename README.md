# dbt-101

Bootstrap dbt project (with Apache Spark)

# Local Setup

1. Create Project directory and clone the repo

```commandline
    md C:\Projects
    cd  C:\Projects
    git clone https://github.com/skadyan/dbt-201.git
    cd dbt-201
```

1. Create Virtual Environment and setup dependencies

```commandline
    C:\tools\python38\python -m venv .venv
    .venv\Scripts\activate
    python -m pip install pip --upgrade
    python -m pip install -r reqirements-dev.txt
```

1. Create dbt profile as following

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
