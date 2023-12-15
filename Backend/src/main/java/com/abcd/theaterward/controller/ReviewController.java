package com.abcd.theaterward.controller;

import com.abcd.theaterward.domain.ReviewInfo;
import com.abcd.theaterward.domain.ReviewRequest;
import com.abcd.theaterward.domain.Reviews;
import com.abcd.theaterward.service.ReviewService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class ReviewController {
    private final ReviewService reviewService;

    public ReviewController(ReviewService reviewService) {
        this.reviewService = reviewService;
    }

    @PostMapping("/review")
    public long saveReview(@RequestBody ReviewInfo reviewInfo) {
        reviewService.joinSsr(reviewInfo);
        return reviewService.joinReview(reviewInfo);
//        if(reviewService.dupe(reviewInfo) == 0) {
//            reviewService.joinSsr(reviewInfo);
//            return reviewService.joinReview(reviewInfo);
//        } else {
//            return -1;
//        }
    }

    @GetMapping("/review")
    public Object findReview(@RequestBody ReviewRequest reviewRequest) {
        return reviewService.findReview(reviewRequest);
    }
}
