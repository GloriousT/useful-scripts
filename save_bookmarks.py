#!/usr/bin/python3
import os
from shutil import copyfile

HOME = os.environ['HOME']
BOOKMARKS_FILENAME = "Bookmarks"
BOOKMARKS_PATH = HOME + "/.config/google-chrome/Default/" + BOOKMARKS_FILENAME
CLOUD_STORAGE_PATH = HOME + "/Dropbox/backups/"
MY_BOOKMARKS_FILE = CLOUD_STORAGE_PATH + BOOKMARKS_FILENAME
MY_BOOKMARKS_BACKUP_FILE = MY_BOOKMARKS_FILE + ".bak"
OLD_BACKUP = MY_BOOKMARKS_BACKUP_FILE + ".old"
exist_file = os.path.isfile
rename_file = os.rename


def main():
    print("Starting")
    print("Path to bookmarks is: " + BOOKMARKS_PATH)
    print("Path to storage is: " + CLOUD_STORAGE_PATH)
    if is_initial_bookmarks_exist():
        prepare_destination_directory()
        rename_existing_bookmark_files()
        copy_new_bookmark_file()
        remove_old_backup_file()
    else:
        print("No bookmarks found to save!")
        print("Finishing!")


def is_initial_bookmarks_exist():
    return exist_file(BOOKMARKS_PATH)


def prepare_destination_directory():
    if not os.path.isdir(CLOUD_STORAGE_PATH):
        print("creating destination directory: " + CLOUD_STORAGE_PATH)
        os.mkdir(CLOUD_STORAGE_PATH)


def rename_existing_bookmark_files():
    if file_and_backup_exist():
        print("updating existing file and bak")
        rename_file(MY_BOOKMARKS_BACKUP_FILE, OLD_BACKUP)
        rename_file(MY_BOOKMARKS_FILE, MY_BOOKMARKS_BACKUP_FILE)
    elif exist_file(MY_BOOKMARKS_FILE):
        print("updating existing file only")
        rename_file(MY_BOOKMARKS_FILE, MY_BOOKMARKS_BACKUP_FILE)


def file_and_backup_exist():
    return exist_file(MY_BOOKMARKS_FILE) and exist_file(MY_BOOKMARKS_BACKUP_FILE)


def copy_new_bookmark_file():
    print("copy in progress")
    copyfile(BOOKMARKS_PATH, MY_BOOKMARKS_FILE)


def remove_old_backup_file():
    print("removing old file if exists")
    if exist_file(OLD_BACKUP):
        os.remove(OLD_BACKUP)

if __name__ == '__main__':
    main()
