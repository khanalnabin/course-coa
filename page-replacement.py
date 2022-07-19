def page_replacement_fifo(data, no_of_frames):
    frame = []
    no_of_hits = 0
    all_frames = []
    current_index = 0
    for _ in range(no_of_frames):
        all_frames.append([])
    for element in data:
        if element in frame:
            no_of_hits += 1
        else:
            if len(frame) < no_of_frames:
                frame.append(element)
            else:
                frame[current_index] = element
                current_index = (current_index + 1) % no_of_frames
        for i in range(no_of_frames):
            if(len(frame) > i):
                all_frames[i].append(frame[i])
            else:
                all_frames[i].append('_')
    return all_frames, no_of_hits


def page_replacement_lru(data, no_of_frames):
    frame = []
    no_of_hits = 0
    all_frames = []
    for _ in range(no_of_frames):
        all_frames.append([])
    for index, element in enumerate(data):
        if element in frame:
            no_of_hits += 1
        else:
            if len(frame) < no_of_frames:
                frame.append(element)
            else:
                present = []

                for i in range(index-1, -1, -1):
                    if data[i] in present:
                        pass
                    elif len(present) < (no_of_frames-1):
                        present.append(data[i])
                    else:
                        to_remove = data[i]
                        break
                to_remove_index = frame.index(to_remove, 0, len(frame))
                frame[to_remove_index] = element
        for i in range(no_of_frames):
            if(len(frame) > i):
                all_frames[i].append(frame[i])
            else:
                all_frames[i].append('_')
    return all_frames, no_of_hits


def page_replacement_lfu(data, no_of_frames):
    frame = {}
    no_of_hits = 0
    all_frames = []
    for _ in range(no_of_frames):
        all_frames.append([])
    for index, element in enumerate(data):
        if element in frame.keys():
            no_of_hits += 1
            frame[element] += 1
        else:
            if len(frame) < no_of_frames:
                frame[element] = 1
            else:
                minval = 1000
                minkey = ''
                for key, value in frame.items():
                    if(value < minval):
                        minval = value
                        minkey = key
                frame.pop(minkey)
                frame[element] = 1

        framelist = [(k, v) for k, v in frame.items()]
        for i in range(no_of_frames):
            if(len(frame) > i):
                all_frames[i].append(framelist[i][0])
            else:
                all_frames[i].append('_')
    return all_frames, no_of_hits


def main():
    # no_of_frames = int(input("Enter the number of frames: "))
    # data = input("Enter the data: ").split(' ')
    no_of_frames = 3
    data = ['2', '3', '2', '1', '5', '2', '4', '5', '3', '2', '5', '2']
    all_frames, no_of_hits = page_replacement_lfu(data, no_of_frames)
    print(data)
    for i in all_frames:
        print(i)
    print("No of hits: ", no_of_hits)
    print("Hit ratio: ", no_of_hits/len(data))


if __name__ == '__main__':
    main()
