# dbt_201

Bootstrap a new dbt project (with Apache Spark) with enterprise grade development configuration.

# Local Setup

1. Create Project directory and clone the repo
   *Pre-requisites*
   > * You must have python >= 3.8, say under C:\tools\python38
   > * You must have installed and configured Apache Spark 3.3.x. See gist for instruction
       >
    * [file-windows-setup-spark-3-1-1-txt](https://gist.github.com/skadyan/fe22a4bf35b1c14821504981887e03f7#file-windows-setup-spark-3-1-1-txt)

    ```commandline
        md C:\Projects
        cd C:\Projects
        git clone https://github.com/skadyan/dbt_201.git
        cd dbt_201
    ```

2. Create Virtual Environment and setup dependencies. Make sure you have run `pre-commit install`

   ```commandline
       C:\tools\python38\python -m venv .venv
       .venv\Scripts\activate
       python -m pip install pip --upgrade
       python -m pip install -r requirements-dev.txt
       pre-commit install
   ```

3. Create dbt profile as following C:\Users\\%USERNAME%\\.dbt\profiles.yml

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

4. Install dbt packages

   ```commandline
       dbt deps
   ```

5. Test Profile and dbt connectivity

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
   Using profiles.yml file at C:\Users\skadyan\.dbt\profiles.yml
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

6. Code Quality Checks

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

7. Commit will run the hooks automatically. Output will look like.

   ```text
   (.venv) C:\Projects\dbt_201>git commit -am "minor fix"
   sqlfluff-lint........................................(no files to check)Skipped
   trim trailing whitespace.................................................Passed
   fix end of files.........................................................Passed
   check yaml...............................................................Passed
   fix requirements.txt.................................(no files to check)Skipped
   flake8...............................................(no files to check)Skipped
   [main 1c248e7] minor fix
    1 file changed, 4 insertions(+)
   ```
