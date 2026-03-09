# Installing and Using `uv` (Python Fast Package Manager)

`uv` is a fast Python package manager and virtual environment tool
written in Rust.\
It can replace tools like `pip`, `pip-tools`, and `virtualenv` while
being significantly faster.

Official project: https://github.com/astral-sh/uv

------------------------------------------------------------------------

# 1. Install `uv`

## Linux / macOS

Run the official install script:

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal after installation.

Verify installation:

``` bash
uv --version
```

------------------------------------------------------------------------

## Windows (PowerShell)

Run:

``` powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Then verify:

``` powershell
uv --version
```

------------------------------------------------------------------------

# 2. Create a Python Virtual Environment

Inside your project folder run:

``` bash
uv venv
```

This creates a `.venv` virtual environment.

Activate it:

### Linux / macOS

``` bash
source .venv/bin/activate
```

### Windows

``` powershell
.venv\Scripts\activate
```

------------------------------------------------------------------------

# 3. Install Project Dependencies

If the project contains a `requirements.txt` file:

``` bash
uv pip install -r requirements.txt
```

Or install packages manually:

``` bash
uv pip install pandas boto3 pyarrow
```

------------------------------------------------------------------------

# 4. Running the Project

For this project run:

``` bash
uv run main.py
```

`uv run` automatically executes the script using the project's virtual
environment.

------------------------------------------------------------------------

# Example Project Workflow

``` bash
git clone <repository>
cd ai-orchestrated-big-data-analytics-aws

uv venv
source .venv/bin/activate

uv pip install -r requirements.txt

uv run main.py
```

------------------------------------------------------------------------

# Why Use `uv`

Benefits:

-   Extremely fast dependency resolution
-   Built-in virtual environment management
-   Compatible with pip workflows
-   Written in Rust (high performance)
-   Increasingly adopted in modern Python projects

------------------------------------------------------------------------

# Documentation

Official docs:

https://github.com/astral-sh/uv
