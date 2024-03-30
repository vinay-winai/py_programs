# https://blog.deviant.works/make-deletions-in-arrays-blazingly-fast - Article link
# setup
item_stream = list(range(1,10_001)) # possibly new items will be added to the stream.
mark_del = 0 # any value that is not expected in the dynamic array.
item_del_count = 0
sweep_run_size = len(item_stream)//2 # ideally choose same order of magnitude as item_stream

# mimicing the receiving of the item to be processed
def request_item_generator(n):
    num = 1  # Start with the first odd number
    while num <= n:  # Generate n odd numbers
        yield num
        num += 2

item_generator = request_item_generator(len(item_stream))
while item_del_count < sweep_run_size:
    item = next(item_generator)
# -------------------------------------------------------------
# mark
    item_index = item_stream.index(item)
    item_stream[item_index] = mark_del
    item_del_count += 1
    # do some processing

# sweep
# possibly parallel to main thread to minimize latency.
if item_del_count >= sweep_run_size:
    new_item_stream = [item for item in item_stream if item != mark_del]
    # pause appending of items to the dynamic array, add them into a temp buffer.
    item_stream = new_item_stream
    print(len(item_stream))
