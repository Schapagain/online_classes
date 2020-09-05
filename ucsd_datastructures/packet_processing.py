






# Uses Python3
import sys

def bufferIsFull(buffer,max_size):
    return len(buffer) == max_size

def bufferIsEmpty(buffer):
    return len(buffer) == 0

def readNewPacket():
    new_packet = list(map(int,sys.stdin.readline().split()))
    return new_packet

def extendBuffer(buffer,new_packet):
    last_packet_finish_time = buffer[-1][0] + buffer[-1][1]
    new_packet[0] = max(last_packet_finish_time,new_packet[0])
    buffer.append(new_packet)

def processPackets(buffer_size,all_packets):

    if buffer_size == 0:
        return []
    buffer = []
    process_times = []
    for new_packet in all_packets:
        if bufferIsEmpty(buffer):
            buffer.append(new_packet)
            process_times.append(new_packet[0])
        else:
            first_packet_start_time = buffer[0][0]
            first_packet_duration = buffer[0][1]
            first_packet_finish_time = first_packet_start_time + first_packet_duration
            new_packet_arrival_time = new_packet[0]
            if new_packet_arrival_time >= first_packet_finish_time:
                extendBuffer(buffer,new_packet)
                buffer.pop(0)
                new_packet_start_time = buffer[-1][0]
                process_times.append(new_packet_start_time)
            else:
                if bufferIsFull(buffer,buffer_size):
                    process_times.append(-1)
                else:
                    extendBuffer(buffer,new_packet)
                    new_packet_start_time = buffer[-1][0]
                    process_times.append(new_packet_start_time)
    return process_times
# Tests

num_tests = 23
fnames = ["packet_processing_tests/{:02d}".format(i) for i in range(1,num_tests)]

for fname in fnames:
    print('test number:',fname[-2:])
    f = open(fname)
    f_ans = open(fname+'.a')

    all_input = f.read().strip().split('\n')
    buffer_size = int(all_input[0].split()[0])
    all_packets_str = all_input[1:]
    all_packets = [list(map(int,packet_str.split())) for packet_str in all_packets_str]
    my_res = processPackets(buffer_size,all_packets)
    expected_res_str = f_ans.read().strip().split('\n')
    if expected_res_str[0] == '':
        expected_res = []
    else:
        expected_res = list(map(int,expected_res_str))
    assert(my_res == expected_res)
print("Everything looks good!")
