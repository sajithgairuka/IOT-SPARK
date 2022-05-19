#https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element

file = open('../topics/location_topic.txt', 'r')
file1 = open('../topics/location_subtopic.txt','r')
lines = file.readlines()
sublines = file1.readlines()
for line in lines:
    location_topic = line[:-1].split(',')
    for subline in sublines:
        location_subtopic = subline[:-1].split(',')
        bw_location_topic = str(*location_topic)
        bw_location_subtopic = str(*location_subtopic)
        print("{}/{}".format(bw_location_topic,bw_location_subtopic))
