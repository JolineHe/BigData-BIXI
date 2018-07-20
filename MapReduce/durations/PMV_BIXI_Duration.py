from mrjob.job import MRJob

class PMV_BIXI_Duration(MRJob):
    def mapper(self, key, line):
        if "duration_sec" not in line:
            start_date, start_station_code, end_date, end_station_code, duration_sec, is_member = line.split(',')
            period = int(duration_sec)/900
            yield [period,int(is_member)], 1


    def reducer(self,period_member,counts):
        yield period_member,sum(counts)



if __name__ == '__main__':
    PMV_BIXI_Duration.run()