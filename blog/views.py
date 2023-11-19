from django.http import HttpResponse
from django.shortcuts import render
import json
from functools import wraps
import time
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

def timer(func):
    """helper function to estimate view execution time"""

    @wraps(func)  # used for copying func metadata
    def wrapper(*args, **kwargs):
        # record start time
        start = time.time()

        # func execution
        result = func(*args, **kwargs)

        duration = (time.time() - start) * 1000
        # output execution time to console
        print('view {} takes {:.2f} ms'.format(
            func.__name__,
            duration
            ))
        return result
    return wrapper


@timer
def index(request):
    # Your existing view logic here

    # here is the js code to use to measure the load time in the frontend

    #     const observer = new PerformanceObserver((list) => {
    #   list.getEntries().forEach((entry) => {
    #     const domContentLoadedTime =
    #       entry.domContentLoadedEventEnd - entry.domContentLoadedEventStart;
    #     console.log(
    #       `${entry.name}: DOMContentLoaded processing time: ${domContentLoadedTime}ms`,
    #     );
    #   });
    # });

    # observer.observe({ type: "navigation", buffered: true });

    return render(request, 'index.html')


#  time the datbase look up
class PostList(APIView):
    def get(self, request, *args, **kwargs):
        global serializer_time
        global db_time

        # start the timer now to measure time taken for database look up
        db_start = time.time()
        posts = Post.objects.all()
        db_time = time.time() - db_start

        # start the serializer timer now to measure time taken for serializer
        serializer_start = time.time()
        serializer = PostSerializer(posts, many=True)
        data = serializer.data
        serializer_time = time.time() - serializer_start

        # get the total time
        total_time = db_time + serializer_time

        # print the total time
        print('Total time taken: {:.2f} ms'.format(total_time * 1000))
        print('Total time taken for database: {:.2f} ms'.format(db_time * 1000))
        print('Total time taken for serializer: {:.2f} ms'.format(serializer_time * 1000))

        # return the data
        return Response(data)


# this gets the coaching in the system 
@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class CoachedPostList(APIView):
    def get(self, request, *args, **kwargs):
        global serializer_time
        global db_time

        # start the timer now to measure time taken for database look up
        db_start = time.time()
        posts = Post.objects.all()
        db_time = time.time() - db_start

        # start the serializer timer now to measure time taken for serializer
        serializer_start = time.time()
        serializer = PostSerializer(posts, many=True)
        data = serializer.data
        serializer_time = time.time() - serializer_start

        # get the total time
        total_time = db_time + serializer_time

        # print the total time
        print('Total time taken: {:.2f} ms'.format(total_time * 1000))
        print('Total time taken for database: {:.2f} ms'.format(db_time * 1000))
        print('Total time taken for serializer: {:.2f} ms'.format(serializer_time * 1000))

        # return the data
        return Response(data)

