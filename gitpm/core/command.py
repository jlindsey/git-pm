import argh
from gitpm.core.initialize import initialize
from argh.decorators import arg, expects_obj

def run():
    argh.dispatch_commands([init])

@expects_obj
@arg('path')
@arg('--branch', '-b', default='git-pm', help='Branch to store git-pm in')
def init(args):
    "Initializes your project"
    return initialize(args.path, args.branch)

