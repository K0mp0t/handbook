from os import listdir  # выбор хендбука из имеющихся в директории?
from recording import *


class Handbook:
    # name - string
    recordings = list()

    def __init__(self, name, *args):
        # для инициализации создать handbook
        # с нужным именем и прочитать его с файла
        # выбор с listdir?
        self.name = name
        self.recordings = list(args)

    def __str__(self):
        return 'Handbook %s with %i recordings' % (self.name, len(self.recordings))

    def save_to_txt(self):
        f = open('%s.txt' % self.name, 'w', encoding='utf-8')
        for i in range(len(self.recordings)):
            output = str(i)+': '+str(self.recordings[i])+'\n'
            f.write(output)
        f.close()

    def read_from_txt(self):
        f = open('%s.txt' % self.name, 'r', encoding='utf-8')
        for line in f:
            # key = int(line.split(': ')[0])
            # ls = line.split(': ')[1].split(', ')
            # self.recordings[key] = ls # нужен ли индекс? при перезаписи будет происходить их сдвиг
            self.recordings.append(Recording(*line[:-1].split(': ')[1].split(', ')))  
            # * для превращения листа в args
            # [:-1] для того, чтобы избавится от переноса строки в конце
        f.close()

    def add_recording(self, recording):
        if not isinstance(recording, Recording):
            raise TypeError('Given recording is not an instance of the Recording class')
        self.recordings.append(recording)

    def remove_recording(self, index):
        if not isinstance(index, int):
            raise TypeError('Given index is not integer')
        if index > len(self.recordings) or index < 0:
            raise ValueError('Index out of range')
        return self.recordings.pop(index)  # cast to str?

    def get_recording_index(self, recording):
        if recording not in self.recordings:
            raise ValueError('There are no such recordings')
        return self.recordings.index(recording)

    def get_recording_by_index(self, index):
        if not isinstance(index, int):
            raise TypeError('Given index is not integer')
        if index > len(self.recordings) or index < 0:
            raise ValueError('Index out of range')
        return self.recordings[index]  # cast to str?
