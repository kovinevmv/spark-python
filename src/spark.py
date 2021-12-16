import threading

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from src.putils import pretty_print


class Spark:
    def __init__(self):
        self.sc = SparkContext(appName="SparkSIFTCounter")
        self.sc.setLogLevel('ERROR')
        self.streaming_sc = StreamingContext(self.sc, 1)
        self.streaming_sc.checkpoint('checkpoint')

    def create(self, stream_dir, converter, function, sift, log=None):
        images = self.streaming_sc.textFileStream(stream_dir)

        aggr = sift.save
        if function == 'save':
            aggr = sift.save
        if function == 'filter':
            aggr = sift.filter
        if function == 'count':
            aggr = sift.count

        stream = images.map(converter).map(aggr)

        if function == 'count':

            def avg(x, y):
                return (x + y) / 2

            stream = stream.reduceByKeyAndWindow(avg, lambda x, y: x - y, 30,
                                                 3)
            pretty_print(stream)

        stream.saveAsTextFiles(log)
        thread = threading.Thread(target=Spark.pending, args=(self, ))
        thread.daemon = True
        thread.start()

    def pending(self):
        self.streaming_sc.start()
        self.streaming_sc.awaitTermination()
