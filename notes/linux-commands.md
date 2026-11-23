# Linux/mac commands


## Navigation
- `pwd`:  where am I
- `ls`: Where is there
    
    - `-l` detailed listing
    - `-a` show hidden files
    - `-lh` human readable file size

## Create dir
- `mkdir dirname`

## Change dir
- `cd directory`
- `cd ..` go up one level
- `cd ~` go home

## Create nested dir
- `mkdir -p path/to/dir`
- `-p`: creates intermediate directories if they don't exist

## creating empty file
`touch sample.txt`
> writing in that file

`echo "Hello World" > sample.txt`
> `>` overwrites the file

`echo "Hello World" >> sample.txt`
> `>>` appends to the file

## Display file Contents
**Entire file**
`cat sample.txt`

**First line**
`head -1 sample.txt`

**First n Lines**
`head -5 sample.txt`

**Last line**
`tail -1 sample.txt`

**Last n Lines**
`tail -5 sample.txt`

## Copy, Move, Rename and delete
- copy: `cp original.txt backup.txt`
- move: `mv original.txt backup.txt`
- rename: `mv oldname newname`
- delete: `rm filename`
- delete directory and its content: `rm -r dirname`


> **NOTE:** Be careful with rm. It doesn't move files to your Trash. Verify your path and filenames before deleting.

## Search files and content
- `find`

**find all txt files in current directory**
`find . -name "*.txt"`

**find all py files in current directory**
`find . -name "*.py"`

**find directories**
`find . -type d`

**find files**
`find . -type f`


## Search in Files
`grep`

**search a word in all files**
`grep "word" *`

**case-insensitive search**
`grep -i "word" *`

**Search recursively through files:**
`grep -r "ERROR" .`

## writing files using nano
`nano filename.txt`

If using nano
- Ctrl + O → save
- Enter → confirm filename
- Ctrl + X → exit
