#setup
import random
item_stream = list(range(1,1_000_001)) # possibly new items will be added to the stream.
mark_del = 0 # any value that is not expected in the dynamic array.
item_del_count = 0
sweep_run_size = 500_000 # ideally choose this size in same order of magnitude as the dynamic array.

# mimicing the receiving of the item to be processed
while item_del_count < sweep_run_size:
    item = random.randint(1, len(item_stream))
# here to keep it simple, just assume that it produces unique integer every time even though it doesn't.
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