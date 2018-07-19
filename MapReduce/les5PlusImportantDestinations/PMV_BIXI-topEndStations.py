from mrjob.job import MRJob
from mrjob.job import MRStep
import heapq


class TopEndStations(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_count,
                   reducer=self.reducer_sum),
            MRStep(mapper=self.mapper_par_start,
                   reducer=self.reducer_top_five)
        ]

    def mapper_count(self, key, value):
        start_date, start_station_code, end_date, end_station_code, duration_sec, is_member = value.split(',')
        yield (start_station_code, end_station_code), 1

    def reducer_sum(self, start_end, ones):
        yield start_end, sum(ones)

    def mapper_par_start(self, start_end, count):
        yield start_end[0], (count, start_end[1])

    def reducer_top_five(self, start, end_counts):
        top_five_end_counts = heapq.nlargest(5,end_counts)
        yield (start, top_five_end_counts)


if __name__ == '__main__':
    TopEndStations.run()
