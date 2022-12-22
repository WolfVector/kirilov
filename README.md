# Kirilov

Kirilov was born due to the necesitiy of **installing** packgaes in a remote machine that has no access to internet. The common thing to do is to setup a local environment with the same python version that exists in the remote machine, then you do `pip freeze > requirements.txt` and proceed to migrate all the code and to start installing the packages using the `requirements.txt` file.

**However**, in some cases the remote machine has no access to internet, so you first have to download the packages and install them in the remote server. **Kirilov** is a script that helps you to automate this. It will compare requirements and gives the option to download the recently added. With a simple command you can manage your requirements without much problem.

## Install

- Download the code
- Inside the directory run: `pip install .`
- The script has no dependecies

## Usage

Kirilov receive two inputs: the two inputs in which we are going to do the comparison, it could be a file or data coming from `pip freeze`. Commonly these are the inputs you are going to use: `requirements.txt` and `pip freeze`.

### Print new requirements and output them to a file

```python
$ kirilov -f1=- -f2=requirements.txt
```

The `-` means `pip freeze`. The script is going to do a comparison between `pip freeze` and `requirements.txt`, then is going to print the requirmentes that do not exists in the `requirements.txt` file. The script is also going to create a file called `kirilov_added.txt` that will contain the new requirements.

**Note**: the order of inputs matters.

### Download the new requirements

```python
$ kirilov -f1=- -f2=requirements.txt --download=True --path=/path/for/your/downloads
``` 
You can especify the path in which you desire to save the downloads. The default is `./downloads`.

### All options

- `--output` or `-op`: Output a file with the new requirements?. Default True
- `--download` or `-d`: Download the new requirements? Default false
- `--path` or `-p`: The path of the download directory. Default ./downloads
- `--file1` or `-f1`: Path to the first requirements file or '-'. The meaning of '-' is pip freeze
- `--file2` or `-f2`: Path to the second requirements file or '-'. The meaning of '-' is pip freeze


