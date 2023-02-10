import ai
import subprocess
import sys
from console import console
from rich.prompt import Prompt
from shell import shell


def run(cmd):
    subprocess.run(cmd, shell=True, executable=shell)


if __name__ == '__main__':
    request = " ".join(sys.argv[1:])
    command = ''
    console.line()
    for comp in ai.nl2cl(request):
        command += comp
        console.print(comp, end='', style='bold')
    console.line(2)
    response = Prompt.ask('Run, explain or abort?', choices=['r', 'e', 'a'], default='r')
    if response == 'r':
        console.line()
        run(command)
    elif response == 'e':
        console.line()
        for comp in ai.explain_command(command):
            console.print(comp, end='', style='italic')
        console.line(2)
        response = Prompt.ask('Run or abort?', choices=['r', 'a'], default='r')
        if response == 'r':
            console.line()
            run(command)
