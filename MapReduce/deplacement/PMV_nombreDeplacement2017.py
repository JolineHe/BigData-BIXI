from mrjob.job import MRJob

class PMV_BIXI_Deplaments2017(MRJob):
    def mapper(self, key, line):
        if "start_station_code" not in line:
            start_date, start_station_code, end_date, end_station_code, duration_sec, is_member = line.split(',')
            yield start_station_code, 1


    def reducer(self,start_station_code,count):
        yield start_station_code,sum(count)



if __name__ == '__main__':
    PMV_BIXI_Deplaments2017.run()