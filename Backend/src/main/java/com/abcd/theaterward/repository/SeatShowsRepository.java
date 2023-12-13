package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.SeatShows;

import java.util.List;

public interface SeatShowsRepository {
    public List<SeatShows> findAllByTheaterNoAndShowNameAndShowYear(int theaterNo, String showName, int showYear, int seatNo);

    public Object[] findRangeByTheaterNo(int theaterNo, int seatNo);
}
