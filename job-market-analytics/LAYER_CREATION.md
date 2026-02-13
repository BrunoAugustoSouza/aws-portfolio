# 🐳 Creating an AWS Lambda Layer (Windows + Docker)

This guide explains how to create an AWS Lambda Layer ZIP file
containing:

-   requests
-   pandas
-   fastparquet

Using: 

- Windows
- PowerShell 
- Docker (no need to install Python locally)

------------------------------------------------------------------------

## ✅ 1. Install Docker Desktop

If you don't have Docker:

1.  Download Docker Desktop:
    https://www.docker.com/products/docker-desktop
2.  Install and restart your machine if required.
3.  Confirm installation:

``` powershell
docker --version
```

------------------------------------------------------------------------

## ✅ 2. Create a Project Folder

Create a folder for your layer:

``` powershell
mkdir lambda-layer
cd lambda-layer
```

------------------------------------------------------------------------

## ✅ 3. Create the Correct Layer Structure

Lambda layers require this structure:

    python/

Create it:

``` powershell
mkdir python
```

------------------------------------------------------------------------

## ✅ 4. Install Linux-Compatible Dependencies Using Docker

AWS Lambda runs on Amazon Linux, so we must build dependencies inside a
compatible container.

Run this command in PowerShell:

``` powershell
docker run --rm `
  -v ${PWD}:/var/task `
  public.ecr.aws/lambda/python:3.9 `
  pip install requests pandas fastparquet -t python/
```

### 🔎 What this does:

-   --rm → removes container after execution
-   -v \${PWD}:/var/task → mounts your current directory into container
-   public.ecr.aws/lambda/python:3.9 → official Lambda runtime image
-   -t python/ → installs packages inside the required folder

------------------------------------------------------------------------

## ✅ 5. Verify Folder Structure

After installation, your folder should look like:

    lambda-layer/
    │
    └── python/
        ├── pandas/
        ├── fastparquet/
        ├── requests/
        └── ...

------------------------------------------------------------------------

## ✅ 6. Create the ZIP File

Now create the layer zip:

``` powershell
Compress-Archive -Path python -DestinationPath layer.zip
```

If you prefer 7zip:

``` powershell
7z a layer.zip python
```

------------------------------------------------------------------------

## ✅ 7. Save Layer on lambda folder

Save your layer.zip file inside lambda folder

    lambda/
    │
    ├── handler.py
    └── layer.zip

------------------------------------------------------------------------