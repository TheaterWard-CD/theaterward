package com.abcd.theaterward.service;

import com.abcd.theaterward.domain.GradeAndPrice;
import com.abcd.theaterward.domain.MinMax;
import com.abcd.theaterward.domain.Seat;
import com.abcd.theaterward.domain.SeatShows;
import com.abcd.theaterward.repository.JpaSeatRepository;
import com.abcd.theaterward.repository.JpaSeatShowsRepository;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class SeatService {
    private final JpaSeatRepository jpaSeatRepository;
    private final JpaSeatShowsRepository jpaSeatShowsRepository;

    public SeatService(JpaSeatRepository jpaSeatRepository, JpaSeatShowsRepository jpaSeatShowsRepository) {
        this.jpaSeatRepository = jpaSeatRepository;
        this.jpaSeatShowsRepository = jpaSeatShowsRepository;
    }

    public List<Seat> findSeats(int theater_no) {
        return jpaSeatRepository.findByTheaterNo(theater_no);
    }

    public List<GradeAndPrice> findGradeAndPriceByTheaterNoAndShowNameAndShowYear(int theater_no, String shows_name, int shows_year, int seat_no) {
        List<SeatShows> GPByShow =
                jpaSeatShowsRepository.findAllByTheaterNoAndShowNameAndShowYear(theater_no, shows_name, shows_year, seat_no);

        List<GradeAndPrice> GP = new ArrayList<>();
        for(SeatShows ss : GPByShow) {
            GradeAndPrice gp = new GradeAndPrice(ss);
            GP.add(gp);
        }

        return GP;
    }

    public MinMax findRangeByTheaterNo(int theater_no, int seat_no) {
        MinMax minMax = new MinMax();
        Object[] arr = jpaSeatShowsRepository.findRangeByTheaterNo(theater_no, seat_no);
        minMax.setMinPrice((Integer)arr[0]);
        minMax.setMaxPrice((Integer)arr[1]);

        return minMax;
    }

//    public List<SeatShows> findGradeAndPriceByTheaterNoAndShowNameAndShowYear(int theater_no, String shows_name, int shows_year, int seat_no) {
//        return jpaSeatShowsRepository.findAllByTheaterNoAndShowNameAndShowYear(theater_no, shows_name, shows_year, seat_no);
//    }
}
