from tempfile import mkstemp
from shutil import move
from os import remove, close

import os, argparse, sys, logging, re

global VERSION
VERSION = "version=.*"


# Replaces version in file with supplied pattern and new string
def replace(file_path, pattern, subst):
    logger.info("Overriding current version with: %s" % subst)

    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(re.sub(pattern, subst, line))
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

global logger
logger = logging.getLogger()


# Handles command line arguments
def handle_args():
    parser = argparse.ArgumentParser(description='Handle file for version bump')
    parser.add_argument('--file', type=str, help='File path to properties file')
    parser.add_argument('--raw-version', type=str, help='Override version number')
    args = parser.parse_args()

    # if args.file:
    #     return args
    # else:
    #     parser.print_help()
    #     sys.exit(1)
    return args


# Main method...
def main():
    args = handle_args()

    logger.info("Updating properties file: %s ..." % args.file)
    if args.raw_version:
        replace(args.file, VERSION, "version=" + args.raw_version)
    else:
        version = find_version(args.file)
        logger.info("Bumping version from previous: %s" % version)
        split_version = str(version).split('.')
        major = split_version[0].replace("version=", "")
        minor = int(split_version[1]) + 1
        patch = split_version[2]

        newversion = "%s.%s.%s" % (major, minor, patch)
        logger.info("New version will be %s" % newversion)
        replace(args.file, VERSION, "version=" + newversion)
        


# Finds the version from file path pased in
def find_version(file_path):
    v = ""
    f = open(file_path, 'r')
    for line in f.readlines():
        if re.match(VERSION, line):
            v = line

    if v:
        return v
    else:
        logger.error("Could not find version in file %s" % file_path)


if __name__ == "__main__":
    main()