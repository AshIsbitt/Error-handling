# File manipulation and Error Handling
The purpose of this project is to cover:
- Error handling
- Exceptions
- try except
- Best practices Using `with`
- Clean up our functions with `finally`
- Opening, Closing, and working with files

THe primary focus is error handling today, as this is the more important concept

## Error Handling
Always assume Murphy's law = Anything that can go wrong, will go wrong.

Assume your code will always break. Make sure you handle the errors correctly

When you handle errors, your code will continue 

### Best Practices
You never want to handle all errors in one go because it can create unstoppable code. Always specify which error you're handling.

```python
try:
    file = open('order.txt')
except FileNotFoundError as errmsg:
    print("THERE HAS BEEN AN ERROR")
```

#### Capture messages
You can capture the actual error message with `as`


## Definitions

### Errors and Exceptions
This is when the code actually breaks or stops. 

#### Raise
THis keyword is used to raise an exception

#### Try: except: finally
Try - this command attempts a segment of code

except - if the above code crashes, this will handle specific errors

finally - this will happen afterwards weather the program crashes or not

#### Open and Close
These can be used to open and close a file in various modes

#### With

This will implicitly open and close a file as long as there is code indented underneath to run

As soon as that code is finished, it'll automatically close the file

#### readline
reads a specific line of text from the file

#### readlines
reads all the lines of text from the file - can be iterated through using a for loop