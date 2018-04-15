import threading
import time

def run(n):
   print 'it is ',n,threading.current_thread()
   time.sleep(5)
   print 'done'

# t1 = threading.Thread(target = run,args=('x1',))
# t2 = threading.Thread(target = run,args=('x1',))
# t1.start()
# t2.start()
# run('x1')
# run('x1')
def run1():
    t1 = threading.Thread(target=run, args=('x1',))
    t1.start()
    print 1111111111111
    return 'yes'

x=run1()
print x