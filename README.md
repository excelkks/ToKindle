# ToKindle
A python3 script that sends e-book(s) to your kindle.
## Usage
#### 1.Setup
You need to set up the default email addresses of both sender and recipient to avoid inputting them each time.
In addition, you will be required to set up server of the sender. 
Here is what you should change in ToKindle.py.
```python
from_addr = 'sender@email.com'
to_addr = 'recipient@email.com'
smtp_server = 'example-stmp'
```
#### 2.Send
Make sure all your e-books are in the same path as Tokindle.py. 
Then, run Tokindle.py. After inputting password of the senders email, send-to-kindle start work. At the same time, your e-books will be moved to a new directory named backup. 
