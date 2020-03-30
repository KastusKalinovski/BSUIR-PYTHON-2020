import os
import tempfile
import sys


class HeapNode:
    def __init__(self, item, file_handler):
        self.item = item
        self.file_handler = file_handler


class ExternalMergeSort:
    def __init__(self):
        self.temp_files_list = []
        self.cwd = os.getcwd()

    def split_files(self, filename, small_size):
        file_handler = open(filename, 'rb')
        temp_buffer = []
        size = 0
        while True:
            number = file_handler.readline()
            if not number:
                break
            temp_buffer.append(number)
            size += 1
            if size % small_size == 0:
                temp_buffer = sorted(temp_buffer, key=lambda num: \
                    int(num.strip()))
                temp_file = tempfile.NamedTemporaryFile(dir=self.cwd
                                                            + '/temp', delete=False)
                temp_file.writelines(temp_buffer)
                temp_file.seek(0)
                self.temp_files_list.append(temp_file)
                temp_buffer = []

    def heapify(self, arr, i):
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(arr) - 1
        smallest = i

        if left <= n and arr[left].item < arr[i].item:
            smallest = left
        if right <= n and arr[right].item < arr[smallest].item:
            smallest = right
        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest)

    def construct_heap(self, arr):
        for i in reversed(range(len(arr) // 2)):
            self.heapify(arr, i)

    def merge_sort(self):
        list_heaps = []
        sorted_output = []
        for file_handler in self.temp_files_list:
            item = int(file_handler.readline().strip())
            list_heaps.append(HeapNode(item, file_handler))

        self.construct_heap(list_heaps)
        while True:
            min = list_heaps[0]
            if min.item == sys.maxsize:
                break
            sorted_output.append(min.item)
            file_handler = min.file_handler
            item = file_handler.readline().strip()
            if not item:
                item = sys.maxsize
            else:
                item = int(item)
            list_heaps[0] = HeapNode(item, file_handler)
            self.heapify(list_heaps, 0)
        return sorted_output


if __name__ == '__main__':
    sort_operator = ExternalMergeSort()
    sort_operator.split_files('numbers.txt', 1000)
    result = open("result.txt", 'w')
    sorted_nums = sort_operator.merge_sort()
    for num in sorted_nums:
        result.write(str(num) + "\n")
    result.close()
