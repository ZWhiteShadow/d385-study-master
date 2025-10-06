# Python Logging

---

The purpose of this lab is to introduce students to the process of creating, accessing, and generating log files using code. Use the template provided in order to write code that outputs log information with the basic configuration of level name and message, based on the information in the template.

When you divide a number by zero, write an error message to the log.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a744b2d-aaeb-49d6-9f4f-e216e2692145/Untitled.png)

```jsx
import logging
import sys

#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:

       quotient = dividend/divisor  
       print (quotient)
        
    except Exception as e:

        #logging error here, use str(e) as part of the output

if __name__ == '__main__': 

    dividend = int(input())
    divisor = int(input())
    
    divideByZeroError(dividend,divisor)
```

## Answer

---

```jsx
import logging
import sys

#log division by zero error to the log, the output is printed to the screen 
def divideByZeroError(dividend, divisor):

    logging.basicConfig(stream=sys.stdout,format='%(levelname)s:%(message)s')
    
    try:

       quotient = dividend/divisor  
       print (quotient)
        
    except Exception as e:

        #logging error here, use str(e) as part of the output
				logging.error(' The exception that occurred is: ' + str(e))

if __name__ == '__main__': 

    dividend = int(input())
    divisor = int(input())
    
    divideByZeroError(dividend,divisor)
```