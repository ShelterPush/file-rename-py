#! python3
# fileRename.py - A script to rename files of a specific file extension in a folder.

from pathlib import Path
import sys, os

def yesNo():
    while True:
        yesNoInput = str(input())
        if yesNoInput.lower() == 'y' or yesNoInput.lower() == 'yes':  
            return 'y'
            break
        if yesNoInput == 'n' or yesNoInput.lower() == 'no':
            return 'n'
            break
        print('Please only answer "yes" or "no", without quotation marks.')
        print()

print('This program renames files within a folder.')

# Make sure the program is operating in the correct folder
print('Is this program in the directory containing the files of interest?')
dirYN = yesNo()
if dirYN == 'y':
    p = Path.cwd()
else:
    print('Please type the absolute path of the directory of interest.')
    p = Path(str(input()))
# Ask for the file format to look for
print('Which file extension are you looking for (e.g. flac, doc, xlsx, etc.)? Do not include the . symbol.')
print('Note: If you mistype the format, you will rename the wrong files.')
fileType = str(input())
globName = str('*.'+fileType)
fileList = list(p.glob(globName))
if fileList == []:
    print('No files with that extension were found within the specified directory.')
    print('Press Enter to exit the program.')
    input()
    sys.exit()
# Report the number of files found with that extension and give the option of canceling
print('%s file(s) with that extension were found in the specified directory.'%(len(fileList)))
print('Are you sure you want to rename %s files?'%(len(fileList)))
filesYN = yesNo()
if filesYN == 'n':
    print('Okay. Press Enter to exit the program.')
    input()
    sys.exit()
renList = []
# Give a choice to just shorten the filenames
print('Do you just want to shorten all the filenames of this type to a specific number of characters?')
shortYN = yesNo()
if shortYN == 'y':
    # Ask how many characters to shorten it to and check if the provided number works
    while True:
        print('How many characters do you want to appear?')
        print('For only the first two characters, type only "2" without the quotations.')
        try:
            charLen = int(input())
        except:
            print('Please type the number of characters you would like to appear in the new filenames.')
            print()
            continue
        minLen = 1000
        for i in range(len(fileList)):
            name = Path(fileList[i]).stem
            nameLen = len(name)
            if nameLen < minLen:
                minLen = nameLen
        if charLen <= minLen:
            break
        else:
            print('The number of characters you would like to shorten it to must be less than the shortest filename.')
            print()
    for i in range(len(fileList)):
        oldName = Path(fileList[i]).stem
        reName = oldName[:charLen]
        renList.append(p / str(reName + '.' + fileType))
else:
    # If you don't want to shorten it, supply names for each file
    for i in range(len(fileList)):
        print('Note: just press Enter to skip renaming this file.')
        print('Rename %s file %s to:'%(fileType,Path(fileList[i]).stem))
        reName = str(input())
        if reName == '':
            renList.append(fileList[i])
            continue
        else:
            renList.append(p / str(reName + '.' + fileType))
        print()
#fileName = unicode(os.path.split(fileItem.filename)[1]) # might be necessary, with other languages
for i in range(len(fileList)):
    oldFile = Path(fileList[i])
    newFile = Path(renList[i])
    if oldFile == newFile: # reduce the number of actual movements
        print('New name is identical; skipping %s ...'%(oldFile))
        continue
    else:
        print('Renaming %s to %s ...'%(oldFile, newFile))
        #os.rename(oldFile, newFile) # Comment to test
