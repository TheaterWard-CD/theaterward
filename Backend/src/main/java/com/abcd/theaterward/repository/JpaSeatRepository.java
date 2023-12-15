package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.Seat;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public class JpaSeatRepository implements SeatRepository {

    private final EntityManager entityManager;

    public JpaSeatRepository(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    @Override
    public List<Seat> findAll() {
        return null;
    }

    /*@Override
    public List<Seat> findByTheaterNo(int theater_no) {
        *//*List<Seat> seat = entityManager.createQuery("select s from seat s where s.theater_no = :theater_no", Seat.class)
                .setParameter("theater_no", theater_no)
                .getResultList();

        //return seat.stream().findAny();
        return seat;*//*

        String jpql = "SELECT s FROM Seat s WHERE s.theater_no = :theater_no";
        return entityManager.createQuery(jpql, Seat.class)
                .setParameter("theaterNo", theater_no)
                .getResultList();
    }*/

    @Override
    public List<Seat> findByTheaterNo(int theater_no) {
        String jpql = "SELECT s FROM Seat s WHERE s.theaterNo = :theater_no";
        return entityManager.createQuery(jpql, Seat.class)
                .setParameter("theater_no", theater_no)
                .getResultList();
    }

}
