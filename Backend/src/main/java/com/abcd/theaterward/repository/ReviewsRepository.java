package com.abcd.theaterward.repository;

import com.abcd.theaterward.domain.*;

import java.util.List;

public interface ReviewsRepository {
    public int save(Reviews reviews);

    public long dupe(ReviewInfo reviewInfo);

    public List<Reviews> searchByShow(ReviewRequest reviewRequest);

    public List<ReviewResponseByTheater> searchByTheater(ReviewRequest reviewRequest);
}
