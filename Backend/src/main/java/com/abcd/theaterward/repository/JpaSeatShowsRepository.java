package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.SeatShows;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class JpaSeatShowsRepository implements SeatShowsRepository{

    private final EntityManager em;

    public JpaSeatShowsRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public List<SeatShows> findAllByTheaterNoAndShowNameAndShowYear(int theaterNo, String showName, int showYear, int seatNo) {
        String jpql = "SELECT ss FROM SeatShows ss WHERE ss.theaterNo = :theaterNo AND ss.showName = :showName AND ss.showYear = :showYear AND ss.seatNo = :seatNo";
        return em.createQuery(jpql, SeatShows.class)
                .setParameter("theaterNo", theaterNo)
                .setParameter("showName", showName)
                .setParameter("showYear", showYear)
                .setParameter("seatNo", seatNo)
                .getResultList();
    }

    @Override
    public Object[] findRangeByTheaterNo(int theaterNo, int seatNo) {
        String jpql = "SELECT MIN(ss.price), MAX(ss.price) FROM SeatShows ss WHERE ss.theaterNo = :theaterNo AND ss.seatNo = :seatNo";
        return (Object[]) em.createQuery(jpql)
                .setParameter("theaterNo", theaterNo)
                .setParameter("seatNo", seatNo)
                .getSingleResult();
    }
}
