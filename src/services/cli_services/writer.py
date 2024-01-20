import sys

def update_progress_bar(progress):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*int(progress/10), progress))
    sys.stdout.flush()