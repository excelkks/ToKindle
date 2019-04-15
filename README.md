# ToKindle
A python3 script that send your ebook to your kindle.
## Usage
#### 1.Setup
You need setup the default email address both sender and receipt in case input them every time.
In addition, you will be requred to setup the servers of the sender. 
Here are what you should change in ToKindle.py.
```python
from_addr = 'sender@email.com'
to_addr = 'recipient@email.com'
smtp_server = 'example-stmp'
```
#### 2.Send
Make sure your ebook at the same path with Tokindle.py. 
Then, run Tokindle.py. After input your password of the sender email, send-to-kindle start work. at the same time, your ebook will be moved to a new directory named backup. 
