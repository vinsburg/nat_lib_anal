class Archive(object):

    def __init__(self, file_name, header, data):
        # lets read all the worksheet exported data
        self.worksheet = dict([("file_name", file_name)])
        self.worksheet['header'] = header
        # print(self.worksheet['header'])
        self.worksheet['data'] = {}
        self.key_dic = {}
        self.key_length = 0
        self.read_file_to_archive(file_name, data)

    def read_file_to_archive(self, file_name, data):
        header_length = len(self.worksheet['header'])
        self.key_length = len(data[0][0])
        for line_ind, line in enumerate(data):
            if line[0] not in self.key_dic:
                self.key_dic[line[0]] = list()
            self.key_dic[line[0]].append([line_ind])
            key = line[0]+'-'+str(line_ind)
            self.worksheet['data'][key] = {}
            line_length = min(len(line), header_length)
            for item_ind in range(line_length):
                self.worksheet['data'][key][self.worksheet['header'][item_ind]] = line[item_ind]
            for item_ind in range(line_length, header_length):
                self.worksheet['data'][key][self.worksheet['header'][item_ind]] = None

    def clean_keys(self):
        temp_dic = {}
        for key, value in self.worksheet['data'].items():
            key_split = key.split('-')
            key = '-'.join(key_split[:len(key_split)-1]).strip('-')
            temp_dic[key] = value
        self.worksheet['data'] = temp_dic
