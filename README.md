# Natural Language Interface (NLI)

NLI is a tool that converts natural language into shell commands. With NLI, you can express your desired actions in plain language, and the tool will generate the corresponding shell commands for you. This approach can make it quicker and easier to execute tasks in the terminal, especially when compared to manual command typing. NLI is powered by GPT-3, a state-of-the-art language model developed by OpenAI.

## Installation

If you're using a Mac with an arm64 processor you can download the executable directly from [releases](https://github.com/ngsilverman/nli/releases).

Otherwise, to install from the source:
```bash
> pyinstaller nli.py
> ln -s dist/nli/nli /usr/local/bin/nli
```

## Usage

```bash
> nli [make a wish]
```

## Example

```
> nli recursively change the user to apple in the current folder but only for files owned by the user banana

find . -user banana -exec chown apple {} \;

Run, explain or abort? [r/e/a] (a): e

• find: searches for files in the current directory and its subdirectories
• .: the current directory
• -user banana: searches for files owned by the user "banana"
• -exec: executes a command on the files found
• chown: changes the owner of the file
• apple: the new owner of the file
• {}: placeholder for the file found
• \;: terminates the command

Run or abort? [r/a] (a): 
```