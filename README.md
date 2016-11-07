# Daily-log-tool
A light weigh and easy to use command line tool to write daily working logs.

# How to use
```
python logger/logger.py -h
```
## Write log
```
python logger/logger.py -l 'my log'
```
## Show log
```
python logger/logger.py -s [-d date-of -log]
```
# Recommendation
Add an alias for this command by the following steps:

In Ubuntu:

```
vim ~/.bashrc
```

And add the following line to the end of the file (create the file if not exists):
```
alias mdl='python /path-to-the-project/logger/logger.py'
```
And then you can easily use the logger as 
```
mdl -l 'my log'
mdl -s
mdl -l 'my second log'
```
