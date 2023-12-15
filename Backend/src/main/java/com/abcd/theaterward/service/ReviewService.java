package com.abcd.theaterward.service;

import com.abcd.theaterward.domain.ReviewInfo;
import com.abcd.theaterward.domain.ReviewRequest;
import com.abcd.theaterward.domain.Reviews;
import com.abcd.theaterward.domain.Ssr;
import com.abcd.theaterward.repository.JpaReviewsRepository;
import com.abcd.theaterward.repository.JpaSsrRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ReviewService {

    private final JpaReviewsRepository jpaReviewsRepository;
    private final JpaSsrRepository jpaSsrRepository;

    public ReviewService(JpaReviewsRepository jpaReviewsRepository, JpaSsrRepository jpaSsrRepository) {
        this.jpaReviewsRepository = jpaReviewsRepository;
        this.jpaSsrRepository = jpaSsrRepository;
    }

    public int joinReview(ReviewInfo reviewInfo) {
        Reviews reviews = new Reviews();
        reviews.setUserId(reviewInfo.getUserId());
        reviews.setReviewScore(reviewInfo.getReviewScore());
        reviews.setReviewContent(reviewInfo.getReviewContent());

        return jpaReviewsRepository.save(reviews);
    }

    public long dupe(ReviewInfo reviewInfo) {
        return jpaReviewsRepository.dupe(reviewInfo);
    }

    public void joinSsr(ReviewInfo reviewInfo) {
        Ssr ssr = new Ssr();
        ssr.setSeatNo(reviewInfo.getSeatNo());
        ssr.setShowName(reviewInfo.getShowName());
        ssr.setShowYear(reviewInfo.getShowYear());
        ssr.setTheaterNo(reviewInfo.getTheaterNo());

        jpaSsrRepository.save(ssr);
    }

    public Object findReview(ReviewRequest reviewRequest) {
        if(reviewRequest.getType() == 1) {
            //Search By Show
            return jpaReviewsRepository.searchByShow(reviewRequest);
        }
        else {
            //Search By Theater
            return jpaReviewsRepository.searchByTheater(reviewRequest);
        }
    }
}
