import boto3
import sys
import threading
import os
from boto3.s3.transfer import S3Transfer


class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(" %s  %s / %s  (%.2f%%)" %
                             (self._filename, self._seen_so_far, self._size, percentage))
            sys.stdout.flush()


transfer = S3Transfer(boto3.client('s3', 'us-west-2'))
# Upload /tmp/myfile to s3://bucket/key and print upload progress.
transfer.upload_file('/tmp/Fundamental_of_Python.pdf', 'hmenow', 'Fundamental_of_Python.pdf',
                     callback=ProgressPercentage('/tmp/Fundamental_of_Python.pdf'))
