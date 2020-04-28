


curr_time = 0
arriving_rate =
transmission_rate =
MAX_BUFFER =

def generate_event (rate):
     double u
     u = drand48()
     return ((-1/rate)*log(1-u))

def process_arrival_event(time, buffer, global_arrival_events, global_departure_events, length):
    curr_time = time
    next_arrival_event = generate_event(arriving_rate) + curr_time
    global_arrival_events.add(next_arrival_event)
    global_arrival_events.sort()
    if length == 0:
        next_depart_event = generate_event(transmission_rate)
        global_departure_events.add(next_depart_event + curr_time)
    else:
        if length < MAX_BUFFER:
            buffer.add(next_arrival_event)
        else: pass

def process_departure_event(time, buffer, global_departure_events):
    pass

def simulation():
    global_arrival_events = []  #global event list
    global_departure_events = []
    buffer = []
    #curr_time = 0
    length = 0   #buffer.size()
    total_num_packets = 0
    total_num_dropped = 0
    first_event = generate_event(arriving_rate) #generate the first arriving event
    global_arrival_events.insert(first_event + curr_time)

    for i in range(100000):
        curr_arrival_event = global_arrival_events[0]
        curr_departure_event = global_departure_events[0]
        if i == curr_arrival_event:
            process_arrival_event(curr_arrival_event, buffer, global_arrival_events, global_departure_events, length)
            global_arrival_events = global_arrival_events[1:]
        if i == curr_departure_event:
            process_departure_event(curr_departure_event, buffer, global_arrival_events)
            global_departure_events = global_departure_events[1:]
        # update the busy time for the server
        # update the number of packets in the queue
        # update the number fo packets dropped

   #utilization = busy time / total time
   #mean_queue_length = total_num_packets / total time
   #num_droppe = total_num_dropped
