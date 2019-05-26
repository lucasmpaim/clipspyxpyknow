
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['clipspy', 'pyknow'], required=True)
parser.add_argument('--track', choices=['y', 'n'], required=True)
parser.add_argument('--with-fix', choices=['y', 'n'], required=False, default='n')

args = parser.parse_args()


if args.type == 'clipspy':
    if args.track == 'y':
        from se.clipspy_version.se_with_time_track import run
        run()
    else:
        from se.clipspy_version.se import run
        run(args.with_fix)
else:
    if args.track == 'y':
        from se.pyknow_version.se_with_track import run
        run()
    else:
        from se.pyknow_version.se import run
        run()
