package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.*;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Repository
public class JpaReviewsRepository implements ReviewsRepository {

    @PersistenceContext
    EntityManager em;
    @Override
    @Transactional
    public int save(Reviews reviews) {
        em.persist(reviews);
        return reviews.getReviewNo();
    }

    @Override
    public long dupe(ReviewInfo reviewInfo) {
        String jpql = "SELECT COUNT(ssr) " +
                "FROM Ssr ssr " +
                "JOIN ssr.reviews review " +
                "WHERE ssr.theaterNo = :theaterNo " +
                "AND ssr.seatNo = :seatNo " +
                "AND ssr.showName = :showsName " +
                "AND ssr.showYear = :showsYear " +
                "AND review.userId = :usersId";

        return em.createQuery(jpql, Long.class)
                .setParameter("theaterNo", reviewInfo.getTheaterNo())
                .setParameter("seatNo", reviewInfo.getSeatNo())
                .setParameter("showsName", reviewInfo.getShowName())
                .setParameter("showsYear", reviewInfo.getShowYear())
                .setParameter("usersId", reviewInfo.getUserId())
                .getSingleResult();
    }


    @Override
    public List<Reviews> searchByShow(ReviewRequest reviewRequest) {
        String jpql = "SELECT r FROM Ssr s JOIN s.reviews r " +
                "WHERE s.theaterNo = :theaterNo " +
                "AND s.seatNo = :seatNo " +
                "AND s.showName = :showsName " +
                "AND s.showYear = :showsYear";

        return em.createQuery(jpql, Reviews.class)
                .setParameter("theaterNo", reviewRequest.getTheaterNo())
                .setParameter("seatNo", reviewRequest.getSeatNo())
                .setParameter("showsName", reviewRequest.getShowName())
                .setParameter("showsYear", reviewRequest.getShowYear())
                .getResultList();
    }


    @Override
    public List<ReviewResponseByTheater> searchByTheater(ReviewRequest reviewRequest) {
        String jpql = "SELECT new com.abcd.theaterward.domain.ReviewResponseByTheater(r.reviewNo, r.reviewScore, r.userId, r.reviewContent, s.showName, s.showYear) " +
                "FROM Ssr s JOIN s.reviews r " +
                "WHERE s.theaterNo = :theaterNo AND s.seatNo = :seatNo";

        return em.createQuery(jpql, ReviewResponseByTheater.class)
                .setParameter("theaterNo", reviewRequest.getTheaterNo())
                .setParameter("seatNo", reviewRequest.getSeatNo())
                .getResultList();
    }





}
